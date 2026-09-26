#!/usr/bin/env python3
"""Render deterministic downstream adoption artifacts for engineering-standards."""

from __future__ import annotations
import argparse, json
from pathlib import Path

SCHEMA = "engineering-standards.repository-adoption.v26.9.21"
ROOT_REPO = "seanchatmangpt/engineering-standards"
ROOT_VERSION = "26.9.21"

def manifest(repo: str, base: str, role: str, root_sha: str, constitution: str) -> dict:
    return {
        "schema": SCHEMA,
        "repository": repo,
        "base_sha": base,
        "mode": "SEMANTIC_WORK",
        "role": role,
        "root": {"repository": ROOT_REPO, "sha": root_sha, "version": ROOT_VERSION},
        "local_constitution": constitution,
        "project_profile": "semantic/engineering-standards-profile.ttl",
        "standing": "UNKNOWN",
        "generator_identity": "engineering-standards/scripts/render-repository-adoption.py",
        "non_claims": [
            "root adoption does not prove local runtime behavior",
            "root adoption does not grant merge, release, deploy, or external DO authority",
            "local repository courts remain authoritative for local runtime standing"
        ]
    }

def profile(repo: str, base: str, role: str, root_sha: str) -> str:
    slug = repo.replace("/", "-")
    return f"""@prefix es: <https://w3id.org/chatman/engineering-standards#> .
@prefix prof: <http://www.w3.org/ns/dx/prof/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix project: <https://w3id.org/chatman/project/{slug}#> .

project:Profile a prof:Profile ;
  dcterms:title "{repo} engineering-standards adoption" ;
  dcterms:description "{role}" ;
  prof:isProfileOf <https://w3id.org/chatman/engineering-standards> ;
  dcterms:source <https://github.com/{ROOT_REPO}/commit/{root_sha}> .

project:Repository a es:RepositorySubject ;
  es:repository "{repo}" ;
  es:baseSha "{base}" .
"""

def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument("--repo",required=True); p.add_argument("--base",required=True)
    p.add_argument("--role",required=True); p.add_argument("--root-sha",required=True)
    p.add_argument("--constitution",default="AGENTS.md"); p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    a.out.mkdir(parents=True,exist_ok=True)
    (a.out/"engineering-standards.json").write_text(json.dumps(manifest(a.repo,a.base,a.role,a.root_sha,a.constitution),indent=2)+"\n")
    sem=a.out/"semantic"; sem.mkdir(exist_ok=True)
    (sem/"engineering-standards-profile.ttl").write_text(profile(a.repo,a.base,a.role,a.root_sha))

if __name__ == "__main__":
    main()
