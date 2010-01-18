# -*- coding: utf-8 -*-
#
# python-chrono - a date/time module for python
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

from . import calendar

import re
import string


class Formatter(object):
    """
    Date/time template formatter, main format method is
    :meth:`chrono.formatter.Formatter.format`.
    """

    __re_replace = re.compile('''
        \$(?:                           # starting variable delimiter
        (?P<escaped>\$)             |   # escape sequence (two delimiters)
        (?P<named>[a-z0-9_]+)       |   # delimiter and identifier
        \{(?P<braced>[a-z0-9_]+)\}  |   # delimiter and braced identifier
        (?P<invalid>)                   # invalid delimiter expression
        )
    ''', re.VERBOSE | re.IGNORECASE)

    @classmethod
    def __cb_replace(cls, match, year, month, day, hour, minute, second):
        "Callback function for replacing variables in a template"

        # handle escaped delimiters
        if match.group("escaped") is not None:
            return "$"

        # handle invalid identifiers
        elif match.group("invalid") is not None:
            return match.group(0)

        # otherwise, find name to use
        name = match.group("named") or match.group("braced")

        # handle year formatting
        if name == "year":
            return year and str(year) or ""

        elif name == "0year":
            return year and str(year).zfill(4) or ""

        elif name == "shortyear":
            return year and str(year)[-2:] or ""

        # handle month formatting
        elif name == "month":
            return month and str(month) or ""

        elif name == "0month":
            return month and str(month).zfill(2) or ""

        elif name == "monthname":
            return month and calendar.Calendar.monthname(month) or ""

        elif name == "shortmonthname":
            return month and calendar.Calendar.monthname(month, True) or ""

        # handle week formatting
        elif name == "week":
            return year and month and day and \
                str(calendar.ISOCalendar.week(year, month, day)[1]) or ""

        elif name == "0week":
            return year and month and day and str(
                calendar.ISOCalendar.week(year, month, day)[1]
            ).zfill(2) or ""

        # handle day formatting
        elif name == "day":
            return day and str(day) or ""

        elif name == "0day":
            return day and str(day).zfill(2) or ""

        # handle weekday formatting
        elif name == "weekday":
            return year and month and day and \
                str(calendar.ISOCalendar.weekday(year, month, day)) or ""

        elif name == "weekdayname":
            return year and month and day and \
                calendar.ISOCalendar.weekdayname(
                    calendar.ISOCalendar.weekday(year, month, day)
                ) or ""

        elif name == "shortweekdayname":
            return year and month and day and \
                calendar.ISOCalendar.weekdayname(
                    calendar.ISOCalendar.weekday(year, month, day), True
                ) or ""

        # handle hour formatting
        elif name == "hour":
            return hour is not None and str(hour) or ""

        elif name == "0hour":
            return hour is not None and str(hour).zfill(2) or ""

        elif name == "012hour":
            return hour is not None and str(hour > 12 and \
                str(hour - 12).zfill(2) or hour) or ""

        elif name == "12hour":
            return hour is not None and str(hour > 12 and \
                str(hour - 12) or hour) or ""

        elif name == "ampm":
            return hour is not None and hour >= 12 and "PM" or "AM"

        # handle minute formatting
        elif name == "minute":
            return minute is not None and str(minute) or ""

        elif name == "0minute":
            return minute is not None and str(minute).zfill(2) or ""

        # handle second formatting
        elif name == "second":
            return second is not None and str(second) or ""

        elif name == "0second":
            return second is not None and str(second).zfill(2) or ""

        # handle unknown variables
        else:
            return match.group(0)

    @classmethod
    def format(
        cls, template,
        year=None, month=None, day=None,
        hour=None, minute=None, second=None
    ):
        """
        Formats *template* by replacing substitution variables of the form
        ``$name`` or ``${name}`` with formatted values based on the input
        date.

        If any necessary values are missing (ie **None**) for a substitution
        variable, it will be replaced with an empty string.

        Valid substitution variables:

        =================== ==================================
        Variable            Description
        =================== ==================================
        012hour             Hour, 12-hour, zero-padded
        0hour               Hour, zero-padded
        0day                Day, zero-padded
        0minute             Minute, zero-padded
        0month              Month, zero-padded
        0second             Second, zero-padded
        0week               Week, zero-padded
        0year               Year, zero-padded
        12hour              Hour, 12-hour
        ampm                AM/PM, based on hour
        day                 Day
        hour                Hour
        minute              Minute
        month               Month
        monthname           Month name
        second              Second
        shortmonthname      Month name, abbreviated
        shortweekdayname    Weekday name, abbreviated
        shortyear           Year, two digits
        week                Week
        weekday             Weekday
        weekdayname         Weekday name
        year                Year
        =================== ==================================
        """

        # wrapper function, needed to get access to date variables, and pass
        # them on to the actual callback function
        def wrapper(match):
            return cls.__cb_replace(
                match, year, month, day, hour, minute, second
            )

        return cls.__re_replace.sub(wrapper, template)
