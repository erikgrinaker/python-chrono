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
from . import error
from . import formatter
from . import parser
from . import utility

import datetime
import time as timemod


class Time(object):
    """
    A class for time handling. For general usage, see the description of
    :class:`chrono.Date` in the :ref:`usage` section, which works in much the
    same way as :class:`chrono.Time`.

    Valid values for *time* can be:

    * string: parses time from a string, see :class:`chrono.parser.ISOParser`
      for valid formats
    * **True**: sets the time to the current time
    * :class:`chrono.Time`: sets time from another Time object
    * :class:`datetime.datetime`: sets time from a :class:`datetime.datetime`
      object
    * :class:`datetime.time`: sets time from a :class:`datetime.time` object
    * :class:`time.struct_time`: sets time from a :class:`time.struct_time`
      object
    * **None**: creates a time with empty attributes
    * **False**: creates a time with empty attributes

    The class can also be instantiated using the keyword arguments
    *hour*, *minute*, and *second*::

        Time(hour=16, minute=27, second=43)

    If both *time* and keywords are specified, *time* takes precedence.
    """

    hour = None
    "Hour, range 0-23"

    minute = None
    "Minute, range 0-59"

    second = None
    "Second, range 0-59"

    def __cmp__(self, other):

        if not isinstance(other, Time):
            other = Time(other)

        if self.hour != other.hour:
            return cmp(self.hour, other.hour)

        elif self.minute != other.minute:
            return cmp(self.minute, other.minute)

        else:
            return cmp(self.second, other.second)

    def __init__(self, time=None, **kwargs):

        if isinstance(time, str):
            self.set_string(time)

        elif time is True:
            self.set_now()

        elif isinstance(time, Time):
            self.set(time.hour, time.minute, time.second)

        elif isinstance(time, datetime.time):
            self.set_datetime(time)

        elif isinstance(time, datetime.datetime):
            self.set_datetime(time)

        elif isinstance(time, timemod.struct_time):
            self.set_struct_time(time)

        elif ("hour" in kwargs or "minute" in kwargs or "second" in kwargs):
            self.set(
                kwargs.get("hour"), kwargs.get("minute"), kwargs.get("second")
            )

        elif time is False:
            pass

        elif time is None:
            pass

        else:
            raise TypeError("Invalid type for Time parameter")

    def __repr__(self):

        args = []

        if self.hour != None:
            args.append("hour={0}".format(self.hour))

        if self.minute != None:
            args.append("minute={0}".format(self.minute))

        if self.second != None:
            args.append("second={0}".format(self.second))

        return "chrono.Time({0})".format(", ".join(args))

    def __setattr__(self, name, value):

        # set None values directly
        if value is None:
            object.__setattr__(self, name, value)

        elif name == "hour":

            while value >= 24:
                value -= 24

            while value < 0:
                value += 24

            object.__setattr__(self, name, value)

        elif name == "minute":

            h = self.hour or 0

            while value >= 60:
                h += 1
                value -= 60

            while value < 0:
                h -= 1
                value += 60

            # set hour, but only if already set
            if self.hour is not None:
                self.hour = h

            object.__setattr__(self, "minute", value)

        elif name == "second":

            m = self.minute or 0

            while value >= 60:
                m += 1
                value -= 60

            while value < 0:
                m -= 1
                value += 60

            # set minute, but only if already set
            if self.minute is not None:
                self.minute = m

            object.__setattr__(self, "second", value)

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
        Makes sure the object has a full time set, ie the attributes
        :attr:`chrono.Time.hour`, :attr:`chrono.Time.minute`, and
        :attr:`chrono.Time.second` are not **None**, and raises
        :exc:`chrono.error.NoDateTimeError` if not.
        """

        if not self.is_set():
            raise error.NoDateTimeError(
                "Time object doesn't contain complete time data"
            )

    def clear(self):
        """
        Clears the time, by setting :attr:`chrono.Time.hour`,
        :attr:`chrono.Time.minute` and :attr:`chrono.Time.second`
        to **None**.
        """

        self.hour = None
        self.minute = None
        self.second = None

    def format(self, template):
        """
        Formats the time using *template*, replacing variables as
        supported by :class:`chrono.formatter.Formatter`.

        Raises :exc:`chrono.error.NoDateTimeError` on missing time data.
        """

        self.assert_set()

        return formatter.Formatter().format(
            template, None, None, None, self.hour, self.minute, self.second
        )

    def get(self):
        """
        Returns the time as a tuple of hour, minute, and second.

        Raises :exc:`chrono.error.NoDateTimeError` on missing time data.
        """

        self.assert_set()

        return (self.hour, self.minute, self.second)

    def get_datetime(self):
        """
        Returns a :class:`datetime.time` instance based on the time.

        Raises :exc:`chrono.error.NoDateTimeError` on missing time data.
        """

        self.assert_set()

        return datetime.time(self.hour, self.minute, self.second)

    def get_string(self):
        """
        Returns a string represenation (*hh:mm:ss*) of the time.

        Raises :exc:`chrono.error.NoDateTimeError` on missing time data.
        """

        return self.format("$0hour:$0minute:$0second")

    def is_set(self):
        """
        Returns **True** if a time is set, ie if the attributes
        :attr:`chrono.Time.hour`, :attr:`chrono.Time.minute`
        and :attr:`chrono.Time.second` are not **None**. Otherwise
        returns **False**.
        """

        return self.hour != None and self.minute != None and \
            self.second != None

    def set(self, hour, minute, second):
        """
        Sets the time.

        Raises :exc:`chrono.error.HourError`, :exc:`chrono.error.MinuteError`,
        or :exc:`chrono.error.SecondError` for invalid values.
        """

        hour = utility.int_hour(hour)
        minute = utility.int_minute(minute)
        second = utility.int_second(second)

        clock.Clock.validate(hour, minute, second)

        self.clear()

        self.hour = hour
        self.minute = minute
        self.second = second

    def set_datetime(self, datetime):
        """
        Sets the time from a :class:`datetime.time` or
        :class:`datetime.datetime` object.
        """

        self.set(datetime.hour, datetime.minute, datetime.second)

    def set_now(self):
        """
        Sets the time to the current time.
        """

        t = datetime.datetime.now()

        self.set(t.hour, t.minute, t.second)

    def set_string(self, string):
        """
        Sets the time from a string. For valid formats, see the
        :class:`chrono.parser.ISOParser` documentation.

        Raises :exc:`chrono.error.ParseError` for invalid input format,
        :exc:`TypeError` for invalid input type, and
        :exc:`chrono.error.HourError`, :exc:`chrono.error.MinuteError`,
        or :exc:`chrono.error.SecondError` for invalid time values.
        """

        h, m, s = parser.ISOParser.parse_time(string)

        self.set(h, m, s)

    def set_struct_time(self, struct_time):
        """
        Sets the time from a :class:`time.struct_time` (as returned by
        various Python functions).
        """

        self.set(
            struct_time.tm_hour,
            struct_time.tm_min,
            struct_time.tm_sec
        )
