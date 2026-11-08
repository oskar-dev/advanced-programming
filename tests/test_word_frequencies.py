import pytest

import zad


def test_word_frequenties():
    assert zad.word_frequencies("To be or not to be") == {
        "to": 2,
        "be": 2,
        "or": 1,
        "not": 1,
    }
    assert zad.word_frequencies("Hello, hello!") == {"hello": 2}
    assert zad.word_frequencies("") == {}
    assert zad.word_frequencies("Python Python python") == {"python": 3}
    assert zad.word_frequencies("Ala ma kota, a kot, ma Ale.") == {
        "ala": 1,
        "ma": 2,
        "kota": 1,
        "a": 1,
        "kot": 1,
        "ale": 1,
    }
