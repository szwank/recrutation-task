import re
from typing import List

from randomuser import RandomUser

from .DayOfBirthData import DayOfBirthData
from .LocationData import LocationData
from .LoginData import LoginData
from .NameData import NameData
from .RegisteredData import RegisteredData
from .IDData import IDData


class PersonData:
    def __init__(self, gender: str, name: NameData, location: LocationData, email: str, login: LoginData, dob: DayOfBirthData,
                 registered: RegisteredData, phone: str, cell: str, id: IDData, nat: str):
        self.gender = gender
        self.name = name
        self.location = location
        self.email = email
        self.login = login
        self.day_of_birth = dob
        self.registered = registered
        self.phone = phone
        self.cell = cell
        self.id = id
        self.nat = nat

    @property
    def clean_phone_number(self):
        return self.__remove_special_characters(self.phone)

    @staticmethod
    def __remove_special_characters(string: str) -> str:
        regex = '[^A-Za-z0-9]+'
        return re.sub(regex, '', string)


def create_random_person_data(how_many: int) -> List[PersonData]:
    # import is in function because circular import
    from .DataDeserializer import DataDeserializer
    users = RandomUser.generate_users(how_many)

    users_data = [user._data for user in users]

    return DataDeserializer.deserialize_many(users_data)
