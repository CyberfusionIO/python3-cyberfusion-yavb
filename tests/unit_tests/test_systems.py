from typing import Generator

import pytest
from cyberfusion.YAVB.exceptions import EmailNameMissingError
from cyberfusion.YAVB.systems import Debian


def test_debian_missing_email_address(
    bogus_directory: Generator[str, None, None],
) -> None:
    with pytest.raises(EmailNameMissingError):
        Debian(directory=bogus_directory).update(
            version="1.0.0",
            changelog_entry="example",
            email_address=None,
            full_name="John Doe",
        )


def test_debian_missing_full_name(
    bogus_directory: Generator[str, None, None],
) -> None:
    with pytest.raises(EmailNameMissingError):
        Debian(directory=bogus_directory).update(
            version="1.0.0",
            changelog_entry="example",
            email_address="john@example.com",
            full_name=None,
        )
