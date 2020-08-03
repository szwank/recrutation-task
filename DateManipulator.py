import datetime


class DateManipulator:

    def days_till_date(self, date: datetime.datetime, time_zone: datetime.timezone = datetime.timezone.utc) -> int:
        """Return days till given date. Hours are not counted into account when calculating number of days.
        Example:
            1. for actual date 2020-08-01 20:30:00 and birth date 1995-08-02 3:00:00 functions return 1 day.
            2. for actual date 2020-08-02 00:00:00 and birth date 1995-08-02 23:59:00 functions return 0 days."""

        now = self.get_now(time_zone)
        now = self.set_time_to_midnight(now)

        years_difference = now.year - date.year
        actual_year_birthdate = self.change_year(date, years_difference)
        actual_year_birthdate = self.set_time_to_midnight(actual_year_birthdate)

        # if the birthday has already taken place this year
        if actual_year_birthdate < now:
            actual_year_birthdate = self.change_year(actual_year_birthdate, 1)

        return (actual_year_birthdate - now).days

    @staticmethod
    def get_now(time_zone: datetime.timezone = datetime.timezone.utc) -> datetime.datetime:
        """Returns datetime for actual date with set timezone."""
        now = datetime.datetime.now()
        return now.replace(tzinfo=time_zone)

    @staticmethod
    def change_year(date: datetime.datetime, years: int) -> datetime.datetime:
        """Function differs year in date. years can be negative, in this case years will be subtracted from date."""
        try:
            # Return same day of the current year
            return date.replace(year=date.year + years)
        except ValueError:
            # Case of leap year. February 29 to March 1 etc.
            return date.replace(year=date.year + years, month=date.month+1, day=1)

    @staticmethod
    def set_time_to_midnight(date: datetime.datetime) -> datetime.datetime:
        """Sets time part of date to 00:00:00.000 (midnight)."""
        return date.replace(hour=0, second=0, minute=0, microsecond=0)

