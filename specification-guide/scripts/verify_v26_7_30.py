#!/usr/bin/env python3
from pathlib import Path
import collections
import hashlib
import json
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "specification-guide" / "src"
SUMMARY = SRC / "SUMMARY.md"
RECEIPTS = ROOT / "receipts"
RECEIPTS.mkdir(exist_ok=True)

failures = []
evidence = []
links = re.findall(r"\[[^]]+\]\(([^)]+\.md)\)", SUMMARY.read_text())
if len(links) < 16:
    failures.append({"code": "SUMMARY_INCOMPLETE", "observed": len(links), "minimum": 16})

paragraphs = []
files = []
total_words = 0
for relative in links:
    path = SRC / relative
    if not path.exists():
        failures.append({"code": "CHAPTER_MISSING", "path": relative})
        continue
    text = path.read_text()
    files.append(path)
    words = len(re.findall(r"\b[\w'–-]+\b", text))
    total_words += words
    h1_count = len(re.findall(r"(?m)^# ", text))
    if h1_count != 1:
        failures.append({"code": "H1_CARDINALITY", "path": relative, "observed": h1_count})
    minimum = 500 if relative.startswith("v26_7_30/") else 350
    if words < minimum:
        failures.append(
            {
                "code": "CHAPTER_NOT_SUBSTANTIVE",
                "path": relative,
                "words": words,
                "minimum": minimum,
            }
        )
    for paragraph in re.split(r"\n\s*\n", text):
        normalized = " ".join(paragraph.split())
        if len(normalized.split()) >= 30 and not normalized.startswith("```"):
            paragraphs.append(normalized)
    evidence.append(
        {
            "kind": "chapter",
            "path": relative,
            "words": words,
            "sha256": hashlib.sha256(text.encode()).hexdigest(),
        }
    )

corpus = "\n".join(path.read_text() for path in files)
required_phrases = [
    "A = μ(O*)",
    "R ⊢ A = μ(O*)",
    "SELECT is not DO",
    "Zero unreceipted actuation",
    "APS and Gall solve adjacent but non-equivalent problems",
    "PARTIAL_ALIVE",
    "ALIVE",
    "BLOCKED",
    "BUILD_BROKEN",
    "UNKNOWN",
    "UNSUPPORTED",
    "same-object falsifier",
    "evidence coordinate",
    "MCP and A2A",
    "HUMAN_AUTHORIZATION_REQUIRED",
]
for phrase in required_phrases:
    if phrase not in corpus:
        failures.append({"code": "INVARIANT_MISSING", "phrase": phrase})

counts = collections.Counter(paragraphs)
duplicate_count = sum(count - 1 for count in counts.values() if count > 1)
duplicate_ratio = duplicate_count / max(1, len(paragraphs))
if duplicate_ratio > 0.12:
    failures.append({"code": "BOILERPLATE_RATIO_EXCEEDED", "ratio": duplicate_ratio})

requirement_ids = re.findall(r"\*\*Requirement ([A-Z0-9-]+)\.\*\*", corpus)
duplicate_requirements = [
    identifier for identifier, count in collections.Counter(requirement_ids).items() if count > 1
]
if duplicate_requirements:
    failures.append({"code": "DUPLICATE_REQUIREMENT_IDS", "ids": duplicate_requirements})

for schema_name in ["work_order.schema.json", "receipt.schema.json"]:
    path = ROOT / "specification-guide" / "schemas" / schema_name
    try:
        json.loads(path.read_text())
    except Exception as error:
        failures.append({"code": "SCHEMA_INVALID", "path": schema_name, "error": str(error)})
    else:
        evidence.append(
            {
                "kind": "schema",
                "path": str(path.relative_to(ROOT)),
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            }
        )

structured_inputs = [
    "specification-guide/examples/aps_v26_7_30_mcp_a2a_safe_work_order.json",
    "simulation/fortune5-safe/config/fortune5-enterprise.json",
    "simulation/fortune5-safe/config/global-core-modernization.json",
    "simulation/fortune5-safe/config/protocol-profile.json",
]
loaded = {}
for relative in structured_inputs:
    path = ROOT / relative
    try:
        loaded[relative] = json.loads(path.read_text())
    except Exception as error:
        failures.append({"code": "STRUCTURED_INPUT_INVALID", "path": relative, "error": str(error)})
    else:
        evidence.append(
            {
                "kind": "structured-input",
                "path": relative,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            }
        )

