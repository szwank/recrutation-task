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

        with pytest.raises(ValueError):
            result = dict_manipulator.get_from_dictionary(dictionary, path)

    def test_get_element_work_with_ints(self):
        dict_manipulator = DictionaryManipulator()
        dictionary = {'file1': 'picture.png',
                      1: {2: {'file2': 'picture2.jpg', 'file3': 'picture3.png'},
                                  'file4': 'install.exe'}}
        path = '\i1/:\i2/:file2'
        expected_result = 'picture2.jpg'

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

    def test_set_element_work_with_no_nesting(self):
        dict_manipulator = DictionaryManipulator()
        dictionary = {'file1': 'picture.png',
                      'folder1': {'folder2': {'file2': 'picture2.jpg', 'file3': 'picture3.png'},
                                  'file4': 'install.exe'}}
        path = 'file2'
        set_value = 'set'
        expected_result = {'file1': 'picture.png',
                           'file2': 'set',
                           'folder1': {'folder2': {'file2': 'picture2.jpg', 'file3': 'picture3.png'},
                                       'file4': 'install.exe'}}

        dict_manipulator.set_element_in_dictionary(dictionary, path, set_value)

        assert dictionary == expected_result

    def test_set_element_work_with_nested_dictionaries(self):
        dict_manipulator = DictionaryManipulator()
        dictionary = {'file1': 'picture.png',
                      'folder1': {'folder2': {'file2': 'picture2.jpg', 'file3': 'picture3.png'},
                                  'file4': 'install.exe'}}
        path = 'folder1/:file5'
        set_value = 'set'
        expected_result = {'file1': 'picture.png',
                           'folder1': {'folder2': {'file2': 'picture2.jpg', 'file3': 'picture3.png'},
                                       'file5': 'set',
                                       'file4': 'install.exe'}}

        dict_manipulator.set_element_in_dictionary(dictionary, path, set_value)

        assert dictionary == expected_result

    def test_set_element_raise_path_dont_exists(self):
        dict_manipulator = DictionaryManipulator()
        dictionary = {'file1': 'picture.png',
                      'folder1': {'folder2': {'file2': 'picture2.jpg', 'file3': 'picture3.png'},
                                  'file4': 'install.exe'}}
        path = 'folder1/:file5:/asd'

        with pytest.raises(ValueError):
            result = dict_manipulator.get_from_dictionary(dictionary, path)

