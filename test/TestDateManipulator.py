from DateManipulator import DateManipulator
import datetime


class TestDateManipulator:

    def test_date_returned_by_get_now_has_set_time_zone(self):
        date = DateManipulator()
        now = date.get_now()

        assert now.tzinfo is not None

    def test_calculation_days_to_date_when_was_yesterday(self, mocker):
        fake_now = datetime.datetime(year=2001, month=8, day=3, hour=10, minute=0, second=0,
                                     tzinfo=datetime.timezone.utc)
        mocker.patch.object(DateManipulator, 'get_now', lambda x, y: fake_now)

        date_handler = DateManipulator()
        birth_date = datetime.datetime(year=1949, month=8, day=2, hour=6, minute=0, second=0, microsecond=0,
                                       tzinfo=datetime.timezone.utc)

        expected_result = 364

        result = date_handler.days_till_date(birth_date)

        assert result == expected_result

    def test_calculation_days_to_date_when_will_be_tomorrow(self, mocker):
        fake_now = datetime.datetime(year=2001, month=8, day=3, hour=10, minute=0, second=0,
                                     tzinfo=datetime.timezone.utc)
        mocker.patch.object(DateManipulator, 'get_now', lambda x, y: fake_now)

        date_handler = DateManipulator()
        birth_date = datetime.datetime(year=1949, month=8, day=4, hour=6, minute=0, second=0, microsecond=0,
                                       tzinfo=datetime.timezone.utc)

        expected_result = 1

        result = date_handler.days_till_date(birth_date)

        assert result == expected_result

    def test_calculation_days_to_date_when_leap_year(self, mocker):
        fake_now = datetime.datetime(year=2000, month=2, day=1, hour=10, minute=0, second=0,
                                     tzinfo=datetime.timezone.utc)
        mocker.patch.object(DateManipulator, 'get_now', lambda x, y: fake_now)

        date_handler = DateManipulator()
        birth_date = datetime.datetime(year=1949, month=3, day=1, hour=6, minute=0, second=0, microsecond=0,
                                       tzinfo=datetime.timezone.utc)

        expected_result = 29

        result = date_handler.days_till_date(birth_date)

        assert result == expected_result

    def test_change_year_work_with_leap_year(self):
        date_handler = DateManipulator()
        date = datetime.datetime(year=2000, month=2, day=29, hour=10, minute=0, second=0, microsecond=0,
                                     tzinfo=datetime.timezone.utc)
        expected_result = datetime.datetime(year=2001, month=3, day=1, hour=10, minute=0, second=0, microsecond=0,
                                     tzinfo=datetime.timezone.utc)

        result = date_handler.change_year(date, 1)

        assert result == expected_result

    def test_change_year_work_without_leap_year(self):
        date_handler = DateManipulator()
        date = datetime.datetime(year=2001, month=3, day=1, hour=10, minute=0, second=0, microsecond=0,
                                     tzinfo=datetime.timezone.utc)
        expected_result = datetime.datetime(year=2002, month=3, day=1, hour=10, minute=0, second=0, microsecond=0,
                                     tzinfo=datetime.timezone.utc)

        result = date_handler.change_year(date, 1)

        assert result == expected_result

    def test_change_year_work_backwards(self):
        date_handler = DateManipulator()
        date = datetime.datetime(year=2001, month=3, day=1, hour=10, minute=0, second=0, microsecond=0,
                                     tzinfo=datetime.timezone.utc)
        expected_result = datetime.datetime(year=2000, month=3, day=1, hour=10, minute=0, second=0, microsecond=0,
                                     tzinfo=datetime.timezone.utc)

        result = date_handler.change_year(date, -1)

        assert result == expected_result

    def test_change_year_work_backwards_with_leap_year(self):
        date_handler = DateManipulator()
        date = datetime.datetime(year=2001, month=2, day=28, hour=10, minute=0, second=0, microsecond=0,
                                     tzinfo=datetime.timezone.utc)
        expected_result = datetime.datetime(year=2000, month=2, day=28, hour=10, minute=0, second=0, microsecond=0,
                                     tzinfo=datetime.timezone.utc)

        result = date_handler.change_year(date, -1)

        assert result == expected_result

    def test_change_year_work_without_time(self):
        date_handler = DateManipulator()
        date = datetime.datetime(year=2001, month=2, day=28, tzinfo=datetime.timezone.utc)
        expected_result = datetime.datetime(year=2000, month=2, day=28, hour=0, minute=0, second=0, microsecond=0,
                                     tzinfo=datetime.timezone.utc)

        result = date_handler.change_year(date, -1)

        assert result == expected_result


