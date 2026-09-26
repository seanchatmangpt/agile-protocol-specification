"""Adversarial court for the engineering-standards v26.9.21 root adoption.

Chicago style: every case runs the real verifier over real files copied into a
temporary directory (or a real subprocess over a full repository copy) and
asserts on the returned failures / receipt state. No test doubles.
"""
import importlib.util
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("aps_verify_adoption", ROOT / "tools/verify.py")
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)

ADOPTION_FILES = ("AGENTS.md", "engineering-standards.json", "semantic")  # semantic/ includes the vendored generator
OTHER_SHA = "0" * 40


def copy_adoption(dst: pathlib.Path) -> pathlib.Path:
    for name in ADOPTION_FILES:
        src = ROOT / name
        if src.is_dir():
            shutil.copytree(src, dst / name)
        else:
            shutil.copy2(src, dst / name)
    return dst


def run(root: pathlib.Path) -> list[str]:
    failures: list[str] = []
    verify.validate_engineering_standards_adoption(root, failures)
    return failures


class CourtFixture(unittest.TestCase):
    """Real adoption files copied into a temporary directory; no test methods."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = copy_adoption(pathlib.Path(self._tmp.name))
        self.manifest_path = self.root / "engineering-standards.json"
        self.profile_path = self.root / "semantic/engineering-standards-profile.ttl"
        self.agents_path = self.root / "AGENTS.md"
        self.manifest = json.loads(self.manifest_path.read_text())

    def tearDown(self):
        self._tmp.cleanup()

    def write_manifest(self):
        self.manifest_path.write_text(json.dumps(self.manifest, indent=2) + "\n")

    def assertRefused(self, needle: str):
        failures = run(self.root)
        self.assertTrue(any(needle in f for f in failures), f"expected {needle!r} in {failures}")



class AdoptionCourt(CourtFixture):
    # -- positive control -------------------------------------------------
    def test_committed_adoption_is_admitted(self):
        self.assertEqual([], run(self.root))

    # -- malformed input --------------------------------------------------
    def test_malformed_manifest_json_refused(self):
        self.manifest_path.write_text("{ not json")
        self.assertRefused("invalid JSON engineering-standards.json")

    def test_non_object_manifest_refused(self):
        self.manifest_path.write_text("[]")
        self.assertRefused("manifest must be a JSON object")

    def test_malformed_turtle_refused(self):
        self.profile_path.write_text(self.profile_path.read_text() + "\nproject:Broken a .\n")
        self.assertRefused("invalid Turtle")

    def test_missing_manifest_refused(self):
        self.manifest_path.unlink()
        self.assertRefused("missing engineering-standards.json")

    def test_missing_profile_refused(self):
        self.profile_path.unlink()
        self.assertRefused("missing semantic/engineering-standards-profile.ttl")

    def test_schema_violation_short_sha_refused(self):
        self.manifest["base_sha"] = "5c31d9d"
        self.write_manifest()
        self.assertRefused("schema violation at ['base_sha']")

    def test_schema_violation_unknown_field_refused(self):
        self.manifest["authority"] = "DO"
        self.write_manifest()
        self.assertRefused("Additional properties are not allowed")

    def test_schema_violation_standing_outside_enum_refused(self):
        self.manifest["standing"] = "VERIFIED"
        self.write_manifest()
        self.assertRefused("schema violation at ['standing']")

    # -- wrong digest / pinned schema tamper -------------------------------
    def test_tampered_pinned_schema_refused(self):
        schema_path = self.root / "semantic/schemas/repository-adoption.schema.json"
        schema = json.loads(schema_path.read_text())
        schema["properties"]["standing"]["enum"].append("VERIFIED")
        schema_path.write_text(json.dumps(schema))
        self.assertRefused("does not match root blob")

    def test_git_blob_id_matches_git(self):
        # Known git blob id of the empty blob and of b"hello\n".
        self.assertEqual("e69de29bb2d1d6434b8b29ae775ad8c2e48c5391", verify.git_blob_id(b""))
        self.assertEqual("ce013625030ba8dba906f756967f9e9ca394464a", verify.git_blob_id(b"hello\n"))

    # -- stale subject / identity mismatch --------------------------------
    def test_manifest_base_sha_disagrees_with_profile_refused(self):
        self.manifest["base_sha"] = OTHER_SHA
        self.write_manifest()
        self.assertRefused("es:baseSha")

    def test_profile_points_at_stale_root_refused(self):
        text = self.profile_path.read_text().replace(self.manifest["root"]["sha"], OTHER_SHA)
        self.profile_path.write_text(text)
        self.assertRefused("dcterms:source must be exactly")

    def test_generator_identity_pinned_to_stale_root_refused(self):
        self.manifest["generator_identity"] = (
            "engineering-standards/scripts/render-repository-adoption.py@" + OTHER_SHA
        )
        self.write_manifest()
        self.assertRefused("is not the generator projection (differing fields: ['generator_identity'])")

    def test_foreign_repository_subject_refused(self):
        self.manifest["repository"] = "seanchatmangpt/some-other-repo"
        self.write_manifest()
        self.assertRefused("repository subject")

    def test_agents_header_bound_to_other_base_refused(self):
        text = self.agents_path.read_text().replace(self.manifest["base_sha"], OTHER_SHA, 1)
        self.agents_path.write_text(text)
        self.assertRefused("AGENTS.md binding header missing")

    def test_agents_header_removed_refused(self):
        text = self.agents_path.read_text().split("\n---\n", 1)[1].lstrip("\n")
        self.agents_path.write_text(text)
        self.assertRefused("must open with the rendered root-binding header")

    def test_wrong_profile_of_refused(self):
        text = self.profile_path.read_text().replace(
            "<https://w3id.org/chatman/engineering-standards>",
            "<https://example.org/not-the-root>",
        )
        self.profile_path.write_text(text)
        self.assertRefused("prof:isProfileOf must be exactly")

    # -- unauthorized action ----------------------------------------------
    def test_dropping_no_do_authority_non_claim_refused(self):
        self.manifest["non_claims"] = [
            c for c in self.manifest["non_claims"] if "DO authority" not in c
        ]
        self.write_manifest()
        self.assertRefused("required non-claim missing")

    def test_agents_header_dropping_no_ambient_do_refused(self):
        text = self.agents_path.read_text().replace("do not acquire ambient DO authority", "may act")
        self.agents_path.write_text(text)
        self.assertRefused("do not acquire ambient DO authority")

    def test_constitution_path_escape_refused(self):
        self.manifest["local_constitution"] = "../AGENTS.md"
        self.write_manifest()
        self.assertRefused("local_constitution must be 'AGENTS.md'")

    # -- duplicate delivery / reordering -----------------------------------
    def test_duplicate_repository_subject_refused(self):
        extra = (
            "\nproject:Repository2 a es:RepositorySubject ;\n"
            f'  es:repository "{self.manifest["repository"]}" ;\n'
            f'  es:baseSha "{self.manifest["base_sha"]}" .\n'
        )
        self.profile_path.write_text(self.profile_path.read_text() + extra)
        self.assertRefused("expected exactly one es:RepositorySubject, got 2")

    def test_second_base_sha_on_one_subject_refused(self):
        self.profile_path.write_text(
            self.profile_path.read_text() + f'\nproject:Repository es:baseSha "{OTHER_SHA}" .\n'
        )
        self.assertRefused("es:baseSha")

    def test_triple_reordering_is_semantically_neutral(self):
        text = self.profile_path.read_text()
        prefixes = [l for l in text.splitlines() if l.startswith("@prefix")]
        body = "\n".join(l for l in text.splitlines() if not l.startswith("@prefix"))
        blocks = [b.strip() for b in body.split("\n\n") if b.strip()]
        self.profile_path.write_text("\n".join(prefixes) + "\n\n" + "\n\n".join(reversed(blocks)) + "\n")
        self.assertEqual([], run(self.root))

    def test_unadmitted_semantic_surface_refused(self):
        (self.root / "semantic/extra.ttl").write_text("")
        self.assertRefused("unadmitted semantic surfaces")


def replace_everywhere(root: pathlib.Path, old: str, new: str) -> None:
    for rel in ("AGENTS.md", "engineering-standards.json", "semantic/engineering-standards-profile.ttl"):
        path = root / rel
        path.write_text(path.read_text().replace(old, new))


class ProjectionCourt(CourtFixture):
    """The adoption files are projections of the pinned root generator; hand edits are refused."""

    def test_committed_manifest_and_profile_equal_real_generator_run(self):
        # Run the vendored root generator as its own real CLI over the pinned
        # parameters and byte-compare with the committed projections.
        with tempfile.TemporaryDirectory() as out:
            proc = subprocess.run(
                [sys.executable, str(ROOT / verify.ADOPTION_GENERATOR),
                 "--repo", verify.ADOPTION_REPOSITORY, "--base", verify.ADOPTION_BASE_SHA,
                 "--role", verify.ADOPTION_ROLE, "--root-sha", verify.ADOPTION_ROOT_SHA,
                 "--out", out],
                capture_output=True, text=True, timeout=60,
            )
            self.assertEqual(0, proc.returncode, proc.stderr)
            out = pathlib.Path(out)
            self.assertEqual((out / "engineering-standards.json").read_bytes(),
                             (ROOT / "engineering-standards.json").read_bytes())
            self.assertEqual((out / "semantic/engineering-standards-profile.ttl").read_bytes(),
                             (ROOT / "semantic/engineering-standards-profile.ttl").read_bytes())

    def test_committed_manifest_standing_is_generator_constant(self):
        self.assertEqual("UNKNOWN", self.manifest["standing"])
        self.assertEqual("engineering-standards/scripts/render-repository-adoption.py",
                         self.manifest["generator_identity"])

    def test_vendored_generator_blob_matches_root(self):
        data = (ROOT / verify.ADOPTION_GENERATOR).read_bytes()
        self.assertEqual(verify.ADOPTION_GENERATOR_BLOB, verify.git_blob_id(data))

    def test_hand_promoted_standing_alive_refused(self):
        self.manifest["standing"] = "ALIVE"
        self.write_manifest()
        failures = run(self.root)
        self.assertTrue(any("stored standing 'ALIVE' is not the generator constant" in f for f in failures), failures)
        self.assertTrue(any("differing fields: ['standing']" in f for f in failures), failures)

    def test_generator_identity_removed_refused(self):
        del self.manifest["generator_identity"]
        self.write_manifest()
        self.assertRefused("differing fields: ['generator_identity']")

    def test_generator_identity_unpinned_hand_written_refused(self):
        self.manifest["generator_identity"] = "hand-written"
        self.write_manifest()
        self.assertRefused("differing fields: ['generator_identity']")

    def test_manifest_reformatting_refused(self):
        self.manifest_path.write_text(json.dumps(self.manifest, indent=4) + "\n")
        self.assertRefused("differing fields: ['formatting']")

    def test_tampered_vendored_generator_refused(self):
        gen = self.root / verify.ADOPTION_GENERATOR
        gen.write_text(gen.read_text().replace('"standing": "UNKNOWN"', '"standing": "ALIVE"'))
        self.assertRefused("does not match root blob " + verify.ADOPTION_GENERATOR_BLOB)

    def test_missing_vendored_generator_refused(self):
        (self.root / verify.ADOPTION_GENERATOR).unlink()
        self.assertRefused("missing vendored generator")

    def test_coordinated_forged_root_sha_refused(self):
        replace_everywhere(self.root, verify.ADOPTION_ROOT_SHA, OTHER_SHA)
        failures = run(self.root)
        self.assertTrue(any("is not the pinned root" in f for f in failures), failures)
        self.assertTrue(any("not the generator projection" in f for f in failures), failures)

    def test_coordinated_forged_base_sha_refused(self):
        replace_everywhere(self.root, verify.ADOPTION_BASE_SHA, OTHER_SHA)
        failures = run(self.root)
        self.assertTrue(any("is not the pinned adoption base" in f for f in failures), failures)
        self.assertTrue(any("graph is not the generator projection" in f for f in failures), failures)

    def test_extra_do_authority_triple_refused(self):
        self.profile_path.write_text(
            self.profile_path.read_text() + '\nproject:Repository es:authority "DO" .\n'
        )
        self.assertRefused("graph is not the generator projection (9 triples vs 8 generated)")

    def test_second_is_profile_of_refused_by_exact_set_check(self):
        self.profile_path.write_text(
            self.profile_path.read_text()
            + "\nproject:Profile prof:isProfileOf <https://example.org/other-root> .\n"
        )
        self.assertRefused("prof:isProfileOf must be exactly")

    def test_no_do_phrase_only_below_header_refused_by_header_scope(self):
        header, body = self.agents_path.read_text().split("\n---\n", 1)
        header = header.replace("do not acquire ambient DO authority", "may act")
        self.agents_path.write_text(header + "\n---\n" + body + "\ndo not acquire ambient DO authority\n")
        self.assertRefused("AGENTS.md binding header missing 'do not acquire ambient DO authority'")

    def test_agents_header_hand_edit_refused(self):
        text = self.agents_path.read_text().replace("- Ecosystem role:", "- Role:", 1)
        self.agents_path.write_text(text)
        self.assertRefused("AGENTS.md header is not the rendered projection")

    def test_agents_body_edit_below_header_admitted(self):
        self.agents_path.write_text(self.agents_path.read_text() + "\nLocal note.\n")
        self.assertEqual([], run(self.root))


class RenderTool(unittest.TestCase):
    """Real subprocess runs of tools/render_adoption.py over a full repository copy."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.copy = pathlib.Path(self._tmp.name) / "aps"
        shutil.copytree(ROOT, self.copy, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def tearDown(self):
        self._tmp.cleanup()

    def render(self, flag):
        return subprocess.run(
            [sys.executable, "tools/render_adoption.py", flag],
            cwd=self.copy, capture_output=True, text=True, timeout=60,
        )

    def test_check_passes_on_committed_tree(self):
        proc = self.render("--check")
        self.assertEqual(0, proc.returncode, proc.stderr)

    def test_hand_edit_detected_and_write_restores_byte_identical(self):
        originals = {rel: (self.copy / rel).read_bytes() for rel in (
            "engineering-standards.json", "semantic/engineering-standards-profile.ttl", "AGENTS.md")}
        manifest = json.loads(originals["engineering-standards.json"])
        manifest["standing"] = "ALIVE"
        (self.copy / "engineering-standards.json").write_text(json.dumps(manifest, indent=2) + "\n")
        agents = self.copy / "AGENTS.md"
        agents.write_text(agents.read_text().replace("- Ecosystem role:", "- Role:", 1))
        proc = self.render("--check")
        self.assertEqual(1, proc.returncode)
        self.assertIn("STALE projection: engineering-standards.json", proc.stderr)
        self.assertIn("STALE projection: AGENTS.md", proc.stderr)
        self.assertEqual(0, self.render("--write").returncode)
        for rel, data in originals.items():
            self.assertEqual(data, (self.copy / rel).read_bytes(), rel)
        self.assertEqual(0, self.render("--check").returncode)


class WholeRepositoryReplay(unittest.TestCase):
    """Real subprocess runs of tools/verify.py over a full repository copy."""

    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory()
        cls.copy = pathlib.Path(cls._tmp.name) / "aps"
        shutil.copytree(ROOT, cls.copy, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()

    def verify_copy(self):
        proc = subprocess.run(
            [sys.executable, "tools/verify.py", "--no-receipt"],
            cwd=self.copy, capture_output=True, text=True, timeout=120,
        )
        return proc.returncode, json.loads(proc.stdout)

    def test_replay_is_byte_identical_and_mutation_is_refused(self):
        code1, receipt1 = self.verify_copy()
        code2, receipt2 = self.verify_copy()
        self.assertEqual((0, "ALIVE"), (code1, receipt1["standing"]))
        self.assertEqual(receipt1, receipt2)
        adoption = receipt1["engineeringStandardsAdoption"]
        self.assertEqual(("ALIVE", []), (adoption["derivedStanding"], adoption["failures"]))
        self.assertEqual("UNKNOWN (generator constant; not standing)", adoption["manifestStandingField"])
        self.assertEqual(verify.ADOPTION_GENERATOR_BLOB, adoption["generatorBlob"])
        checked = {c["path"] for c in receipt1["checkedAuthorityFiles"]}
        self.assertTrue({
            "engineering-standards.json",
            "semantic/engineering-standards-profile.ttl",
            "semantic/schemas/repository-adoption.schema.json",
        } <= checked)

        manifest_path = self.copy / "engineering-standards.json"
        original = manifest_path.read_bytes()
        try:
            data = json.loads(original)
            data["base_sha"] = "f" * 40
            manifest_path.write_text(json.dumps(data, indent=2) + "\n")
            code3, receipt3 = self.verify_copy()
        finally:
            manifest_path.write_bytes(original)
        self.assertEqual((1, "REFUSED"), (code3, receipt3["standing"]))
        self.assertEqual("REFUSED", receipt3["engineeringStandardsAdoption"]["derivedStanding"])
        self.assertNotEqual(receipt1["authoritySetSha256"], receipt3["authoritySetSha256"])


class AdoptionBenchmark(unittest.TestCase):
    """Deterministic timing bound; measured numbers live in tools/bench_adoption.py receipts.

    Bound is ~50x the measured 1.26 ms median (n=200, arm64, Python 3.14, pinned CI deps),
    so it catches algorithmic regressions (e.g. per-call full-repo scans), not jitter.
    """

    BOUND_MEDIAN_SECONDS = 0.06

    def test_adoption_court_median_within_bound(self):
        samples = []
        for _ in range(15):
            start = time.perf_counter()
            failures = run(ROOT)
            samples.append(time.perf_counter() - start)
            self.assertEqual([], failures)
        samples.sort()
        median = samples[len(samples) // 2]
        self.assertLess(median, self.BOUND_MEDIAN_SECONDS, f"median {median:.4f}s samples {samples}")


if __name__ == "__main__":
    unittest.main()
