def is_even(num: int) -> bool:
    return (num & 1) == 0

output = is_even(2)

if output:
    print("Liczba Parzysta")
else:
    print("Liczba Nieparzysta")