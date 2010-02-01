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
    A parser for US date formats, such as mm/dd/yyyy. Valid formats::
    """

    re_dasheddate = re.compile('''
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

    re_dotteddate = re.compile('''
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
    def dasheddate(cls, date):
        """
        Parses a dash-separated US date (*mm/dd/yyyy*), and returns a tuple
        with year, month, and day. Two-digit years will be interpreted in range
        1930-2029.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and
        :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`,
        or :exc:`chrono.error.DayError` for invalid date values.
        """

        match = cls.regexp(cls.re_dasheddate, date)

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
        month, and day. Two-digit years will be interpreted in range
        1930-2029.

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
    def dotteddate(cls, date):
        """
        Parses a dot-separated US date (*mm.dd.yyyy*), and returns a tuple
        with year, month, and day. Two-digit years will be interpreted in range
        1930-2029.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and
        :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`,
        or :exc:`chrono.error.DayError` for invalid date values.
        """

        match = cls.regexp(cls.re_dotteddate, date)

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
        tuple with year, month, and day. Two-digit years will be interpreted in
        range 1930-2029.

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

        # date (mm/dd/yyyy)
        try:
            return cls.date(date)

        except error.ParseError:
            pass

        # named date (dd-mmm-yyyy)
        try:
            return cls.namedate(date)

        except error.ParseError:
            pass

        # dashed date (mm-dd-yyyy)
        try:
            return cls.dasheddate(date)

        except error.ParseError:
            pass

        # dotted date
        try:
            return cls.dotteddate(date)

        except error.ParseError:
            pass

        # handle unknown formats
        raise error.ParseError("Invalid US date value '{0}'".format(date))

    @classmethod
    def parse_datetime(cls, datetime):
        """
        Parses an ISO datetime in any supported format and returns a tuple
        with year, month, day, hour, minute, and second. Omitted minutes
        and/or seconds will be interpreted as 0.

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

        # time (hh:mm:ss am/pm)
        try:
            return cls.time(time)

        except error.ParseError:
            pass

        # handle unknown formats
        raise error.ParseError("Invalid US time value '{0}'".format(time))

    @classmethod
    def time(cls, time):
        """
        Parses a US time (*hh:mm:ss am/pm*), and returns a tuple with hour,
        minute, and second, using 24-hour clock. Minutes and/or seconds may be
        omitted, which will be interpreted as 0. Leading zeroes may be omitted.

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
