from datetime import datetime

import pytest

from database.Database import Database
from database.tables.DayOfBirth import DayOfBirth
from database.tables.Location import Location
from database.tables.Login import Login
from database.tables.Person import Person
from database.DataFetcher import DataFetcher


class TestDataFetcher:

    def test_get_gender_percentage_mixed_gender(self):
        database = Database(':memory:')
        session = database.get_session()

        person_1 = Person(gender='female')
        person_2 = Person(gender='female')
        person_3 = Person(gender='female')
        person_4 = Person(gender='male')
        session.bulk_save_objects([person_1, person_2, person_3, person_4])
        session.commit()

        data_fetcher = DataFetcher(database)

        values, columns = data_fetcher.get_gender_percentage()
        expected = [('male', 25), ('female', 75)]

        assert set(values) == set(expected)

    def test_get_gender_percentage_single_gender(self):
        database = Database(':memory:')
        session = database.get_session()

        person_1 = Person(gender='female')
        person_2 = Person(gender='female')
        person_3 = Person(gender='female')
        session.bulk_save_objects([person_1, person_2, person_3])
        session.commit()

        data_fetcher = DataFetcher(database)

        values, columns = data_fetcher.get_gender_percentage()
        expected = [('female', 100)]

        assert set(values) == set(expected)

    def test_get_average_age_mixed_gender(self):
        database = Database(':memory:')
        session = database.get_session()

        person_1 = Person(gender='female')
        dbo_1 = DayOfBirth(age=10)
        person_1.day_of_birth = [dbo_1]
        person_2 = Person(gender='male')
        dbo_2 = DayOfBirth(age=20)
        person_2.day_of_birth = [dbo_2]

        session.add(person_1)
        session.add(person_2)
        session.commit()

        data_fetcher = DataFetcher(database)

        values, columns = data_fetcher.get_average_age()
        expected = [('female', 10), ('male', 20), ('both', 15)]

        assert set(values) == set(expected)

    def test_get_average_age_single_gender(self):
        database = Database(':memory:')
        session = database.get_session()

        person_1 = Person(gender='female')
        dbo_1 = DayOfBirth(age=10)
        person_1.day_of_birth = [dbo_1]
        person_2 = Person(gender='female')
        dbo_2 = DayOfBirth(age=20)
        person_2.day_of_birth = [dbo_2]

        session.add(person_1)
        session.add(person_2)
        session.commit()

        data_fetcher = DataFetcher(database)

        values, columns = data_fetcher.get_average_age()
        expected = [('female', 15), ('both', 15)]

        assert set(values) == set(expected)

    def test_get_most_popular_cities_fetch_one_city_when_there_is_many(self):
        database = Database(':memory:')
        session = database.get_session()

        locations = []
        locations.append(Location(city='Sejny'))
        locations.append(Location(city='Sejny'))
        locations.append(Location(city='Sejny'))
        locations.append(Location(city='Gdańsk'))
        locations.append(Location(city='Gdańsk'))
        locations.append(Location(city='Gdańsk'))
        locations.append(Location(city='Gdańsk'))
        locations.append(Location(city='Augustów'))

        session.add_all(locations)
        session.commit()

        data_fetcher = DataFetcher(database)

        values, columns = data_fetcher.get_most_popular_cities(1)
        expected = [('Gdańsk', 4)]

        assert set(values) == set(expected)


    def test_get_most_popular_cities_fetch_many_city_when_there_is_many(self):
        database = Database(':memory:')
        session = database.get_session()

        locations = []
        locations.append(Location(city='Sejny'))
        locations.append(Location(city='Sejny'))
        locations.append(Location(city='Sejny'))
        locations.append(Location(city='Gdańsk'))
        locations.append(Location(city='Gdańsk'))
        locations.append(Location(city='Gdańsk'))
        locations.append(Location(city='Gdańsk'))
        locations.append(Location(city='Augustów'))

        session.add_all(locations)
        session.commit()

        data_fetcher = DataFetcher(database)

        values, columns = data_fetcher.get_most_popular_cities(2)
        expected = [('Gdańsk', 4), ('Sejny', 3)]

        assert set(values) == set(expected)

    def test_get_most_popular_cities_fetch_many_city_when_there_is_one(self):
        database = Database(':memory:')
        session = database.get_session()

        locations = []
        locations.append(Location(city='Sejny'))
        locations.append(Location(city='Sejny'))
        locations.append(Location(city='Sejny'))

        session.add_all(locations)
        session.commit()

        data_fetcher = DataFetcher(database)

        values, columns = data_fetcher.get_most_popular_cities(4)
        expected = [('Sejny', 3)]

        assert set(values) == set(expected)

    def test_get_most_popular_passwords_fetch_one(self):
        database = Database(':memory:')
        session = database.get_session()

        logins = []
        logins.append(Login(password='tricky'))
        logins.append(Login(password='tricky'))
        logins.append(Login(password='thrasher'))

        session.add_all(logins)
        session.commit()

        data_fetcher = DataFetcher(database)

        values, columns = data_fetcher.get_most_popular_passwords(1)
        expected = [('tricky', 2)]

        assert set(values) == set(expected)

    def test_get_most_popular_passwords_when_fetching_more_than_is_in_database(self):
        database = Database(':memory:')
        session = database.get_session()

        logins = []
        logins.append(Login(password='tricky'))
        logins.append(Login(password='tricky'))
        logins.append(Login(password='thrasher'))

        session.add_all(logins)
        session.commit()

        data_fetcher = DataFetcher(database)

        values, columns = data_fetcher.get_most_popular_passwords(6)
        expected = [('tricky', 2), ('thrasher', 1)]

        assert set(values) == set(expected)

    passwords_strength = [
        (['Aricky', 'a'], 'Aricky'),
        (['Aricky', 'aaGs4'], 'aaGs4'),
        (['supertajne', 'aaGs4'], 'supertajne'),
        (['supe%', 'aaGs'], 'supe%'),
        (['supert@jne', 'acQs4+'], 'supert@jne'),
        (['supert@jne', 'acQs4%', 'suPadrt@jne7'], 'suPadrt@jne7'),
        (['asd', 'asd', 'asd', 'yes5'], 'yes5'),
        (['aSaD', 'asd', 'Des5'], 'Des5'),
    ]

    @pytest.mark.parametrize('passwords,expected', passwords_strength)
    def test_get_strongest_password(self, passwords, expected):
        database = Database(':memory:')
        session = database.get_session()

        logins = []
        for password in passwords:
            logins.append(Login(password=password))

        session.add_all(logins)
        session.commit()

        data_fetcher = DataFetcher(database)

        values, columns = data_fetcher.get_strongest_password()

        assert set(values) == set([(expected, )])

    def test_get_persons_born_between(self):
        database = Database(':memory:')
        session = database.get_session()

        dob_1 = DayOfBirth(date=datetime(year=1963, month=7, day=15))
        dob_2 = DayOfBirth(date=datetime(year=1975, month=1, day=3))
        dob_3 = DayOfBirth(date=datetime(year=2020, month=3, day=20))

        person_1 = Person(email='to early')
        person_1.day_of_birth = [dob_1]
        person_2 = Person(email='should be returned')
        person_2.day_of_birth = [dob_2]
        person_3 = Person(email='to late')
        person_3.day_of_birth = [dob_3]

        min_date = datetime(year=1970, month=1, day=1)
        max_date = datetime(year=1999, month=12, day=30)

        session.add_all([person_1, person_2, person_3])
        session.commit()

        data_fetcher = DataFetcher(database)

        values, columns = data_fetcher.get_persons_born_between(min_date=min_date, max_date=max_date)

        assert len(values) == 1
        assert values[0][0].email == 'should be returned'
