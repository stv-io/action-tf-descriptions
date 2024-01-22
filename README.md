# action-tf-descriptions

A github action to check the outputs and variables defined for defined, and unique, descriptions.

## Why

Until this discusson and feature by [tflint](https://github.com/terraform-linters/tflint) is implemented - <https://github.com/terraform-linters/tflint-ruleset-terraform/discussions/112>

## Usage

To use tfswitch github action, configure a YAML workflow file, e.g.

```yaml
jobs:
  check-for-valid-descriptions:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Setup tfswitch
      uses: stv-io/action-tf-descriptions@v1
    - run: |
      with:
        path: "path/to/terraform"
```

## TODO

Docs
Test this from another project
Releases
Publish to market place
