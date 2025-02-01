"""
Retrieves and writes a plain-text list of GitHub login IDs from the contributors of the
specified repositories.

Args (taken from environment variables as passed by the "with" block of the action):
    INPUT_REPO_NAME (str): Name of the repository to scan.
    INPUT_FILE_NAME (str): Name of the output file.
    INPUT_ACCESS_TOKEN (str): GitHub access token.

Returns:
    None

Raises:
    ValueError: If any of the required environment variables are empty.
"""

import os

from github import Github

__app_name__ = "List Contributors Simple"
__version__ = "1.0.2"


env_vars = ["INPUT_REPO_NAME", "INPUT_FILE_NAME", "INPUT_ACCESS_TOKEN"]

# Get input from environment variables
repo_name, file_name, access_token = (os.environ.get(var) for var in env_vars)

# raise an error if any of the required environment variables are ""
for var in repo_name, access_token, file_name:
    if not var:
        raise ValueError(
            f"::error title={__app_name__}::{__version__} - {env_vars[env_vars.index(var)]} is required."
        )

output_path = os.environ.get["GITHUB_WORKSPACE"]
github = Github(access_token)

# if "repo_name" contains a comma, turn it into a list.  Need to ensure there are no spaces around the comma!!
if "," in repo_name:
    repo_name = repo_name.replace(", ", ",")
    repo_name = repo_name.split(",")


# for each repo in repo_name, get the list of contributors' login IDs and append them to the file
for repo_name in repo_name:
    repo = github.get_repo(repo_name)

    with open(os.path.join(output_path, file_name), "a", encoding="utf-8") as f:
        f.write(
            "\n".join([contributor.login for contributor in repo.get_contributors()])
        )
