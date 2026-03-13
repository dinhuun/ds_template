"""
project metadata that user can access
>>> import {{cookiecutter.project_slug}}
>>> {{cookiecutter.project_slug}}.author
>>> ...
>>> {{cookiecutter.project_slug}}.version
>>> {{cookiecutter.project_slug}}.__version__
"""

import importlib.metadata
from email.utils import parseaddr


metadata = importlib.metadata.metadata("{{cookiecutter.project_slug}}")
author_email = metadata["author-email"]
author, a_email = parseaddr(author_email)
description = summary = metadata["summary"]
maintainer_email = metadata["maintainer-email"]
maintainer, m_email = parseaddr(maintainer_email)
name = metadata["name"]
url = metadata["Project-URL"].split(", ", 1)[1]
version = __version__ = metadata["version"]
