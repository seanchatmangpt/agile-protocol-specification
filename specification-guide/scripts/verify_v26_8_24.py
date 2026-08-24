#!/usr/bin/env python3
"""Verify the APS v26.8.24 candidate source set without external dependencies."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "specification-guide" / "src"
VERSION = SRC / "v26_8_24"
RECEIPTS = ROOT / "receipts"

FILES = [
    "00_source_admission_and_paradigm_reset.md",
    "01_chatmans_law.md",
    "02_fuller_ephemeralization_and_reconstitution.md",
    "03_jig_maturity.md",
    "04_dfcm_and_adversarial_manufacturing_search.md",
    "05_executable_enterprise_architecture.md",
    "06_universal_execution_and_process_intelligence.md",
    "07_governance_compression.md",
    "08_fortune500_economics.md",
    "09_aps_constitution.md",
    "10_falsifiers_and_research_agenda.md",
]

REQUIRED_PHRASES = {
    "01_chatmans_law.md": ["Chatman's Law", "zero preservation privilege"],
    "02_fuller_ephemeralization_and_reconstitution.md": ["Zero uninformed elimination", "reconstitutable"],
    "03_jig_maturity.md": ["Level 0", "Level 5", "seven independent dimensions"],
    "04_dfcm_and_adversarial_manufacturing_search.md": ["Design for Combinatorial Maximalism", "candidate falsifier"],
    "05_executable_enterprise_architecture.md": ["semantic-operational closure", "AshR2RML"],
    "06_universal_execution_and_process_intelligence.md": ["Process conformance is not process fitness", "OCEL"],
    "07_governance_compression.md": ["Validate manufacturing law", "once per admitted version"],
    "08_fortune500_economics.md": ["enterprise code = current inventory", "Knowledge Leverage"],
    "09_aps_constitution.md": ["Zero unreceipted actuation", "SELECT / CONSTRUCT / DO"],
    "10_falsifiers_and_research_agenda.md": ["Crown hypothesis", "Failure of the paradigm itself"],
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    failures: list[str] = []
    hashes: dict[str, str] = {}

    summary = (SRC / "SUMMARY.md").read_text(encoding="utf-8")
    if "v26_7_30/" in summary:
        failures.append("SUMMARY.md still routes active navigation through v26_7_30")

    for name in FILES:
        path = VERSION / name
        if not path.is_file():
            failures.append(f"missing canonical source: {name}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("# "):
            failures.append(f"{name}: missing H1 title")
        if len(text.strip()) < 800:
            failures.append(f"{name}: suspiciously small candidate chapter")
        for phrase in REQUIRED_PHRASES.get(name, []):
            if phrase not in text:
                failures.append(f"{name}: missing constitutional phrase {phrase!r}")
        if f"v26_8_24/{name}" not in summary:
            failures.append(f"SUMMARY.md does not route to {name}")
        hashes[name] = digest(path)

    readme = ROOT / "README.md"
    syntax = ROOT / ".aps-syntax.md"
    claude = ROOT / "CLAUDE.md"
    for path, phrase in [
        (readme, "Chatman's Law"),
        (syntax, "everything is sunk"),
        (claude, "Zero continuation privilege"),
    ]:
        if not path.is_file() or phrase not in path.read_text(encoding="utf-8"):
            failures.append(f"{path.relative_to(ROOT)} missing required v26.8.24 doctrine")
        elif path.is_file():
            hashes[str(path.relative_to(ROOT))] = digest(path)

    archive = ROOT / "archive" / "pre-v26.8.24"
    if not archive.exists():
        failures.append("pre-v26.8.24 archive tree is missing")

    receipt = {
        "schema": "aps-v26.8.24-source-verifier.v1",
        "candidate": "v26.8.24",
        "status": "ALIVE" if not failures else "REFUSED",
        "source_hashes_sha256": dict(sorted(hashes.items())),
        "failures": failures,
        "claim": "current candidate source set is structurally coherent and contains required constitutional anchors",
        "nonclaim": "this verifier does not prove the enterprise-manufacturing crown hypothesis",
    }
    RECEIPTS.mkdir(parents=True, exist_ok=True)
    out = RECEIPTS / "APS-v26.8.24-source-verifier.json"
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if failures:
        for failure in failures:
            print(f"REFUSED: {failure}")
        return 1

    print(f"ALIVE: verified {len(FILES)} v26.8.24 chapters; receipt={out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
