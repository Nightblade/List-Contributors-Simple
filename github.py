# stub for testing


class Github:
    def __init__(self, access_token):
        self.access_token = access_token
        self.repos = {
            "Nightblade/List-Contributors-Simple": Repository(
                "Nightblade/List-Contributors-Simple"
            ),
            "another_repo": Repository("another_repo"),
        }

    def get_repo(self, repo_name):
        return self.repos.get(repo_name)


class Repository:
    def __init__(self, name):
        self.name = name

    def get_contributors(self):
        if self.name == "test_repo":
            contributors = [
                Contributor("contrib_name1", "contrib_login1"),
                Contributor("contrib_name1", "contrib_login2"),
            ]
        elif self.name == "another_repo":
            contributors = [
                Contributor("another_contrib_name1", "another_contrib_login1"),
                Contributor("another_contrib_name2", "another_contrib_login2"),
            ]
        else:
            contributors = []
        return contributors


class Contributor:
    def __init__(self, name, login):
        self.name = name
        self.login = login
