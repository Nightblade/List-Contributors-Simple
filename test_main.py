import os
import unittest
import subprocess

os.environ["INPUT_REPO_NAME"] = "Nightblade/List-Contributors-Simple, another_repo"
os.environ["INPUT_FILENAME"] = "test_file"
os.environ["INPUT_ACCESS_TOKEN"] = "test_token"
os.environ["GITHUB_WORKSPACE"] = "."


class TestMain(unittest.TestCase):
    def test_main(self):
        result = subprocess.run(["python", "main.py"], capture_output=True, text=True)
        print(result.stdout)
        self.assertEqual(result.returncode, 0)
        with open("test_file", "r") as file:
            output = file.read()
        self.assertIn("contrib_login1", output)
        self.assertIn("contrib_login2", output)
        self.assertIn("another_contrib_login1", output)
        self.assertIn("another_contrib_login2", output)


if __name__ == "__main__":
    unittest.main()
