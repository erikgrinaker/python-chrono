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

from . import clock
from . import date
from . import error
from . import formatter
from . import time
from . import utility

import chrono
import datetime as datetimemod
import time as timemod


class DateTime(date.Date, time.Time):
    """
    A class for date/time handling. For general usage, see the description of
    :class:`chrono.Date` in the :ref:`usage` section, which works in much the
    same way as :class:`chrono.DateTime`.

    Valid values for *datetime* can be:

    * string: parses date/time from a string using the set parser (defaults
      to the value of :attr:`chrono.DEFAULT_PARSER`, normally
      :class:`chrono.parser.CommonParser`)
    * **True**: sets the date/time to the current date
    * integer: assumes input is a UNIX timestamp, sets date/time accordingly
    * :class:`chrono.DateTime`: sets date/time from another DateTime object
    * :class:`datetime.datetime`: sets date/time from a
      :class:`datetime.datetime` object
    * :class:`time.struct_time`: sets date/time from a
      :class:`time.struct_time` object
    * **None**: creates a date/time with empty attributes
    * **False**: creates a date/time with empty attributes

    The class can also be initialized using the keyword arguments
    *year*, *month*, *day*, *hour*, *minute*, and *second*::

        Date(year=2000, month=10, day=16, hour=16, minute=27, second=43)

    If both *datetime* and keywords are specified, *datetime* takes
    precedence.

    *parser* determines which parser to use for parsing dates and times
    from strings. By default the value of :attr:`chrono.DEFAULT_PARSER` is
    used - normally :class:`chrono.parser.CommonParser`, which supports the
    most common date and time formats. See :mod:`chrono.parser` for a list of
    available parsers.

    *calendar* determines which calendar to use for calendar operations.
    By default the value of :attr:`chrono.DEFAULT_CALENDAR` is used - normally
    :class:`chrono.calendar.ISOCalendar`. See
    :mod:`chrono.calendar` for a list of available calendars.
    """

    def __cmp__(self, other):

        if not isinstance(other, DateTime):
            other = DateTime(other)

        c = date.Date.__cmp__(self, other)

        if c > 0:
            return 1

        elif c < 0:
            return -1

        return time.Time.__cmp__(self, other)

    def __init__(self, datetime=None, parser=None, calendar=None, **kwargs):

        self.parser = parser or chrono.DEFAULT_PARSER
        self.calendar = calendar or chrono.DEFAULT_CALENDAR

        if isinstance(datetime, str):
            self.set_string(datetime)

        elif datetime is True:
            self.set_now()

        elif isinstance(datetime, int):
            self.set_unix(datetime)

        elif isinstance(datetime, DateTime):
            self.set(
                datetime.year, datetime.month, datetime.day,
                datetime.hour, datetime.minute, datetime.second
            )

        elif isinstance(datetime, date.Date):
            self.set(datetime.year, datetime.month, datetime.day, 0, 0, 0)

        elif isinstance(datetime, datetimemod.datetime):
            self.set_datetime(datetime)

        elif isinstance(datetime, timemod.struct_time):
            self.set_struct_time(datetime)

        elif "year" in kwargs or "month" in kwargs or "day" in kwargs or \
            "hour" in kwargs or "minute" in kwargs or "second" in kwargs:

            self.set(
                kwargs.get("year"), kwargs.get("month"), kwargs.get("day"),
                kwargs.get("hour"), kwargs.get("minute"), kwargs.get("second")
            )

        elif datetime is False:
            pass

        elif datetime is None:
            pass

        else:
            raise TypeError("Invalid type for DateTime parameter")

    def __repr__(self):

        args = []

        if self.year != None:
            args.append("year={0}".format(self.year))

        if self.month != None:
            args.append("month={0}".format(self.month))

        if self.day != None:
            args.append("day={0}".format(self.day))

        if self.hour != None:
            args.append("hour={0}".format(self.hour))

        if self.minute != None:
            args.append("minute={0}".format(self.minute))

        if self.second != None:
            args.append("second={0}".format(self.second))

        return "chrono.DateTime({0})".format(", ".join(args))

    def __setattr__(self, name, value):

        if value is None:
            object.__setattr__(self, name, value)

        elif name in ("minute", "second"):
            time.Time.__setattr__(self, name, value)

        elif name == "hour":

            day = self.day or 1

            while value >= 24:
                value -= 24
                day += 1

            while value < 0:
                value += 24
                day -= 1

            # set day, but only if already set
            object.__setattr__(self, "day", self.day and day or self.day)

            object.__setattr__(self, "hour", value)

        else:
            date.Date.__setattr__(self, name, value)

    def __str__(self):

        try:
            return self.get_string()

        except error.NoDateTimeError:
            return ""

    def assert_set(self):
        """
        Makes sure the object has a full date set, ie the attributes
        :attr:`chrono.DateTime.year`, :attr:`chrono.DateTime.month`,
        :attr:`chrono.DateTime.day`, :attr:`chrono.DateTime.hour`,
        :attr:`chrono.DateTime.minute`, and :attr:`chrono.DateTime.second`
        are not **None**

        Raises :exc:`chrono.error.NoDateTimeError` on missing attributes.
        """

        date.Date.assert_set(self)
        time.Time.assert_set(self)

    def clear(self):
        """
        Clears the date/time, by setting :attr:`chrono.DateTime.year`,
        :attr:`chrono.DateTime.month`, :attr:`chrono.DateTime.day`,
        :attr:`chrono.DateTime.hour`, :attr:`chrono.DateTime.minute`,
        and :attr:`chrono.DateTime.second` to **None**.
        """

        date.Date.clear(self)
        time.Time.clear(self)

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
            template, self.year, self.month, self.day,
            self.hour, self.minute, self.second
        )

    def get(self):
        """
        Returns the datetime as a tuple of year, month, day, hour, minute,
        and second.

        Raises :exc:`chrono.error.NoDateTimeError` on missing datetime data.
        """

        self.assert_set()

        return (
            self.year, self.month, self.day,
            self.hour, self.minute, self.second
        )

    def get_datetime(self):
        """
        Returns a :class:`datetime.datetime` instance based on the date/time.

        Raises :exc:`chrono.error.NoDateTimeError` on missing date data.
        """

        self.assert_set()

        return datetimemod.datetime(
            self.year, self.month, self.day,
            self.hour, self.minute, self.second
        )

    def get_julian(self):
        """
        Returns the julian day number for the datetime.

        Raises :exc:`chrono.error.NoDateTimeError` on missing date data.
        """

        self.assert_set()

        return date.Date.get_julian(self) + time.Time.get_julian(self)

    def get_string(self):
        """
        Returns a string representation (*yyyy-mm-dd hh:mm:ss*) of the
        date/time.

        Raises :exc:`chrono.error.NoDateTimeError` on missing date/time data.
        """

        return self.format("$0year-$0month-$0day $0hour:$0minute:$0second")

    def is_set(self):
        """
        Returns **True** if a date is set, ie if the attributes
        :attr:`chrono.DateTime.year`, :attr:`chrono.DateTime.month`,
        :attr:`chrono.DateTime.day`, :attr:`chrono.DateTime.hour`,
        :attr:`chrono.DateTime.minute`, and :attr:`chrono.DateTime.second`
        are not **None**, otherwise returns **False**.
        """

        return date.Date.is_set(self) and time.Time.is_set(self)

    def set(self, year, month, day, hour, minute, second):
        """
        Sets the date.

        Raises an appropriate subclass of :exc:`chrono.error.DateTimeError`
        for invalid values.
        """

        year = utility.int_year(year)
        month = utility.int_month(month)
        day = utility.int_day(day)
        hour = utility.int_hour(hour)
        minute = utility.int_minute(minute)
        second = utility.int_second(second)

        self.calendar.validate(year, month, day)
        clock.Clock.validate(hour, minute, second)

        self.clear()

        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    def set_datetime(self, datetime):
        """
        Sets the date from a :class:`datetime.datetime` object.
        """

        self.set(
            datetime.year, datetime.month, datetime.day,
            datetime.hour, datetime.minute, datetime.second
        )

    def set_julian(self, julian):
        """
        Sets the datetime from a julian day number.

        Raises :exc:`chrono.error.DayError` or
        :exc:`chrono.error.TimeError` on invalid julian day.
        """

        year, month, day = self.calendar.julian_to_date(julian)
        hour, minute, second = clock.Clock.julian_to_time(julian)

        self.set(year, month, day, hour, minute, second)


    def set_now(self):
        """
        Sets the datetime to the current date and time.
        """

        d = datetimemod.datetime.now()

        self.set(d.year, d.month, d.day, d.hour, d.minute, d.second)

    def set_string(self, string):
        """
        Sets the datetime from a string, parsed with the parser set in
        :attr:`chrono.DateTime.parser` - by default the parser set in
        :attr:`chrono.DEFAULT_PARSER`, normally
        :class:`chrono.parser.CommonParser`.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and an appropriate
        :exc:`chrono.error.DateTimeError` subclass for invalid date values.
        """

        year, month, date, hour, minute, second = \
            self.parser.parse_datetime(string)

        self.set(year, month, date, hour, minute, second)

    def set_struct_time(self, struct_time):
        """
        Sets the datetime from a :class:`time.struct_time` (as returned by
        various Python functions).
        """

        self.set(
            struct_time.tm_year,
            struct_time.tm_mon,
            struct_time.tm_mday,
            struct_time.tm_hour,
            struct_time.tm_min,
            struct_time.tm_sec
        )

    def set_unix(self, timestamp):
        """
        Sets the date from an integer UNIX timestamp.
        """

        dt = datetimemod.datetime.fromtimestamp(int(timestamp))

        self.set(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
