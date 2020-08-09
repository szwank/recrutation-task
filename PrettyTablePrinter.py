import itertools
from typing import List, Iterable


class PrettyTablePrinter:
    """Class for pretty printing tabular data."""
    def __init__(self, columns_names: List[str], margin: int = 3):
        self.__columns_names = columns_names
        self.__columns_names_len = self.__get_columns_name_length()
        self.__margin = margin

    def __get_columns_name_length(self) -> List[int]:
        """Returns lengths of column names lenghts."""
        max_lengths = []

        for value in self.__columns_names:
            value_length = len(str(value))
            max_lengths.append(value_length)

        return max_lengths

    def show(self, data: List[Iterable]) -> None:
        """Displays tabular data."""
        columns_lengths = self.__get_table_columns_lengths(data)
        print_statement = self.__get_print_statement(columns_lengths)

        for row in itertools.chain((self.__columns_names, ), data):
            print(print_statement.format(*row))

    def __get_table_columns_lengths(self, data: List[Iterable]) -> List[int]:
        max_lengths = self.__columns_names_len

        for row in data:
            for i, value in enumerate(row):
                value_length = len(str(value))
                if value_length > max_lengths[i]:
                    max_lengths[i] = value_length

        return max_lengths


    def __get_print_statement(self, columns_lengths: List[int]) -> str:
        """Returns fromating string based on column lengths"""
        statement = []
        for length in columns_lengths:
            statement.append('{:^')
            statement.append(str(length + self.__margin * 2))
            statement.append('}')

        return "".join(statement)





