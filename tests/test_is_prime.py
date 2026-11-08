import pytest

import zad


def test_is_prime():
    assert zad.is_prime(2) == True
    assert zad.is_prime(3) == True
    assert zad.is_prime(4) == False
    assert zad.is_prime(0) == False
    assert zad.is_prime(1) == False
    assert zad.is_prime(5) == True
    assert zad.is_prime(97) == True
