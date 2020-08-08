from typing import List, Tuple, Any

from sqlalchemy import func, cast, Float
from sqlalchemy.sql.expression import literal
from sqlalchemy.orm import Query
from database.Database import Database
from database.tables.DayOfBirth import DayOfBirth
from database.tables.Person import Person


class DataFetcher:
    """Class for fetching information from database"""
    def __init__(self, database: Database):
        self.__database = database

    def get_gender_percentage(self) -> Tuple[List[Tuple[Any]], List[str]]:
        """Returns percentage of gender in Person table."""
        session = self.__get_session()
        subquery = session.query(func.count(1).label('sum_all')).select_from(Person).subquery()

        gender_percentage = session.query(Person.gender,
                                          (cast(100 * func.count(1), Float) / subquery.c.sum_all)) \
            .group_by(Person.gender) \
            .all()
        return self.__get_query_result(gender_percentage)

    def __get_session(self):
        return self.__database.get_session()

    def __get_columns_name(self, query: Query) -> List[str]:
        """Returns query columns names."""
        columns_name = []
        for column_information in query.column_descriptions:
            columns_name.append(column_information['name'])

        return columns_name

    def __get_query_result(self, query: Query) -> Tuple[List[Tuple[Any]], List[str]]:
        columns_names = self.__get_columns_name(query)
        result = query.all()
        return result, columns_names

    def get_average_age(self) -> Tuple[List[Tuple[Any]], List[str]]:
        """Returns average age of genders and average age of all rows persons. Information are fetched based on tables:
        Person, DateOfBirth"""
        session = self.__get_session()
        avg_age_by_sex = session.query(Person.gender.label('gender'), func.avg(DayOfBirth.age).label('age')) \
            .select_from(Person)\
            .join(DayOfBirth)\
            .group_by(Person.gender)


        avg_age_on_all = session.query(literal('both').label('gender'), func.avg(DayOfBirth.age).label('age')) \
            .select_from(Person) \
            .join(DayOfBirth)

        avg_age = avg_age_by_sex.union_all(avg_age_on_all).subquery()

        avg_age_round = session.query(avg_age.c.gender.label('Gender'), func.round(avg_age.c.age, 2).label('Average_age')) \
            .select_from(avg_age)

        return self.__get_query_result(avg_age_round)
