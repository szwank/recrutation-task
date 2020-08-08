from database.Database import Database
from database.tables.DayOfBirth import DayOfBirth
from database.tables.Person import Person
from database.DataFetcher import DataFetcher


class TestDataFetcher:

    def test_get_gender_percentage_mixed_gender(self):
        database = Database(':memory:')
        database.create_missing_tables()
        session = database.get_session()

        person_1 = Person(gender='female')
        person_2 = Person(gender='female')
        person_3 = Person(gender='female')
        person_4 = Person(gender='male')
        session.bulk_save_objects([person_1, person_2, person_3, person_4])
        session.commit()

        data_fetcher = DataFetcher(database)

        result = data_fetcher.get_gender_percentage()
        expected = [('male', 25), ('female', 75)]

        assert set(result) == set(expected)

    def test_get_gender_percentage_single_gender(self):
        database = Database(':memory:')
        database.create_missing_tables()
        session = database.get_session()

        person_1 = Person(gender='female')
        person_2 = Person(gender='female')
        person_3 = Person(gender='female')
        session.bulk_save_objects([person_1, person_2, person_3])
        session.commit()

        data_fetcher = DataFetcher(database)

        result = data_fetcher.get_gender_percentage()
        expected = [('female', 100)]

        assert set(result) == set(expected)

    def test_get_average_age_mixed_gender(self):
        database = Database(':memory:')
        database.create_missing_tables()
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

        result = data_fetcher.get_average_age()
        expected = [('female', 10), ('male', 20), ('All', 15)]

        assert set(result) == set(expected)

    def test_get_average_age_single_gender(self):
        database = Database(':memory:')
        database.create_missing_tables()
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

        result = data_fetcher.get_average_age()
        expected = [('female', 15), ('All', 15)]

        assert set(result) == set(expected)