profile = loaded.get("simulation/fortune5-safe/config/protocol-profile.json", {})
if profile:
    if profile.get("mcp", {}).get("version") != "2025-11-25":
        failures.append({"code": "MCP_VERSION_MISMATCH"})
    if profile.get("a2a", {}).get("version") != "1.0.0":
        failures.append({"code": "A2A_VERSION_MISMATCH"})

enterprise = loaded.get("simulation/fortune5-safe/config/fortune5-enterprise.json", {})
if enterprise:
    teams = (
        enterprise.get("portfolios", 0)
        * enterprise.get("value_streams_per_portfolio", 0)
        * enterprise.get("solution_trains_per_value_stream", 0)
        * enterprise.get("arts_per_solution_train", 0)
        * enterprise.get("teams_per_art", 0)
    )
    if teams < 500:
        failures.append({"code": "FORTUNE5_SCALE_FLOOR_NOT_MET", "teams": teams})

simulation_sources = [
    "simulation/fortune5-safe/Cargo.toml",
    "simulation/fortune5-safe/src/model.rs",
    "simulation/fortune5-safe/src/ledger.rs",
    "simulation/fortune5-safe/src/broker.rs",
    "simulation/fortune5-safe/src/autonomics.rs",
    "simulation/fortune5-safe/src/engine.rs",
    "simulation/fortune5-safe/src/mcp.rs",
    "simulation/fortune5-safe/src/a2a.rs",
    "simulation/fortune5-safe/src/main.rs",
    "simulation/fortune5-safe/tests/protocols.rs",
    "simulation/fortune5-safe/scripts/verify.py",
]
for relative in simulation_sources:
    path = ROOT / relative
    if not path.exists():
        failures.append({"code": "SIMULATION_SOURCE_MISSING", "path": relative})
        continue
    evidence.append(
        {
            "kind": "simulation-source",
            "path": relative,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }
    )

if any("/book/" in str(path) for path in files):
    failures.append({"code": "GENERATED_OUTPUT_IN_SOURCE_MANIFEST"})

mdbook = shutil.which("mdbook")
render = {"standing": "UNSUPPORTED", "reason": "mdbook not installed"}
if mdbook:
    result = subprocess.run(
        [mdbook, "build"],
        cwd=ROOT / "specification-guide",
        text=True,
        capture_output=True,
    )
    render = {
        "standing": "ALIVE" if result.returncode == 0 else "BUILD_BROKEN",
        "returncode": result.returncode,
        "stdout": result.stdout[-2000:],
        "stderr": result.stderr[-2000:],
    }
    if result.returncode:
        failures.append({"code": "MDBOOK_BUILD_FAILED"})

standing = "ALIVE" if not failures else "BLOCKED"
receipt = {
    "schema": "aps.receipt.v26.7.30",
    "operation_id": "aps-v26.7.30-book-verifier",
    "subject": "sha256:" + hashlib.sha256(corpus.encode()).hexdigest(),
    "coordinate": {
        "source": "seanchatmangpt/agile-protocol-specification",
        "revision": "WORKTREE",
        "command": "python3 specification-guide/scripts/verify_v26_7_30.py",
        "toolchain": sys.version.split()[0],
        "environment": sys.platform,
    },
    "standing": standing,
    "metrics": {
        "chapters": len(files),
        "words": total_words,
        "long_paragraphs": len(paragraphs),
        "duplicate_paragraph_ratio": duplicate_ratio,
        "simulation_sources": len(simulation_sources),
    },
    "render": render,
    "failures": failures,
    "evidence": evidence,
    "lineage": {
        "parents": ["7a713c199e23f7b24b4c2d0d80a86996dd106f5c"],
        "supersedes": ["heading-only mdBook source scaffold"],
    },
    "replay": {
        "command": "python3 specification-guide/scripts/verify_v26_7_30.py",
        "expected": "MATCH",
    },
    "nonclaims": [
        "ALIVE is bounded to the checks recorded here",
        "mdBook rendering is separate when the tool is unavailable",
        "runtime simulation standing is assigned by the Rust simulation verifier",
        "no real Fortune 5 company is represented",
    ],
}
out = RECEIPTS / "APS-v26.7.30-verifier.json"
out.write_text(json.dumps(receipt, indent=2) + "\n")
print(
    json.dumps(
        {
            "standing": standing,
            "chapters": len(files),
            "words": total_words,
            "duplicate_paragraph_ratio": duplicate_ratio,
            "mdbook": render["standing"],
            "simulation_sources": len(simulation_sources),
            "receipt": str(out.relative_to(ROOT)),
            "failures": failures,
        },
        indent=2,
    )
)
sys.exit(0 if not failures else 1)
