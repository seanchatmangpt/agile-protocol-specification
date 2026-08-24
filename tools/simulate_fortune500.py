#!/usr/bin/env python3
"""Deterministic synthetic Fortune-500 manufacturing sensitivity model."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def calculate(model: dict) -> dict:
    if model.get("evidenceClass") != "SYNTHETIC_SENSITIVITY_MODEL_NOT_FORECAST":
        raise ValueError("model must be explicitly synthetic")
    a = model["assumptions"]
    capabilities = int(a["enterpriseCapabilities"])
    projections = int(a["projectionFamiliesPerCapability"])
    variants = int(a["environmentVariants"])
    candidates = int(a["architectureCandidates"])
    avg_lines = int(a["averageGeneratedLinesPerProjectionArtifact"])
    human_hours_per_artifact = sum(float(v) for v in a["humanLifecycleHoursPerProjectionArtifact"].values())

    selected_artifacts = capabilities * projections * variants
    candidate_artifacts = selected_artifacts * candidates
    selected_lines = selected_artifacts * avg_lines
    candidate_lines = candidate_artifacts * avg_lines
    human_selected_hours = selected_artifacts * human_hours_per_artifact
    human_candidate_hours = candidate_artifacts * human_hours_per_artifact

    k = a["manufacturingKnowledgeObjects"]
    manufacturing_knowledge_objects = sum(int(v) for v in k.values())
    board_validation_objects = int(k["publicOntologyProfiles"]) + int(k["manufacturingPatterns"]) + int(k["authorityPolicies"]) + int(k["verifierPolicies"])

    return {
        "selectedProjectionArtifacts": selected_artifacts,
        "DfCMCandidateProjectionArtifacts": candidate_artifacts,
        "selectedGeneratedLinesSensitivity": selected_lines,
        "DfCMGeneratedLinesSensitivity": candidate_lines,
        "humanLifecycleHoursSelectedSensitivity": human_selected_hours,
        "humanLifecycleHoursDfCMCandidateSensitivity": human_candidate_hours,
        "humanLifecycleHoursPerProjectionArtifactAssumption": human_hours_per_artifact,
        "manufacturingKnowledgeObjects": manufacturing_knowledge_objects,
        "boardValidationObjectsAssumption": board_validation_objects,
        "governanceCompressionSelectedArtifactsPerBoardObject": selected_artifacts / board_validation_objects,
        "candidateBreadthMultiplier": candidates
    }


def run(path: Path) -> dict:
    raw = path.read_bytes()
    model = json.loads(raw)
    return {
        "schema": "aps.synthetic-fortune500-sensitivity.v26.8.24",
        "standing": "ALIVE",
        "inputSha256": hashlib.sha256(raw).hexdigest(),
        "evidenceClass": model["evidenceClass"],
        "metrics": calculate(model),
        "nonClaims": model.get("nonClaims", []) + [
            "ALIVE means the deterministic sensitivity model executed and its arithmetic closed.",
            "The metrics are consequences of supplied assumptions, not empirical Fortune-500 measurements."
        ]
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("model", type=Path)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    result = run(args.model)
    output = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(output)
    print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
