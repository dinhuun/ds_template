import shutil
from collections import namedtuple
from pathlib import Path

import pytest
from cookiecutter import main


TEMPLATE_ROOT = Path(__file__).parents[2].resolve()
Project = namedtuple("Project", ["path", "context"])
custom_context = {
    "project_name": "test-project",
    "project_slug": "test_project",
    "author_name": "test author",
    "author_email": "test@example.com",
    "description": "test project",
    "open_source_license": "MIT",
}


@pytest.fixture(params=[{}, custom_context])
def cut_project(tmpdir_factory, request):
    """
    fixture that generates project and returns (path, context) tuple
    """
    temp = tmpdir_factory.mktemp("temp")
    temp_dpath = Path(temp).resolve()

    context = request.param
    main.cookiecutter(
        str(TEMPLATE_ROOT),
        no_input=True,
        extra_context=context,
        output_dir=str(temp_dpath),
    )

    project_name = context.get("project_name", "your project name, such as more-itertools")
    project_dpath = temp_dpath / project_name
    yield Project(path=project_dpath, context=context)

    shutil.rmtree(temp_dpath)
