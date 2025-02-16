"""Main test file."""

from {{cookiecutter.project_slug}}.foo import foo


def test_foo() -> None:
    """Main Test."""
    assert foo("foo") == "foo"
