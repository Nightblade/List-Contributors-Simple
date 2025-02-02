"""
Retrieves and writes a plain-text list of GitHub login IDs from the contributors of the
specified repositories.

Args (taken from environment variables as passed by the "with" block of the action):
    INPUT_REPO_NAMES (str): One or more comma-separated repository names.
    INPUT_OUTPUT_FILE (str): Name of the output file.
    INPUT_ACCESS_TOKEN (str): GitHub access token.

Returns:
    None

Raises:
    ValueError: If any of the required environment variables are empty.
"""

import os
from typing import List

from github import Github

__app_name__ = "List Contributors Simple"
__version__ = "1.1.0"


env_vars = [
    "INPUT_REPO_NAMES",
    "INPUT_OUTPUT_FILE",
    "INPUT_ACCESS_TOKEN",
]

# Get input from environment variables
repo_names: str = os.environ.get("INPUT_REPO_NAMES")
output_file: str = os.environ.get("INPUT_OUTPUT_FILE")
access_token: str = os.environ.get("INPUT_ACCESS_TOKEN")

print(f"::repo_names::{repo_names}")

# raise an error if any of the required environment variables are ""
for v, e in zip([repo_names, output_file, access_token], env_vars):
    if v is None or v == "":
        print(f"::error title={__app_name__}::{__version__} - {e} is required.")
        raise ValueError(f"{e} is required.")

workspace_path: str = os.environ.get("GITHUB_WORKSPACE")
g: Github = Github(access_token)

# split repo_names by "\n" or ","
if "\n" in repo_names:
    cooked_repo_names: List[str] = repo_names.split("\n")
elif "," in repo_names:
    cooked_repo_names: List[str] = repo_names.split(",")

# remove leading and trailing spaces from each element of cooked_repo_names
for i, r in enumerate(cooked_repo_names):
    cooked_repo_names[i] = r.strip()

# for each repo in cooked_repo_names, get each contributor in repo, get their login ID, append to the 
# output file
for repo in cooked_repo_names:
    r = g.get_repo(repo)
    contributors = r.get_contributors()
    with open(os.path.join(workspace_path, output_file), "a", encoding="utf-8") as f:
        for c in contributors:
            f.write(f"{c.login}\n")
