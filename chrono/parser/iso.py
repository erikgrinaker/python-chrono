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


class ISOParser(parser.Parser):
    """
    A parser for ISO 8601 date formats, using the ISO calendar.
    For more information on the ISO calendar, see the
    :class:`chrono.calendar.ISOCalendar` documentation.

    The most commonly used ISO formats are *yyyy-mm-dd* and
    *yyyy-mm-dd hh:mm:ss*, but the standard specifies a range of formats,
    listed below. Datetimes can be composed of any combination of
    the date and time formats listed, separated by whitespace or
    a T.

    =================== =================== ======================= ===============================================
    Format              Example             Description             Method
    =================== =================== ======================= ===============================================
    yyyy-mm-dd          2009-12-27          Date                    :meth:`chrono.parser.ISOParser.date`
    hh:mm:ss            15:27:43            Time [#f1]_             :meth:`chrono.parser.ISOParser.time`
    yyyy-ddd            2009-163            Ordinal day             :meth:`chrono.parser.ISOParser.ordinal`
    yyyy-Www-d          2009-W36-3          Week and weekday        :meth:`chrono.parser.ISOParser.weekdate`
    yyyy-Www            2009-W36            Week                    :meth:`chrono.parser.ISOParser.week`
    yyyy-mm             2009-12             Month                   :meth:`chrono.parser.ISOParser.month`
    yyyy                2009                Year                    :meth:`chrono.parser.ISOParser.year`
    yyyymmdd            20091227            Compact date            :meth:`chrono.parser.ISOParser.compactdate`
    hhmmss              152743              Compact time [#f1]_     :meth:`chrono.parser.ISOParser.compacttime`
    yyyyddd             2009163             Compact ordinal day     :meth:`chrono.parser.ISOParser.compactordinal`
    yyyyWwwd            2009W363            Compact week and day    :meth:`chrono.parser.ISOParser.compactweekdate`
    yyyyWww             2009W36             Compact week            :meth:`chrono.parser.ISOParser.compactweek`
    =================== =================== ======================= ===============================================

    .. [#f1] Seconds and minutes may be omitted in times
    """

    re_compactdate = re.compile('''
        ^\s*                    # ignore whitespace at start
        (?P<year>\d{4})         # year
        (?P<month>\d{2})        # month
        (?P<day>\d{2})          # day
        \s*$                    # ignore whitespace at end
    ''', re.VERBOSE)

    re_compactordinal = re.compile('''
        ^\s*                    # ignore whitespace at start
        (?P<year>\d{4})         # year
        (?P<day>\d{3})          # day
        \s*$                    # ignore whitespace at end
    ''', re.VERBOSE)

    re_compacttime = re.compile('''
        ^\s*                    # ignore whitespace at start
        (?P<hour>\d{2})         # hour
        (?:(?P<minute>\d{2}))?  # minute
        (?:(?P<second>\d{2}))?  # second
        \s*$                    # ignore whitespace at end
    ''', re.VERBOSE)

    re_compactweek = re.compile('''
        ^\s*                    # ignore whitespace at start
        (?P<year>\d{1,4})       # year
        W(?P<week>\d{1,2})      # week
        \s*$                    # ignore whitespace at end
    ''', re.VERBOSE | re.IGNORECASE)

    re_compactweekdate = re.compile('''
        ^\s*                    # ignore whitespace at start
        (?P<year>\d{4})         # year
        W(?P<week>\d{2})        # week
        (?P<day>\d)             # day
        \s*$                    # ignore whitespace at end
    ''', re.VERBOSE | re.IGNORECASE)

    re_date = re.compile('''
        ^\s*                    # ignore whitespace at start
        (?P<year>\d{1,4})       # year
        -(?P<month>\d{1,2})     # month
        -(?P<day>\d{1,2})       # day
        \s*$                    # ignore whitespace at end
    ''', re.VERBOSE)

    re_datetime = re.compile('''
        ^\s*                    # ignore whitespace at start
        (?P<date>\S+?)          # date
        (?:T|\s+)               # separator
        (?P<time>\S+?)          # time
        \s*$                    # ignore whitespace at end
    ''', re.VERBOSE | re.IGNORECASE)

    re_month = re.compile('''
        ^\s*                    # ignore whitespace at start
        (?P<year>\d{1,4})       # year
        -(?P<month>\d{1,2})     # month
        \s*$                    # ignore whitespace at end
    ''', re.VERBOSE)

    re_ordinal = re.compile('''
        ^\s*                    # ignore whitespace at start
        (?P<year>\d{4})         # year
        -(?P<day>\d{3})         # day
        \s*$                    # ignore whitespace at end
    ''', re.VERBOSE)

    re_time = re.compile('''
        ^\s*                    # ignore whitespace at start
        (?P<hour>\d{1,2})       # hour
        (?::(?P<minute>\d{1,2}))? # minute
        (?::(?P<second>\d{1,2}))? # second
        \s*$                    # ignore whitespace at end
    ''', re.VERBOSE)

    re_week = re.compile('''
        ^\s*                    # ignore whitespace at start
        (?P<year>\d{1,4})       # year
        -W(?P<week>\d{1,2})     # week
        \s*$                    # ignore whitespace at end
    ''', re.VERBOSE | re.IGNORECASE)

    re_weekdate = re.compile('''
        ^\s*                    # ignore whitespace at start
        (?P<year>\d{1,4})       # year
        -W(?P<week>\d{1,2})     # week
        -(?P<day>\d)            # day
        \s*$                    # ignore whitespace at end
    ''', re.VERBOSE | re.IGNORECASE)

    re_year = re.compile('''
        ^\s*                    # ignore whitespace at start
        (?P<year>\d{1,4})       # year
        \s*$                    # ignore whitespace at end
    ''', re.VERBOSE)

    @classmethod
    def compactdate(cls, date):
        """
        Parses a compact ISO date (*yyyymmdd*), and returns a tuple with
        year, month, and day.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and
        :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`,
        or :exc:`chrono.error.DayError` for invalid date values.
        """

        match = utility.integer(cls.regexp(cls.re_compactdate, date))

        calendar.ISOCalendar.validate(
            match["year"],
            match["month"],
            match["day"]
        )

        return (match["year"], match["month"], match["day"])

    @classmethod
    def compactordinal(cls, date):
        """
        Parses a compact ISO ordinal date (*yyyyddd*), and returns a tuple
        with year and ordinal day.

        Raises :exc:`chrono.error.ParseError` for
        invalid input format, :exc:`TypeError` for invalid input type,
        and :exc:`chrono.error.YearError` or :exc:`chrono.error.DayError`
        for invalid date values.
        """

        match = utility.integer(cls.regexp(cls.re_compactordinal, date))

        calendar.ISOCalendar.validate_ordinal(
            match["year"],
            match["day"]
        )

        return (match["year"], match["day"])

    @classmethod
    def compacttime(cls, time):
        """
        Parses a compact ISO time (*hhmmss*), and returns a tuple with
        hour, minute, and second. Minutes and/or seconds may be omitted,
        which will be interpreted as 0.

        Raises :exc:`chrono.error.ParseError`
        for invalid input format, :exc:`TypeError` for invalid input type,
        and :exc:`chrono.error.HourError`, :exc:`chrono.error.MinuteError`,
        or :exc:`chrono.error.SecondError` for invalid time values.
        """

        match = utility.integer(cls.regexp(cls.re_compacttime, time))

        hour = match["hour"]
        minute = match["minute"] or 0
        second = match["second"] or 0

        clock.Clock.validate(hour, minute, second)

        return (hour, minute, second)

    @classmethod
    def compactweek(cls, date):
        """
        Parses a compact ISO week (*yyyyWww*), and returns a tuple with year
        and week number. Leading zeroes may be omitted, even though the ISO
        standard requires them.

        Raises :exc:`chrono.error.ParseError`
        for invalid input format, :exc:`TypeError` for invalid input type,
        and :exc:`chrono.error.YearError` or :exc:`chrono.error.WeekError`
        for invalid date values.
        """

        match = utility.integer(cls.regexp(cls.re_compactweek, date))

        calendar.ISOCalendar.validate_week(
            match["year"],
            match["week"]
        )

        return (match["year"], match["week"])

    @classmethod
    def compactweekdate(cls, date):
        """
        Parses a compact ISO weekdate (*yyyyWwwd*), and returns a tuple with
        year, week, and weekday.

        Raises :exc:`chrono.error.ParseError` for
        invalid input format, :exc:`TypeError` for invalid input type, and
        :exc:`chrono.error.YearError`, :exc:`chrono.error.WeekError`,
        or :exc:`chrono.error.DayError` for invalid date values.
        """

        match = utility.integer(cls.regexp(cls.re_compactweekdate, date))

        calendar.ISOCalendar.validate_weekdate(
            match["year"],
            match["week"],
            match["day"]
        )

        return (match["year"], match["week"], match["day"])

    @classmethod
    def date(cls, date):
        """
        Parses a ISO date (*yyyy-mm-dd*), and returns a tuple with year,
        month, and day. Leading zeroes may be omitted, even though the ISO
        standard requires them.

        Raises :exc:`chrono.error.ParseError` for
        invalid input format, :exc:`TypeError` for invalid input type,
        and :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`,
        or :exc:`chrono.error.DayError` for invalid date values.
        """

        match = utility.integer(cls.regexp(cls.re_date, date))

        calendar.ISOCalendar.validate(
            match["year"],
            match["month"],
            match["day"]
        )

        return (match["year"], match["month"], match["day"])

    @classmethod
    def month(cls, date):
        """
        Parses an ISO month (*yyyy-mm*), and returns a tuple with year and
        month. Leading zeroes may be omitted, even though the ISO standard
        requires them.

        Raises :exc:`chrono.error.ParseError` for
        invalid input format, :exc:`TypeError` for invalid input type,
        and :exc:`chrono.error.YearError` or :exc:`chrono.error.MonthError`
        for invalid date values.
        """

        match = utility.integer(cls.regexp(cls.re_month, date))

        calendar.ISOCalendar.validate_year(match["year"])
        calendar.ISOCalendar.validate_month(match["month"])

        return (match["year"], match["month"])

    @classmethod
    def ordinal(cls, date):
        """
        Parses an ISO ordinal date (*yyyy-ddd*), and returns a tuple with
        year and ordinal day.

        Raises :exc:`chrono.error.ParseError` for
        invalid input format, :exc:`TypeError` for invalid input type,
        and :exc:`chrono.error.YearError` or :exc:`chrono.error.DayError`
        for invalid date values.
        """

        match = utility.integer(cls.regexp(cls.re_ordinal, date))

        calendar.ISOCalendar.validate_ordinal(
            match["year"],
            match["day"]
        )

        return (match["year"], match["day"])

    @classmethod
    def parse_date(cls, date):
        """
        Parses an ISO date in any supported format, and returns a tuple with
        year, month, and day. For formats which doesn't provide data with day
        precision, the earliest possible day is used - for example,
        *2009-W32* would return (2009, 8, 3), the Monday of week 32 2009.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and an appropriate
        :exc:`chrono.error.DateError` subclass for invalid date values.
        """

        # date (yyyy-mm-dd)
        try:
            return cls.date(date)

        except error.ParseError:
            pass

        # compact date (yyyymmdd)
        try:
            return cls.compactdate(date)

        except error.ParseError:
            pass

        # month (yyyy-mm)
        try:
            y, m = cls.month(date)

            return (y, m, 1)

        except error.ParseError:
            pass

        # year (yyyy)
        try:
            return (cls.year(date), 1, 1)

        except error.ParseError:
            pass

        # week (yyyy-Www)
        try:
            y, w = cls.week(date)

            return calendar.ISOCalendar.week_to_date(y, w)

        except error.ParseError:
            pass

        # compact week (yyyyWww)
        try:
            y, w = cls.compactweek(date)

            return calendar.ISOCalendar.week_to_date(y, w)

        except error.ParseError:
            pass

        # weekdate (yyyy-Www-d)
        try:
            y, w, d = cls.weekdate(date)

            return calendar.ISOCalendar.weekdate_to_date(y, w, d)

        except error.ParseError:
            pass

        # compact weekdate (yyyyWwwd)
        try:
            y, w, d = cls.compactweekdate(date)

            return calendar.ISOCalendar.weekdate_to_date(y, w, d)

        except error.ParseError:
            pass

        # ordinal (yyyy-ddd)
        try:
            y, d = cls.ordinal(date)

            return calendar.ISOCalendar.ordinal_to_date(y, d)

        except error.ParseError:
            pass

        # compact ordinal (yyyy-ddd)
        try:
            y, d = cls.compactordinal(date)

            return calendar.ISOCalendar.ordinal_to_date(y, d)

        except error.ParseError:
            pass

        # handle unknown formats
        raise error.ParseError("Invalid ISO date value '{0}'".format(date))

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
        Parses an ISO time in any supported format and returns a tuple with
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

        raise error.ParseError("Invalid ISO time value '{0}'".format(time))

    @classmethod
    def time(cls, time):
        """
        Parses an ISO time (*hh:mm:ss*), and returns a tuple with hour,
        minute, and second. Minutes and/or seconds may be omitted, which
        will be interpreted as 0. Leading zeroes may be omitted, even though
        the ISO standard requires them.

        Raises :exc:`chrono.error.ParseError`
        for invalid input format, :exc:`TypeError` for invalid input type,
        and :exc:`chrono.error.HourError`, :exc:`chrono.error.MinuteError`,
        or :exc:`chrono.error.SecondError` for invalid time values.
        """

        match = utility.integer(cls.regexp(cls.re_time, time))

        h = match["hour"]
        m = match["minute"] or 0
        s = match["second"] or 0

        clock.Clock.validate(h, m, s)

        return (h, m, s)

    @classmethod
    def week(cls, date):
        """
        Parses an ISO week (*yyyy-Www*), and returns a tuple with year
        and week number. Leading zeroes may be omitted, even though the ISO
        standard requires them.

        Raises :exc:`chrono.error.ParseError`
        for invalid input format, :exc:`TypeError` for invalid input type,
        and :exc:`chrono.error.YearError` or :exc:`chrono.error.WeekError`
        for invalid date values.
        """

        match = utility.integer(cls.regexp(cls.re_week, date))

        calendar.ISOCalendar.validate_week(
            match["year"],
            match["week"]
        )

        return (match["year"], match["week"])

    @classmethod
    def weekdate(cls, date):
        """
        Parses an ISO weekdate (*yyyy-Www-d*), and returns a tuple with
        year, week, and weekday. Leading zeroes may be omitted, even though
        the ISO standard requires them.

        Raises :exc:`chrono.error.ParseError`
        for invalid input format, :exc:`TypeError` for invalid input type,
        and :exc:`chrono.error.YearError`, :exc:`chrono.error.WeekError`,
        or :exc:`chrono.error.DayError` for invalid date values.
        """

        match = utility.integer(cls.regexp(cls.re_weekdate, date))

        calendar.ISOCalendar.validate_weekdate(
            match["year"],
            match["week"],
            match["day"]
        )

        return (match["year"], match["week"], match["day"])

    @classmethod
    def year(cls, date):
        """
        Parses an ISO year (*yyyy*), and returns it. Leading zeroes may be
        omitted, even though the ISO standard requires them.

        Raises
        :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and
        :exc:`chrono.error.YearError` for invalid year value.
        """

        match = utility.integer(cls.regexp(cls.re_year, date))

        calendar.ISOCalendar.validate_year(match["year"])

        return match["year"]
