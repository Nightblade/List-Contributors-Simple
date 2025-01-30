"""
Retrieves and writes a list of contributors' login IDs from a given repository.

Args:
    repo_name (str): The name of the repository to scan.
    filename (str): The name of the output file.
    access_token (str): The GitHub access token.

Returns:
    None

Raises:
    ValueError: If any of the required environment variables are missing or empty.
"""

import os
import sys

from github import Github

__app_name__ = "List Contributors Simple"
__version__ = "1.0.1"


def get_env(var_name: str) -> str:
    """Returns the value of a given GitHub Actions input variable.

    Args:
        var_name: The name of the input variable sans "INPUT_" prefix.

    Returns:
        The value of the input variable.
    """
    var_name = f"INPUT_{var_name}"
    var_value = os.environ.get(var_name) or ""
    print(f"{var_name} is '{var_value}'")
    if var_value == "":
        sys.stderr.write(
            f"::error:: {var_name} is required ({__app_name__} v{__version__}).\n"
        )
        raise ValueError(f"{var_name} is required.")
    return var_value


def get_contributors_login_ids(repository) -> list[str]:
    """Retrieves a list of contributor's login IDs from a given GitHub repository.

    If a contributor's login is not available, placeholder "Unknown" is used instead.

    Args:
        repository: A PyGithub repository object from which to retrieve contributor's login IDs.

    Returns:
        A list of strings representing the requested login IDs of the contributors.
    """
    contributor_logins = []
    for contributor in repository.get_contributors():
        login_id = contributor.login or "Unknown"
        contributor_logins.append(login_id)

    return contributor_logins


repo_name, file_name, access_token = (
    get_env("REPO_NAME"),
    get_env("FILENAME"),
    get_env("ACCESS_TOKEN"),
)

output_path = os.environ["GITHUB_WORKSPACE"]

github = Github(access_token)

repo = github.get_repo(repo_name)

login_ids = get_contributors_login_ids(repo)

with open(output_path + "/" + file_name, "w", encoding="utf-8") as f:
    f.write("\n".join(login_ids))
