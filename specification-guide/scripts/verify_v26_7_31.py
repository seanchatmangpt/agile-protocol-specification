#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "specification-guide" / "src"
SUMMARY = SRC / "SUMMARY.md"
RECEIPT = ROOT / "receipts" / "APS-v26.7.31-book-verifier.json"
EXPECTED_TOP_LEVEL = 18
EXPECTED_TOTAL_LINKS = 19
MINIMUM_WORDS = 500
INCLUDE_RE = re.compile(r"\{\{#include\s+([^}\s:]+)(?::[^}\s]+)?\s*\}\}")
LINK_RE = re.compile(r"^\s*[-*]\s+\[[^]]+\]\(([^)]+\.md)\)\s*$", re.MULTILINE)
TOP_LINK_RE = re.compile(r"^[-*]\s+\[[^]]+\]\(([^)]+\.md)\)\s*$", re.MULTILINE)
WORD_RE = re.compile(r"\b[\w'’–-]+\b")
REQUIRED_PHRASES = [
    "A = μ(O*)", "R ⊢ A = μ(O*)", "SELECT is not DO", "Zero unreceipted actuation",
    "APS and Gall solve adjacent but non-equivalent problems", "PARTIAL_ALIVE", "ALIVE",
    "BLOCKED", "BUILD_BROKEN", "UNKNOWN", "UNSUPPORTED", "same-object falsifier",
    "evidence coordinate", "MCP and A2A", "HUMAN_AUTHORIZATION_REQUIRED",
    "ggen Manufacturing, Building Blocks, and Release Law", "Enterprise Architecture as Strategy with ggen",
    "Evidence-Bearing Self-Governance", "Stage 5 is a ggen extension", "GGEN-EA-CROWN",
]
SCHEMAS = [
    "specification-guide/schemas/work_order.schema.json",
    "specification-guide/schemas/receipt.schema.json",
]
STRUCTURED_INPUTS = [
    "specification-guide/examples/aps_v26_7_30_mcp_a2a_safe_work_order.json",
    "simulation/fortune5-safe/config/fortune5-enterprise.json",
    "simulation/fortune5-safe/config/global-core-modernization.json",
    "simulation/fortune5-safe/config/protocol-profile.json",
    "specification-guide/standards/ggen-v26.7.62.json",
    "specification-guide/standards/ggen-enterprise-architecture-v26.7.31.json",
]
SIMULATION_SOURCES = [
    "simulation/fortune5-safe/Cargo.toml", "simulation/fortune5-safe/Cargo.lock",
    "simulation/fortune5-safe/src/model.rs", "simulation/fortune5-safe/src/ledger.rs",
    "simulation/fortune5-safe/src/broker.rs", "simulation/fortune5-safe/src/autonomics.rs",
    "simulation/fortune5-safe/src/engine.rs", "simulation/fortune5-safe/src/mcp.rs",
    "simulation/fortune5-safe/src/a2a.rs", "simulation/fortune5-safe/src/main.rs",
    "simulation/fortune5-safe/tests/protocols.rs", "simulation/fortune5-safe/scripts/verify.py",
]


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_set_digest(paths: list[Path]) -> str:
    hasher = hashlib.sha256()
    for path in sorted(set(paths), key=relative):
        label = relative(path).encode()
        content = path.read_bytes()
        hasher.update(len(label).to_bytes(8, "big")); hasher.update(label)
        hasher.update(len(content).to_bytes(8, "big")); hasher.update(content)
    return hasher.hexdigest()


def expand_markdown(path: Path, stack: tuple[Path, ...] = ()) -> tuple[str, list[Path]]:
    resolved = path.resolve()
    src_root = SRC.resolve()
    if resolved != src_root and src_root not in resolved.parents:
        raise ValueError(f"INCLUDE_ESCAPES_SOURCE_ROOT:{relative(path)}")
    if resolved in stack:
        cycle = " -> ".join(relative(item) for item in (*stack, resolved))
        raise ValueError(f"INCLUDE_CYCLE:{cycle}")
    text = path.read_text()
    dependencies = [path]

    def replace(match: re.Match[str]) -> str:
        include = (path.parent / match.group(1)).resolve()
        if include != src_root and src_root not in include.parents:
            raise ValueError(f"INCLUDE_ESCAPES_SOURCE_ROOT:{match.group(1)}")
        if not include.exists() or not include.is_file():
            raise ValueError(f"INCLUDE_MISSING:{include.relative_to(ROOT)}")
        expanded, nested = expand_markdown(include, (*stack, resolved))
        dependencies.extend(nested)
        return expanded

    return INCLUDE_RE.sub(replace, text), dependencies


