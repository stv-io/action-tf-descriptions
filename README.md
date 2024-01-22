# action-tf-descriptions

A github action to check the outputs and variables defined for defined, and unique, descriptions.

References:

- <https://developer.hashicorp.com/terraform/language/values/variables#input-variable-documentation>
- <https://developer.hashicorp.com/terraform/language/values/outputs#description-output-value-documentation>

## Why

Until this discusson and feature by [tflint](https://github.com/terraform-linters/tflint) is implemented - <https://github.com/terraform-linters/tflint-ruleset-terraform/discussions/112>

## Usage

To use this action in your workflow, checkout your terraform, and configure the action with the path where your `.tf` files are

```yaml
jobs:
  check-for-valid-descriptions:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: stv-io/action-tf-descriptions@v0.1.0
      with:
        path: "path/to/terraform"
```

In the case of a mono-repo, this can be executed in parallel, pasing the path using the [matrix strategy](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs)

```yaml
jobs:
  check-for-valid-descriptions:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        path:
          - /path/one
          - /path/two
          # - ..
    steps:
    - uses: actions/checkout@v4
    - uses: stv-io/action-tf-descriptions@v0.1.0
      with:
        path: "${{ matrix.path }}"
```

## Local testing

Note - these same tests are asserted in the action's own checks, with an output of the status to a PR comment.

```console
python src/run.py test/passing/
python src/run.py test/failing-missing/
python src/run.py test/failing-non-unique/
```
