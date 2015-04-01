import pytest

from proppy.exceptions import (
  InvalidCommand,
  InvalidConfiguration
)
from proppy.main import main


def test_calling_with_other_than_toml():
  with pytest.raises(InvalidCommand):
    main("hello.json")


def test_config_without_theme():
  with pytest.raises(InvalidConfiguration):
    # TODO: create tmp file instead
    main("proppy/tests/fixtures/no_theme.toml")


def test_config_without_customer():
  with pytest.raises(InvalidConfiguration):
    # TODO: create tmp file instead
    main("proppy/tests/fixtures/no_customer.toml")


def test_config_without_project():
  with pytest.raises(InvalidConfiguration):
    # TODO: create tmp file instead
    main("proppy/tests/fixtures/no_project.toml")
