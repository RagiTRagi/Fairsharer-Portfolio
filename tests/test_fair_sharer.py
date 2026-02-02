"""Tests for the fairsharer.my_module module.
"""
import pytest

from fairsharer.fair_sharer import fair_sharer


def test_fair_sharer():
    assert fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0]


def test_fair_sharer_multiple_iterations():
    assert fair_sharer([0, 1000, 800, 0], 2) == [100, 890, 720, 90]

def test_fair_sharer_with_error():
    with pytest.raises(ValueError):
        fair_sharer([], 1)

@pytest.fixture
def some_values():
    return [0, 1000, 800, 0]


def test_fair_sharer_with_fixture(some_values):
    assert fair_sharer(some_values, 1) == [100, 800, 900, 0]