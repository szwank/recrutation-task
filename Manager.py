import json
import argparse

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
        elif self.options.get_age:
            self.__show_average_age()
        elif self.options.get_cities_popularity:
            self.__show_most_popular_cities(self.options.get_cities_popularity)
        elif self.options.get_password_popularity:
            self.__show_most_popular_passwords(self.options.get_password_popularity)

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
        """Fetch data about gender and prints it."""
        data_fetcher = DataFetcher(self.__database)
        information, columns_names = data_fetcher.get_gender_percentage()

        pretty_table = PrettyTable(columns_names)
        pretty_table.show(information)

    def __show_average_age(self):
        """Fetch data about age and prints it"""
        data_fetcher = DataFetcher(self.__database)
        information, columns_names = data_fetcher.get_average_age()

        pretty_table = PrettyTable(columns_names)
        pretty_table.show(information)

    def __show_most_popular_cities(self, how_much):
        """Fetch data about n most popular cities and prints it"""
        data_fetcher = DataFetcher(self.__database)
        information, columns_names = data_fetcher.get_most_popular_cities(how_much)

        pretty_table = PrettyTable(columns_names)
        pretty_table.show(information)

    def __show_most_popular_passwords(self, how_much):
        """Fetch data about n most popular cities and prints it"""
        data_fetcher = DataFetcher(self.__database)
        information, columns_names = data_fetcher.get_most_popular_passwords(how_much)

        pretty_table = PrettyTable(columns_names)
        pretty_table.show(information)

