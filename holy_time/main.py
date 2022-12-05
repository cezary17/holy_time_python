from datetime import datetime

from holy_time import constants


class HolyTime:
    Units = constants.TimeUnits

    def __init__(self, initial_date: datetime = datetime.now(), utc=False):
        self.date = HolyTime.resolve_date(initial_date)
        self.utc = utc

    @staticmethod
    def resolve_date(time):
        # TODO: validate
        if isinstance(time, datetime):
            return time
        if isinstance(time, HolyTime):
            return time.get_date()
        return datetime.fromtimestamp(time)

    @staticmethod
    def get_unit(unit: str):
        return HolyTime.Units[unit.lower()[:-1]]

    @staticmethod
    def now():
        return HolyTime()

    def UTC(self):
        self.utc = True
        return self

    @staticmethod
    def add(time, amount, unit="milliseconds"):
        return HolyTime(
            HolyTime.resolve_date(time).timestamp() + (amount * HolyTime.get_unit(unit))
        )

    def add(self, amount, unit="milliseconds"):
        self.date = datetime.fromtimestamp(
            self.date.timestamp() + (amount * HolyTime.get_unit(unit))
        )
        return self

    @staticmethod
    def subtract(time, amount, unit="milliseconds"):
        return HolyTime.add(time, -amount, unit)

    def subtract(self, amount, unit="milliseconds"):
        return self.add(-amount, unit)

    @staticmethod
    def in_(amount, unit="milliseconds"):
        return HolyTime(
            datetime.now().timestamp() + (amount * HolyTime.get_unit(unit or "milliseconds"))
        )

    @staticmethod
    def is_equal(time_a, time_b):
        return HolyTime.resolve_date(time_a).timestamp() == HolyTime.resolve_date(time_b).timestamp()

    def is_equal(self, time):
        return self.date.timestamp() == HolyTime.resolve_date(time).timestamp()

    @staticmethod
    def is_weekend(time, utc=False):
        date = HolyTime.resolve_date(time)

        week_day = date.weekday() if utc else date.isoweekday()
        return week_day == 6 or week_day == 7

    def is_weekend(self):
        return HolyTime.is_weekend(self, self.utc)

    @staticmethod
    def between(time_a, time_b):
        return abs(
            HolyTime.resolve_date(time_a).timestamp()
            - HolyTime.resolve_date(time_b).timestamp()
        )

    @staticmethod
    def is_after(time_a, time_b):
        return (
                HolyTime.resolve_date(time_a).timestamp()
                > HolyTime.resolve_date(time_b).timestamp()
        )

    def is_after(self, time):
        return (
                self.date.timestamp() > HolyTime.resolve_date(time).timestamp()
        )

    @staticmethod
    def is_before(time_a, time_b):
        return (
                HolyTime.resolve_date(time_a).timestamp()
                < HolyTime.resolve_date(time_b).timestamp()
        )

    def is_before(self, time):
        return self.date.timestamp() < HolyTime.resolve_date(time).timestamp()

    @staticmethod
    def format(time, format_string):
        date = HolyTime.resolve_date(time)
        return date.strftime(format_string)

    def format(self, format_string):
        return self.date.strftime(format_string)

    @staticmethod
    def from_format(time_string, format_string):
        date = datetime.strptime(time_string, format_string)
        return HolyTime(date)

    def get_date(self):
        return self.date

    def set_date(self, time):
        self.date = HolyTime.resolve_date(time)
