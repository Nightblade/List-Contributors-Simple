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
          repo_names: |
            nightblade/pob-dict
            Nightblade/List-Contributors-Simple
          output_file: "contributors.txt"
          access_token: ${{secrets.GITHUB_TOKEN}}
      - run: cat contributors.txt
```

## Inputs

| Input        | Default | Required | Description                         |
| ------------ | ------- | -------- | ----------------------------------- |
| repo_names   | N/A     | True     | A list of one or more repo names[^1] |
| output_file  | N/A     | True     | Name of the output file.            |
| access_token | N/A     | True     | GitHub token.                       |

[^1]: Use pipe ("\|") syntax if more than one repo name, as shown in example above.
