<!-- These are examples of badges you might want to add to your README:
     please update the URLs accordingly

[![Built Status](https://api.cirrus-ci.com/github/<USER>/pre-commit-hooks.svg?branch=main)](https://cirrus-ci.com/github/<USER>/pre-commit-hooks)
[![ReadTheDocs](https://readthedocs.org/projects/pre-commit-hooks/badge/?version=latest)](https://pre-commit-hooks.readthedocs.io/en/stable/)
[![Coveralls](https://img.shields.io/coveralls/github/<USER>/pre-commit-hooks/main.svg)](https://coveralls.io/r/<USER>/pre-commit-hooks)
[![PyPI-Server](https://img.shields.io/pypi/v/pre-commit-hooks.svg)](https://pypi.org/project/pre-commit-hooks/)
[![Conda-Forge](https://img.shields.io/conda/vn/conda-forge/pre-commit-hooks.svg)](https://anaconda.org/conda-forge/pre-commit-hooks)
[![Monthly Downloads](https://pepy.tech/badge/pre-commit-hooks/month)](https://pepy.tech/project/pre-commit-hooks)
[![Twitter](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter)](https://twitter.com/pre-commit-hooks)
-->

[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org/)



# pre-commit-hooks

> A collection of custom Git pre-commit hooks for the OpenSemanticLab / -World packages.

Some out-of-the-box hooks for pre-commit.

See also: https://github.com/pre-commit/pre-commit


### Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0  # Use the ref you want to point at
    hooks:
    -   id: trailing-whitespace
    # -   id: ...
```
or in case of the test hook created within this package:

```yaml
-   repo: https://github.com/OpenSemanticLab/pre-commit-hooks
    rev: v0.1.0  # Use the ref you want to point at
    hooks:
    - id: print-arguments
```

### Hooks available

#### `print-arguments`
Prints the arguments passed to the hook. Source: https://dev.to/jalvaradosegura/create-your-own-pre-commit-hook-3kh


<!-- pyscaffold-notes -->

## Note

This project has been set up using PyScaffold 4.4. For details and usage
information on PyScaffold see https://pyscaffold.org/.
