# -*- coding: utf-8 -*-
#
# python-chrono - a Python module for easy and convenient date/time handling
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import absolute_import

from . import parser
from .. import calendar
from .. import clock
from .. import error
from .. import utility

import re


class USParser(parser.Parser):
    """
    A parser for US date formats, such as *mm/dd/yyyy*.

    Valid formats:

    =================== =================== ======================== ===============================================
    Format              Example             Description              Method
    =================== =================== ======================== ===============================================
    mm/dd/yyyy          07/23/2010          Date                     :meth:`chrono.parser.USParser.date`
    mm-dd-yyyy          07-23-2010          Dashed date              :meth:`chrono.parser.USParser.dashdate`
    mm.dd.yyyy          07.23.2010          Dotted date              :meth:`chrono.parser.USParser.dotdate`
    mmddyyyy            07232010            Compact date             :meth:`chrono.parser.USParser.compactdate`
    dd-mmm-yyyy         23-JUL-2010         Date with month name     :meth:`chrono.parser.USParser.namedate`
    hh:mm:ss am/pm      04:27:43 PM         Time, 12-hour            :meth:`chrono.parser.USParser.time`
    hhmmss am/pm        042743 PM           Compact time, 12-hour    :meth:`chrono.parser.USParser.compacttime`
    =================== =================== ======================== ===============================================

    Datetime formats can consist of any combination of the date and time
    formats above, separated by space.

    Leading zeroes may be omitted in days and months, and years may be
    specified with 2 digits, which will be interpreted in the range 1930-2029.

    Seconds and minutes may be omitted in times, which will be interpreted
    as 0.
    """

    re_compactdate = re.compile('''
        ^\s*                    # strip whitespace
        (?P<month>\d{2})        # month
        (?P<day>\d{2})          # day
        (?P<year>\d{2}|\d{4})   # year
        \s*$                    # strip whitespace
    ''', re.VERBOSE)

    re_compacttime = re.compile('''
        ^\s*                    # ignore whitespace at start
        (?P<hour>\d{2})         # hour
        (?:(?P<minute>\d{2}))?  # minute
        (?:(?P<second>\d{2}))?  # second
        \s*                     # separator
        (?P<ampm>[ap]\.?\s*m\.?) # am/pm
        \s*$                    # ignore whitespace at end
    ''', re.VERBOSE | re.IGNORECASE)

    re_dashdate = re.compile('''
        ^\s*                    # strip whitespace
        (?P<month>\d{1,2})      # month
        -(?P<day>\d{1,2})       # day
        -(?P<year>\d{1,4})      # year
        \s*$                    # strip whitespace
    ''', re.VERBOSE)

    re_date = re.compile('''
        ^\s*                    # strip whitespace
        (?P<month>\d{1,2})      # month
        /(?P<day>\d{1,2})       # day
        /(?P<year>\d{1,4})      # year
        \s*$                    # strip whitespace
    ''', re.VERBOSE)

    re_datetime = re.compile('''
        ^\s*                    # ignore whitespace at start
        (?P<date>\S+?)          # date
        \s+                     # separator
        (?P<time>.*?)           # time
        \s*$                    # ignore whitespace at end
    ''', re.VERBOSE | re.IGNORECASE)

    re_dotdate = re.compile('''
        ^\s*                    # strip whitespace
        (?P<month>\d{1,2})      # month
        \.(?P<day>\d{1,2})      # day
        \.(?P<year>\d{1,4})     # year
        \s*$                    # strip whitespace
    ''', re.VERBOSE)

    re_namedate = re.compile('''
        ^\s*                    # strip whitespace
        (?P<day>\d{1,2})        # day
        -(?P<month>[a-z]+)      # month
        -(?P<year>\d{1,4})      # year
        \s*$                    # strip whitespace
    ''', re.VERBOSE | re.IGNORECASE)

    re_time = re.compile('''
        ^\s*                    # strip whitespace
        (?P<hour>\d{1,2})       # hour
        (?::(?P<minute>\d{1,2}))? # minute
        (?::(?P<second>\d{1,2}))? # second
        \s*                     # separator
        (?P<ampm>[ap]\.?\s*m\.?)  # am/pm
        \s*$                    # strip whitespace
    ''', re.VERBOSE | re.IGNORECASE)

    @classmethod
    def compactdate(cls, date):
        """
        Parses a compact US date (*mmddyyyy*), and returns a tuple with year,
        month, and day.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and
        :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`,
        or :exc:`chrono.error.DayError` for invalid date values.
        """

        match = cls.regexp(cls.re_compactdate, date)

        if len(match["year"]) == 2:
            match["year"] = calendar.Calendar.fullyear(match["year"])

        match = utility.integer(match)

        calendar.USCalendar.validate(
                match["year"],
                match["month"],
                match["day"]
        )

        return (match["year"], match["month"], match["day"])

    @classmethod
    def compacttime(cls, time):
        """
        Parses a compact US time (*hhmmss am/pm*), and returns a tuple with
        hour, minute, and second, using 24-hour clock.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and
        :exc:`chrono.error.HourError`, :exc:`chrono.error.MinuteError`,
        or :exc:`chrono.error.SecondError` for invalid time values.
        """

        match = cls.regexp(cls.re_compacttime, time)

        h = utility.integer(match["hour"])
        m = utility.integer(match["minute"]) or 0
        s = utility.integer(match["second"]) or 0
        ampm = match["ampm"].replace(".", "").replace(" ", "").lower()

        clock.USClock.validate(h, m, s)

        h = clock.USClock.to_24(h, ampm == "pm")

        return (h, m, s)

    @classmethod
    def dashdate(cls, date):
        """
        Parses a dash-separated US date (*mm/dd/yyyy*), and returns a tuple
        with year, month, and day.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and
        :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`,
        or :exc:`chrono.error.DayError` for invalid date values.
        """

        match = cls.regexp(cls.re_dashdate, date)

        if len(match["year"]) == 2:
            match["year"] = calendar.Calendar.fullyear(match["year"])

        match = utility.integer(match)

        calendar.USCalendar.validate(
                match["year"],
                match["month"],
                match["day"]
        )

        return (match["year"], match["month"], match["day"])

    @classmethod
    def date(cls, date):
        """
        Parses a US date (*mm/dd/yyyy*), and returns a tuple with year,
        month, and day.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and
        :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`,
        or :exc:`chrono.error.DayError` for invalid date values.
        """

        match = cls.regexp(cls.re_date, date)

        if len(match["year"]) == 2:
            match["year"] = calendar.Calendar.fullyear(match["year"])

        match = utility.integer(match)

        calendar.USCalendar.validate(
                match["year"],
                match["month"],
                match["day"]
        )

        return (match["year"], match["month"], match["day"])

    @classmethod
    def dotdate(cls, date):
        """
        Parses a dot-separated US date (*mm.dd.yyyy*), and returns a tuple
        with year, month, and day.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and
        :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`,
        or :exc:`chrono.error.DayError` for invalid date values.
        """

        match = cls.regexp(cls.re_dotdate, date)

        if len(match["year"]) == 2:
            match["year"] = calendar.Calendar.fullyear(match["year"])

        match = utility.integer(match)

        calendar.USCalendar.validate(
                match["year"],
                match["month"],
                match["day"]
        )

        return (match["year"], match["month"], match["day"])

    @classmethod
    def namedate(cls, date):
        """
        Parses a US date with short month name (*dd-mmm-yyyy*), and returns a
        tuple with year, month, and day.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and
        :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`,
        or :exc:`chrono.error.DayError` for invalid date values.
        """

        match = cls.regexp(cls.re_namedate, date)

        if len(match["year"]) == 2:
            match["year"] = calendar.Calendar.fullyear(match["year"])

        else:
            match["year"] = utility.integer(match["year"])

        match["month"] = {
            "jan": 1,
            "feb": 2,
            "mar": 3,
            "apr": 4,
            "may": 5,
            "jun": 6,
            "jul": 7,
            "aug": 8,
            "sep": 9,
            "oct": 10,
            "nov": 11,
            "dec": 12,
        }.get(match["month"].lower(), match["month"])

        match["day"] = utility.integer(match["day"])

        calendar.USCalendar.validate(
                match["year"],
                match["month"],
                match["day"]
        )

        return (match["year"], match["month"], match["day"])

    @classmethod
    def parse_date(cls, date):
        """
        Parses a US date in any supported format, and returns a tuple with
        year, month, and day.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and an appropriate
        :exc:`chrono.error.DateError` subclass for invalid date values.
        """

        parsers = (
            cls.date,
            cls.namedate,
            cls.dashdate,
            cls.dotdate,
            cls.compactdate
        )

        for parser in parsers:
            try:
                return parser(date)

            except error.ParseError:
                pass

        raise error.ParseError("Invalid US date value '{0}'".format(date))

    @classmethod
    def parse_datetime(cls, datetime):
        """
        Parses an ISO datetime in any supported format and returns a tuple
        with year, month, day, hour, minute, and second.

        Raises
        :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and an appropriate
        :exc:`chrono.error.DateTimeError` subclass for invalid datetime
        values.
        """

        match = cls.regexp(cls.re_datetime, datetime)

        year, month, day = cls.parse_date(match["date"])
        hour, minute, second = cls.parse_time(match["time"])

        return (year, month, day, hour, minute, second)

    @classmethod
    def parse_time(cls, time):
        """
        Parses a US time in any supported format, and returns a tuple with
        hour, minute, and second in 24-hour format.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and an appropriate
        :exc:`chrono.error.TimeError` subclass for invalid time values.
        """

        parsers = (
            cls.time,
            cls.compacttime
        )

        for parser in parsers:
            try:
                return parser(time)

            except error.ParseError:
                pass

        raise error.ParseError("Invalid US time value '{0}'".format(time))

    @classmethod
    def time(cls, time):
        """
        Parses a US time (*hh:mm:ss am/pm*), and returns a tuple with hour,
        minute, and second, using 24-hour clock.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and
        :exc:`chrono.error.HourError`, :exc:`chrono.error.MinuteError`,
        or :exc:`chrono.error.SecondError` for invalid time values.
        """

        match = cls.regexp(cls.re_time, time)

        h = utility.integer(match["hour"])
        m = utility.integer(match["minute"]) or 0
        s = utility.integer(match["second"]) or 0
        ampm = match["ampm"].replace(".", "").replace(" ", "").lower()

        clock.USClock.validate(h, m, s)

        h = clock.USClock.to_24(h, ampm == "pm")

        return (h, m, s)
