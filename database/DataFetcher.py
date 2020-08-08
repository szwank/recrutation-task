from typing import List, Tuple, Any

from sqlalchemy import func, cast, Float
from sqlalchemy.sql.expression import literal
from database.Database import Database
from database.tables.DayOfBirth import DayOfBirth
from database.tables.Person import Person


class DataFetcher:
    """Class for fetching information from database"""
    def __init__(self, database: Database):
        self.__database = database

    def get_gender_percentage(self) -> List[Tuple[Any]]:
        """Returns percentage of gender in Person table."""
        session = self.__get_session()
        subquery = session.query(func.count(1).label('sum_all')).select_from(Person).subquery()

        return session.query(Person.gender,
                             (cast(100 * func.count(1), Float) / subquery.c.sum_all)) \
            .group_by(Person.gender) \
            .all()

    def __get_session(self):
        return self.__database.get_session()

    def get_average_age(self) -> List[Tuple[Any]]:
        """Returns average age of genders and average age of all rows persons. Information are fetched based on tables:
        Person, DateOfBirth"""
        session = self.__get_session()
        avg_age_by_sex = session.query(Person.gender.label('gender'), func.avg(DayOfBirth.age).label('age')) \
            .select_from(Person)\
            .join(DayOfBirth)\
            .group_by(Person.gender)


        avg_age_on_all = session.query(literal('All').label('gender'), func.avg(DayOfBirth.age).label('age')) \
            .select_from(Person) \
            .join(DayOfBirth)

        return avg_age_by_sex.union_all(avg_age_on_all).all()

