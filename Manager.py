import json
import argparse

from data.DataDeserializer import DataDeserializer
from database.Database import Database
from database.DatabaseLoader import DatabaseLoader


class Manager:
    """Class handling actions that should be done based on passed arguments to script."""
    def __init__(self, options: argparse.Namespace):
        self.options = options

    def run(self):
        """Invokes the appropriate action based on passed arguments"""
        if self.options.data_path:
            self.__load_data()


    def __load_data(self):
        """Loads data from file to database. Path to file is passed by options field."""
        database = Database()
        database_loader = DatabaseLoader(database)

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