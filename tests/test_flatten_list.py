import pytest

import zad


def test_flatten_list():
    assert zad.flatten_list([1, 2, 3]) == [1, 2, 3]
    assert zad.flatten_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]
    assert zad.flatten_list([]) == []
    assert zad.flatten_list([[[1]]]) == [1]
    assert zad.flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]
