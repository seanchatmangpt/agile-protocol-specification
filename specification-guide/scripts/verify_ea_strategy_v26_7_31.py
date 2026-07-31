#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
PROFILE = ROOT / "specification-guide" / "standards" / "ggen-enterprise-architecture-v26.7.31.json"
CHAPTER = ROOT / "specification-guide" / "src" / "v26_7_30" / "17_enterprise_architecture_as_strategy.md"
SUMMARY = ROOT / "specification-guide" / "src" / "SUMMARY.md"
RECEIPT = ROOT / "receipts" / "APS-v26.7.31-ggen-enterprise-architecture.json"
CHAPTER_PARTS = [
    CHAPTER.parent / "ea_strategy" / "01_rwr_execution_foundation.md",
    CHAPTER.parent / "ea_strategy" / "02_graph_building_blocks_transition.md",
    CHAPTER.parent / "ea_strategy" / "03_portfolio_governance_evidence.md",
    CHAPTER.parent / "ea_strategy" / "04_maturity_gall_operationalization.md",
]

EXPECTED_MODELS = {
    ("Diversification", "LOW", "LOW"),
    ("Coordination", "HIGH", "LOW"),
    ("Replication", "LOW", "HIGH"),
    ("Unification", "HIGH", "HIGH"),
}
EXPECTED_RWR_STAGES = [
    "Business Silos",
    "Standardized Technology",
    "Optimized Core",
    "Business Modularity",
]
EXPECTED_STATES = [
    "PARTIAL_ALIVE",
    "ALIVE",
    "BLOCKED",
    "BUILD_BROKEN",
    "UNKNOWN",
    "UNSUPPORTED",
    "REFUSED",
]
EXPECTED_LADDER = [
    "unit",
    "integration",
    "e2e",
    "chaos",
    "stress",
    "benchmark",
    "verifier_report",
]
REQUIRED_PHRASES = [
    "Enterprise architecture becomes strategy when admitted architectural knowledge",
    "Preserve the RWR fence",
    "Diversification",
    "Coordination",
    "Replication",
    "Unification",
    "Business Silos",
    "Business Modularity",
    "Evidence-Bearing Self-Governance",
    "Stage 5 is a ggen extension",
    "FoundationForExecution",
    "Core diagram as a projection, not authority",
    "ggen architecture doctor",
    "Architecture Building Block",
    "Solution Building Block",
    "gpc",
    "Little’s Law",
    "Conway’s Law",
    "Zero unreceipted actuation",
    "21 conjunctive dimensions and 63 proof obligations",
    "GGEN-EA-CROWN",
    "The architecture may generate every lawful consequence",
]
REQUIRED_DOMAINS = {
    "Strategy", "Business", "Information", "Application and technology",
    "Manufacturing", "Transition", "Governance and evidence",
}
EXPECTED_CHECKPOINTS = [
    "GGEN-EA-000","GGEN-EA-010","GGEN-EA-020","GGEN-EA-030",
    "GGEN-EA-040","GGEN-EA-050","GGEN-EA-060","GGEN-EA-070",
    "GGEN-EA-080","GGEN-EA-090","GGEN-EA-100","GGEN-EA-110",
    "GGEN-EA-120","GGEN-EA-130","GGEN-EA-CROWN",
]

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main() -> int:
    failures: list[dict] = []
    for path in [PROFILE, CHAPTER, SUMMARY, *CHAPTER_PARTS]:
        if not path.exists():
            failures.append({"code": "REQUIRED_FILE_MISSING", "path": str(path.relative_to(ROOT))})

    data = {}
    chapter = ""
    summary = ""
    if not failures:
        try:
            data = json.loads(PROFILE.read_text())
        except Exception as exc:
            failures.append({"code": "PROFILE_JSON_INVALID", "error": str(exc)})
        chapter_stub = CHAPTER.read_text()
        chapter = chapter_stub + "\n" + "\n".join(path.read_text() for path in CHAPTER_PARTS)
        summary = SUMMARY.read_text()

    if data:
        if data.get("schema") != "aps.ggen.enterprise-architecture.profile.v26.7.31":
            failures.append({"code": "SCHEMA_MISMATCH"})
        if data.get("standing") != "ADMITTED":
            failures.append({"code": "PROFILE_STANDING_MISMATCH"})
        if data.get("source", {}).get("ggen_revision") != "68952593c40214ac1a681073d65f3902a9cdfce4":
            failures.append({"code": "GGEN_SOURCE_REVISION_MISMATCH"})

        fence = data.get("rwr_fence", {})
        models = {
            (x.get("name"), x.get("integration"), x.get("standardization"))
            for x in fence.get("operating_models", [])
        }
        if models != EXPECTED_MODELS:
            failures.append({"code": "OPERATING_MODEL_FENCE_MISMATCH", "observed": sorted(models)})
        if fence.get("preserved_maturity_stages") != EXPECTED_RWR_STAGES:
            failures.append({"code": "RWR_MATURITY_FENCE_MISMATCH"})
        extension = fence.get("ggen_extension", {})
        if extension.get("stage") != 5 or extension.get("is_original_rwr_stage") is not False:
            failures.append({"code": "STAGE5_ATTRIBUTION_VIOLATION"})
        if extension.get("conjunctive") is not True:
            failures.append({"code": "STAGE5_NOT_CONJUNCTIVE"})

        if data.get("states") != EXPECTED_STATES:
            failures.append({"code": "STATE_VOCABULARY_MISMATCH"})
        if data.get("evidence_ladder") != EXPECTED_LADDER:
            failures.append({"code": "EVIDENCE_LADDER_MISMATCH"})
        if data.get("authority", {}).get("canonical") != "architecture_graph":
            failures.append({"code": "ARCHITECTURE_GRAPH_AUTHORITY_MISSING"})
        if data.get("authority", {}).get("views_are_authority") is not False:
            failures.append({"code": "VIEW_AUTHORITY_VIOLATION"})
        if data.get("actuation", {}).get("direct_actuation_allowed") is not False:
            failures.append({"code": "DIRECT_ACTUATION_ALLOWED"})
        if data.get("actuation", {}).get("exclusive_path") != "BRCE":
            failures.append({"code": "BRCE_BOUNDARY_MISSING"})
        if data.get("building_blocks", {}).get("kernel_count") != 1:
            failures.append({"code": "GBB_KERNEL_CARDINALITY"})
        if data.get("building_blocks", {}).get("accepted_cli_aliases", {}).get("gpc") != "GCP":
            failures.append({"code": "GPC_ALIAS_MISSING"})

        level5 = data.get("maturity", {}).get("level_5", {})
        dims = data.get("dimensions", [])
        obligations = sum(len(x.get("proof_obligations", [])) for x in dims)
        ids = [x.get("id") for x in dims]
        if level5.get("required_dimensions") != 21 or len(dims) != 21:
            failures.append({"code": "DIMENSION_COUNT_MISMATCH", "observed": len(dims)})
        if len(ids) != len(set(ids)):
            failures.append({"code": "DUPLICATE_DIMENSION_ID"})
        if level5.get("proof_obligations") != 63 or obligations != 63:
            failures.append({"code": "PROOF_OBLIGATION_COUNT_MISMATCH", "observed": obligations})
        if level5.get("conjunctive") is not True or level5.get("same_coordinate_required") is not True:
            failures.append({"code": "LEVEL5_CROWN_LAW_MISSING"})
        for dim in dims:
            if len(dim.get("proof_obligations", [])) != 3:
                failures.append({"code": "DIMENSION_OBLIGATION_ARITY", "id": dim.get("id")})
            if not dim.get("falsifier"):
                failures.append({"code": "DIMENSION_FALSIFIER_MISSING", "id": dim.get("id")})

        if data.get("gall_checkpoints") != EXPECTED_CHECKPOINTS:
            failures.append({"code": "GALL_CHECKPOINT_LEDGER_MISMATCH"})
        if not data.get("named_falsifier"):
            failures.append({"code": "NAMED_FALSIFIER_MISSING"})

    if chapter:
        words = len(re.findall(r"\b[\w'’–-]+\b", chapter))
        if words < 3600:
            failures.append({"code": "CHAPTER_NOT_SUBSTANTIVE", "words": words, "minimum": 3600})
        if chapter.count("\n# ") != 0 or not chapter.startswith("# "):
            failures.append({"code": "H1_CARDINALITY"})
        folded = chapter.casefold()
        for phrase in REQUIRED_PHRASES:
            if phrase.casefold() not in folded:
                failures.append({"code": "CHAPTER_INVARIANT_MISSING", "phrase": phrase})
        for domain in REQUIRED_DOMAINS:
            if domain.casefold() not in folded:
                failures.append({"code": "METAMODEL_DOMAIN_MISSING", "domain": domain})
        if "v26_7_30/17_enterprise_architecture_as_strategy.md" not in summary:
            failures.append({"code": "SUMMARY_LINK_MISSING"})
        top_level = len(re.findall(r"^[-*] \[[^]]+\]\([^)]+\.md\)$", summary, re.MULTILINE))
        total_links = len(re.findall(r"^\s*[-*] \[[^]]+\]\([^)]+\.md\)$", summary, re.MULTILINE))
        if top_level != 18:
            failures.append({"code": "SUMMARY_TOP_LEVEL_COUNT", "observed": top_level, "expected": 18})
        if total_links != 19:
            failures.append({"code": "SUMMARY_TOTAL_LINK_COUNT", "observed": total_links, "expected": 19})

    evidence = []
    for path, kind in [(PROFILE,"profile"),(CHAPTER,"chapter_stub"), *[(part,"chapter_part") for part in CHAPTER_PARTS], (SUMMARY,"summary")]:
        if path.exists():
            evidence.append({
                "kind": kind,
                "path": str(path.relative_to(ROOT)),
                "sha256": digest(path),
            })
    subject = b"".join(path.read_bytes() for path in [PROFILE,CHAPTER,*CHAPTER_PARTS,SUMMARY] if path.exists())
    report = {
        "schema": "aps.receipt.v26.7.31",
        "operation_id": "aps-v26.7.31-ggen-enterprise-architecture",
        "subject": "sha256:" + hashlib.sha256(subject).hexdigest(),
        "coordinate": {
            "source": "seanchatmangpt/agile-protocol-specification",
            "revision": "WORKTREE",
            "command": "python3 specification-guide/scripts/verify_ea_strategy_v26_7_31.py",
            "toolchain": sys.version.split()[0],
            "ggen_source_revision": "68952593c40214ac1a681073d65f3902a9cdfce4",
        },
        "standing": "ALIVE" if not failures else "BLOCKED",
        "metrics": {
            "dimensions": len(data.get("dimensions", [])) if data else 0,
            "proof_obligations": sum(len(x.get("proof_obligations", [])) for x in data.get("dimensions", [])) if data else 0,
            "chapter_words": len(re.findall(r"\b[\w'’–-]+\b", chapter)) if chapter else 0,
            "failures": len(failures),
        },
        "failures": failures,
        "evidence": evidence,
        "replay": {
            "command": "python3 specification-guide/scripts/verify_ea_strategy_v26_7_31.py",
            "expected": "MATCH",
        },
        "nonclaims": [
            "ALIVE is bounded to APS profile structure and invariant verification.",
            "The ggen enterprise-architecture implementation was not executed by this verifier.",
            "Stage 5 is a ggen extension, not an original RWR maturity stage.",
            "No production actuation authority is granted.",
        ],
    }
    RECEIPT.parent.mkdir(exist_ok=True)
    RECEIPT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "standing": report["standing"],
        **report["metrics"],
        "receipt": str(RECEIPT.relative_to(ROOT)),
        "failures_detail": failures,
    }, indent=2))
    return 0 if not failures else 1

if __name__ == "__main__":
    raise SystemExit(main())
