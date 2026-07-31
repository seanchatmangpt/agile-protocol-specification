#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
PROFILE = ROOT / "specification-guide" / "standards" / "ggen-v26.7.62.json"
CHAPTER = ROOT / "specification-guide" / "src" / "v26_7_30" / "16_ggen_manufacturing_standard.md"
SUMMARY = ROOT / "specification-guide" / "src" / "SUMMARY.md"
RECEIPT = ROOT / "receipts" / "APS-v26.7.31-ggen-standard.json"

EXPECTED_SOURCE = {
    "repository": "seanchatmangpt/ggen",
    "release": "26.7.62",
    "revision": "68952593c40214ac1a681073d65f3902a9cdfce4",
    "consolidation_merge": "faa52dac474d456ae00105869770161d666ba31f",
    "exact_aggregate_head": "036ab703e885aff90a79536a5db5b24608e8a32f",
}
REQUIRED_STANDARD_IDS = {
    "GGEN-AUTH-001", "GGEN-CALC-001", "GGEN-FM-001", "GGEN-REFUSE-001",
    "GGEN-ACT-001", "GGEN-GBB-001", "GGEN-CMD-001", "GGEN-PLAY-001",
    "GGEN-STAND-001", "GGEN-GALL-001", "GGEN-OCEL-001", "GGEN-PROOF-001",
    "GGEN-REL-001", "GGEN-ID-001", "GGEN-DRYRUN-001", "GGEN-REPLAY-001",
}
EXPECTED_STATES = ["PARTIAL_ALIVE", "ALIVE", "BLOCKED", "BUILD_BROKEN", "UNKNOWN", "UNSUPPORTED"]
EXPECTED_LADDER = ["unit", "integration", "e2e", "chaos", "stress", "benchmark", "verifier_report"]
REQUIRED_PHRASES = [
    "ontology-to-artifact manufacturing system", "HAND_CODED_GENERATED_OUTPUT",
    "parse -> route -> admit/refuse", "DuplicateReplay", "Zero unreceipted actuation",
    "ggen Building Block", "Combinatorial maximalism", "deterministic non-LLM self-play",
    "Logical time and OCEL evidence", "ggen-first Lean 4 to Rust", "Exact-head release law",
    "https://chatmangpt.com",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify() -> tuple[dict, int]:
    failures: list[dict] = []
    evidence: list[dict] = []
    for path in [PROFILE, CHAPTER, SUMMARY]:
        if not path.exists():
            failures.append({"code": "REQUIRED_FILE_MISSING", "path": str(path.relative_to(ROOT))})
    if failures:
        data, chapter, summary = {}, "", ""
    else:
        try:
            data = json.loads(PROFILE.read_text())
        except Exception as error:
            failures.append({"code": "PROFILE_JSON_INVALID", "error": str(error)})
            data = {}
        chapter = CHAPTER.read_text()
        summary = SUMMARY.read_text()

    if data:
        if data.get("schema") != "aps.ggen.profile.v26.7.31":
            failures.append({"code": "SCHEMA_MISMATCH", "observed": data.get("schema")})
        if data.get("source") != EXPECTED_SOURCE:
            failures.append({"code": "SOURCE_COORDINATE_MISMATCH", "observed": data.get("source")})
        window = data.get("observation_window", {})
        if window.get("start") != "2026-07-23T00:00:00-07:00":
            failures.append({"code": "WINDOW_START_MISMATCH", "observed": window.get("start")})
        if window.get("end") != "2026-07-30T21:50:00-07:00":
            failures.append({"code": "WINDOW_END_MISMATCH", "observed": window.get("end")})
        if data.get("states") != EXPECTED_STATES:
            failures.append({"code": "STATE_VOCABULARY_MISMATCH", "observed": data.get("states")})
        if data.get("evidence_ladder") != EXPECTED_LADDER:
            failures.append({"code": "EVIDENCE_LADDER_MISMATCH", "observed": data.get("evidence_ladder")})
        authority = data.get("authority", {})
        if authority.get("canonical_authority") != "ontology": failures.append({"code": "ONTOLOGY_AUTHORITY_MISSING"})
        if authority.get("generated_outputs_are_authority") is not False: failures.append({"code": "GENERATED_OUTPUT_AUTHORITY_VIOLATION"})
        if authority.get("hand_edit_generated_outputs") != "REFUSED": failures.append({"code": "HAND_EDIT_REFUSAL_MISSING"})
        if authority.get("second_sync_expected") != "BYTE_IDENTICAL": failures.append({"code": "SECOND_SYNC_CONTRACT_MISSING"})
        actuation = data.get("actuation", {})
        if actuation.get("direct_actuation_allowed") is not False: failures.append({"code": "DIRECT_ACTUATION_ALLOWED"})
        if actuation.get("exclusive_path") != "BRCE": failures.append({"code": "BRCE_PATH_MISSING"})
        if actuation.get("invariant") != "Zero unreceipted actuation": failures.append({"code": "ACTUATION_INVARIANT_MISMATCH"})
        receipt = data.get("receipt", {})
        if receipt.get("ggen_algorithm") != "BLAKE3": failures.append({"code": "BLAKE3_REQUIRED"})
        if receipt.get("independent_replay_required") is not True: failures.append({"code": "INDEPENDENT_REPLAY_REQUIRED"})
        replay = data.get("replay", {})
        if replay.get("refusal_precedence") != ["DuplicateReplay", "ChainPositionViolation"]: failures.append({"code": "REPLAY_PRECEDENCE_MISMATCH"})
        if replay.get("refusal_preserves_state") is not True: failures.append({"code": "REFUSAL_STATE_SAFETY_MISSING"})
        blocks = data.get("building_blocks", {})
        if blocks.get("canonical_kernel_count") != 1: failures.append({"code": "CANONICAL_KERNEL_CARDINALITY"})
        if blocks.get("lifecycle_separate_from_standing") is not True: failures.append({"code": "LIFECYCLE_STANDING_COLLAPSED"})
        if blocks.get("profile_conflict") != "TYPED_REFUSAL": failures.append({"code": "PROFILE_CONFLICT_REFUSAL_MISSING"})
        self_play = data.get("self_play", {})
        if self_play.get("llm_calls_allowed") is not False: failures.append({"code": "LLM_SELF_PLAY_NOT_REFUSED"})
        if self_play.get("actors") != "EXPLICIT_STATE_MACHINES": failures.append({"code": "ACTOR_STATE_MACHINE_MISSING"})
        standards = data.get("standards", [])
        ids = [item.get("id") for item in standards]
        if len(ids) != len(set(ids)): failures.append({"code": "DUPLICATE_STANDARD_IDS"})
        missing = sorted(REQUIRED_STANDARD_IDS - set(ids)); extra = sorted(set(ids) - REQUIRED_STANDARD_IDS)
        if missing: failures.append({"code": "REQUIRED_STANDARDS_MISSING", "ids": missing})
        if extra: failures.append({"code": "UNADMITTED_STANDARDS_PRESENT", "ids": extra})
        for index, item in enumerate(standards):
            for key in ["id", "title", "law", "admission", "obligations", "exclusions", "falsifier", "source_evidence"]:
                if not item.get(key): failures.append({"code": "STANDARD_FIELD_MISSING", "index": index, "field": key})
            if item.get("admission") != "ADMITTED": failures.append({"code": "STANDARD_NOT_ADMITTED", "id": item.get("id")})
            if len(item.get("obligations", [])) < 2: failures.append({"code": "OBLIGATION_SET_INCOMPLETE", "id": item.get("id")})
            if not item.get("exclusions"): failures.append({"code": "EXCLUSION_SET_MISSING", "id": item.get("id")})

    if chapter:
        words = len(re.findall(r"\b[\w'–-]+\b", chapter))
        if words < 1800: failures.append({"code": "CHAPTER_NOT_SUBSTANTIVE", "words": words, "minimum": 1800})
        if chapter.count("\n# ") != 0 or not chapter.startswith("# "): failures.append({"code": "H1_CARDINALITY"})
        folded = chapter.casefold()
        for phrase in REQUIRED_PHRASES:
            if phrase.casefold() not in folded: failures.append({"code": "CHAPTER_INVARIANT_MISSING", "phrase": phrase})
        if "v26_7_30/16_ggen_manufacturing_standard.md" not in summary: failures.append({"code": "SUMMARY_LINK_MISSING"})

    for path, kind in [(PROFILE, "profile"), (CHAPTER, "chapter"), (SUMMARY, "summary")]:
        if path.exists(): evidence.append({"kind": kind, "path": str(path.relative_to(ROOT)), "sha256": sha256(path)})
    subject_material = b"".join(path.read_bytes() for path in [PROFILE, CHAPTER, SUMMARY] if path.exists())
    subject = "sha256:" + hashlib.sha256(subject_material).hexdigest()
    standing = "ALIVE" if not failures else "BLOCKED"
    report = {
        "schema": "aps.receipt.v26.7.31",
        "operation_id": "aps-v26.7.31-ggen-standard",
        "subject": subject,
        "coordinate": {
            "source": "seanchatmangpt/agile-protocol-specification",
            "revision_kind": "SOURCE_SET",
            "revision": subject,
            "command": "python3 specification-guide/scripts/verify_ggen_v26_7_31.py",
            "toolchain_contract": "python>=3.11",
            "ggen_source_revision": EXPECTED_SOURCE["revision"],
        },
        "standing": standing,
        "metrics": {"standards": len(data.get("standards", [])) if data else 0, "chapter_words": len(re.findall(r"\b[\w'–-]+\b", chapter)) if chapter else 0, "failures": len(failures)},
        "failures": failures,
        "evidence": evidence,
        "replay": {"command": "python3 specification-guide/scripts/verify_ggen_v26_7_31.py", "expected": "MATCH"},
        "nonclaims": [
            "ALIVE is bounded to APS profile structure and invariant checks.",
            "The ggen implementation was not executed by this verifier.",
            "The APS receipt uses the existing SHA-256 receipt schema; ggen execution identities remain normatively BLAKE3.",
            "No production actuation authority is granted.",
        ],
    }
    RECEIPT.parent.mkdir(exist_ok=True)
    RECEIPT.write_text(json.dumps(report, indent=2) + "\n")
    return report, 0 if not failures else 1


if __name__ == "__main__":
    result, code = verify()
    print(json.dumps({"standing": result["standing"], "standards": result["metrics"]["standards"], "chapter_words": result["metrics"]["chapter_words"], "receipt": str(RECEIPT.relative_to(ROOT)), "failures": result["failures"]}, indent=2))
    raise SystemExit(code)
