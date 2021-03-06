from typing import List

from .CoordinatesData import CoordinatesData
from .NameData import NameData
from .PersonData import PersonData
from .DayOfBirthData import DayOfBirthData
from .IDData import IDData
from .LocationData import LocationData
from .LoginData import LoginData
from .RegisteredData import RegisteredData
from .StreetData import StreetData
from .TimeZoneData import TimeZoneData


class DataDeserializer:
    """Class deserializing data into objects"""
    @staticmethod
    def deserialize_many(data: List[dict]):
        deserialized_data = []
        for dictionary in data:
            deserialized_data.append(DataDeserializer.deserialize(dictionary))

        return deserialized_data

    @staticmethod
    def deserialize(data: dict) -> PersonData:
        location = DataDeserializer.__get_location(data)

        login = LoginData(**data['login'])
        day_of_birth = DayOfBirthData(**data['dob'])
        name = NameData(**data['name'])
        registered = RegisteredData(**data['registered'])
        id = IDData(**data['id'])

        data_container_args = data.copy()
        data_container_args['login'] = login
        data_container_args['dob'] = day_of_birth
        data_container_args['registered'] = registered
        data_container_args['id'] = id
        data_container_args['location'] = location
        data_container_args['name'] = name
        data_container_args.pop('picture', None)

        return PersonData(**data_container_args)

    @staticmethod
    def __get_location(data):
        street = StreetData(**data['location']['street'])
        coordinates = CoordinatesData(**data['location']['coordinates'])
        timezone = TimeZoneData(**data['location']['timezone'])

        location_args = data['location'].copy()
        location_args['street'] = street
        location_args['coordinates'] = coordinates
        location_args['timezone'] = timezone

        return LocationData(**location_args)
