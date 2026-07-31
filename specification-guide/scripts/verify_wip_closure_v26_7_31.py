#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
RECEIPT = ROOT / "receipts" / "APS-v26.7.31-wip-closure.json"
REQUIRED_FILES = [
    ".aps-syntax.md", "APS_V26_7_31_RELEASE_NOTES.md", "README.md", "specification-guide/book.toml",
    "specification-guide/src/SUMMARY.md", "specification-guide/scripts/verify_ggen_v26_7_31.py",
    "specification-guide/scripts/verify_ea_strategy_v26_7_31.py", "specification-guide/scripts/verify_v26_7_31.py",
    "specification-guide/scripts/verify_wip_closure_v26_7_31.py", "simulation/fortune5-safe/Cargo.toml",
    "simulation/fortune5-safe/scripts/verify.py", ".github/workflows/converge-fortune5-safe.yml",
    ".github/workflows/verify-fortune5-safe-sim.yml", ".github/workflows/verify-ggen-standard.yml",
    ".github/workflows/verify-ea-strategy-v26.7.31.yml", ".github/workflows/verify-wip-closure-v26.7.31.yml",
]
OBSOLETE_PATHS = [
    ".aps-bootstrap", ".aps-safe-bootstrap", ".aps-enterprise-bootstrap",
    ".github/workflows/publish-aps-v26.7.30.yml",
]
SCAN_ROOTS = [
    ".aps-syntax.md", "README.md", "APS_V26_7_31_RELEASE_NOTES.md", "specification-guide/src",
    "specification-guide/scripts", "specification-guide/standards", "simulation/fortune5-safe/src",
    "simulation/fortune5-safe/tests", "simulation/fortune5-safe/scripts", ".github/workflows",
]
MARKER_RE = re.compile(r"(?i)(?<![A-Za-z0-9_])(TODO|FIXME|TBD|XXX|HACK)(?![A-Za-z0-9_])")
USES_RE = re.compile(r"(?m)^\s*-?\s*uses:\s*([^\s@]+)@([^\s#]+)")
SUMMARY_LINK_RE = re.compile(r"^\s*[-*]\s+\[[^]]+\]\([^)]+\.md\)\s*$", re.MULTILINE)
SUMMARY_TOP_RE = re.compile(r"^[-*]\s+\[[^]]+\]\([^)]+\.md\)\s*$", re.MULTILINE)


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def iter_scan_files() -> list[Path]:
    result: set[Path] = set()
    for item in SCAN_ROOTS:
        path = ROOT / item
        if not path.exists(): continue
        if path.is_file(): result.add(path); continue
        for candidate in path.rglob("*"):
            if not candidate.is_file(): continue
            rel = relative(candidate)
            if rel.startswith("specification-guide/book/") or "/target/" in rel: continue
            if candidate.suffix.lower() not in {".md", ".py", ".json", ".yml", ".yaml", ".rs", ".toml"}: continue
            result.add(candidate)
    return sorted(result, key=relative)


def source_set_digest(paths: list[Path]) -> str:
    hasher = hashlib.sha256()
    for path in sorted(set(paths), key=relative):
        label = relative(path).encode(); content = path.read_bytes()
        hasher.update(len(label).to_bytes(8, "big")); hasher.update(label)
        hasher.update(len(content).to_bytes(8, "big")); hasher.update(content)
    return hasher.hexdigest()


