import argparse


class Options:
    """Parse arguments and store configuration of ArgumentParser class."""
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Example script.")

        self.parser.add_argument("--load_data", "-l",
                                 dest="data_path",
                                 help="Create database if needed and load data from passed path.")

        self.parser.add_argument("--gender_percentage", "-gp",
                                 dest="get_gender_percentage",
                                 action='store_true',
                                 help="Returns gender percentage loaded to database.")

        self.parser.add_argument("--average_age", "-a",
                                 dest="get_age_gender",
                                 choices=['male', 'female', 'both'],
                                 nargs='?',
                                 help="Returns average age of genders and overall average age.")

        self.parser.add_argument("--cities_popularity", "-c",
                                 dest="get_cities_popularity",
                                 nargs='?',
                                 type=int,
                                 help="Returns n most popular cities.")

        self.parser.add_argument("--password_popularity", "-p",
                                 dest="get_password_popularity",
                                 nargs='?',
                                 type=int,
                                 help="Returns n most popular passwords.")

        self.parser.add_argument("--strongest_password", "-sp",
                                 dest="get_strongest_password",
                                 action='store_true',
                                 help="Returns strongest password in database.")

        self.parser.add_argument("--born_between", "-b",
                                 dest="get_born_between",
                                 nargs=2,
                                 help="Returns persons born between passed dates. First date should be the earlier one.")

        self.arguments = self.parser.parse_args()

    def get_arguments(self) -> argparse.Namespace:
        """Returns parsed arguments"""
        return self.arguments
