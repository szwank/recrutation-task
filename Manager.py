import json
import argparse
import datetime

from DateManipulator import DateManipulator
from PrettyTable import PrettyTable
from data.DataDeserializer import DataDeserializer
from database.DataFetcher import DataFetcher
from database.Database import Database
from database.DatabaseLoader import DatabaseLoader


class Manager:
    """Class handling actions that should be done based on passed arguments to script."""
    def __init__(self, options: argparse.Namespace, database: Database):
        self.options = options
        self.__database = database

    def run(self):
        """Invokes the appropriate action based on passed arguments"""
        if self.options.data_path:
            self.__load_data()

        elif self.options.get_gender_percentage:
            self.__show_gender_percentage()

        elif self.options.get_age_gender:
            self.__show_average_age(self.options.get_age_gender)

        elif self.options.get_cities_popularity:
            self.__show_most_popular_cities(self.options.get_cities_popularity)

        elif self.options.get_password_popularity:
            self.__show_most_popular_passwords(self.options.get_password_popularity)

        elif self.options.get_strongest_password:
            self.__show_strongest_password()

        elif self.options.get_born_between:
            self.__show_persons_born_between(*self.options.get_born_between)

        else:
            print("Unknown argument or no argument passed.")


    def __load_data(self):
        """Loads data from file to database. Path to file is passed by options field."""
        database_loader = DatabaseLoader(self.__database)

        data = self.__load_results()

        data_deserializer = DataDeserializer()
        deserialized_data = data_deserializer.deserialize_many(data)

        database_loader.load_many_persons_data(deserialized_data)

    def __load_results(self):
        """Loads data from file. Path to file is passed by options field."""
        data_path = self.options.data_path
        with open(data_path, encoding="utf8") as file:
            data = json.loads(file.read())

        return data['results']

    def __show_gender_percentage(self):
        """Fetch and display data about gender and prints it."""
        data_fetcher = DataFetcher(self.__database)
        information, columns_names = data_fetcher.get_gender_percentage()

        pretty_table = PrettyTable(columns_names)
        pretty_table.show(information)

    def __show_average_age(self, gender):
        """Fetch and display data about age and prints it"""
        data_fetcher = DataFetcher(self.__database)
        information, columns_names = data_fetcher.get_average_age(gender)

        pretty_table = PrettyTable(columns_names)
        pretty_table.show(information)

    def __show_most_popular_cities(self, how_much):
        """Fetch and display data about n most popular cities and prints it"""
        data_fetcher = DataFetcher(self.__database)
        information, columns_names = data_fetcher.get_most_popular_cities(how_much)

        pretty_table = PrettyTable(columns_names)
        pretty_table.show(information)

    def __show_most_popular_passwords(self, how_much):
        """Fetch and display data about n most popular passwords and prints it"""
        data_fetcher = DataFetcher(self.__database)
        information, columns_names = data_fetcher.get_most_popular_passwords(how_much)

        pretty_table = PrettyTable(columns_names)
        pretty_table.show(information)

    def __show_strongest_password(self):
        """Fetch and display data about n most popular passwords and prints it"""
        data_fetcher = DataFetcher(self.__database)
        information, columns_names = data_fetcher.get_strongest_password()

        pretty_table = PrettyTable(columns_names)
        pretty_table.show(information)

    def __show_persons_born_between(self, min_date: str, max_date: str):
        """Fetch and display persons born between passed dates."""
        min_date = self.__str_to_date(min_date)
        max_date = self.__str_to_date(max_date)

        data_fetcher = DataFetcher(self.__database)
        information, columns_names = data_fetcher.get_persons_born_between(min_date, max_date)

        pretty_table = PrettyTable(columns_names)
        pretty_table.show(information)

    def __str_to_date(self, date: str):
        return datetime.datetime.strptime(date, '%Y-%m-%d')