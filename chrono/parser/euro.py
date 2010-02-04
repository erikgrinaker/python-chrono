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
from .iso import ISOParser
from .. import calendar
from .. import clock
from .. import error
from .. import utility

import re


class EuroParser(parser.Parser):
    """
    A parser for european/western date formats, such as *dd.mm.yyyy*.
    Valid formats:

    =================== =================== ======================= ===============================================
    Format              Example             Description             Method
    =================== =================== ======================= ===============================================
    dd.mm.yyyy          23.07.2010          Date                    :meth:`chrono.parser.EuroParser.date`
    dd-mm-yyyy          23-07-2010          Dashed date             :meth:`chrono.parser.EuroParser.dashdate`
    dd/mm/yyyy          23/07/2010          Slashed date            :meth:`chrono.parser.EuroParser.slashdate`
    ddmmyyyy            23072010            Compact date            :meth:`chrono.parser.EuroParser.compactdate`
    hh:mm:ss            15:27:43            Time                    :meth:`chrono.parser.EuroParser.time`
    hhmmss              152743              Compact time            :meth:`chrono.parser.EuroParser.compacttime`
    =================== =================== ======================= ===============================================
    """

    re_compactdate = re.compile('''
        ^\s*                    # ignore whitespace at start
        (?P<day>\d{2})          # day
        (?P<month>\d{2})        # month
        (?P<year>\d{2}|\d{4})   # year
        \s*$                    # ignore whitespace at end
    ''', re.VERBOSE)

    re_dashdate = re.compile('''
        ^\s*                    # strip whitespace
        (?P<day>\d{1,2})        # day
        -(?P<month>\d{1,2})     # month
        -(?P<year>\d{1,4})      # year
        \s*$                    # strip whitespace
    ''', re.VERBOSE)

    re_date = re.compile('''
        ^\s*                    # ignore whitespace at start
        (?P<day>\d{1,2})        # day
        \.(?P<month>\d{1,2})    # month
        \.(?P<year>\d{1,4})     # year
        \s*$                    # ignore whitespace at end
    ''', re.VERBOSE)

    re_datetime = re.compile('''
        ^\s*                    # ignore whitespace at start
        (?P<date>\S+)           # date
        \s+                     # separator
        (?P<time>\S+)           # time
        \s*$                    # ignore whitespace at end
    ''', re.VERBOSE | re.IGNORECASE)

    re_slashdate = re.compile('''
        ^\s*                    # strip whitespace
        (?P<day>\d{1,2})        # day
        /(?P<month>\d{1,2})     # month
        /(?P<year>\d{1,4})      # year
        \s*$                    # strip whitespace
    ''', re.VERBOSE)

    @classmethod
    def compactdate(cls, date):
        """
        Parses a compact european date (*ddmmyyyy*), and returns a tuple
        with year, month, and day. Two-digit years will be interpreted in range
        1930-2029.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and
        :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`,
        or :exc:`chrono.error.DayError` for invalid date values.
        """

        match = cls.regexp(cls.re_compactdate, date)

        if len(match["year"]) == 2:
            match["year"] = calendar.Calendar.fullyear(match["year"])

        match = utility.integer(match)

        calendar.ISOCalendar.validate(
                match["year"],
                match["month"],
                match["day"]
        )

        return (match["year"], match["month"], match["day"])

    @classmethod
    def compacttime(cls, time):
        """
        Parses a compact european time (*hhmmss*), and returns a tuple with
        hour, minute, and second. Minutes and/or seconds may be omitted,
        which will be interpreted as 0.

        Raises :exc:`chrono.error.ParseError`
        for invalid input format, :exc:`TypeError` for invalid input type,
        and :exc:`chrono.error.HourError`, :exc:`chrono.error.MinuteError`,
        or :exc:`chrono.error.SecondError` for invalid time values.
        """

        return ISOParser.compacttime(time)

    @classmethod
    def dashdate(cls, date):
        """
        Parses a dash-separated european date (*dd-mm-yyyy*), and returns a
        tuple with year, month, and day. Two-digit years will be interpreted
        in range 1930-2029.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and
        :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`,
        or :exc:`chrono.error.DayError` for invalid date values.
        """

        match = cls.regexp(cls.re_dashdate, date)

        if len(match["year"]) == 2:
            match["year"] = calendar.Calendar.fullyear(match["year"])

        match = utility.integer(match)

        calendar.ISOCalendar.validate(
                match["year"],
                match["month"],
                match["day"]
        )

        return (match["year"], match["month"], match["day"])

    @classmethod
    def date(cls, date):
        """
        Parses a european date (*dd.mm.yyyy*), and returns a tuple with year,
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

        calendar.ISOCalendar.validate(
                match["year"],
                match["month"],
                match["day"]
        )

        return (match["year"], match["month"], match["day"])

    @classmethod
    def parse_date(cls, date):
        """
        Parses a european date in any supported format, and returns a tuple
        with year, month, and day.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and an appropriate
        :exc:`chrono.error.DateError` subclass for invalid date values.
        """

        # date (mm/dd/yyyy)
        try:
            return cls.date(date)

        except error.ParseError:
            pass

        # compact date
        try:
            return cls.compactdate(date)

        except error.ParseError:
            pass

        # dash date (mm-dd-yyyy)
        try:
            return cls.dashdate(date)

        except error.ParseError:
            pass

        # slash date
        try:
            return cls.slashdate(date)

        except error.ParseError:
            pass

        # handle unknown formats
        raise error.ParseError(
            "Invalid european date value '{0}'".format(date)
        )

    @classmethod
    def parse_datetime(cls, datetime):
        """
        Parses a US datetime in any supported format and returns a tuple
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
        Parses a european time in any supported format and returns a tuple with
        hour, minutes, and seconds. Omitted minutes and/or seconds will be
        interpreted as 0.

        Raises :exc:`chrono.error.ParseError` for invalid
        input format, :exc:`TypeError` for invalid input type, and an
        appropriate :exc:`chrono.error.TimeError` subclass for invalid time
        values.
        """

        # full time
        try:
            return cls.time(time)

        except error.ParseError:
            pass

        # compact time
        try:
            return cls.compacttime(time)

        except error.ParseError:
            pass

        raise error.ParseError(
            "Invalid european time value '{0}'".format(time)
        )


    @classmethod
    def slashdate(cls, date):
        """
        Parses a slash-separated european date (*mm/dd/yyyy*), and returns a
        tuple with year, month, and day. Two-digit years will be interpreted
        in range 1930-2029.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and
        :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`,
        or :exc:`chrono.error.DayError` for invalid date values.
        """

        match = cls.regexp(cls.re_slashdate, date)

        if len(match["year"]) == 2:
            match["year"] = calendar.Calendar.fullyear(match["year"])

        match = utility.integer(match)

        calendar.ISOCalendar.validate(
                match["year"],
                match["month"],
                match["day"]
        )

        return (match["year"], match["month"], match["day"])

    @classmethod
    def time(cls, time):
        """
        Parses a european time (*hh:mm:ss*), and returns a tuple with hour,
        minute, and second. Minutes and/or seconds may be omitted, which
        will be interpreted as 0. Leading zeroes may be omitted.

        Raises :exc:`chrono.error.ParseError`
        for invalid input format, :exc:`TypeError` for invalid input type,
        and :exc:`chrono.error.HourError`, :exc:`chrono.error.MinuteError`,
        or :exc:`chrono.error.SecondError` for invalid time values.
        """

        return ISOParser.time(time)