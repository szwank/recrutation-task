import datetime

from data.DayOfBirth import DayOfBirth
from DateManipulator import DateManipulator


class TestDayOfBirth:

    def test_date_str_to_datetime_conversion(self):
        day_of_birth = DayOfBirth('1966-06-26T11:50:25.558Z', 54)
        expected = datetime.datetime(year=1966, month=6, day=26, hour=11, minute=50, second=25, microsecond=558000,
                                     tzinfo=datetime.timezone.utc)

        assert day_of_birth.date == expected

    def test_days_till_birthday(self, mocker):
        fake_now = datetime.datetime(year=2001, month=8, day=3, hour=10, minute=0, second=0,
                                    tzinfo=datetime.timezone.utc)
        mocker.patch.object(DateManipulator, 'get_now', lambda x, y: fake_now)

        day_of_birth = DayOfBirth('1949-08-02T11:50:25.558Z', 54)
        expected_result = 364

        assert day_of_birth.days_to_birthday == expected_result

