from typing_extensions import disjoint_base


def is_palidrome(text: str) -> bool:
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Value cannot be negative")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b


def count_vowels(text: str) -> int:
    text = text.lower()
    vowels = "aeiouóyąę"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count


def calulate_discount(price: float, discount: float) -> float:
    if discount > 1 or discount < 0:
        raise ValueError("Discount is out of range <0;1>")

    return price - (price * discount)


def flatten_list(nested_list: list) -> list:
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat


def word_frequencies(text: str) -> dict:
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~„”—"

    text = text.lower()

    for char in punctuation:
        text = text.replace(char, "")

    words = text.split()

    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1

    return frequencies


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True
