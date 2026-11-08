import pytest

import zad


def test_fibonacci():
    assert zad.fibonacci(0) == 0
    assert zad.fibonacci(1) == 1
    assert zad.fibonacci(5) == 5
    assert zad.fibonacci(10) == 55

    with pytest.raises(ValueError):
        assert zad.fibonacci(-1) == ValueError
