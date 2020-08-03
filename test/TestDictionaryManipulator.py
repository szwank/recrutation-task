import pytest

from DictionaryManipulator import DictionaryManipulator


class TestDictionaryManipulator:

    def test_get_element(self):
        dict_manipulator = DictionaryManipulator()
        dictionary = {'file1': 'picture.png',
                      'folder1': {'folder2': {'file2': 'picture2.jpg', 'file3': 'picture3.png'},
                                  'file4': 'install.exe'}}
        path = 'folder1/:file4'
        expected_result = 'install.exe'

        result = dict_manipulator.get_from_dictionary(dictionary, path)

        assert result == expected_result

    def test_get_element_error_rise(self):
        dict_manipulator = DictionaryManipulator()
        dictionary = {'file1': 'picture.png',
                      'folder1': {'folder2': {'file2': 'picture2.jpg', 'file3': 'picture3.png'},
                                  'file4': 'install.exe'}}
        path = ''
        with pytest.raises(ValueError):
            result = dict_manipulator.get_from_dictionary(dictionary, path)

    def test_get_element_return_none_when_element_dont_exists(self):
        dict_manipulator = DictionaryManipulator()
        dictionary = {'file1': 'picture.png',
                      'folder1': {'folder2': {'file2': 'picture2.jpg', 'file3': 'picture3.png'},
                                  'file4': 'install.exe'}}
        path = 'file10'
        expected_result = None

        result = dict_manipulator.get_from_dictionary(dictionary, path)

        assert result == expected_result


    def test_get_element_work_with_no_nesting(self):
        dict_manipulator = DictionaryManipulator()
        dictionary = {'file1': 'picture.png',
                      'folder1': {'folder2': {'file2': 'picture2.jpg', 'file3': 'picture3.png'},
                                  'file4': 'install.exe'}}
        path = 'file1'
        expected_result = 'picture.png'

        result = dict_manipulator.get_from_dictionary(dictionary, path)

        assert result == expected_result

