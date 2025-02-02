# List Contributors Simple

Action to write a plain-text list of contributors' login IDs to a file.

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
      - uses: nightblade/list-contributors-simple@v1
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
