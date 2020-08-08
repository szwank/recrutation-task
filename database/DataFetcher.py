from typing import List, Tuple, Any

from sqlalchemy import func, cast, Float, desc
from sqlalchemy.sql.expression import literal
from sqlalchemy.orm import Query
from database.Database import Database
from database.tables.DayOfBirth import DayOfBirth
from database.tables.Location import Location
from database.tables.Login import Login
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
            .group_by(Person.gender)

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

    def get_most_popular_cities(self, how_much):
        """Returns n most popular cities in database. Information is fetched from table Location."""
        session = self.__get_session()
        popular_cities = session.query(Location.city.label('City'), func.count(1).label('Number of occurrences')) \
            .select_from(Location) \
            .group_by(Location.city) \
            .order_by(desc(func.count(1))) \
            .limit(how_much)
        return self.__get_query_result(popular_cities)

    def get_most_popular_passwords(self, how_much):
        """Returns n most popular passwords in database. Information is fetched from table Login."""
        session = self.__get_session()
        popular_passwords = session.query(Login.password.label('Password'), func.count(1).label('Number of occurrences')) \
            .select_from(Login) \
            .group_by(Login.password) \
            .order_by(desc(func.count(1))) \
            .limit(how_much)
        return self.__get_query_result(popular_passwords)