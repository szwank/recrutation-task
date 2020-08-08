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
                                 dest="get_age",
                                 action='store_true',
                                 help="Returns average age of genders and overall average age.")

        self.arguments = self.parser.parse_args()

    def get_arguments(self) -> argparse.Namespace:
        """Returns parsed arguments"""
        return self.arguments
