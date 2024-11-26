from typing import Generator

from cyberfusion.YAVB.systems import Debian, PyProject
from typer.testing import CliRunner
from cyberfusion.YAVB import app
import os

runner = CliRunner()


def test_pyproject_version_increased(
    pyproject_project_directory: Generator[str, None, None],
) -> None:
    old_version = PyProject(pyproject_project_directory).version

    assert old_version == "1.0"

    result = runner.invoke(
        app,
        [
            "--system",
            "pyproject",
            "--bump",
            "patch",
            "--directory",
            pyproject_project_directory,
        ],
    )

    assert result.exit_code == 0, result.output

    new_version = PyProject(pyproject_project_directory).version

    assert new_version == "1.0.1"


def test_debian_version_increased(
    debian_project_directory: Generator[str, None, None],
) -> None:
    old_version = Debian(debian_project_directory).version

    assert old_version == "1.0"

    result = runner.invoke(
        app,
        [
            "--system",
            "debian",
            "--bump",
            "patch",
            "--directory",
            debian_project_directory,
        ],
    )

    assert result.exit_code == 0, result.output

    new_version = Debian(debian_project_directory).version

    assert new_version == "1.0.1"


def test_debian_changelog_entry_added(
    debian_project_directory: Generator[str, None, None],
) -> None:
    CHANGELOG_ENTRY = "foobar"
    NAME = "John Doe"
    EMAIL = "john@example.com"

    def find_changelog_entry() -> None:
        lines = (
            open(os.path.join(debian_project_directory, "debian", "changelog"), "r")
            .read()
            .splitlines()
        )

        assert "  * " + CHANGELOG_ENTRY in lines, "Changelog entry not found"

        assert any(
            line.startswith(" -- " + NAME + " <" + EMAIL + ">") for line in lines
        ), "Name and email not found"

    result = runner.invoke(
        app,
        [
            "--system",
            "debian",
            "--bump",
            "patch",
            "--directory",
            debian_project_directory,
            "--changelog",
            CHANGELOG_ENTRY,
            "--name",
            NAME,
            "--email",
            EMAIL,
        ],
    )

    assert result.exit_code == 0, result.output

    find_changelog_entry()
