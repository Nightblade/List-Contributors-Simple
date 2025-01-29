#!/usr/bin/env python

from github import Github
import os


def get_gh_input(input_name: str) -> str:
    """Returns the value of a given GitHub Actions input variable.

    Args:
        input_name: The name of the input variable.

    Returns:
        The value of the input variable.
    """
    return os.environ[f"INPUT_{input_name}"]


def get_contributors_logins(repo) -> list[str]:
    """Retrieves a list of contributor's logins from a given GitHub repository.

    If a contributor's login is not available, a placeholder "Unknown" is used instead.

    Args:
        repo: A PyGithub Repository object from which to retrieve contributor's logins.

    Returns:
        A list of strings representing the requested logins of the contributors.
    """
    contributor_logins = []
    for contributor in repo.get_contributors():
        logins = contributor.login or "Unknown"
        contributor_logins.append(logins)

    return contributor_logins


repo_name, file_path, access_token = (
    get_gh_input("REPO_NAME"),
    get_gh_input("FILENAME"),
    get_gh_input("ACCESS_TOKEN"),
)

github = Github(access_token)

repo = github.get_repo(repo_name)

logins = get_contributors_logins(repo)

try:
    with open(file_path, "w") as f:
        f.write("\n".join(logins))
except IOError as e:
    print(f"Error writing to file: {e}")
except PermissionError as e:
    print(f"Permission denied writing to file: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
