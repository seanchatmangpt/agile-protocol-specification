#!/usr/bin/env python3
"""Whole-repository verifier for APS v26.8.24.

This verifier qualifies repository coherence. It does not prove the long-horizon
enterprise-manufacturing hypothesis.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STANDING = {"ALIVE", "PARTIAL_ALIVE", "BLOCKED", "BUILD_BROKEN", "UNKNOWN", "UNSUPPORTED", "REFUSED"}
EXPECTED_TOP = {
    ".aps-syntax.md", ".claude", ".github", ".gitignore", "AGENTS.md", "CLAUDE.md",
    "CONTRIBUTING.md", "LICENSE", "MANIFEST.json", "Makefile", "README.md", "SECURITY.md",
    "archive", "contracts", "examples", "ontology", "receipts", "simulation",
    "specification-guide", "tests", "tools",
    # engineering-standards v26.9.21 root adoption (validated by
    # validate_engineering_standards_adoption; admission is not standing).
    "engineering-standards.json", "semantic",
}
ADOPTION_MANIFEST = "engineering-standards.json"
ADOPTION_PROFILE = "semantic/engineering-standards-profile.ttl"
ADOPTION_SCHEMA = "semantic/schemas/repository-adoption.schema.json"
# Git blob id of semantic/schemas/repository-adoption.schema.json at
# seanchatmangpt/engineering-standards@5a3bb6446aeaee2255a7523d4d8cebf6042960c3.
ADOPTION_SCHEMA_BLOB = "e51eebe15964237cdd1298eb4a3827209bdfb1b4"
ADOPTION_REPOSITORY = "seanchatmangpt/agile-protocol-specification"
ADOPTION_ROOT_IRI = "https://w3id.org/chatman/engineering-standards"
ADOPTION_SEMANTIC_FILES = {ADOPTION_PROFILE, ADOPTION_SCHEMA}
ADOPTION_NON_CLAIMS = (
    "root adoption does not prove local runtime behavior",
    "root adoption does not grant merge, release, deploy, or external DO authority",
    "local repository courts remain authoritative for local runtime standing",
)
EXPECTED_CHAPTERS = [
    "00_source_admission_and_paradigm_reset.md", "01_chatmans_law.md",
    "02_fuller_ephemeralization_and_reconstitution.md", "03_jig_maturity.md",
    "04_dfcm_and_adversarial_manufacturing_search.md", "05_contract_first_ggen_first.md",
    "06_executable_enterprise_architecture.md", "07_universal_execution_and_process_intelligence.md",
    "08_software_manufacturing_capex.md", "09_governance_compression.md",
    "10_fortune500_economics.md", "11_adversarial_adoption_and_evolutionary_pressure.md",
    "12_board_and_organizational_operating_model.md", "13_aps_constitution.md",
    "14_conformance_metrology_and_replay.md", "15_falsifiers_and_research_agenda.md",
    "16_autonomic_manufacturing_manifesto.md", "17_rices_theorem_and_epistemic_boundaries.md",
    "18_reference_manufacturing_stack.md", "19_industrial_lineage_from_jig_to_autonomic_factory.md",
]
STALE_PATH_MARKERS = (
    "v26_7_", "V26_7_", "fortune5-safe", ".aps-enterprise-bootstrap",
    "work_order.schema", "ggen-v26.7.62", "ggen-enterprise-architecture-v26.7.31"
)
STALE_CONTENT_MARKERS = (
    "Current candidate: " + "v26." + "7", "APS " + "v26." + "7.30",
    "APS " + "v26." + "7.31",
    "comprehensive framework and documentation standard " + "designed for agile software development",
)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def active_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        parts = path.relative_to(ROOT).parts
        if ".git" in parts or (parts and parts[0] == "archive"):
            continue
        yield path


def text_file(path: Path) -> bool:
    return path.suffix.lower() in {".md", ".json", ".py", ".yml", ".yaml", ".toml", ".ttl", ".css", ".txt"} or path.name == "Makefile"


def load_json(path: Path, failures: list[str]):
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        failures.append(f"invalid JSON {rel(path)}: {exc}")
        return None


def require_phrases(text: str, phrases: list[str], scope: str, failures: list[str]) -> None:
    for phrase in phrases:
        if phrase not in text:
            failures.append(f"{scope} missing required doctrine: {phrase}")


def validate_machine_readable(failures: list[str]) -> None:
    try:
        from jsonschema import Draft202012Validator
        from rdflib import Graph
        from referencing import Registry, Resource
        from pyshacl import validate as shacl_validate
    except ImportError as exc:
        failures.append(f"semantic qualification dependency unavailable: {exc}")
        return

    graphs = {}
    for path in sorted((ROOT / "ontology").glob("*.ttl")):
        try:
            graph = Graph()
            graph.parse(path, format="turtle")
            graphs[path.name] = graph
        except Exception as exc:
            failures.append(f"invalid Turtle {rel(path)}: {exc}")

    if "fortune500-fibo-profile.ttl" in graphs and "aps-shapes.ttl" in graphs:
        try:
            conforms, _, report = shacl_validate(
                data_graph=graphs["fortune500-fibo-profile.ttl"],
                shacl_graph=graphs["aps-shapes.ttl"],
                inference="rdfs",
                abort_on_first=False,
                allow_infos=False,
                allow_warnings=False,
                meta_shacl=True,
                advanced=False,
                js=False,
            )
            if not conforms:
                failures.append(f"SHACL validation failed for synthetic FIBO profile: {report}")
        except Exception as exc:
            failures.append(f"SHACL execution failed: {exc}")

    schemas = {}
    resources = []
    for path in sorted((ROOT / "contracts").glob("*.schema.json")):
        schema = load_json(path, failures)
        if not schema:
            continue
        try:
            Draft202012Validator.check_schema(schema)
            schemas[path.name] = schema
            resources.append((schema["$id"], Resource.from_contents(schema)))
        except Exception as exc:
            failures.append(f"invalid JSON Schema {rel(path)}: {exc}")
    registry = Registry().with_resources(resources)

    def validate_instance(instance, schema_name: str, scope: str) -> None:
        schema = schemas.get(schema_name)
        if not schema:
            failures.append(f"cannot validate {scope}: missing schema {schema_name}")
            return
        try:
            Draft202012Validator(schema, registry=registry).validate(instance)
        except Exception as exc:
            failures.append(f"schema validation failed for {scope}: {exc}")

    contract = load_json(ROOT / "examples/fortune500-fibo/knowledge-contract.json", failures)
    reconstitution = load_json(ROOT / "examples/fortune500-fibo/reconstitution.json", failures)
    events = load_json(ROOT / "examples/fortune500-fibo/process-events.json", failures)
    if contract:
        validate_instance(contract, "knowledge-contract.schema.json", "synthetic knowledge contract")
    if reconstitution:
        validate_instance(reconstitution, "reconstitution.schema.json", "synthetic reconstitution plan")
    if isinstance(events, list):
        for index, event in enumerate(events):
            validate_instance(event, "process-event.schema.json", f"process event {index}")


def git_blob_id(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def validate_engineering_standards_adoption(root: Path, failures: list[str]) -> None:
    """Qualify the engineering-standards root adoption at ``root``.

    Checks exact-identity agreement between the adoption manifest, the RDF
    project profile and the AGENTS.md binding header; refuses stale root
    coordinates, pinned-schema tampering, path escape, duplicate subjects,
    unadmitted semantic surfaces and any drop of the no-DO-authority non-claims.
    """
    scope = "engineering-standards adoption"
    manifest_path = root / ADOPTION_MANIFEST
    schema_path = root / ADOPTION_SCHEMA
    if not manifest_path.is_file():
        failures.append(f"{scope}: missing {ADOPTION_MANIFEST}")
        return
    try:
        manifest = json.loads(manifest_path.read_text())
    except Exception as exc:
        failures.append(f"{scope}: invalid JSON {ADOPTION_MANIFEST}: {exc}")
        return
    if not isinstance(manifest, dict):
        failures.append(f"{scope}: manifest must be a JSON object")
        return

    if not schema_path.is_file():
        failures.append(f"{scope}: missing pinned schema {ADOPTION_SCHEMA}")
    else:
        schema_bytes = schema_path.read_bytes()
        if git_blob_id(schema_bytes) != ADOPTION_SCHEMA_BLOB:
            failures.append(f"{scope}: pinned schema {ADOPTION_SCHEMA} does not match root blob {ADOPTION_SCHEMA_BLOB}")
        else:
            try:
                from jsonschema import Draft202012Validator
                validator = Draft202012Validator(json.loads(schema_bytes))
                for error in sorted(validator.iter_errors(manifest), key=lambda e: list(e.path)):
                    failures.append(f"{scope}: schema violation at {list(error.path)}: {error.message}")
            except ImportError as exc:
                failures.append(f"{scope}: jsonschema unavailable: {exc}")

    repo = manifest.get("repository")
    base = manifest.get("base_sha")
    root_meta = manifest.get("root") if isinstance(manifest.get("root"), dict) else {}
    root_sha = root_meta.get("sha")
    root_repo = root_meta.get("repository")
    if repo != ADOPTION_REPOSITORY:
        failures.append(f"{scope}: repository subject {repo!r} is not {ADOPTION_REPOSITORY!r}")
    if manifest.get("project_profile") != ADOPTION_PROFILE:
        failures.append(f"{scope}: project_profile must be {ADOPTION_PROFILE!r}")
    constitution = manifest.get("local_constitution")
    if constitution != "AGENTS.md":
        failures.append(f"{scope}: local_constitution must be 'AGENTS.md', got {constitution!r}")
    generator = manifest.get("generator_identity")
    if isinstance(generator, str) and "@" in generator and generator.rsplit("@", 1)[1] != root_sha:
        failures.append(f"{scope}: generator_identity pinned to stale root {generator.rsplit('@', 1)[1]!r}, root is {root_sha!r}")
    non_claims = manifest.get("non_claims")
    if not isinstance(non_claims, list):
        non_claims = []
    for claim in ADOPTION_NON_CLAIMS:
        if claim not in non_claims:
            failures.append(f"{scope}: required non-claim missing: {claim!r}")

    semantic_dir = root / "semantic"
    if semantic_dir.exists():
        present = {p.relative_to(root).as_posix() for p in semantic_dir.rglob("*") if p.is_file()}
        extra = sorted(present - ADOPTION_SEMANTIC_FILES)
        if extra:
            failures.append(f"{scope}: unadmitted semantic surfaces: {extra}")

    profile_path = root / ADOPTION_PROFILE
    if not profile_path.is_file():
        failures.append(f"{scope}: missing {ADOPTION_PROFILE}")
    else:
        try:
            from rdflib import Graph, Literal, Namespace, URIRef
            from rdflib.namespace import DCTERMS, RDF
        except ImportError as exc:
            failures.append(f"{scope}: rdflib unavailable: {exc}")
        else:
            graph = Graph()
            try:
                graph.parse(profile_path, format="turtle")
            except Exception as exc:
                failures.append(f"{scope}: invalid Turtle {ADOPTION_PROFILE}: {exc}")
                graph = None
            if graph is not None:
                es = Namespace("https://w3id.org/chatman/engineering-standards#")
                prof = Namespace("http://www.w3.org/ns/dx/prof/")
                subjects = list(graph.subjects(RDF.type, es.RepositorySubject))
                profiles = list(graph.subjects(RDF.type, prof.Profile))
                if len(subjects) != 1:
                    failures.append(f"{scope}: expected exactly one es:RepositorySubject, got {len(subjects)}")
                if len(profiles) != 1:
                    failures.append(f"{scope}: expected exactly one prof:Profile, got {len(profiles)}")
                for subject in subjects:
                    repos = set(graph.objects(subject, es.repository))
                    bases = set(graph.objects(subject, es.baseSha))
                    if repos != {Literal(repo)}:
                        failures.append(f"{scope}: profile es:repository {sorted(map(str, repos))} != manifest {repo!r}")
                    if bases != {Literal(base)}:
                        failures.append(f"{scope}: profile es:baseSha {sorted(map(str, bases))} != manifest {base!r}")
                source = URIRef(f"https://github.com/{root_repo}/commit/{root_sha}")
                for profile in profiles:
                    if set(graph.objects(profile, prof.isProfileOf)) != {URIRef(ADOPTION_ROOT_IRI)}:
                        failures.append(f"{scope}: prof:isProfileOf must be exactly <{ADOPTION_ROOT_IRI}>")
                    if set(graph.objects(profile, DCTERMS.source)) != {source}:
                        failures.append(f"{scope}: dcterms:source must be exactly <{source}>")

    agents_path = (root / constitution) if isinstance(constitution, str) else None
    if agents_path is None or not agents_path.resolve().is_relative_to(root.resolve()) or not agents_path.is_file():
        failures.append(f"{scope}: local constitution {constitution!r} is not a file inside the repository")
    else:
        agents = agents_path.read_text()
        if not agents.startswith("# Engineering Standards Root Binding\n"):
            failures.append(f"{scope}: AGENTS.md must open with the generated root-binding header")
        header = agents.split("\n---\n", 1)[0]
        for phrase in (
            f"`{root_repo}@{root_sha}`",
            f"`{repo}@{base}`",
            f"`{ADOPTION_MANIFEST}`",
            f"`{ADOPTION_PROFILE}`",
            "do not acquire ambient DO authority",
        ):
            if phrase not in header:
                failures.append(f"{scope}: AGENTS.md binding header missing {phrase!r}")


def verify_repository() -> tuple[list[str], dict]:
    failures: list[str] = []

    actual_top = {p.name for p in ROOT.iterdir() if p.name != ".git"}
    missing = sorted(EXPECTED_TOP - actual_top)
    extra = sorted(actual_top - EXPECTED_TOP)
    if missing:
        failures.append(f"missing top-level surfaces: {missing}")
    if extra:
        failures.append(f"unadmitted top-level surfaces: {extra}")

    for path in active_files():
        rp = rel(path)
        if any(marker in rp for marker in STALE_PATH_MARKERS):
            failures.append(f"stale active path: {rp}")
        if text_file(path):
            try:
                text = path.read_text()
            except UnicodeDecodeError:
                failures.append(f"non-UTF8 active text surface: {rp}")
                continue
            for marker in STALE_CONTENT_MARKERS:
                if marker in text:
                    failures.append(f"stale active content marker {marker!r} in {rp}")

    version_dir = ROOT / "specification-guide/src/v26_8_24"
    actual_chapters = sorted(p.name for p in version_dir.glob("*.md")) if version_dir.exists() else []
    if actual_chapters != EXPECTED_CHAPTERS:
        failures.append(f"chapter set mismatch: expected {EXPECTED_CHAPTERS}, got {actual_chapters}")
    summary = (ROOT / "specification-guide/src/SUMMARY.md").read_text()
    for chapter in EXPECTED_CHAPTERS:
        if f"v26_8_24/{chapter}" not in summary:
            failures.append(f"SUMMARY missing {chapter}")

    jig = (version_dir / "03_jig_maturity.md").read_text()
    levels = re.findall(r"^### L([1-5]) — ", jig, flags=re.MULTILINE)
    if levels != ["1", "2", "3", "4", "5"]:
        failures.append(f"jig maturity must be exactly five levels L1-L5; got {levels}")
    if re.search(r"^### (?:L0\b|Level 0\b)", jig, flags=re.MULTILINE):
        failures.append("jig maturity defines forbidden sixth baseline L0")
    for dimension in ["Product knowledge", "Work positioning", "Operation guidance", "Process sequence", "Error prevention", "Measurement & qualification", "Adaptation & learning"]:
        if f"| {dimension} |" not in jig:
            failures.append(f"jig matrix missing dimension: {dimension}")

    require_phrases((version_dir / "13_aps_constitution.md").read_text(), [
        "Everything is sunk", "Preserve truth, not implementations", "Zero continuation privilege",
        "Zero uninformed elimination", "Contract before implementation", "No ambient DO authority",
        "Zero unreceipted actuation", "No prose outranks evidence", "factory itself must remain reconstitutable"
    ], "constitution", failures)
    require_phrases((version_dir / "05_contract_first_ggen_first.md").read_text(), [
        "Known pattern? Compose it.", "Known tool? Generate its invocation.",
        "Novel mechanism? Discover it once, then teach the factory.", "Application =", "Library ="
    ], "ggen-first chapter", failures)
    require_phrases((version_dir / "17_rices_theorem_and_epistemic_boundaries.md").read_text(), [
        "Rice's Theorem", "arbitrary programs", "bounded standing", "model confidence is not standing"
    ], "Rice chapter", failures)
    require_phrases((version_dir / "18_reference_manufacturing_stack.md").read_text(), [
        "ggen-marketplace", "ggen-legacy", "ggen-create", "ggen-spec-kit", "clap-noun-verb", "ggen-mcp",
        "ash_r2rml", "XaaS", "AutoFDE Lab", "GymAct", "ex4pm", "Reference implementations are themselves sunk"
    ], "reference stack", failures)
    require_phrases((version_dir / "19_industrial_lineage_from_jig_to_autonomic_factory.md").read_text(), [
        "industrial memory", "Jidoka", "poka-yoke", "Automated craftsmanship versus manufacture"
    ], "industrial lineage", failures)

    core_ontology = (ROOT / "ontology/aps-core.ttl").read_text()
    for marker in ["http://www.w3.org/ns/prov#", "http://www.w3.org/ns/odrl/2/", "http://www.w3.org/ns/shacl#", "http://www.w3.org/ns/dqv#"]:
        if marker not in core_ontology:
            failures.append(f"core ontology missing public vocabulary {marker}")
    fibo = (ROOT / "ontology/fortune500-fibo-profile.ttl").read_text()
    if "https://spec.edmcouncil.org/fibo/ontology/master/latest/BE/LegalEntities/LegalPersons/" not in fibo:
        failures.append("FIBO profile missing admitted LegalPersons import")

    enterprise = load_json(ROOT / "examples/fortune500-fibo/enterprise.json", failures)
    contract = load_json(ROOT / "examples/fortune500-fibo/knowledge-contract.json", failures)
    reconstitution = load_json(ROOT / "examples/fortune500-fibo/reconstitution.json", failures)
    events = load_json(ROOT / "examples/fortune500-fibo/process-events.json", failures)
    manifest = load_json(ROOT / "MANIFEST.json", failures)
    if enterprise and enterprise.get("evidenceClass") != "SYNTHETIC_SENSITIVITY_MODEL_NOT_FORECAST":
        failures.append("Fortune-500 example must remain explicitly synthetic")
    if contract and contract.get("standingRule") not in STANDING:
        failures.append("example contract uses invalid standing")
    if reconstitution and len(reconstitution.get("candidateStrategies", [])) < 3:
        failures.append("reconstitution example lacks DfCM strategy breadth")
    if events:
        for i, event in enumerate(events):
            for key in ("eventId", "activity", "time", "objects", "authorityRef", "receiptRef"):
                if key not in event:
                    failures.append(f"process event {i} missing {key}")
    if manifest:
        if manifest.get("version") != "26.8.24":
            failures.append("MANIFEST version mismatch")
        if manifest.get("predecessor", {}).get("commit") != "ab04337b2db63c66fa23c217bf76622fc9c73b6d":
            failures.append("MANIFEST predecessor coordinate mismatch")

    validate_machine_readable(failures)
    validate_engineering_standards_adoption(ROOT, failures)

    if (ROOT / "specification-guide/book").exists() or (ROOT / "specification-guide/dist").exists():
        failures.append("generated book/dist outputs must not be committed as active source")

    authority_paths = [
        ROOT / "MANIFEST.json", ROOT / ".aps-syntax.md",
        ROOT / ADOPTION_MANIFEST, ROOT / ADOPTION_PROFILE, ROOT / ADOPTION_SCHEMA,
        *sorted((ROOT / "ontology").glob("*.ttl")),
        *sorted((ROOT / "contracts").glob("*.json")),
        *[version_dir / name for name in EXPECTED_CHAPTERS],
    ]
    digest = hashlib.sha256()
    checked = []
    for path in authority_paths:
        if not path.exists():
            continue
        data = path.read_bytes()
        digest.update(rel(path).encode() + b"\0" + data + b"\0")
        checked.append({"path": rel(path), "sha256": hashlib.sha256(data).hexdigest()})

    receipt = {
        "schema": "aps.repository-verification.v26.8.24",
        "standing": "ALIVE" if not failures else "REFUSED",
        "scope": "repository-coherence-not-crown-hypothesis",
        "authoritySetSha256": digest.hexdigest(),
        "checkedAuthorityFiles": checked,
        "failures": failures,
        "nonClaims": [
            "ALIVE here means the repository satisfies its declared structural constitution and executable semantic/schema qualification.",
            "It does not prove Fortune-500 semantic closure, economic dominance, or safe universal actuation."
        ]
    }
    return failures, receipt


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--no-receipt", action="store_true")
    args = parser.parse_args()
    failures, receipt = verify_repository()
    if args.receipt and not args.no_receipt:
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if failures:
        for failure in failures:
            print(f"REFUSED: {failure}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
