#!/usr/bin/env python3
"""Deterministic timing benchmark for the engineering-standards adoption court.

Measures the adoption court alone and the whole-repository verifier, prints a
JSON bench receipt (optionally written with --receipt outside the repository),
and exits non-zero if a median exceeds its regression bound.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import platform
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOUNDS = {"adoption_court_median_s": 0.06, "verify_repository_median_s": 30.0}


def load_verify():
    spec = importlib.util.spec_from_file_location("aps_verify_bench", ROOT / "tools/verify.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def measure(fn, iterations: int) -> list[float]:
    samples = []
    for _ in range(iterations):
        start = time.perf_counter()
        fn()
        samples.append(time.perf_counter() - start)
    return samples


def summary(samples: list[float]) -> dict:
    ordered = sorted(samples)
    return {
        "n": len(ordered),
        "min_s": round(ordered[0], 6),
        "median_s": round(statistics.median(ordered), 6),
        "p90_s": round(ordered[int(0.9 * (len(ordered) - 1))], 6),
        "max_s": round(ordered[-1], 6),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--iterations", type=int, default=200)
    parser.add_argument("--repo-iterations", type=int, default=5)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    verify = load_verify()

    def court():
        failures: list[str] = []
        verify.validate_engineering_standards_adoption(ROOT, failures)
        if failures:
            raise SystemExit(f"adoption court refused: {failures}")

    def whole():
        failures, _ = verify.verify_repository()
        if failures:
            raise SystemExit(f"repository verifier refused: {failures}")

    court()  # warm imports
    court_stats = summary(measure(court, args.iterations))
    repo_stats = summary(measure(whole, args.repo_iterations))
    subject = hashlib.sha256()
    for rel in (verify.ADOPTION_MANIFEST, verify.ADOPTION_PROFILE, verify.ADOPTION_SCHEMA, verify.ADOPTION_GENERATOR, "AGENTS.md", "tools/verify.py", "tools/render_adoption.py"):
        subject.update(rel.encode() + b"\0" + (ROOT / rel).read_bytes() + b"\0")
    breaches = []
    if court_stats["median_s"] > BOUNDS["adoption_court_median_s"]:
        breaches.append("adoption_court_median_s")
    if repo_stats["median_s"] > BOUNDS["verify_repository_median_s"]:
        breaches.append("verify_repository_median_s")
    receipt = {
        "schema": "aps.bench.engineering-standards-adoption.v26.9.26",
        "subjectSha256": subject.hexdigest(),
        "host": {"python": sys.version.split()[0], "platform": platform.platform()},
        "adoption_court": court_stats,
        "verify_repository": repo_stats,
        "bounds": BOUNDS,
        "standing": "ALIVE" if not breaches else "REFUSED",
        "breaches": breaches,
        "nonClaims": ["Timing is host-relative; bounds catch algorithmic regressions, not jitter."],
    }
    text = json.dumps(receipt, indent=2, sort_keys=True)
    if args.receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(text + "\n")
    print(text)
    return 1 if breaches else 0


if __name__ == "__main__":
    raise SystemExit(main())
