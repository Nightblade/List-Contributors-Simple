# List Contributors Simple

GitHub Action to write a plain-text list of contributors to a file.

Based on [https://github.com/Maanuj-Vora/List-Contributors](https://github.com/Maanuj-Vora/List-Contributors).

## Setting Up The Workflow Run

| Input Tag    | Required | Default Value | Example                             |
| ------------ | -------- | ------------- | ----------------------------------- |
| repo_name    | True     | N/A           | nightblade/list-contributors-simple |
| filename     | True     | N/A           | contributors.txt                    |
| access_token | True     | N/A           | ${{secrets.GITHUB_TOKEN}}           |

```yaml
name: Example usage

on:
  workflow_dispatch:

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - uses: nightblade/list-contributors-simple@main
        with:
          repo_name: "nightblade/list-contributors-simple"
          filename: "contributors.txt"
          access_token: ${{secrets.GITHUB_TOKEN}}
      - run: cat contributors.txt
```
