"""
replace me with your test
"""

from {{cookiecutter.project_slug}}.hello import hello


def test_hello():
    assert hello("{{cookiecutter.author_name}}") == "hello, {{cookiecutter.author_name}}"