def main() -> int:
    failures: list[dict] = []
    evidence_paths: list[Path] = []
    for item in REQUIRED_FILES:
        path = ROOT / item
        if not path.exists(): failures.append({"code": "REQUIRED_FILE_MISSING", "path": item})
        elif not path.is_file() or path.stat().st_size == 0: failures.append({"code": "REQUIRED_FILE_EMPTY", "path": item})
        else: evidence_paths.append(path)
    for item in OBSOLETE_PATHS:
        if (ROOT / item).exists(): failures.append({"code": "OBSOLETE_SURFACE_PRESENT", "path": item})
    syntax = ROOT / ".aps-syntax.md"
    if syntax.exists() and syntax.stat().st_size < 2500: failures.append({"code": "APS_SYNTAX_NOT_SUBSTANTIVE", "bytes": syntax.stat().st_size})
    summary_path = ROOT / "specification-guide/src/SUMMARY.md"
    if summary_path.exists():
        summary = summary_path.read_text(); top = len(SUMMARY_TOP_RE.findall(summary)); total = len(SUMMARY_LINK_RE.findall(summary))
        if top != 18 or total != 19: failures.append({"code": "SUMMARY_TOPOLOGY", "top_level": top, "total": total})
    readme = ROOT / "README.md"
    if readme.exists():
        text = readme.read_text()
        for phrase in [
            "Current candidate:** v26.7.31", "Last immutable published projection:** v26.7.30",
            "They do not repair source, commit generated files, or push the PR branch.",
            "verify_wip_closure_v26_7_31.py",
        ]:
            if phrase not in text: failures.append({"code": "README_RELEASE_BOUNDARY_MISSING", "phrase": phrase})
    for path in iter_scan_files():
        rel = relative(path); text = path.read_text(errors="replace")
        if rel.endswith("verify_wip_closure_v26_7_31.py"): continue
        matches = sorted(set(match.group(1).upper() for match in MARKER_RE.finditer(text)))
        if matches: failures.append({"code": "ACTIVE_WIP_MARKER", "path": rel, "markers": matches})
        evidence_paths.append(path)

    workflows = sorted((ROOT / ".github/workflows").glob("*.yml")) + sorted((ROOT / ".github/workflows").glob("*.yaml"))
    required_commands = {
        ".github/workflows/converge-fortune5-safe.yml": [
            "verify_ggen_v26_7_31.py", "verify_ea_strategy_v26_7_31.py", "verify_v26_7_31.py",
            "verify_wip_closure_v26_7_31.py", "simulation/fortune5-safe/scripts/verify.py --require-cargo",
        ],
    }
    forbidden = ["git commit", "git push", "git pull --rebase", "contents: write", "sed -i", "Repair admitted source", "Admit digest-pinned"]
    for path in workflows:
        rel = relative(path); text = path.read_text()
        for action, revision in USES_RE.findall(text):
            if not re.fullmatch(r"[0-9a-f]{40}", revision):
                failures.append({"code": "MUTABLE_ACTION_REFERENCE", "path": rel, "action": action, "revision": revision})
        for fragment in forbidden:
            if fragment in text: failures.append({"code": "WORKFLOW_SELF_MUTATION", "path": rel, "fragment": fragment})
        for command in required_commands.get(rel, []):
            if command not in text: failures.append({"code": "CROWN_COMMAND_MISSING", "path": rel, "command": command})
        evidence_paths.append(path)

    subject = source_set_digest(evidence_paths) if evidence_paths else hashlib.sha256(b"").hexdigest()
    standing = "ALIVE" if not failures else "BLOCKED"
    report = {
        "schema": "aps.wip-closure.receipt.v26.7.31", "operation_id": "aps-v26.7.31-wip-closure",
        "subject": "sha256:" + subject,
        "coordinate": {
            "source": "seanchatmangpt/agile-protocol-specification", "revision_kind": "SOURCE_SET",
            "revision": "sha256:" + subject, "command": "python3 specification-guide/scripts/verify_wip_closure_v26_7_31.py",
            "toolchain_contract": "python>=3.11",
        },
        "standing": standing,
        "metrics": {"required_files": len(REQUIRED_FILES), "obsolete_paths": len(OBSOLETE_PATHS), "workflows": len(workflows), "scanned_files": len(set(evidence_paths)), "failures": len(failures)},
        "failures": failures,
        "evidence": [{"path": relative(path), "sha256": digest(path)} for path in sorted(set(evidence_paths), key=relative) if path.exists() and path.is_file()],
        "replay": {"command": "python3 specification-guide/scripts/verify_wip_closure_v26_7_31.py", "expected": "MATCH_AT_SAME_SOURCE_SET"},
        "nonclaims": [
            "ALIVE means no active WIP surfaces matched this declared repository contract.",
            "Historical conversation archives and generated mdBook output are excluded from marker scanning.",
            "External GitHub runner availability and queued checks remain separate standing dimensions.",
            "No production actuation authority is granted.",
        ],
    }
    RECEIPT.parent.mkdir(exist_ok=True); RECEIPT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"standing": standing, **report["metrics"], "failures_detail": failures}, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
