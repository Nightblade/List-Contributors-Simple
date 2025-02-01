"""
Retrieves and writes a plain-text list of GitHub login IDs from the contributors of the
specified repositories.

Args (taken from environment variables as passed by the "with" block of the action):
    INPUT_REPO_NAME (str): Name of the repository to scan.
    INPUT_FILENAME (str): Name of the output file.
    INPUT_ACCESS_TOKEN (str): GitHub access token.

Returns:
    None

Raises:
    ValueError: If any of the required environment variables are empty.
"""

import os
from typing import List

try:
    from github import Github, Repository
except ImportError:
    from .github import Github, Repository


__app_name__ = "List Contributors Simple"
__version__ = "1.0.2"


env_vars = [
    "INPUT_REPO_NAME",
    "INPUT_FILENAME",
    "INPUT_ACCESS_TOKEN",
]

# Get input from environment variables
repo_name: str = os.environ.get("INPUT_REPO_NAME")
file_name: str = os.environ.get("INPUT_FILENAME")
access_token: str = os.environ.get("INPUT_ACCESS_TOKEN")

print(f"::repo_name::{repo_name}")

# raise an error if any of the required environment variables are ""
for v, e in zip([repo_name, file_name, access_token], env_vars):
    if v is None or v == "":
        print(f"::error title={__app_name__}::{__version__} - {e} is required.")
        raise ValueError(f"{e} is required.")

output_path: str = os.environ.get("GITHUB_WORKSPACE")
github: Github = Github(access_token)

# split repo_name by ","
repo_name: List[str] = repo_name.split(",")

# remove leading and trailing spaces from each element of repo_name
for i, r in enumerate(repo_name):
    repo_name[i] = r.strip()

# for each repo in repo_name, get the list of contributors' login IDs and append them to the file
for r in repo_name:
    if r == "":
        continue
    print(f"::repo::{r}")
    repo: Repository = github.get_repo(r)

    with open(os.path.join(output_path, file_name), "a", encoding="utf-8") as f:
        f.write(
            "\n".join([contributor.login for contributor in repo.get_contributors()])
            + "\n"
        )
