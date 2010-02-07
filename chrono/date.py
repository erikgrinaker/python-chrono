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

from . import calendar as calendarmod
from . import error
from . import formatter
from . import parser as parsermod
from . import utility

import datetime
import time


class Date(object):
    """
    A class for date handling. For general usage, see the :ref:`usage`
    section.

    Valid values for *date* can be:

    * string: parses date from a string using the given parser (by default
      :class:`chrono.parser.CommonParser`)
    * **True**: sets the date to the current date
    * integer: assumes input is a UNIX timestamp, sets date accordingly
    * :class:`chrono.Date`: sets date from another Date object
    * :class:`datetime.date`: sets date from a :class:`datetime.date` object
    * :class:`time.struct_time`: sets date from a :class:`time.struct_time`
      object
    * **None**: creates a date with empty attributes
    * **False**: creates a date with empty attributes

    The class can also be initialized using the keyword arguments
    *year*, *month*, and *day*::

        Date(year=2000, month=10, day=16)

    If both *date* and keywords are specified, *date* takes precedence.

    *parser* determines which parser to use for parsing dates from strings.
    By default :class:`chrono.parser.CommonParser` is used, which supports
    the most common date and time formats. See :mod:`chrono.parser` for
    a list of available parsers.

    *calendar* determines which calendar to use for calendar operations.
    By default :class:`chrono.calendar.ISOCalendar` is used, see
    :mod:`chrono.calendar` for a list of available calendars.
    """

    calendar = None
    """
    Calendar to use for calendar operations. Defaults to
    :class:`chrono.calendar.ISOCalendar`. See :mod:`chrono.calendar`
    for available calendars.
    """

    day = None
    """
    Day number, range 1-31 depending on :attr:`chrono.Date.month` and
    :attr:`chrono.Date.year`.
    """

    month = None
    "Month number, range 1-12."

    parser = None
    """
    Parser to use for parsing dates and times from strings. See
    :mod:`chrono.parser` for available parsers.
    """

    year = None
    "Year number, range 1-9999."

    def __cmp__(self, other):

        if not isinstance(other, Date):
            other = Date(other)

        if not self.is_set() and not other.is_set():
            return 0

        elif not other.is_set():
            return 1

        elif not self.is_set():
            return -1

        if self.year != other.year:
            return utility.cmp(self.year, other.year)

        elif self.month != other.month:
            return utility.cmp(self.month, other.month)

        else:
            return utility.cmp(self.day, other.day)

    def __eq__(self, other):

        return self.__cmp__(other) == 0

    def __ge__(self, other):

        return self.__cmp__(other) >= 0

    def __gt__(self, other):

        return self.__cmp__(other) > 0

    def __init__(self, date=None, parser=None, calendar=None, **kwargs):

        self.parser = parser or parsermod.CommonParser
        self.calendar = calendar or calendarmod.ISOCalendar

        if isinstance(date, str):
            self.set_string(date)

        elif date is True:
            self.set_now()

        elif isinstance(date, int):
            self.set_unix(date)

        elif isinstance(date, Date):
            self.set(date.year, date.month, date.day)

        elif isinstance(date, datetime.date):
            self.set_datetime(date)

        elif isinstance(date, time.struct_time):
            self.set_struct_time(date)

        elif "year" in kwargs or "month" in kwargs or "day" in kwargs:
            self.set(
                kwargs.get("year"), kwargs.get("month"), kwargs.get("day")
            )

        elif date is False:
            pass

        elif date is None:
            pass

        else:
            raise TypeError("Invalid type for Date parameter")

    def __le__(self, other):

        return self.__cmp__(other) <= 0

    def __lt__(self, other):

        return self.__cmp__(other) < 0

    def __ne__(self, other):

        return self.__cmp__(other) != 0

    def __repr__(self):

        args = []

        if self.year != None:
            args.append("year={0}".format(self.year))

        if self.month != None:
            args.append("month={0}".format(self.month))

        if self.day != None:
            args.append("day={0}".format(self.day))

        return "chrono.Date({0})".format(", ".join(args))

    def __setattr__(self, name, value):

        if value is None:
            object.__setattr__(self, name, value)

        elif name == "year":

            if not 1 <= utility.int_year(value) <= 9999:
                raise error.YearError("Year '{0}' not in range 1-9999")

            object.__setattr__(self, name, value)

            # re-set month attribute, to trigger re-calculation
            # of month and day (is case of leap years etc)
            self.month = self.month

        elif name == "month":

            y = self.year or 0

            while value > 12:
                y += 1
                value -= 12

            while value < 1:
                y -= 1
                value += 12

            # set year, but only if already set
            object.__setattr__(self, "year", self.year and y or self.year)

            object.__setattr__(self, "month", value)

            # re-set day to itself, to trigger day re-calculation
            # (in case of leap months etc)
            self.day = self.day

        elif name == "day":

            # use current attribute values for calculations, or fall back to
            # sensible defaults if not set
            dt = datetime.date(self.year or 1900, self.month or 1, 1)
            dt += datetime.timedelta(value - 1)

            # set attributes, but only if they are already set
            object.__setattr__(
                self, "year", self.year and dt.year or self.year
            )
            object.__setattr__(
                self, "month", self.month and dt.month or self.month
            )
            object.__setattr__(self, "day", dt.day)

        # set other attributes directly
        else:
            object.__setattr__(self, name, value)

    def __str__(self):

        try:
            return self.get_string()

        except error.NoDateTimeError:
            return ""

    def assert_set(self):
        """
        Makes sure the object has a full date set, ie the attributes
        :attr:`chrono.Date.year`, :attr:`chrono.Date.month`, and
        :attr:`chrono.Date.day` are not **None**.

        Raises :exc:`chrono.error.NoDateTimeError` on missing attributes.
        """

        if not self.is_set():
            raise error.NoDateTimeError(
                "Date object doesn't contain complete date data"
            )

    def clear(self):
        """
        Clears the date, by setting :attr:`chrono.Date.year`,
        :attr:`chrono.Date.month` and :attr:`chrono.Date.day` to **None**.
        """

        self.year = None
        self.month = None
        self.day = None

    def delta(self, date):
        """
        Returns the difference between the current object and another date or
        datetime as seconds.

        Raises :exc:`chrono.error.NoDateTimeError` on missing attributes.
        """

        self.assert_set()
        date.assert_set()

        return date.get_unix() - self.get_unix()

    def format(self, template):
        """
        Formats the date using *template*, replacing variables as
        supported by :class:`chrono.formatter.Formatter`. This value is
        dependent on the calendar set in :attr:`chrono.Date.calendar`, by
        default :class:`chrono.calendar.ISOCalendar`.

        Raises :exc:`chrono.error.NoDateTimeError` on missing date data.
        """

        self.assert_set()

        return formatter.Formatter(self.calendar).format(
            template, self.year, self.month, self.day
        )

    def get(self):
        """
        Returns the date as a tuple of year, month, and day.

        Raises :exc:`chrono.error.NoDateTimeError` on missing date data.
        """

        self.assert_set()

        return (self.year, self.month, self.day)

    def get_datetime(self):
        """
        Returns a :class:`datetime.date` instance based on the date.

        Raises :exc:`chrono.error.NoDateTimeError` on missing date data.
        """

        self.assert_set()

        return datetime.date(self.year, self.month, self.day)

    def get_string(self):
        """
        Returns a string representation (*yyyy-mm-dd*) of the date.

        Raises :exc:`chrono.error.NoDateTimeError` on missing date data.
        """

        return self.format("$0year-$0month-$0day")

    def get_struct_time(self):
        """
        Returns a :class:`time.struct_time` representation of the date
        (expected as input to many Python functions).

        Raises :exc:`chrono.error.NoDateTimeError` on missing date data.
        """

        self.assert_set()

        return time.struct_time(self.get_datetime().timetuple())

    def get_unix(self):
        """
        Returns a UNIX timestamp representation of the date.

        Raises :exc:`chrono.error.NoDateTimeError` on missing date data.
        """

        self.assert_set()

        return int(time.mktime(self.get_struct_time()))

    def is_set(self):
        """
        Returns **True** if a date is set, ie if the attributes
        :attr:`chrono.Date.year`, :attr:`chrono.Date.month` and
        :attr:`chrono.Date.day` are not **None**, otherwise returns
        **False**.
        """

        return self.year != None and self.month != None and self.day != None

    def leapyear(self):
        """
        Returns **True** if the date is in a leap year, otherwise **False**.

        Raises :exc:`chrono.error.NoDateTimeError` on missing date data.
        """

        self.assert_set()

        return self.calendar.leapyear(self.year)

    def monthdays(self):
        """
        Returns the number of days in the set month.

        Raises :exc:`chrono.error.NoDateTimeError` on missing date data.
        """

        self.assert_set()

        return self.calendar.monthdays(self.year, self.month)

    def ordinal(self):
        """
        Returns the ordinal day (day number in the year) of the set date.

        Raises :exc:`chrono.error.NoDateTimeError` on missing date data.
        """

        self.assert_set()

        return self.calendar.ordinal(self.year, self.month, self.day)

    def set(self, year, month, day):
        """
        Sets the date.

        Raises :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`,
        or :exc:`chrono.error.DayError` for invalid values.
        """

        year = utility.int_year(year)
        month = utility.int_month(month)
        day = utility.int_day(day)

        self.calendar.validate(year, month, day)

        self.clear()

        self.year = year
        self.month = month
        self.day = day

    def set_datetime(self, datetime):
        """
        Sets the date from a :class:`datetime.date` object.
        """

        self.set(datetime.year, datetime.month, datetime.day)

    def set_now(self):
        """
        Sets the date to the current date.
        """

        d = datetime.date.today()

        self.set(d.year, d.month, d.day)

    def set_string(self, string):
        """
        Sets the date from a string, parsed with the parser set in
        :attr:`chrono.Date.parser`, by default
        :class:`chrono.parser.CommonParser`.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and an appropriate
        :exc:`chrono.error.DateError` subclass for invalid date values.
        """

        y, m, d = self.parser.parse_date(string)

        self.set(y, m, d)

    def set_struct_time(self, struct_time):
        """
        Sets the date from a :class:`time.struct_time` (as returned by
        various Python functions).
        """

        self.set(
            struct_time.tm_year,
            struct_time.tm_mon,
            struct_time.tm_mday
        )

    def set_unix(self, timestamp):
        """
        Sets the date from an integer UNIX timestamp.
        """

        dt = datetime.date.fromtimestamp(int(timestamp))

        self.set(dt.year, dt.month, dt.day)

    def week(self):
        """
        Returns the week of the set date as a tuple with year and week
        number. This value is dependent on the calendar set in
        :attr:`chrono.Date.calendar`, by default
        :class:`chrono.calendar.ISOCalendar`.

        Raises :exc:`chrono.error.NoDateTimeError` on missing date data.
        """

        self.assert_set()

        return self.calendar.week(self.year, self.month, self.day)

    def weekdate(self):
        """
        Returns the week date of the set date as a tuple with year,
        week, and weekday. This value is dependent on the calendar set in
        :attr:`chrono.Date.calendar`, by default
        :class:`chrono.calendar.ISOCalendar`.

        Raises :exc:`chrono.error.NoDateTimeError` on missing date data.
        """

        self.assert_set()

        return self.calendar.weekdate(self.year, self.month, self.day)

    def weekday(self):
        """
        Returns the week day of the set date, or **None** if no
        date is set. This value is dependent on the calendar set in
        :attr:`chrono.Date.calendar`, by default
        :class:`chrono.calendar.ISOCalendar`.

        Raises :exc:`chrono.error.NoDateTimeError` on missing date data.
        """

        self.assert_set()

        return self.calendar.weekday(self.year, self.month, self.day)

    def weeks(self):
        """
        Returns the number of weeks in the set year. This value is
        dependent on the calendar set in :attr:`chrono.Date.calendar`,
        by default :class:`chrono.calendar.ISOCalendar`.

        Raises :exc:`chrono.error.NoDateTimeError` on missing date data.
        """

        self.assert_set()

        return self.calendar.weeks(self.year)

    def yeardays(self):
        """
        Returns the number of days in the year.

        Raises :exc:`chrono.error.NoDateTimeError` on missing date data.
        """

        self.assert_set()

        return self.calendar.yeardays(self.year)
