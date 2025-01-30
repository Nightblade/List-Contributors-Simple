# List Contributors Simple

[![GitHub Super-Linter](https://github.com/nightblade/list-contributors-simple/actions/workflows/linter.yml/badge.svg)](https://github.com/super-linter/super-linter)
![CI](https://github.com/nightblade/list-contributors-simple/actions/workflows/CI.yml/badge.svg)

GitHub Action to write a plain-text list of contributors to a file.

Based on [https://github.com/Maanuj-Vora/List-Contributors](https://github.com/Maanuj-Vora/List-Contributors).

## Usage

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

## Inputs

| Input        | Default | Required | Description                     |
| ------------ | ------- | -------- | ------------------------------- |
| repo_name    | N/A     | True     | Name of the repository to scan. |
| filename     | N/A     | True     | Name of the output file.        |
| access_token | N/A     | True     | GitHub token.                   |
