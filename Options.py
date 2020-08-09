import argparse


class Options:
    """Parse arguments and store configuration of ArgumentParser class."""
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Program for displaying various informations about loaded"
                                                          "data.")

        self.parser.add_argument("--load_data", "-l",
                                 dest="data_path",
                                 help="Create database if needed and load data from file in passed path.",
                                 nargs='?',
                                 const='inputs/persons.json',
                                 metavar='PATH_TO_DATA')

        self.parser.add_argument("--gender_percentage", "-gp",
                                 dest="get_gender_percentage",
                                 action='store_true',
                                 help="Displays gender percentage.")

        self.parser.add_argument("--average_age", "-a",
                                 dest="get_age_gender",
                                 choices=['male', 'female', 'both'],
                                 help="Displays average age of chosen gender. Available choices are: male, female, both.")

        self.parser.add_argument("--cities_popularity", "-c",
                                 dest="get_cities_popularity",
                                 type=int,
                                 help="Displays n most popular cities.",
                                 metavar='N')

        self.parser.add_argument("--password_popularity", "-p",
                                 dest="get_password_popularity",
                                 type=int,
                                 help="Displays n most popular passwords.",
                                 metavar='N')

        self.parser.add_argument("--strongest_password", "-sp",
                                 dest="get_strongest_password",
                                 action='store_true',
                                 help="Displays strongest password in database.")

        self.parser.add_argument("--born_between", "-b",
                                 dest="get_born_between",
                                 nargs=2,
                                 help="Displays persons born between passed dates. First date should be the earlier"
                                      "one. Dates should be in format YYYY-MM-DD",
                                 metavar=('MIN_DATE', 'MAX_DATE'))

        self.arguments = self.parser.parse_args()

    def get_arguments(self) -> argparse.Namespace:
        """Returns parsed arguments"""
        return self.arguments
