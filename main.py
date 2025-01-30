#!/usr/bin/env python3

import os

from github import Github


def gh_input(input_name: str) -> str:
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


repo_name, file_name, access_token = (
    gh_input("REPO_NAME"),
    gh_input("FILENAME"),
    gh_input("ACCESS_TOKEN"),
)

output_path = os.environ["GITHUB_WORKSPACE"]

github = Github(access_token)

repo = github.get_repo(repo_name)

logins = get_contributors_logins(repo)

with open(output_path + "/" + file_name, "w", encoding="utf-8") as f:
    f.write("\n".join(logins))
