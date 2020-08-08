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

    def load_person_data(self, person_data: PersonData) -> Person:
        session = self.__get_session()

        person = Person.from_data(person_data)

        person.id_relationship = [ID.from_data(person_data.id)]
        person.registered = [Registered.from_data(person_data.registered)]
        person.login = [Login.from_data(person_data.login)]
        person.day_of_birth = [DayOfBirth.from_data(person_data.day_of_birth)]
        person.name = [Name.from_data(person_data.name)]
        person.location = [self.load_location_data(person_data.location)]

        session.add(person)
        session.commit()
        session.close()
        return person

    def __get_session(self):
        return self.__database.get_session()

    def load_location_data(self, location_data: LocationData) -> Location:
        session = self.__get_session()

        location = Location.from_data(location_data)
        location.timezone = [TimeZone.from_data(location_data.timezone)]
        location.coordinates = [Coordinates.from_data(location_data.coordinates)]
        location.street = [Street.from_data(location_data.street)]

        session.add(location)
        session.commit()
        session.close()
        return location