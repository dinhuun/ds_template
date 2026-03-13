## Cookiecutter Python Project Template

This is a `cookiecutter` package with a Python DS project template that you can use to create new DS projects.

### Prerequisites
Python 3.13+, `cookiecutter`, `make`, `uv`

### Requirements
see `pyproject.toml`, `dependencies` and `dependency-groups`

### Create new project
```
cookiecutter https://github.com/dinhuun/ds_template.git  # or ds_template if cloned to local
project_name: your project name, Enter
project_slug: your project slug, Enter
author_name: author name, Enter
author_email: author email, Enter
description: description, Enter
open_source_license: 1/2/3, Enter
```
and a new project `project_slug` will be created in current directory.

It will look like this
```
project_name               <- top level
├── data                   <- data
├── notebooks              <- jupyter notebooks
├── src                    <- source code
    └── project_slug       <- where modules are
        ├── hello.py       <- module hello
        └── __init__.py
└── tests                  <- tests
    ├── integration        <- integration tests to test that internal parts and external parts collectively work
    └── unit               <- unit tests to test that internal parts individually work
        ├── test_hello.py  <- tests for module hello
        └── __init__.py
├── .gitignore
├── Makefile               <- Makefile with commands like `make install` or `make lint`
├── pyproject.toml         <- makes project pip installable, such as `pip install -e .` so that src can be imported
├── README.md              <- README for this project
```
