import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("aps_verify", ROOT / "tools/verify.py")
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class RepositoryConstitutionTest(unittest.TestCase):
    def test_whole_repository_constitution(self):
        failures, receipt = verify.verify_repository()
        self.assertEqual([], failures, "\n".join(failures))
        self.assertEqual("ALIVE", receipt["standing"])


if __name__ == "__main__":
    unittest.main()
