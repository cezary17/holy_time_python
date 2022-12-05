import datetime

from holy_time.main import HolyTime
from holy_time import constants


def test_resolve_date():
    # test with datetime object
    assert HolyTime.resolve_date(datetime.datetime(2020, 1, 1)) == datetime.datetime(2020, 1, 1)

    # test with HolyTime object
    holy_time = HolyTime(datetime.datetime(2020, 1, 1))
    assert HolyTime.resolve_date(holy_time) == datetime.datetime(2020, 1, 1)

    # test with timestamp
    assert HolyTime.resolve_date(1577880000) == datetime.datetime(2020, 1, 1)


def test_get_unit():
    # test with 'milliseconds'
    assert HolyTime.get_unit("milliseconds") == constants.TimeUnits["MILLISECOND"]

    # test with 'seconds'
    assert HolyTime.get_unit("seconds") == constants.TimeUnits["SECOND"]


def test_add():
    # test with datetime object
    date = datetime.datetime(2020, 1, 1)
    expected_date = datetime.datetime(2020, 1, 1, 0, 0, 1)
    assert HolyTime.add(date, 1, "seconds") == HolyTime(expected_date)

    # test with HolyTime object
    holy_time = HolyTime(date)
    expected_holy_time = HolyTime(expected_date)
    assert HolyTime.add(holy_time, 1, "seconds") == expected_holy_time

    # test with timestamp
    assert HolyTime.add(1577880000, 1, "seconds") == expected_holy_time


def test_subtract():
    # test with datetime object
    date = datetime.datetime(2020, 1, 1)
    expected_date = datetime.datetime(2019, 12, 31, 23, 59, 59)
    assert HolyTime.subtract(date, 1, "seconds") == HolyTime(expected_date)

    # test with HolyTime object
    holy_time = HolyTime(date)
    expected_holy_time = HolyTime(expected_date)
    assert HolyTime.subtract(holy_time, 1, "seconds") == expected_holy_time

    # test with timestamp
    assert HolyTime.subtract(1577880000, 1, "seconds") == expected_holy_time


def test_in_():
    # test with 'milliseconds'
    expected_date = datetime.datetime(2020, 1, 1, 0, 0, 0, 1)
    assert HolyTime.in_(1, "milliseconds") == HolyTime(expected_date)

    # test with 'seconds'
    expected_date = datetime.datetime(2020, 1, 1, 0, 0, 1)
    assert HolyTime.in_(1, "seconds") == HolyTime(expected_date)


def test_is_equal():
    # test with datetime object
    date = datetime.datetime(2020, 1, 1)
    assert HolyTime.is_equal(date, date)

def test_is_weekend():
    # test with datetime object on Saturday
    date = datetime.datetime(2020, 1, 4)
    assert HolyTime.is_weekend(date) == True

    # test with HolyTime object on Sunday
    holy_time = HolyTime(datetime.datetime(2020, 1, 5))
    assert HolyTime.is_weekend(holy_time) == True

    # test with timestamp on Monday
    assert HolyTime.is_weekend(1577958400) == False


def test_between():
    # test with datetime objects
    date_1 = datetime.datetime(2020, 1, 1)
    date_2 = datetime.datetime(2020, 1, 1, 0, 0, 1)
    assert HolyTime.between(date_1, date_2) == 1000

    # test with HolyTime objects
    holy_time_1 = HolyTime(date_1)
    holy_time_2 = HolyTime(date_2)
    assert HolyTime.between(holy_time_1, holy_time_2) == 1000

    # test with timestamps
    assert HolyTime.between(1577880000, 1577880100) == 1000


def test_is_after():
    # test with datetime objects
    date_1 = datetime.datetime(2020, 1, 1)
    date_2 = datetime.datetime(2020, 1, 2)
    assert HolyTime.is_after(date_1, date_2) == False

    # test with HolyTime objects
    holy_time_1 = HolyTime(date_1)
    holy_time_2 = HolyTime(date_2)
    assert HolyTime.is_after(holy_time_1, holy_time_2) == False

    # test with timestamps
    assert HolyTime.is_after(1577880000, 1578463200) == False


def test_is_before():
    # test with datetime objects
    date_1 = datetime.datetime(2020, 1, 1)
    date_2 = datetime.datetime(2020, 1, 2)
    assert HolyTime.is_before(date_1, date_2) == True

    # test with HolyTime objects
    holy_time_1 = HolyTime(date_1)
    holy_time_2 = HolyTime(date_2)
    assert HolyTime.is_before
