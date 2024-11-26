import semver

from cyberfusion.YAVB import (
    increment_semver_version,
    SemanticVersioningVersion,
    convert_string_to_versioninfo,
)


def test_increment_semver_version_patch() -> None:
    current_version = semver.VersionInfo.parse(
        "1.0.0",
    )

    assert increment_semver_version(
        current_version, SemanticVersioningVersion.PATCH
    ) == semver.VersionInfo.parse("1.0.1")


def test_increment_semver_version_minor() -> None:
    current_version = semver.VersionInfo.parse(
        "1.0.0",
    )

    assert increment_semver_version(
        current_version, SemanticVersioningVersion.MINOR
    ) == semver.VersionInfo.parse("1.1.0")


def test_increment_semver_version_major() -> None:
    current_version = semver.VersionInfo.parse(
        "1.0.0",
    )

    assert increment_semver_version(
        current_version, SemanticVersioningVersion.MAJOR
    ) == semver.VersionInfo.parse("2.0.0")


def test_convert_string_to_versioninfo_missing_none() -> None:
    assert convert_string_to_versioninfo("1.0.0") == semver.VersionInfo.parse(
        "1.0.0",
    )


def test_convert_string_to_versioninfo_missing_patch() -> None:
    assert convert_string_to_versioninfo("1.0") == semver.VersionInfo.parse(
        "1.0.0",
    )


def test_convert_string_to_versioninfo_missing_patch_minor() -> None:
    assert convert_string_to_versioninfo("1") == semver.VersionInfo.parse(
        "1.0.0",
    )


def test_convert_string_to_versioninfo_excess() -> None:
    assert convert_string_to_versioninfo("1.2.3.4") == semver.VersionInfo.parse(
        "1.2.3",
    )
