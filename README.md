# List Contributors Simple

[![GitHub Super-Linter](https://github.com/nightblade/list-contributors-simple/actions/workflows/linter.yml/badge.svg)](https://github.com/super-linter/super-linter)
![CI](https://github.com/nightblade/list-contributors-simple/actions/workflows/CI.yml/badge.svg)

Action to write a plain-text list of contributors' login IDs to a file.

Based on [https://github.com/Maanuj-Vora/List-Contributors](https://github.com/Maanuj-Vora/List-Contributors).

## Usage

```yaml
name: Example usage

on:
  workflow_dispatch:

permissions: read-all

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - uses: nightblade/list-contributors-simple@v2
        with:
          repo_names: "nightblade/list-contributors-simple"
          output_file: "contributors.txt"
          access_token: ${{secrets.GITHUB_TOKEN}}
      - run: cat contributors.txt
```

## Inputs

| Input        | Default | Required | Description                                   |
| ------------ | ------- | -------- | --------------------------------------------- |
| repo_names   | N/A     | True     | One or more comma-separated repository names. |
| output_file  | N/A     | True     | Name of the output file.                      |
| access_token | N/A     | True     | GitHub token.                                 |
