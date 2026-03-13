## {{cookiecutter.project_slug}}
This package
* does this
* does that

### Prerequisites
Python 3.13+, `make`, `uv`

### Requirements
see `pyproject.toml`, `dependencies` and `dependency-groups`

### Usage
example:
```bash
$ cd {{cookiecutter.project_name}}
{{cookiecutter.project_name}} $ make install
{{cookiecutter.project_name}} $ source .venv/bin/activate
({{cookiecutter.project_slug}}) {{cookiecutter.project_name}} $ python src/{{cookiecutter.project_slug}}/hello.py
({{cookiecutter.project_slug}}) {{cookiecutter.project_name}} $ pytest tests/unit/test_hello.py
({{cookiecutter.project_slug}}) {{cookiecutter.project_name}} $ python
>>> from {{cookiecutter.project_slug}}.hello import hello
>>> print(hello("{{cookiecutter.author_name}}"))
```

### Tests
see `tests/unit/` and `tests/integration`
