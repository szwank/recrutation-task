import datetime

from data.CoordinatesData import CoordinatesData
from data.DayOfBirthData import DayOfBirthData
from data.IDData import IDData
from data.LocationData import LocationData
from data.LoginData import LoginData
from data.NameData import NameData
from data.RegisteredData import RegisteredData
from data.StreetData import StreetData
from database.Database import Database
from database.DatabaseLoader import DatabaseLoader
from data.PersonData import PersonData
from data.TimeZoneData import TimeZoneData
from database.tables.Name import Name
from database.tables.Person import Person
from database.tables.DayOfBirth import DayOfBirth
from database.tables.Login import Login
from database.tables.Registered import Registered
from database.tables.ID import ID
from database.tables.Location import Location
from database.tables.Coordinates import Coordinates
from database.tables.Street import Street
from database.tables.TimeZone import TimeZone


class TestDatabaseLoader:
    data = {
        "gender": "female",
        "name": {
            "title": "Miss",
            "first": "Louane",
            "last": "Vidal"
        },
        "location": {
            "street": {
                "number": 2479,
                "name": "Place du 8 Février 1962"
            },
            "city": "Avignon",
            "state": "Vendée",
            "country": "France",
            "postcode": 78276,
            "coordinates": {
                "latitude": "2.0565",
                "longitude": "95.2422"
            },
            "timezone": {
                "offset": "+1:00",
                "description": "Brussels, Copenhagen, Madrid, Paris"
            }
        },
        "email": "louane.vidal@example.com",
        "login": {
            "uuid": "9f07341f-c7e6-45b7-bab0-af6de5a4582d",
            "username": "angryostrich988",
            "password": "r2d2",
            "salt": "B5ywSDUM",
            "md5": "afce5fbe8f32bcec1a918f75617ab654",
            "sha1": "1a5b1afa1d9913cf491af64ce78946d18fea6b04",
            "sha256": "0124895aa1e6e5fb0596fad4c413602e0922e8a8c2dc758bbdb3fa070ad25a07"
        },
        "dob": {
            "date": "1966-06-26T11:50:25.558Z",
            "age": 54
        },
        "registered": {
            "date": "2016-08-11T06:51:52.086Z",
            "age": 4
        },
        "phone": "02-62-35-18-98",
        "cell": "06-07-80-83-11",
        "id": {
            "name": "INSEE",
            "value": "2NNaN01776236 16"
        },
        "picture": {
            "large": "https://randomuser.me/api/portraits/women/88.jpg",
            "medium": "https://randomuser.me/api/portraits/med/women/88.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/women/88.jpg"
        },
        "nat": "FR"
    }

    def test_add_location_data_add_tables(self):
        database = Database(':memory:')
        session = database.get_session()
        database.create_missing_tables()
        database_loader = DatabaseLoader(database)

        location = self.get_location_data()
        database_loader.load_location_data(location)

        assert len(session.query(Location).all()) == 1
        assert len(session.query(TimeZone).all()) == 1
        assert len(session.query(Coordinates).all()) == 1
        assert len(session.query(Street).all()) == 1

    def get_location_data(self) -> LocationData:
        data = self.data['location'].copy()

        timezone = TimeZoneData(**data['timezone'])
        coordinates = CoordinatesData(**data['coordinates'])
        street = StreetData(**data['street'])

        data['timezone'] = timezone
        data['coordinates'] = coordinates
        data['street'] = street

        return LocationData(**data)

    def test_add_location_data_set_coordinates_table_row(self):
        database = Database(':memory:')
        session = database.get_session()
        database.create_missing_tables()
        database_loader = DatabaseLoader(database)

        location = self.get_location_data()

        expected = self.data['location']['coordinates']

        database_loader.load_location_data(location)
        result = session.query(Coordinates).first()

        assert result.latitude == expected['latitude']
        assert result.longitude == expected['longitude']

    def test_add_location_data_set_timezone_table_row(self):
        database = Database(':memory:')
        session = database.get_session()
        database.create_missing_tables()
        database_loader = DatabaseLoader(database)

        location = self.get_location_data()

        expected = self.data['location']['timezone']

        database_loader.load_location_data(location)
        result = session.query(TimeZone).first()

        assert result.offset == expected['offset']
        assert result.description == expected['description']

    def test_add_location_data_set_location_table_row(self):
        database = Database(':memory:')
        session = database.get_session()
        database.create_missing_tables()
        database_loader = DatabaseLoader(database)

        location = self.get_location_data()

        expected = self.data['location']

        database_loader.load_location_data(location)
        result = session.query(Location).first()

        assert result.city == expected['city']
        assert result.state == expected['state']
        assert result.country == expected['country']
        assert result.postcode == expected['postcode']

    def test_add_person_data_add_all_tables(self):
        database = Database(':memory:')
        session = database.get_session()
        database.create_missing_tables()
        database_loader = DatabaseLoader(database)

        person = self.get_person_data()
        database_loader.load_person_data(person)

        assert len(session.query(Location).all()) == 1
        assert len(session.query(Name).all()) == 1
        assert len(session.query(Login).all()) == 1
        assert len(session.query(DayOfBirth).all()) == 1
        assert len(session.query(Registered).all()) == 1
        assert len(session.query(ID).all()) == 1
        assert len(session.query(Person).all()) == 1

    def get_person_data(self):
        login = LoginData(**self.data['login'])
        day_of_birth = DayOfBirthData(**self.data['dob'])
        name = NameData(**self.data['name'])
        registered = RegisteredData(**self.data['registered'])
        id = IDData(**self.data['id'])

        data_container_args = self.data.copy()
        data_container_args['login'] = login
        data_container_args['dob'] = day_of_birth
        data_container_args['registered'] = registered
        data_container_args['id'] = id
        data_container_args['location'] = self.get_location_data()
        data_container_args['name'] = name
        data_container_args.pop('picture', None)

        return PersonData(**data_container_args)

    def test_load_person_data_set_person_table_row(self):
        database = Database(':memory:')
        session = database.get_session()
        database.create_missing_tables()
        database_loader = DatabaseLoader(database)

        person = self.get_person_data()
        database_loader.load_person_data(person)
        result = session.query(Person).first()

        assert result.gender == self.data['gender']
        assert result.email == self.data['email']
        assert result.phone == "0262351898"
        assert result.cell == self.data['cell']
        assert result.nat == self.data['nat']

    def test_load_person_data_set_name_table_row(self):
        database = Database(':memory:')
        session = database.get_session()
        database.create_missing_tables()
        database_loader = DatabaseLoader(database)

        person = self.get_person_data()
        database_loader.load_person_data(person)
        result = session.query(Name).first()
        expected = self.data['name']

        assert result.title == expected['title']
        assert result.first == expected['first']
        assert result.last == expected['last']

    def test_load_person_data_set_login_table_row(self):
        database = Database(':memory:')
        session = database.get_session()
        database.create_missing_tables()
        database_loader = DatabaseLoader(database)

        person = self.get_person_data()
        database_loader.load_person_data(person)
        result = session.query(Login).first()
        expected = self.data['login']

        assert result.uuid == expected['uuid']
        assert result.username == expected['username']
        assert result.password == expected['password']
        assert result.salt == expected['salt']
        assert result.md5 == expected['md5']
        assert result.sha1 == expected['sha1']
        assert result.sha256 == expected['sha256']

    def test_load_person_data_set_day_of_birth_table_row(self):
        database = Database(':memory:')
        session = database.get_session()
        database.create_missing_tables()
        database_loader = DatabaseLoader(database)

        person = self.get_person_data()
        database_loader.load_person_data(person)
        result = session.query(DayOfBirth).first()
        expected = self.data['dob']

        assert result.date == datetime.datetime(year=1966, month=6, day=26, hour=11, minute=50, second=25,
                                                microsecond=558000)
        assert result.age == expected['age']

    def test_load_person_data_set_registered_table_row(self):
        database = Database(':memory:')
        session = database.get_session()
        database.create_missing_tables()
        database_loader = DatabaseLoader(database)

        person = self.get_person_data()
        database_loader.load_person_data(person)
        result = session.query(Registered).first()
        expected = self.data['registered']

        assert result.date == datetime.datetime(year=2016, month=8, day=11, hour=6, minute=51, second=52,
                                                microsecond=86000)
        assert result.age == expected['age']

    def test_load_person_data_set_id_table_row(self):
        database = Database(':memory:')
        session = database.get_session()
        database.create_missing_tables()
        database_loader = DatabaseLoader(database)

        person = self.get_person_data()
        database_loader.load_person_data(person)
        result = session.query(ID).first()
        expected = self.data['id']

        assert result.name == expected['name']
        assert result.value == expected['value']