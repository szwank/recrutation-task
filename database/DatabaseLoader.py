from data.LocationData import LocationData
from data.PersonData import PersonData
from database.Database import Database
from database.tables.Name import Name
from database.tables.Person import Person
from database.tables.DayOfBirth import DayOfBirth
from database.tables.Login import Login
from database.tables.Registered import Registered
from database.tables.ID import ID
from database.tables.Location import Location
from database.tables.Coordinates import Coordinates
from database.tables.Street import Street
from database.tables.TimeZone import TimeZone


class DatabaseLoader:
    """Class for loading data to database"""
    def __init__(self, database: Database):
        self.__database = database

    def load_person_data(self, person_data: PersonData):
        session = self.__get_session()

        self.load_location_data(person_data.location)
        session.add(ID.from_data(person_data.id))
        session.add(Registered.from_data(person_data.registered))
        session.add(Login.from_data(person_data.login))
        session.add(DayOfBirth.from_data(person_data.day_of_birth))
        session.add(Name.from_data(person_data.name))
        session.add(Person.from_data(person_data))

        session.commit()

    def __get_session(self):
        return self.__database.get_session()

    def load_location_data(self, location_data: LocationData) -> None:
        session = self.__get_session()

        session.add(Street.from_data(location_data.street))
        session.add(TimeZone.from_data(location_data.timezone))
        session.add(Coordinates.from_data(location_data.coordinates))
        session.add(Location.from_data(location_data))

        session.commit()