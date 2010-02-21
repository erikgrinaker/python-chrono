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
from __future__ import division

from .. import error
from .. import utility

import calendar
import datetime
import math


class Clock(object):
    """
    Basic 24-hour clock handling.
    """

    @classmethod
    def julian(cls, hour, minute, second):
        """
        Returns the julian time for the given time, as a float between
        0.0 and 1,0.

        Raises :exc:`chrono.error.HourError`, :exc:`chrono.error.MinuteError`,
        or :exc:`chrono.error.SecondError` if *hour*, *minute*, or *second*
        is invalid.
        """

        hour = utility.int_hour(hour)
        minute = utility.int_minute(minute)
        second = utility.int_second(second)

        cls.validate(hour, minute, second)

        seconds = hour * 60 * 60 + minute * 60 + second

        return seconds / 86400

    @classmethod
    def julian_to_time(cls, julian):
        """
        Converts a julian time as a float between 0 and 1 to a tuple of hour,
        minute, and second. For values > 0, only the decimal part is used.

        Raises :exc:`chrono.error.TimeError` on invalid input.
        """

        try:
            julian = float(julian)

        except ValueError:
            raise error.TimeError("Invalid julian time '{0}'".format(julian))

        julian = julian - math.floor(julian)

        julian *= 86400

        hour = math.floor(julian / 60 / 60)
        minute = math.floor(julian / 60 % 60)
        second = math.floor(julian % 60)

        return (hour, minute, second)

    @classmethod
    def validate(cls, hour, minute, second):
        """
        Validates a time: *hour* must be in range 0-23, *minute* in range
        0-59, and *second* in range 0-59.

        Raises :exc:`chrono.error.HourError`, :exc:`chrono.error.MinuteError`,
        or :exc:`chrono.error.SecondError` if *hour*, *minute*, or *second*
        is invalid.
        """

        cls.validate_hour(hour)
        cls.validate_minute(minute)
        cls.validate_second(second)

    @classmethod
    def validate_hour(cls, hour):
        """
        Validates an hour: must be in range 0-23.

        Raises :exc:`chrono.error.HourError` if *hour* is invalid.
        """

        if not 0 <= utility.int_hour(hour) <= 23:
            raise error.HourError("Hour '{0}' not in range 0-23".format(hour))

    @classmethod
    def validate_minute(cls, minute):
        """
        Validates a minute: must be in range 0-59.

        Raises :exc:`chrono.error.MinuteError` is *minute* is invalid.
        """

        if not 0 <= utility.int_minute(minute) <= 59:
            raise error.MinuteError(
                "Minute '{0}' not in range 0-59".format(minute)
            )

    @classmethod
    def validate_second(cls, second):
        """
        Validates a second: must be in range 0-59.

        Raises :exc:`chrono.error.SecondError` is *second* is invalid.
        """

        if not 0 <= utility.int_second(second) <= 59:
            raise error.SecondError(
                "Second '{0}' not in range 0-59".format(second)
            )