def main() -> int:
    failures: list[dict] = []
    evidence_paths: list[Path] = []
    chapter_evidence: list[dict] = []
    paragraphs: list[str] = []
    expanded_chapters: list[str] = []
    total_words = 0
    if not SUMMARY.exists():
        failures.append({"code": "SUMMARY_MISSING"}); summary = ""
    else:
        summary = SUMMARY.read_text(); evidence_paths.append(SUMMARY)
    links = LINK_RE.findall(summary)
    top_level = TOP_LINK_RE.findall(summary)
    if len(top_level) != EXPECTED_TOP_LEVEL:
        failures.append({"code": "SUMMARY_TOP_LEVEL_COUNT", "observed": len(top_level), "expected": EXPECTED_TOP_LEVEL})
    if len(links) != EXPECTED_TOTAL_LINKS:
        failures.append({"code": "SUMMARY_TOTAL_LINK_COUNT", "observed": len(links), "expected": EXPECTED_TOTAL_LINKS})
    if len(links) != len(set(links)):
        failures.append({"code": "SUMMARY_DUPLICATE_LINK", "links": links})

    for link in links:
        path = SRC / link
        if not path.exists():
            failures.append({"code": "CHAPTER_MISSING", "path": link}); continue
        try:
            expanded, dependencies = expand_markdown(path)
        except ValueError as error:
            failures.append({"code": "MDBOOK_INCLUDE_REFUSED", "path": link, "error": str(error)}); continue
        expanded_chapters.append(expanded); evidence_paths.extend(dependencies)
        words = len(WORD_RE.findall(expanded)); total_words += words
        h1_count = len(re.findall(r"(?m)^# ", expanded))
        if h1_count != 1: failures.append({"code": "H1_CARDINALITY", "path": link, "observed": h1_count})
        if words < MINIMUM_WORDS: failures.append({"code": "CHAPTER_NOT_SUBSTANTIVE", "path": link, "words": words, "minimum": MINIMUM_WORDS})
        for paragraph in re.split(r"\n\s*\n", expanded):
            normalized = " ".join(paragraph.split())
            if len(normalized.split()) >= 30 and not normalized.startswith("```"): paragraphs.append(normalized)
        chapter_evidence.append({
            "kind": "expanded-chapter", "path": link, "words": words,
            "source_files": sorted({relative(item) for item in dependencies}),
            "sha256": hashlib.sha256(expanded.encode()).hexdigest(),
        })

    corpus = "\n".join(expanded_chapters); folded = corpus.casefold()
    for phrase in REQUIRED_PHRASES:
        if phrase.casefold() not in folded: failures.append({"code": "INVARIANT_MISSING", "phrase": phrase})
    counts = Counter(paragraphs)
    duplicate_count = sum(count - 1 for count in counts.values() if count > 1)
    duplicate_ratio = duplicate_count / max(1, len(paragraphs))
    if duplicate_ratio > 0.12: failures.append({"code": "BOILERPLATE_RATIO_EXCEEDED", "ratio": duplicate_ratio})
    requirement_ids = re.findall(r"\*\*Requirement ([A-Z0-9-]+)\.\*\*", corpus)
    duplicate_requirements = sorted(identifier for identifier, count in Counter(requirement_ids).items() if count > 1)
    if duplicate_requirements: failures.append({"code": "DUPLICATE_REQUIREMENT_IDS", "ids": duplicate_requirements})

    loaded: dict[str, dict] = {}
    for item in [*SCHEMAS, *STRUCTURED_INPUTS]:
        path = ROOT / item
        if not path.exists(): failures.append({"code": "STRUCTURED_FILE_MISSING", "path": item}); continue
        try: loaded[item] = json.loads(path.read_text())
        except Exception as error: failures.append({"code": "JSON_INVALID", "path": item, "error": str(error)})
        else: evidence_paths.append(path)
    profile = loaded.get("simulation/fortune5-safe/config/protocol-profile.json", {})
    if profile:
        if profile.get("mcp", {}).get("version") != "2025-11-25": failures.append({"code": "MCP_VERSION_MISMATCH"})
        if profile.get("a2a", {}).get("version") != "1.0.0": failures.append({"code": "A2A_VERSION_MISMATCH"})
    enterprise = loaded.get("simulation/fortune5-safe/config/fortune5-enterprise.json", {})
    if enterprise:
        teams = enterprise.get("portfolios", 0) * enterprise.get("value_streams_per_portfolio", 0) * enterprise.get("solution_trains_per_value_stream", 0) * enterprise.get("arts_per_solution_train", 0) * enterprise.get("teams_per_art", 0)
        if teams < 500: failures.append({"code": "FORTUNE5_SCALE_FLOOR_NOT_MET", "teams": teams})
    ggen = loaded.get("specification-guide/standards/ggen-v26.7.62.json", {})
    if ggen:
        if ggen.get("authority", {}).get("canonical_authority") != "ontology": failures.append({"code": "GGEN_AUTHORITY_MISMATCH"})
        if ggen.get("actuation", {}).get("exclusive_path") != "BRCE": failures.append({"code": "GGEN_BRCE_BOUNDARY_MISSING"})
        if len(ggen.get("standards", [])) != 16: failures.append({"code": "GGEN_STANDARD_COUNT", "observed": len(ggen.get("standards", []))})
    ea = loaded.get("specification-guide/standards/ggen-enterprise-architecture-v26.7.31.json", {})
    if ea:
        dimensions = ea.get("dimensions", []); obligations = sum(len(item.get("proof_obligations", [])) for item in dimensions)
        if len(dimensions) != 21 or obligations != 63: failures.append({"code": "EA_CROWN_CARDINALITY", "dimensions": len(dimensions), "proof_obligations": obligations})
        if ea.get("actuation", {}).get("direct_actuation_allowed") is not False: failures.append({"code": "EA_DIRECT_ACTUATION_ALLOWED"})
    for item in SIMULATION_SOURCES:
        path = ROOT / item
        if not path.exists(): failures.append({"code": "SIMULATION_SOURCE_MISSING", "path": item})
        else: evidence_paths.append(path)
    if any("/book/" in relative(path) for path in evidence_paths): failures.append({"code": "GENERATED_OUTPUT_IN_SOURCE_SET"})

    unique_paths = sorted(set(evidence_paths), key=relative)
    subject = source_set_digest(unique_paths) if unique_paths else hashlib.sha256(b"").hexdigest()
    standing = "ALIVE" if not failures else "BLOCKED"
    evidence = chapter_evidence + [{"kind": "source", "path": relative(path), "sha256": digest(path)} for path in unique_paths if path.exists()]
    report = {
        "schema": "aps.book-verifier.receipt.v26.7.31",
        "operation_id": "aps-v26.7.31-book-verifier",
        "subject": "sha256:" + subject,
        "coordinate": {
            "source": "seanchatmangpt/agile-protocol-specification", "revision_kind": "SOURCE_SET",
            "revision": "sha256:" + subject, "command": "python3 specification-guide/scripts/verify_v26_7_31.py",
            "toolchain_contract": "python>=3.11",
        },
        "standing": standing,
        "metrics": {
            "top_level_chapters": len(top_level), "total_chapters": len(links), "expanded_words": total_words,
            "long_paragraphs": len(paragraphs), "duplicate_paragraph_ratio": duplicate_ratio,
            "simulation_sources": len(SIMULATION_SOURCES), "source_files": len(unique_paths), "failures": len(failures),
        },
        "render": {"standing": "UNKNOWN", "reason": "Rendering is verified by the exact-head publication workflow, not this deterministic source verifier."},
        "failures": failures, "evidence": evidence,
        "lineage": {"base_edition": "v26.7.30", "extends": ["ggen manufacturing profile", "Enterprise Architecture as Strategy profile"]},
        "replay": {"command": "python3 specification-guide/scripts/verify_v26_7_31.py", "expected": "BYTE_IDENTICAL_RECEIPT"},
        "nonclaims": [
            "ALIVE is bounded to deterministic canonical-source checks.",
            "mdBook HTML and PDF rendering require the separate publication workflow.",
            "Rust runtime simulation standing is assigned by the simulation verifier.",
            "No real Fortune-5 company is represented.", "No production actuation authority is granted.",
        ],
    }
    RECEIPT.parent.mkdir(exist_ok=True); RECEIPT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"standing": standing, **report["metrics"], "receipt": relative(RECEIPT), "failures_detail": failures}, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
