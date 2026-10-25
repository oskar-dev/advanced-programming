import properties.Property


class Flat(properties.Property.Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self._floor = floor

    def __str__(self) -> str:
        return super().__str__() + f", {self._floor}"
