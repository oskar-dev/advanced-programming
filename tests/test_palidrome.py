import zad


def test_is_palidrome():
    assert zad.is_palidrome("kajak") == True
    assert zad.is_palidrome("Kobyła ma mały bok") == True
    assert zad.is_palidrome("python") == False
    assert zad.is_palidrome("") == True
    assert zad.is_palidrome("A") == True
