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
            self.__get_gender_percentage()

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

    def __get_gender_percentage(self):
        data_fetcher = DataFetcher(self.__database)
        information = data_fetcher.get_gender_percentage()

        pretty_table = PrettyTable(['Gender', 'Percentage [%]'])
        pretty_table.show(information)