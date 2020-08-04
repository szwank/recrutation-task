import re

from .DayOfBirth import DayOfBirth
from .Registered import Registered
from .ID import ID


class Person:
    def __init__(self, gender: str, name: str, location: str, email: str, login: str, dob: DayOfBirth,
                 registered: Registered, phone: str, cell: str, id: ID, nat):
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
    def clean_number(self):
        return self.__remove_special_characters(self.phone)

    @staticmethod
    def __remove_special_characters(string: str) -> str:
        regex = '[^A-Za-z0-9]+'
        return re.sub(regex, '', string)
