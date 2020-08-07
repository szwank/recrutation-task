import datetime

from data.DataDeserializer import DataDeserializer


class TestDataDeserializer:
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

    def test_deserialize_person_correctly(self):
        data_deserializer = DataDeserializer()

        result = data_deserializer.deserialize(self.data)

        assert result.gender == self.data['gender']
        assert result.clean_phone_number == "0262351898"
        assert result.email == self.data['email']
        assert result.cell == self.data['cell']
        assert result.nat == self.data['nat']

    def test_deserialize_location_correctly(self):
        data_deserializer = DataDeserializer()
        expected = self.data['location']

        result = data_deserializer.deserialize(self.data)
        location = result.location

        assert location.city == expected['city']
        assert location.state == expected['state']
        assert location.country == expected['country']
        assert location.postcode == expected['postcode']

    def test_deserialize_street_correctly(self):
        data_deserializer = DataDeserializer()
        expected = self.data['location']['street']

        result = data_deserializer.deserialize(self.data)
        street = result.location.street

        assert street.number == expected['number']
        assert street.name == expected['name']

    def test_deserialize_coordinates_correctly(self):
        data_deserializer = DataDeserializer()
        expected = self.data['location']['coordinates']

        result = data_deserializer.deserialize(self.data)
        coordinates = result.location.coordinates

        assert coordinates.latitude == float(expected['latitude'])
        assert coordinates.longitude == float(expected['longitude'])

    def test_deserialize_timezone_correctly(self):
        data_deserializer = DataDeserializer()
        expected = self.data['location']['timezone']

        result = data_deserializer.deserialize(self.data)
        timezone = result.location.timezone

        assert timezone.offset == expected['offset']
        assert timezone.description == expected['description']

    def test_deserialize_name_correctly(self):
        data_deserializer = DataDeserializer()
        expected = self.data['name']

        result = data_deserializer.deserialize(self.data)
        name = result.name

        assert name.title == expected['title']
        assert name.first == expected['first']
        assert name.last == expected['last']

    def test_deserialize_login_correctly(self):
        data_deserializer = DataDeserializer()
        expected = self.data['login']

        result = data_deserializer.deserialize(self.data)
        login = result.login

        assert login.uuid == expected['uuid']
        assert login.username == expected['username']
        assert login.password == expected['password']
        assert login.salt == expected['salt']
        assert login.md5 == expected['md5']
        assert login.sha1 == expected['sha1']
        assert login.sha256 == expected['sha256']

    def test_deserialize_day_of_birth_correctly(self):
        data_deserializer = DataDeserializer()
        expected = self.data['dob']

        result = data_deserializer.deserialize(self.data)
        day_of_birth = result.day_of_birth

        assert day_of_birth.date == datetime.datetime(year=1966, month=6, day=26, hour=11, minute=50, second=25,
                                                      microsecond=558000, tzinfo=datetime.timezone.utc)
        assert day_of_birth.age == expected['age']

    def test_deserialize_registered_correctly(self):
        data_deserializer = DataDeserializer()
        expected = self.data['registered']

        result = data_deserializer.deserialize(self.data)
        registered = result.registered

        assert registered.date == datetime.datetime(year=2016, month=8, day=11, hour=6, minute=51, second=52,
                                                      microsecond=86000, tzinfo=datetime.timezone.utc)
        assert registered.age == expected['age']

    def test_deserialize_id_correctly(self):
        data_deserializer = DataDeserializer()
        expected = self.data['id']

        result = data_deserializer.deserialize(self.data)
        id = result.id

        assert id.name == expected['name']
        assert id.value == expected['value']
