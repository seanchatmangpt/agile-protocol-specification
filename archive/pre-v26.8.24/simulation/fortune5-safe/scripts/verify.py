#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]


def run(
    command: list[str],
    cwd: Path = ROOT,
    input_text: str | None = None,
) -> dict:
    process = subprocess.run(
        command,
        cwd=cwd,
        text=True,
        capture_output=True,
        input=input_text,
    )
    return {
        "command": " ".join(command),
        "returncode": process.returncode,
        "stdout": process.stdout if "self-test" in command else process.stdout[-4000:],
        "stderr": process.stderr[-4000:],
    }


def load(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text())


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-cargo", action="store_true")
    parser.add_argument(
        "--out",
        default="target/aps-safe-sim/verification-receipt.json",
    )
    args = parser.parse_args()

    failures: list[dict] = []
    evidence: list[dict] = []
    commands: list[dict] = []

    enterprise = load("config/fortune5-enterprise.json")
    scenario = load("config/global-core-modernization.json")
    profile = load("config/protocol-profile.json")
    fixture_paths = sorted((ROOT / "fixtures").glob("*.json"))
    for fixture in fixture_paths:
        json.loads(fixture.read_text())
        evidence.append(
            {
                "kind": "fixture",
                "path": str(fixture.relative_to(REPO)),
                "sha256": sha256(fixture),
            }
        )

    scale = {
        "portfolios": enterprise["portfolios"],
        "value_streams": enterprise["portfolios"]
        * enterprise["value_streams_per_portfolio"],
    }
    scale["solution_trains"] = (
        scale["value_streams"] * enterprise["solution_trains_per_value_stream"]
    )
    scale["arts"] = scale["solution_trains"] * enterprise["arts_per_solution_train"]
    scale["teams"] = scale["arts"] * enterprise["teams_per_art"]
    scale["team_people"] = scale["teams"] * enterprise["people_per_team"]

    if enterprise.get("schema") != "aps.safe-enterprise.v26.7.30":
        failures.append({"code": "ENTERPRISE_SCHEMA_MISMATCH"})
    if scenario.get("schema") != "aps.safe-scenario.v26.7.30":
        failures.append({"code": "SCENARIO_SCHEMA_MISMATCH"})
    if scale["teams"] < 500 or scale["team_people"] < 4500:
        failures.append({"code": "FORTUNE5_SCALE_FLOOR_NOT_MET", "scale": scale})
    if profile["mcp"]["version"] != "2025-11-25":
        failures.append({"code": "MCP_VERSION_MISMATCH"})
    if profile["a2a"]["version"] != "1.0.0":
        failures.append({"code": "A2A_VERSION_MISMATCH"})

    required_mcp = {
        "initialize",
        "tools/list",
        "tools/call",
        "resources/list",
        "resources/read",
        "prompts/list",
        "prompts/get",
    }
    required_a2a = {
        "agent/getCard",
        "message/send",
        "tasks/get",
        "tasks/list",
        "tasks/cancel",
    }
    if not required_mcp.issubset(profile["mcp"]["methods"]):
        failures.append({"code": "MCP_METHOD_PROFILE_INCOMPLETE"})
    if not required_a2a.issubset(profile["a2a"]["methods"]):
        failures.append({"code": "A2A_METHOD_PROFILE_INCOMPLETE"})

    required_sources = {
        "src/broker.rs": [
            "HUMAN_AUTHORIZATION_REQUIRED",
            "BOUNDED_DELTA_REFUSED",
            "actuation.applied",
            "actuation.refused",
        ],
        "src/mcp.rs": [
            '"initialize"',
            '"tools/list"',
            '"tools/call"',
            '"resources/read"',
        ],
        "src/main.rs": ["mcp-stdio", "a2a-jsonl", "JSON_RPC_PARSE_ERROR"],
        "src/model.rs": ["AutonomicPolicy", "EnterpriseTopology", "TeamNode"],
        "src/a2a.rs": [
            '"agent/getCard"',
            '"message/send"',
            '"tasks/cancel"',
            "AgentCard",
        ],
        "src/engine.rs": [
            "invoke_mcp_action",
            "submit_a2a_task",
            "zero_unreceipted_actuation",
            "receipt_chain_valid",
            "topology_cardinality_exact",
            "topology_digest",
        ],
        "src/autonomics.rs": ["wip-guard", "dependency-controller", "budget-watch"],
    }
    for relative, tokens in required_sources.items():
        path = ROOT / relative
        if not path.exists():
            failures.append({"code": "SOURCE_MISSING", "path": relative})
            continue
        text = path.read_text()
        missing = [token for token in tokens if token not in text]
        if missing:
            failures.append(
                {"code": "SOURCE_INVARIANT_MISSING", "path": relative, "tokens": missing}
            )
        evidence.append(
            {
                "kind": "source",
                "path": str(path.relative_to(REPO)),
                "sha256": sha256(path),
            }
        )

    cargo = shutil.which("cargo")
    runtime = {"standing": "UNSUPPORTED", "reason": "cargo not installed"}
    report = None
    self_test = None
    if cargo:
        command_set = [
            [cargo, "fmt", "--manifest-path", str(ROOT / "Cargo.toml"), "--", "--check"],
            [cargo, "test", "--manifest-path", str(ROOT / "Cargo.toml"), "--all-targets"],
        ]
        for command in command_set:
            result = run(command)
            commands.append(result)
            if result["returncode"]:
                failures.append(
                    {
                        "code": "COMMAND_FAILED",
                        "command": result["command"],
                        "stderr": result["stderr"],
                    }
                )

        output_dir = ROOT / "target" / "aps-safe-sim"
        output_dir.mkdir(parents=True, exist_ok=True)

        config_args = [
            "--config",
            str(ROOT / "config/fortune5-enterprise.json"),
            "--scenario",
            str(ROOT / "config/global-core-modernization.json"),
        ]
        fixture_expectations = [
            (
                "mcp-fixture",
                "fixtures/mcp_initialize.json",
                "/result/protocolVersion",
                "2025-11-25",
            ),
            (
                "mcp-fixture",
                "fixtures/mcp_rebalance.json",
                "/result/structuredContent/code",
                "CAPACITY_REBALANCED",
            ),
            (
                "mcp-fixture",
                "fixtures/mcp_budget_refusal.json",
                "/result/structuredContent/code",
                "HUMAN_AUTHORIZATION_REQUIRED",
            ),
            (
                "a2a-fixture",
                "fixtures/a2a_plan_pi.json",
                "/result/state",
                "completed",
            ),
            (
                "a2a-fixture",
                "fixtures/a2a_release_gate.json",
                "/result/state",
                "completed",
            ),
        ]
        fixture_outputs = {}
        for subcommand, fixture, pointer, expected in fixture_expectations:
            result = run(
                [
                    cargo,
                    "run",
                    "--quiet",
                    "--manifest-path",
                    str(ROOT / "Cargo.toml"),
                    "--",
                    subcommand,
                    *config_args,
                    "--request",
                    str(ROOT / fixture),
                ]
            )
            commands.append(result)
            if result["returncode"]:
                failures.append(
                    {
                        "code": "PROTOCOL_FIXTURE_EXECUTION_FAILED",
                        "fixture": fixture,
                        "stderr": result["stderr"],
                    }
                )
                continue
            response = json.loads(result["stdout"])
            fixture_outputs[fixture] = response
            observed = response
            for token in pointer.strip("/").split("/"):
                observed = observed.get(token) if isinstance(observed, dict) else None
            if observed != expected:
                failures.append(
                    {
                        "code": "PROTOCOL_FIXTURE_EXPECTATION_FAILED",
                        "fixture": fixture,
                        "pointer": pointer,
                        "expected": expected,
                        "observed": observed,
                    }
                )

        mcp_session_input = "\n".join(
            [
                json.dumps(load("fixtures/mcp_initialize.json")),
                json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "id": 9,
                        "method": "tools/list",
                        "params": {},
                    }
                ),
            ]
        ) + "\n"
        mcp_session = run(
            [
                cargo,
                "run",
                "--quiet",
                "--manifest-path",
                str(ROOT / "Cargo.toml"),
                "--",
                "mcp-stdio",
                *config_args,
            ],
            input_text=mcp_session_input,
        )
        commands.append(mcp_session)
        if mcp_session["returncode"]:
            failures.append(
                {"code": "MCP_STDIO_SESSION_FAILED", "stderr": mcp_session["stderr"]}
            )
        else:
            session_lines = [
                json.loads(line) for line in mcp_session["stdout"].splitlines() if line.strip()
            ]
            if len(session_lines) != 2 or len(
                session_lines[1].get("result", {}).get("tools", [])
            ) < 8:
                failures.append(
                    {"code": "MCP_STDIO_SESSION_INCOMPLETE", "responses": session_lines}
                )

        a2a_session_input = "\n".join(
            [
                json.dumps(load("fixtures/a2a_plan_pi.json")),
                json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "id": 10,
                        "method": "tasks/get",
                        "params": {"id": "a2a-task-000001"},
                    }
                ),
            ]
        ) + "\n"
        a2a_session = run(
            [
                cargo,
                "run",
                "--quiet",
                "--manifest-path",
                str(ROOT / "Cargo.toml"),
                "--",
                "a2a-jsonl",
                *config_args,
            ],
            input_text=a2a_session_input,
        )
        commands.append(a2a_session)
        if a2a_session["returncode"]:
            failures.append(
                {"code": "A2A_JSONL_SESSION_FAILED", "stderr": a2a_session["stderr"]}
            )
        else:
            session_lines = [
                json.loads(line) for line in a2a_session["stdout"].splitlines() if line.strip()
            ]
            if (
                len(session_lines) != 2
                or session_lines[1].get("result", {}).get("id") != "a2a-task-000001"
                or session_lines[1].get("result", {}).get("state") != "completed"
            ):
                failures.append(
                    {"code": "A2A_JSONL_SESSION_INCOMPLETE", "responses": session_lines}
                )

        report_path = output_dir / "simulation-report.json"
        simulate = run(
            [
                cargo,
                "run",
                "--quiet",
                "--manifest-path",
                str(ROOT / "Cargo.toml"),
                "--",
                "simulate",
                "--config",
                str(ROOT / "config/fortune5-enterprise.json"),
                "--scenario",
                str(ROOT / "config/global-core-modernization.json"),
                "--out",
                str(report_path),
            ]
        )
        commands.append(simulate)
        if simulate["returncode"]:
            failures.append(
                {
                    "code": "SIMULATION_EXECUTION_FAILED",
                    "stderr": simulate["stderr"],
                }
            )
        elif report_path.exists():
            report = json.loads(report_path.read_text())
            if report.get("standing") != "ALIVE":
                failures.append(
                    {"code": "SIMULATION_NOT_ALIVE", "standing": report.get("standing")}
                )
            if len(report.get("receipt_head", "")) != 64:
                failures.append({"code": "RECEIPT_HEAD_INVALID"})
            if len(report.get("topology_digest", "")) != 64:
                failures.append({"code": "TOPOLOGY_DIGEST_INVALID"})
            if not all(report.get("invariants", {}).values()):
                failures.append(
                    {"code": "SIMULATION_INVARIANT_FAILED", "invariants": report.get("invariants")}
                )

        self_test_path = output_dir / "self-test.json"
        self_test_run = run(
            [
                cargo,
                "run",
                "--quiet",
                "--manifest-path",
                str(ROOT / "Cargo.toml"),
                "--",
                "self-test",
                "--config",
                str(ROOT / "config/fortune5-enterprise.json"),
                "--scenario",
                str(ROOT / "config/global-core-modernization.json"),
            ]
        )
        commands.append({**self_test_run, "stdout": self_test_run["stdout"][-4000:]})
        if self_test_run["returncode"]:
            failures.append(
                {
                    "code": "SELF_TEST_FAILED",
                    "stderr": self_test_run["stderr"],
                    "stdout": self_test_run["stdout"],
                }
            )
        else:
            self_test_path.write_text(self_test_run["stdout"])
            self_test = json.loads(self_test_run["stdout"])
            if self_test.get("standing") != "ALIVE":
                failures.append({"code": "SELF_TEST_NOT_ALIVE"})
        runtime = {
            "standing": "ALIVE" if not failures else "BUILD_BROKEN",
            "cargo": subprocess.check_output([cargo, "--version"], text=True).strip(),
        }
    elif args.require_cargo:
        failures.append({"code": "CARGO_REQUIRED_BUT_UNAVAILABLE"})

    standing = "ALIVE" if not failures else "BLOCKED"
    receipt = {
        "schema": "aps.safe-simulation-verifier.v26.7.30",
        "standing": standing,
        "subject": "fortune5-safe-mcp-a2a-simulation",
        "protocols": {
            "mcp": profile["mcp"]["version"],
            "a2a": profile["a2a"]["version"],
        },
        "scale": scale,
        "runtime": runtime,
        "simulation": report,
        "self_test": self_test,
        "protocol_fixture_outputs": fixture_outputs if cargo else None,
        "commands": commands,
        "failures": failures,
        "evidence": evidence,
        "falsifiers": [
            "an autonomous budget reallocation must produce HUMAN_AUTHORIZATION_REQUIRED",
            "a capacity delta greater than five percent must produce BOUNDED_DELTA_REFUSED",
            "an unknown MCP method must produce MCP_METHOD_NOT_FOUND",
            "an unknown A2A skill must end in rejected state",
            "two runs at the same admitted coordinate must produce the same receipt head",
        ],
        "nonclaims": [
            "the fictional enterprise is not any real Fortune 5 company",
            "the semantic protocol profiles are not complete network conformance suites",
            "SAFe certification or affiliation is not claimed",
        ],
    }
    output = ROOT / args.out
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(
        json.dumps(
            {
                "standing": standing,
                "scale": scale,
                "runtime": runtime["standing"],
                "receipt": str(output.relative_to(ROOT)),
                "failures": failures,
            },
            indent=2,
        )
    )
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
