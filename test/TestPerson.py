from unittest.mock import Mock

import pytest

from data.PersonData import PersonData


class TestPerson:
    person_args = {'gender':'female',
            'name': Mock(),
            'location': Mock(),
            'email': 'louane.vidal@example.com',
            'login': Mock(),
            'dob': Mock(),
            'registered': Mock(),
            'phone': '02-62-35-18-98',
            'cell': '06-07-80-83-11',
            'id': Mock(),
            'nat': 'FR'}

    numbers = [('123 135 123', '123135123'),
               ('(123) 123 345', '123123345'),
               ('(12)-345-123', '12345123'),
               ('123-123 534', '123123534')]

    @pytest.mark.parametrize('number,expected', numbers)
    def test_clean_number(self, number, expected):
        person_args = self.person_args.copy()
        person_args['phone'] = number

        person = PersonData(**person_args)

        assert person.clean_number == expected

