from .Coordinates import Coordinates
from .Person import Person
from .DayOfBirth import DayOfBirth
from .ID import ID
from .Location import Location
from .Login import Login
from .Registered import Registered
from .Street import Street
from .TimeZone import TimeZone


class DataDeserializer:

    @staticmethod
    def deserialize(data: dict) -> Person:
        location = DataDeserializer.__get_location(data)

        login = Login(**data['login'])
        day_of_birth = DayOfBirth(**data['dob'])
        registered = Registered(**data['registered'])
        id = ID(**data['id'])

        data_container_args = data.copy()
        data_container_args['login'] = login
        data_container_args['dob'] = day_of_birth
        data_container_args['registered'] = registered
        data_container_args['id'] = id
        data_container_args['location'] = location
        data_container_args.pop('picture', None)

        return Person(**data_container_args)

    @staticmethod
    def __get_location(data):
        street = Street(**data['location']['street'])
        coordinates = Coordinates(**data['location']['coordinates'])
        timezone = TimeZone(**data['location']['timezone'])

        location_args = data['location'].copy()
        location_args['street'] = street
        location_args['coordinates'] = coordinates
        location_args['timezone'] = timezone

        return Location(**location_args)
