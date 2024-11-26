import shutil
from typing import Generator

import pytest
import os
from pathlib import Path
import tempfile


@pytest.fixture(scope="session")
def debian_project_directory(projects_directory: Generator[str, None, None]) -> str:
    return str(Path(os.path.join(projects_directory, "debian")).absolute())


@pytest.fixture(scope="session")
def pyproject_project_directory(projects_directory: Generator[str, None, None]) -> str:
    return str(Path(os.path.join(projects_directory, "pyproject")).absolute())


@pytest.fixture(scope="session")
def projects_directory() -> Generator[str, None, None]:
    """Directory containing 'fake' projects for all systems."""
    original_directory = os.path.join("tests", "projects")

    temporary_directory = tempfile.TemporaryDirectory()
    projects_directory = os.path.join(temporary_directory.name, "projects")

    shutil.copytree(original_directory, projects_directory)

    yield projects_directory

    temporary_directory.cleanup()


@pytest.fixture(scope="session")
def bogus_directory() -> Generator[str, None, None]:
    """Directory that exists, but does not contain a project."""
    directory = tempfile.TemporaryDirectory()

    yield directory

    directory.cleanup()
