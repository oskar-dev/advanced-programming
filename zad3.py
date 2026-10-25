class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self._area = area
        self._rooms = rooms
        self._price = price
        self._address = address

    def __str__(self) -> str:
        return f"{self._area}, {self._rooms}, {self._price}, {self._address}"


class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self._plot = plot

    def __str__(self) -> str:
        return super().__str__() + f", {self._plot}"


class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self._floor = floor

    def __str__(self) -> str:
        return super().__str__() + f", {self._floor}"


house0 = House(323.03, 8, 12345667, "Wsoka 5", 1234)
flat0 = Flat(30.2, 1, 123000, "Niska 2", 3)

print("House", house0)
print("Flat", flat0)
