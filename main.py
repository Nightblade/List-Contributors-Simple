"""Uses PyGithub library to retrieve and writea list of contributors' login IDs from a repository.

The script takes in three arguments: the name of the repository, the name of the output file, and
the GitHub access token. It then uses PyGithub to retrieve the list of contributors's login IDs
from the repository and writes them to a plain text file with the specified name, one ID per line.
"""

import os

from github import Github

__version__ = "1.0.1"


def get_env(var_name: str) -> str:
    """Returns the value of a given GitHub Actions input variable.

    Args:
        var_name: The name of the input variable sans "INPUT_" prefix.

    Returns:
        The value of the input variable.
    """
    var_name = f"INPUT_{var_name}"
    if var_name not in os.environ or os.environ[var_name] is None:
        raise ValueError(f"{var_name} is required")
    return os.environ[var_name]


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
