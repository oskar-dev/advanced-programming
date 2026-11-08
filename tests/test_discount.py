import pytest

import zad


def test_discount():
    assert zad.calulate_discount(100, 0.2) == 80.0
    assert zad.calulate_discount(50, 0) == 50
    assert zad.calulate_discount(200, 1) == 0

    with pytest.raises(ValueError):
        zad.calulate_discount(100, -0.1)
        zad.calulate_discount(100, 1.5)
