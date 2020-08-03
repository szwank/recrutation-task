from typing import Any, List


class DictionaryManipulator:
    """Class for manipulating nested dictionaries.
    args:
        separator: indicates separated keys when given path
        int_symbol: indicates that given key is int key"""
    def __init__(self, separator: str = '/:', int_symbol: str = '\i'):
        self.__separator = separator
        self.__int_symbol = int_symbol

    def get_from_dictionary(self, dictionary: dict, path: str) -> Any:
        """Get element from nested dictionary. Path attribute is a regex that indicate target element. path should
        consist of keys in nested dictionaries that we are following separated by separator set in constructor.
        Default separator is '/:'."""
        if not path:
            raise ValueError("Attribute path is empty.")

        element = dictionary

        for key in self.__parse_path(path):
            element = element.get(key, ElementDontExist())

            if isinstance(element, ElementDontExist):
                raise ValueError(f"There is no key {key} in this path: {path}")

        return element

    def __parse_path(self, path: str) -> List[str]:
        """Return parsed path."""
        parsed_path = path.split(self.__separator)
        parsed_path = self.__parse_ints(parsed_path)
        return parsed_path


    def __parse_ints(self, parsed_path: List[str]):
        """Method converts to int elements that starts with int_symbol."""
        for i, key in enumerate(parsed_path):
            if key.startswith(self.__int_symbol):
                parsed_path[i] = int(key.replace(self.__int_symbol, ''))
        return parsed_path


    def set_element_in_dictionary(self, dictionary: dict, path: str, element: Any) -> Any:
        """Method creates a key in indicated path and seting its values as element."""
        parsed_path = self.__parse_path(path)
        last_key = parsed_path[-1]
        if self.__is_nested(parsed_path):
            internal_dictionary = self.get_from_dictionary(dictionary, self.__cut_last_key(path))

            internal_dictionary[last_key] = element
        else:
            dictionary[last_key] = element

    def __is_nested(self, parsed_path):
        return len(parsed_path) > 1

    def __create_path(self, elements_list: List[str]) -> str:
        """Create path from list of strings"""
        return self.__separator.join(elements_list)

    def __cut_last_key(self, path: str) -> str:
        """"""
        parsed_path = self.__parse_path(path)
        return self.__create_path(parsed_path[:-1])

    def remove_key(self, dictionary: dict, path: str) -> None:
        parsed_path = self.__parse_path(path)
        last_key = parsed_path[-1]
        if self.__is_nested(parsed_path):
            internal_dictionary = self.get_from_dictionary(dictionary, self.__cut_last_key(path))

            internal_dictionary.pop(last_key, None)
        else:
            dictionary.pop(last_key, None)

class ElementDontExist:
    """Class indicating no element when fetching one by class DictionaryManipulator"""
    pass

