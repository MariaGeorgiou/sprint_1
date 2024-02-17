import pytest
import bloomdata.bloomdata as bd

def test_incrememt_int():
    assert bd.increment(3) == 4
    assert bd.increment(-2) == -1

def test_incrememt_float():
    assert bd.increment(1.5) == 2.5


def test_increment_int_return_type():
    assert isinstance (bd.increment(3), int)

