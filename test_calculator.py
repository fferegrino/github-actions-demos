import pytest
from calculator import add

def test_add():
    assert 4 == add(1, 2)
