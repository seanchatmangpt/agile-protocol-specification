import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("aps_sim", ROOT / "tools/simulate_fortune500.py")
sim = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sim)


class Fortune500SensitivityTest(unittest.TestCase):
    def setUp(self):
        self.model = json.loads((ROOT / "examples/fortune500-fibo/enterprise.json").read_text())

    def test_candidate_space_multiplies_selected_space(self):
        m = sim.calculate(self.model)
        self.assertEqual(
            m["selectedProjectionArtifacts"] * self.model["assumptions"]["architectureCandidates"],
            m["DfCMCandidateProjectionArtifacts"],
        )

    def test_board_validation_objects_do_not_scale_with_artifact_count(self):
        m = sim.calculate(self.model)
        expected = sum(self.model["assumptions"]["manufacturingKnowledgeObjects"][k] for k in (
            "publicOntologyProfiles", "manufacturingPatterns", "authorityPolicies", "verifierPolicies"
        ))
        self.assertEqual(expected, m["boardValidationObjectsAssumption"])
        self.assertGreater(m["governanceCompressionSelectedArtifactsPerBoardObject"], 1)

    def test_model_is_explicitly_non_empirical(self):
        result = sim.run(ROOT / "examples/fortune500-fibo/enterprise.json")
        self.assertEqual("SYNTHETIC_SENSITIVITY_MODEL_NOT_FORECAST", result["evidenceClass"])
        self.assertTrue(any("not empirical" in x.lower() or "not measurements" in x.lower() for x in result["nonClaims"]))


if __name__ == "__main__":
    unittest.main()
