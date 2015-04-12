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

from . import parser
from .euro import EuroParser
from .iso import ISOParser
from .us import USParser
from .. import error

import re


class CommonParser(parser.Parser):
    """
    A parser for the most common date and time formats. Only the methods
    :meth:`chrono.parser.CommonParser.parse_date`,
    :meth:`chrono.parser.CommonParser.parse_datetime`,
    and :meth:`chrono.parser.CommonParser.parse_time`, are implemented here,
    methods for individual formats can be found in the classes
    :class:`chrono.parser.EuroParser`, :class:`chrono.parser.ISOParser`,
    and :class:`chrono.parser.USParser`.

    Valid formats:

    ============================= ============================= =================================
    Format                        Example                       Description
    ============================= ============================= =================================
    yyyy-mm-dd                    2009-12-27                    ISO date
    mm/dd/yyyy                    07/23/2010                    US date
    dd.mm.yyyy                    23.07.2010                    European date
    yyyy-ddd                      2009-163                      ISO ordinal date
    yyyy-Www-d                    2009-W36-3                    ISO weekdate
    yyyy-Www                      2009-W36                      ISO week
    yyyy-mm                       2009-12                       ISO month
    yyyy                          2009                          ISO year
    hh:mm:ss                      16:27:43                      ISO time
    hhmmss                        162743                        Compact ISO time
    hh:mm:ss am/pm                4:27:43 PM                    US 12-hour time
    hhmmss am/pm                  042743 PM                     Compact US 12-hour time
    ============================= ============================= =================================

    Datetime formats can consist of any combination of the date and time
    formats above, separated by space, or a T in the case of ISO formats.

    Leading zeroes may be omitted in days and months, and years may be
    specified with 2 digits in non-ISO formats, which will be interpreted in the
    range 1930-2029.

    Seconds and minutes may be omitted in times, which will be interpreted
    as 0.
    """

    re_datetime = re.compile('''
        ^\s*                    # ignore whitespace at start
        (?P<date>\S+?)          # date
        (?P<sep>\s+|T)          # separator
        (?P<time>.*?)           # time
        \s*$                    # ignore whitespace at end
    ''', re.VERBOSE | re.IGNORECASE)

    @classmethod
    def parse_date(cls, date):
        """
        Parses a date in any supported format, and returns a tuple with year,
        month, and day.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and an appropriate
        :exc:`chrono.error.DateError` subclass for invalid date values.
        """

        parsers = (
            USParser.date,
            EuroParser.date,
            ISOParser.date,
            ISOParser.ordinal,
            ISOParser.weekdate,
            ISOParser.week,
            ISOParser.month,
            ISOParser.year
        )

        for parser in parsers:
            try:
                return parser(date)

            except error.ParseError:
                pass

        raise error.ParseError("Invalid date value '{0}'".format(date))

    @classmethod
    def parse_datetime(cls, datetime):
        """
        Parses a date and time in any supported format and returns a tuple
        with year, month, day, hour, minute, and second.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and an appropriate
        :exc:`chrono.error.DateTimeError` subclass for invalid datetime
        values.
        """

        match = cls.regexp(cls.re_datetime, datetime)

        if match["sep"].upper() == "T":
            return ISOParser.parse_datetime(datetime)

        year, month, day = cls.parse_date(match["date"])
        hour, minute, second = cls.parse_time(match["time"])

        return (year, month, day, hour, minute, second)

    @classmethod
    def parse_time(cls, time):
        """
        Parses a time in any supported format and returns a tuple with
        hour, minutes, and seconds.

        Raises :exc:`chrono.error.ParseError` for invalid
        input format, :exc:`TypeError` for invalid input type, and an
        appropriate :exc:`chrono.error.TimeError` subclass for invalid time
        values.
        """

        parsers = (
            ISOParser.time,
            ISOParser.compacttime,
            USParser.time,
            USParser.compacttime
        )

        for parser in parsers:
            try:
                return parser(time)

            except error.ParseError:
                pass

        raise error.ParseError("Invalid time value '{0}'".format(time))
