# List Contributors Simple

GitHub Action to write a plain-text list of contributors to a file.

Based on [https://github.com/Maanuj-Vora/List-Contributors](https://github.com/Maanuj-Vora/List-Contributors).

## Setting Up The Workflow Run

| Input Tag    | Required | Default Value    | Example                             |
| ------------ | -------- | ---------------- | ----------------------------------- |
| REPO_NAME    | True     | N/A              | Nightblade/List-Contributors-Simple |
| FILENAME     | False    | contributors.txt | some-file.txt                       |
| ACCESS_TOKEN | True     | N/A              | ${{secrets.GITHUB_TOKEN}}           |

```yaml
name: Example usage

on:
  workflow_dispatch:

jobs:
  get-contributors:
    runs-on: ubuntu-latest
    steps:
      - uses: nightblade/get-contributors-list@main
        with:
          repo_name: 'nightblade/list-contributors-simple'
          filename: 'contributors.txt'
          access_token: ${{secrets.GITHUB_TOKEN}}
      - run: |
        cat contributors.txt
```
