from typing import Any, List


class DictionaryManipulator:
    """Class for manipulating nested dictionaries."""
    def __init__(self, separator: str = '/:'):
        self.__separator = separator

    def get_from_dictionary(self, dictionary: dict, path: str) -> Any:
        """Get element from nested dictionary. Path attribute is a regex that indicate target element. path should
        consist of keys in nested dictionaries that we are following separated by separator set in constructor.
        Default separator is '/:'."""
        if not path:
            raise ValueError("Attribute path is empty")

        element = dictionary

        for level in self.__parse_path(path):
            element = element.get(level, ElementDontExist())

            if isinstance(element, ElementDontExist):
                return None

        return element

    def __parse_path(self, path: str) -> List[str]:
        """Return parsed path"""
        return path.split(self.__separator)


class ElementDontExist:
    """Class indicating no element when fetching one by class DictionaryManipulator"""
    pass

