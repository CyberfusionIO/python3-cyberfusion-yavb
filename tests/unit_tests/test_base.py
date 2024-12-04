from typing import Generator

from pytest_mock import MockerFixture

from cyberfusion.YAVB.systems import PyProject
from typer.testing import CliRunner
from cyberfusion.YAVB import app

runner = CliRunner()


def test_directories_glob(
    pyproject_project_directory: Generator[str, None, None], mocker: MockerFixture
) -> None:
    spy_init = mocker.spy(PyProject, "__init__")

    result = runner.invoke(
        app,
        [
            "--system",
            "pyproject",
            "--bump",
            "patch",
            "--directory",
            pyproject_project_directory[:-1] + "*",
        ],
    )

    assert result.exit_code == 0, result.output

    spy_init.assert_called_with(mocker.ANY, pyproject_project_directory)
