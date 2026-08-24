#!/usr/bin/env python3
"""Static court for APS's ggen ecosystem manufacturing contract.

Execution of ggen itself belongs to CI. This verifier independently checks that
APS has admitted an exact runtime, exact marketplace pack, and RDF-owned mdBook
projection contract before that execution occurs.
"""
from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path

from rdflib import Graph, Namespace, RDF

ROOT = Path(__file__).resolve().parents[1]
MFG = ROOT / "specification-guide" / "manufacturing"
LOCK = MFG / "ecosystem.lock.json"
CONSUMER = MFG / "ggen.toml"
BOOK_GRAPH = MFG / "docs" / "book.ttl"
SUMMARY = ROOT / "specification-guide" / "src" / "SUMMARY.md"
BOOK_TOML = ROOT / "specification-guide" / "book.toml"

EXPECTED_GGEN = {
    "version": "26.8.21",
    "commit": "f4e1bce1efdcdc4f6c2531be9f66070950f7ec93",
    "releaseTag": "v26.8.21",
    "asset": "ggen-x86_64-unknown-linux-gnu.tar.gz",
    "assetSha256": "17c1c36d8b021052e2a482f191a3e32fb24fa088c7a824a16a9c0ce8e10595a4",
}
EXPECTED_MARKETPLACE = {
    "commit": "0a3d7b7df9d7053070417864ef11a3953b5e6aab",
    "pack": "mdbook-pattern-language-pack",
    "packVersion": "0.1.0",
    "blobs": {
        "pack.toml": "87af566fcb20a3590f96b67ea0fa612d0c4b2316",
        "ontology.ttl": "20bf77b48ac48f2364c0c0980089661703a49079",
        "templates/SUMMARY.md.tmpl": "c8e528e0130db20b39cc28ca4daaa265ba90bb08",
        "templates/book.toml.tmpl": "b6db92ca59c35a781797bc12468795530b272c4e",
    },
}
EXPECTED_CHAPTERS = [
    ("Source Admission and Paradigm Reset", "v26_8_24/00_source_admission_and_paradigm_reset.md"),
    ("Chatman's Law", "v26_8_24/01_chatmans_law.md"),
    ("Fuller, Ephemeralization, and Reconstitution", "v26_8_24/02_fuller_ephemeralization_and_reconstitution.md"),
    ("Five-Level × Seven-Dimension Jig Maturity", "v26_8_24/03_jig_maturity.md"),
    ("DfCM and Adversarial Manufacturing Search", "v26_8_24/04_dfcm_and_adversarial_manufacturing_search.md"),
    ("Contract First, ggen First", "v26_8_24/05_contract_first_ggen_first.md"),
    ("Executable Enterprise Architecture", "v26_8_24/06_executable_enterprise_architecture.md"),
    ("Universal Execution and Full Process Intelligence", "v26_8_24/07_universal_execution_and_process_intelligence.md"),
    ("Software Manufacturing as CapEx", "v26_8_24/08_software_manufacturing_capex.md"),
    ("Governance Compression and Board-Level Validation", "v26_8_24/09_governance_compression.md"),
    ("Fortune-500 Economics and Human Lifecycle Cost", "v26_8_24/10_fortune500_economics.md"),
    ("Adversarial Adoption and Evolutionary Pressure", "v26_8_24/11_adversarial_adoption_and_evolutionary_pressure.md"),
    ("Board and Organizational Operating Model", "v26_8_24/12_board_and_organizational_operating_model.md"),
    ("APS Constitution: Authority, Standing, and Consequence", "v26_8_24/13_aps_constitution.md"),
    ("Conformance, Metrology, and Replay", "v26_8_24/14_conformance_metrology_and_replay.md"),
    ("Falsifiers and Research Agenda", "v26_8_24/15_falsifiers_and_research_agenda.md"),
    ("Autonomic Manufacturing Manifesto", "v26_8_24/16_autonomic_manufacturing_manifesto.md"),
    ("Rice's Theorem and Epistemic Boundaries", "v26_8_24/17_rices_theorem_and_epistemic_boundaries.md"),
    ("Reference Manufacturing Stack", "v26_8_24/18_reference_manufacturing_stack.md"),
    ("Industrial Lineage: From Jig to Autonomic Factory", "v26_8_24/19_industrial_lineage_from_jig_to_autonomic_factory.md"),
]


def refuse(message: str, failures: list[str]) -> None:
    failures.append(message)


