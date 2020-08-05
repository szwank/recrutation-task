from .Coordinates import Coordinates
from .Street import Street
from .TimeZone import TimeZone


class Location:
    def __init__(self, street: Street, city: str, state: str, country: str, postcode: int, coordinates: Coordinates,
                 timezone: TimeZone):
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.postcode = postcode
        self.coordinates = coordinates
        self.timezone = timezone
        