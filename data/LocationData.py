from .CoordinatesData import CoordinatesData
from .StreetData import StreetData
from .TimeZoneData import TimeZoneData


class LocationData:
    def __init__(self, street: StreetData, city: str, state: str, country: str, postcode: int, coordinates: CoordinatesData,
                 timezone: TimeZoneData):
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.postcode = postcode
        self.coordinates = coordinates
        self.timezone = timezone
        