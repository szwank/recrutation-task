import datetime


class RegisteredData:
    def __init__(self, date: str, age: int):
        self.date = self.str_to_datetime(date)
        self.age = age

    def str_to_datetime(self, date):
        return datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f%z')
