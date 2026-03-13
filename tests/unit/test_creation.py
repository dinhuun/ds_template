def no_curlies(fpath):
    """
    utility to make sure no curly braces in a file
    that is, whether Jinja is able to render everything
    """
    data = fpath.read_text()
    template_strings = ["{{", "}}", "{%", "%}"]
    return not any(s in data for s in template_strings)


def test_project_created(cut_project):
    """
    tests that project directory is created
    """
    assert cut_project.path.exists()
    assert cut_project.path.is_dir()


def test_project_name(cut_project):
    """
    tests that project name is as expected
    """
    if cut_project.context.get("project_name"):
        assert cut_project.path.name == "test-project"
    else:
        assert cut_project.path.name == "your project name, such as more-itertools"


def test_folder_structure(cut_project):
    """
    tests that folder structure is as expected
    """
    expected_dirs = [
        "data",
        "notebooks",
        "src",
        "tests",
        "tests/integration",
        "tests/unit",
    ]
    for dname in expected_dirs:
        assert (cut_project.path / dname).is_dir()


def test_src_structure(cut_project):
    """
    tests that src structure is as expected
    """
    if cut_project.context.get("project_slug"):
        package_dpath = "test_project"
    else:
        package_dpath = "your project slug, aka package name in snake case, such as more_itertools"
    package_dpath = cut_project.path / "src" / package_dpath
    assert package_dpath.is_dir()


def test_tests_structure(cut_project):
    """
    tests that tests structure is as expected
    """
    unit_test_fpath = cut_project.path / "tests/unit/test_hello.py"
    assert unit_test_fpath.is_file()


def test_gitignore(cut_project):
    """
    tests that .gitignore is as expected
    """
    gitignore_fpath = cut_project.path / ".gitignore"
    assert gitignore_fpath.exists()
    assert no_curlies(gitignore_fpath)


def test_makefile(cut_project):
    """
    tests that Makefile is as expected
    """
    makefile_fpath = cut_project.path / "Makefile"
    assert makefile_fpath.exists()
    assert no_curlies(makefile_fpath)


def test_pyproject_toml(cut_project):
    """
    tests that pyproject.toml is as expected
    """
    pyproject_fpath = cut_project.path / "pyproject.toml"
    assert pyproject_fpath.exists()
    assert no_curlies(pyproject_fpath)

    content = pyproject_fpath.read_text()
    assert "[build-system]" in content
    assert "uv_build" in content

    if cut_project.context.get("project_slug"):
        assert "test_project" in content
    if cut_project.context.get("author_name"):
        assert "test author" in content


def test_readme(cut_project):
    """
    tests that README.md is as expected
    """
    readme_fpath = cut_project.path / "README.md"
    assert readme_fpath.exists()
    assert no_curlies(readme_fpath)
