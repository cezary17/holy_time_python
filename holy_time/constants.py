import re
from typing import Any, Dict, Union, Callable

TimeUnits = {
    "YEAR": 31536000000,
    "MONTH": 2678400000,
    "WEEK": 604800000,
    "DAY": 86400000,
    "HOUR": 3600000,
    "MINUTE": 60000,
    "SECOND": 1000,
    "MILLISECOND": 1,
}

FORMAT_REGEX = re.compile(
    r"\[(?P<escaped>[^]]+)]|Y{4}|Y{2}|M{1,4}|D{1,2}|d{1,4}|h{1,2}|m{1,2}|s{1,2}"
)
MONTH_NAMES = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

RELATIVE_MAP: Dict[Union[int, str], Union[str, Callable[[int], str]]] = {
    TimeUnits["SECOND"] * 0: "a few seconds",
    TimeUnits["SECOND"] * 5: lambda milliseconds: f"{int(milliseconds / TimeUnits['SECOND'])} seconds",
    TimeUnits["MINUTE"]: "a minute",
    TimeUnits["MINUTE"] * 2: lambda milliseconds: f"{int(milliseconds / TimeUnits['MINUTE'])} minutes",
    TimeUnits["HOUR"]: "an hour",
    TimeUnits["HOUR"] * 2: lambda milliseconds: f"{int(milliseconds / TimeUnits['HOUR'])} hours",
    TimeUnits["DAY"]: "a day",
    TimeUnits["DAY"] * 2: lambda milliseconds: f"{int(milliseconds / TimeUnits['DAY'])} days",
    TimeUnits["MONTH"]: "a month",
    TimeUnits["MONTH"] * 2: lambda milliseconds: f"{int(milliseconds / TimeUnits['MONTH'])} months",
    TimeUnits["YEAR"]: "a year",
    TimeUnits["YEAR"] * 2: lambda milliseconds: f"{int(milliseconds / TimeUnits['YEAR'])} years",
}
