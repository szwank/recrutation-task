from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .tables.base import Base
# imports needed for Database class to initialize tables correctly
from database.tables.DayOfBirth import DayOfBirth
from database.tables.Person import Person
from database.tables.Login import Login
from database.tables.Registered import Registered
from database.tables.ID import ID
from database.tables.Location import Location
from database.tables.Coordinates import Coordinates
from database.tables.TimeZone import TimeZone


class Database:
    """Class for database communication"""
    def __init__(self, filepath: str = 'database.dbo', *args, **kwargs):
        self.__engine = create_engine(f'sqlite:///{filepath}', *args, **kwargs)
        self.__Session = sessionmaker(bind=self.__engine)

    def get_session(self):
        """Returns connection session"""
        return self.__Session()

    def create_missing_tables(self):
        """Create all tables base on classes that inherent from Base class instance."""
        Base.metadata.create_all(self.__engine)

