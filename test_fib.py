import pytest

from fib import fibonacci


def test_fib_9_is_34():
    assert fibonacci(9) == 34


def test_fib_negative_raise_error():
    with pytest.raises(ValueError):
        fibonacci(-1)
