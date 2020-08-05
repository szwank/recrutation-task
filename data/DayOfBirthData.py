import datetime

from DateManipulator import DateManipulator


class DayOfBirth:
    def __init__(self, date: str, age: int):
        self.date = self.str_to_datetime(date)
        self.age = age

    def str_to_datetime(self, date):
        return datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f%z')

    @property
    def days_to_birthday(self):
        date_manipulator = DateManipulator()
        return date_manipulator.days_till_date(self.date)

