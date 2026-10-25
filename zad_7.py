import requests


class Brewery:
    _id: str
    _name: str
    _type: str
    _address1: str
    _address2: str
    _address3: str
    _city: str
    _state_province: str
    _postal_code: str
    _country: str
    _longitude: float
    _latitude: float
    _phone: str
    _website: str
    _state: str
    _street: str

    def __init__(self, brewery_json):
        self._id = brewery_json.get("id")
        self._name = brewery_json.get("name")
        self._type = brewery_json.get("brewery_type")
        self._address1 = brewery_json.get("address_1")
        self._address2 = brewery_json.get("address_2")
        self._address3 = brewery_json.get("address_3")
        self._city = brewery_json.get("city")
        self._state_province = brewery_json.get("state_province")
        self._postal_code = brewery_json.get("postal_code")
        self._country = brewery_json.get("country")
        self._longitude = brewery_json.get("longitude")
        self._latitude = brewery_json.get("latitude")
        self._phone = brewery_json.get("phone")
        self._website = brewery_json.get("website")
        self._state = brewery_json.get("state")
        self._street = brewery_json.get("street")

    def __str__(self):
        return (
            f"name={self._name}, type={self._type},"
            + f" address={self._address1}, website={self._website},"
            + " phone={self._phone}"
        )


x = requests.get("https://api.openbrewerydb.org/v1/breweries?per_page=20")

breweries = []

for json in x.json():
    breweries.append(Brewery(json))

for brewery in breweries:
    print(brewery)
