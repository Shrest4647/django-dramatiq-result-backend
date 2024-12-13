import pytest
from django_dramatiq_result_backend import __version__


def test_version():
    assert __version__ is not None
