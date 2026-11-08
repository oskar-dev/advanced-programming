import zad


def test_count_vowels():
    assert zad.count_vowels("Python") == 2
    assert zad.count_vowels("AEIOUY") == 6
    assert zad.count_vowels("bcd") == 0
    assert zad.count_vowels("") == 0
    assert zad.count_vowels("Próba żółwia") == 4
