#!/usr/bin/env python3
"""Whole-repository verifier for APS v26.8.24.

This verifier qualifies repository coherence. It does not prove the long-horizon
enterprise-manufacturing hypothesis.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STANDING = {"ALIVE", "PARTIAL_ALIVE", "BLOCKED", "BUILD_BROKEN", "UNKNOWN", "UNSUPPORTED", "REFUSED"}
EXPECTED_TOP = {
    ".aps-syntax.md", ".claude", ".github", ".gitignore", "AGENTS.md", "CLAUDE.md",
    "CONTRIBUTING.md", "LICENSE", "MANIFEST.json", "Makefile", "README.md", "SECURITY.md",
    "archive", "contracts", "examples", "ontology", "receipts", "simulation",
    "specification-guide", "tests", "tools"
}
EXPECTED_CHAPTERS = [
    "00_source_admission_and_paradigm_reset.md",
    "01_chatmans_law.md",
    "02_fuller_ephemeralization_and_reconstitution.md",
    "03_jig_maturity.md",
    "04_dfcm_and_adversarial_manufacturing_search.md",
    "05_contract_first_ggen_first.md",
    "06_executable_enterprise_architecture.md",
    "07_universal_execution_and_process_intelligence.md",
    "08_software_manufacturing_capex.md",
    "09_governance_compression.md",
    "10_fortune500_economics.md",
    "11_adversarial_adoption_and_evolutionary_pressure.md",
    "12_board_and_organizational_operating_model.md",
    "13_aps_constitution.md",
    "14_conformance_metrology_and_replay.md",
    "15_falsifiers_and_research_agenda.md",
    "16_autonomic_manufacturing_manifesto.md",
]
STALE_PATH_MARKERS = (
    "v26_7_", "V26_7_", "fortune5-safe", ".aps-enterprise-bootstrap",
    "work_order.schema", "ggen-v26.7.62", "ggen-enterprise-architecture-v26.7.31"
)
# Split historical literals so the verifier does not self-match its own blacklist.
STALE_CONTENT_MARKERS = (
    "Current candidate: " + "v26." + "7",
    "APS " + "v26." + "7.30",
    "APS " + "v26." + "7.31",
    "comprehensive framework and documentation standard " + "designed for agile software development",
)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def active_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        parts = path.relative_to(ROOT).parts
        if ".git" in parts or (parts and parts[0] == "archive"):
            continue
        yield path


def text_file(path: Path) -> bool:
    return path.suffix.lower() in {".md", ".json", ".py", ".yml", ".yaml", ".toml", ".ttl", ".css", ".txt"} or path.name == "Makefile"


def load_json(path: Path, failures: list[str]):
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        failures.append(f"invalid JSON {rel(path)}: {exc}")
        return None


def verify_repository() -> tuple[list[str], dict]:
    failures: list[str] = []

    actual_top = {p.name for p in ROOT.iterdir() if p.name != ".git"}
    missing = sorted(EXPECTED_TOP - actual_top)
    extra = sorted(actual_top - EXPECTED_TOP)
    if missing:
        failures.append(f"missing top-level surfaces: {missing}")
    if extra:
        failures.append(f"unadmitted top-level surfaces: {extra}")

    for path in active_files():
        rp = rel(path)
        if any(marker in rp for marker in STALE_PATH_MARKERS):
            failures.append(f"stale active path: {rp}")
        if text_file(path):
            try:
                text = path.read_text()
            except UnicodeDecodeError:
                failures.append(f"non-UTF8 active text surface: {rp}")
                continue
            for marker in STALE_CONTENT_MARKERS:
                if marker in text:
                    failures.append(f"stale active content marker {marker!r} in {rp}")

    version_dir = ROOT / "specification-guide/src/v26_8_24"
    actual_chapters = sorted(p.name for p in version_dir.glob("*.md")) if version_dir.exists() else []
    if actual_chapters != EXPECTED_CHAPTERS:
        failures.append(f"chapter set mismatch: expected {EXPECTED_CHAPTERS}, got {actual_chapters}")

    summary = (ROOT / "specification-guide/src/SUMMARY.md").read_text()
    for chapter in EXPECTED_CHAPTERS:
        if f"v26_8_24/{chapter}" not in summary:
            failures.append(f"SUMMARY missing {chapter}")

    jig = (version_dir / "03_jig_maturity.md").read_text()
    levels = re.findall(r"^### L([1-5]) — ", jig, flags=re.MULTILINE)
    if levels != ["1", "2", "3", "4", "5"]:
        failures.append(f"jig maturity must be exactly five levels L1-L5; got {levels}")
    if re.search(r"^### (?:L0\b|Level 0\b)", jig, flags=re.MULTILINE):
        failures.append("jig maturity defines forbidden sixth baseline L0")
    dimensions = [
        "Product knowledge", "Work positioning", "Operation guidance", "Process sequence",
        "Error prevention", "Measurement & qualification", "Adaptation & learning"
    ]
    for dimension in dimensions:
        if f"| {dimension} |" not in jig:
            failures.append(f"jig matrix missing dimension: {dimension}")

    constitution = (version_dir / "13_aps_constitution.md").read_text()
    for phrase in [
        "Everything is sunk", "Preserve truth, not implementations", "Zero continuation privilege",
        "Zero uninformed elimination", "Contract before implementation", "No ambient DO authority",
        "Zero unreceipted actuation", "No prose outranks evidence", "factory itself must remain reconstitutable"
    ]:
        if phrase not in constitution:
            failures.append(f"constitution missing invariant: {phrase}")

    ggen = (version_dir / "05_contract_first_ggen_first.md").read_text()
    for phrase in [
        "Known pattern? Compose it.",
        "Known tool? Generate its invocation.",
        "Novel mechanism? Discover it once, then teach the factory.",
        "Application =", "Library ="
    ]:
        if phrase not in ggen:
            failures.append(f"ggen-first chapter missing doctrine: {phrase}")

    core_ontology = (ROOT / "ontology/aps-core.ttl").read_text()
    for marker in [
        "http://www.w3.org/ns/prov#", "http://www.w3.org/ns/odrl/2/",
        "http://www.w3.org/ns/shacl#", "http://www.w3.org/ns/dqv#"
    ]:
        if marker not in core_ontology:
            failures.append(f"core ontology missing public vocabulary {marker}")
    fibo = (ROOT / "ontology/fortune500-fibo-profile.ttl").read_text()
    if "https://spec.edmcouncil.org/fibo/ontology/master/latest/BE/LegalEntities/LegalPersons/" not in fibo:
        failures.append("FIBO profile missing admitted LegalPersons import")

    for schema_path in sorted((ROOT / "contracts").glob("*.schema.json")):
        schema = load_json(schema_path, failures)
        if schema and not all(k in schema for k in ("$schema", "$id", "type")):
            failures.append(f"schema lacks required meta fields: {rel(schema_path)}")

    enterprise = load_json(ROOT / "examples/fortune500-fibo/enterprise.json", failures)
    contract = load_json(ROOT / "examples/fortune500-fibo/knowledge-contract.json", failures)
    reconstitution = load_json(ROOT / "examples/fortune500-fibo/reconstitution.json", failures)
    events = load_json(ROOT / "examples/fortune500-fibo/process-events.json", failures)
    manifest = load_json(ROOT / "MANIFEST.json", failures)
    if enterprise and enterprise.get("evidenceClass") != "SYNTHETIC_SENSITIVITY_MODEL_NOT_FORECAST":
        failures.append("Fortune-500 example must remain explicitly synthetic")
    if contract and contract.get("standingRule") not in STANDING:
        failures.append("example contract uses invalid standing")
    if reconstitution and len(reconstitution.get("candidateStrategies", [])) < 3:
        failures.append("reconstitution example lacks DfCM strategy breadth")
    if events:
        for i, event in enumerate(events):
            for key in ("eventId", "activity", "time", "objects", "authorityRef", "receiptRef"):
                if key not in event:
                    failures.append(f"process event {i} missing {key}")
    if manifest:
        if manifest.get("version") != "26.8.24":
            failures.append("MANIFEST version mismatch")
        if manifest.get("predecessor", {}).get("commit") != "ab04337b2db63c66fa23c217bf76622fc9c73b6d":
            failures.append("MANIFEST predecessor coordinate mismatch")

    if (ROOT / "specification-guide/book").exists() or (ROOT / "specification-guide/dist").exists():
        failures.append("generated book/dist outputs must not be committed as active source")

    authority_paths = [
        ROOT / "MANIFEST.json", ROOT / ".aps-syntax.md",
        ROOT / "ontology/aps-core.ttl", ROOT / "ontology/jig-maturity.ttl",
        ROOT / "ontology/fortune500-fibo-profile.ttl",
        *sorted((ROOT / "contracts").glob("*.json")),
        *[version_dir / name for name in EXPECTED_CHAPTERS],
    ]
    digest = hashlib.sha256()
    checked = []
    for path in authority_paths:
        if not path.exists():
            continue
        data = path.read_bytes()
        digest.update(rel(path).encode() + b"\0" + data + b"\0")
        checked.append({"path": rel(path), "sha256": hashlib.sha256(data).hexdigest()})

    receipt = {
        "schema": "aps.repository-verification.v26.8.24",
        "standing": "ALIVE" if not failures else "REFUSED",
        "scope": "repository-coherence-not-crown-hypothesis",
        "authoritySetSha256": digest.hexdigest(),
        "checkedAuthorityFiles": checked,
        "failures": failures,
        "nonClaims": [
            "ALIVE here means the repository satisfies its declared structural constitution.",
            "It does not prove Fortune-500 semantic closure, economic dominance, or safe universal actuation."
        ]
    }
    return failures, receipt


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--no-receipt", action="store_true")
    args = parser.parse_args()
    failures, receipt = verify_repository()
    if args.receipt and not args.no_receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if failures:
        for failure in failures:
            print(f"REFUSED: {failure}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