def main() -> int:
    failures: list[str] = []

    try:
        lock = json.loads(LOCK.read_text())
    except Exception as exc:
        refuse(f"cannot load ecosystem lock: {exc}", failures)
        lock = {}

    if lock.get("schema") != "aps.ggen-ecosystem-lock.v26.8.24":
        refuse("ecosystem lock schema mismatch", failures)
    if lock.get("ggen") != EXPECTED_GGEN:
        refuse(f"ggen coordinate drift: {lock.get('ggen')!r}", failures)
    if lock.get("marketplace") != EXPECTED_MARKETPLACE:
        refuse(f"marketplace coordinate drift: {lock.get('marketplace')!r}", failures)

    try:
        manifest = tomllib.loads(CONSUMER.read_text())
    except Exception as exc:
        refuse(f"invalid ggen consumer manifest: {exc}", failures)
        manifest = {}
    if manifest.get("ontology", {}).get("source") != "docs/book.ttl":
        refuse("ggen consumer must take docs/book.ttl as ontology source", failures)
    pack = manifest.get("packs", {}).get("mdbook-pattern-language-pack", {})
    if pack.get("path") != "packs/mdbook-pattern-language-pack":
        refuse("ggen consumer must compose the marketplace mdbook-pattern-language-pack", failures)

    mdp = Namespace("https://seanchatmangpt.github.io/ggen-marketplace/mdbook-pattern-language#")
    dcterms = Namespace("http://purl.org/dc/terms/")
    try:
        graph = Graph().parse(BOOK_GRAPH, format="turtle")
    except Exception as exc:
        refuse(f"invalid manufacturing book graph: {exc}", failures)
        graph = Graph()

    books = list(graph.subjects(RDF.type, mdp.Book))
    if len(books) != 1:
        refuse(f"manufacturing graph must define exactly one mdp:Book; got {len(books)}", failures)
    else:
        book = books[0]
        expected_book = {
            dcterms.title: "Agile Protocol Specification v26.8.24",
            dcterms.creator: "Sean Chatman",
            dcterms.language: "en",
            mdp.srcDir: "src",
            mdp.buildDir: "book",
            mdp.repositoryUrl: "https://github.com/seanchatmangpt/agile-protocol-specification",
        }
        for predicate, expected in expected_book.items():
            actual = [str(value) for value in graph.objects(book, predicate)]
            if actual != [expected]:
                refuse(f"mdp:Book field {predicate} mismatch: {actual!r}", failures)

    rows = []
    for subject in graph.subjects(RDF.type, mdp.NavigationEntry):
        try:
            position = int(next(graph.objects(subject, mdp.position)))
            kind = str(next(graph.objects(subject, mdp.kind)))
            title = str(next(graph.objects(subject, dcterms.title)))
            path = str(next(graph.objects(subject, mdp.path)))
            rows.append((position, kind, title, path))
        except Exception as exc:
            refuse(f"incomplete navigation entry {subject}: {exc}", failures)
    rows.sort()
    expected_rows = [(i + 1, "chapter", title, path) for i, (title, path) in enumerate(EXPECTED_CHAPTERS)]
    if rows != expected_rows:
        refuse(f"RDF navigation does not exactly match active chapter contract: {rows!r}", failures)

    expected_summary = (
        "# Summary\n\n"
        "<!-- GENERATED by ggen from mdbook-pattern-language-pack. -->\n"
        "<!-- Edit admitted RDF/template source, not this projection. -->\n\n"
        + "\n".join(f"- [{title}]({path})" for title, path in EXPECTED_CHAPTERS)
        + "\n"
    )
    try:
        actual_summary = SUMMARY.read_text()
        if actual_summary != expected_summary:
            refuse("committed SUMMARY.md is not the exact admitted marketplace projection", failures)
    except Exception as exc:
        refuse(f"cannot read committed SUMMARY.md: {exc}", failures)

    try:
        book_toml = tomllib.loads(BOOK_TOML.read_text())
        if book_toml.get("book", {}).get("title") != "Agile Protocol Specification v26.8.24":
            refuse("committed book.toml title disagrees with manufacturing graph", failures)
        if book_toml.get("book", {}).get("authors") != ["Sean Chatman"]:
            refuse("committed book.toml author disagrees with manufacturing graph", failures)
        if book_toml.get("book", {}).get("src") != "src":
            refuse("committed book.toml src disagrees with manufacturing graph", failures)
        if book_toml.get("build", {}).get("build-dir") != "book":
            refuse("committed book.toml build-dir disagrees with manufacturing graph", failures)
    except Exception as exc:
        refuse(f"invalid committed book.toml: {exc}", failures)

    result = {
        "schema": "aps.ggen-ecosystem-static-court.v26.8.24",
        "standing": "ALIVE" if not failures else "REFUSED",
        "ggen": EXPECTED_GGEN,
        "marketplace": EXPECTED_MARKETPLACE,
        "navigationEntries": len(rows),
        "failures": failures,
        "nonClaims": [
            "This static court does not claim ggen executed; exact-head CI must execute the pinned binary.",
            "It proves only that the admitted consumer inputs and committed projection are internally coherent."
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    for failure in failures:
        print(f"REFUSED: {failure}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
