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
from .. import error
from .. import utility


class USClock(clock.Clock):
    """
    US 12-hour clock handling.
    """

    @classmethod
    def from_24(cls, hour):
        """
        Converts a 24-hour clock hour to 12-hour. Returns a tuple of hour and
        a boolean, which if **True** indicates PM, otherwise AM.

        Raises :exc:`chrono.error.HourError` if *hour* is invalid.
        """

        hour = utility.int_hour(hour)

        clock.Clock.validate_hour(hour)

        pm = False

        if hour >= 12:
            hour -= 12
            pm = True

        if hour == 0:
            hour = 12

        return (hour, pm)

    @classmethod
    def to_24(cls, hour, pm):
        """
        Converts a 12-hour clock hour to 24-hour. *pm* is a boolean, which if
        **True** indicates time is PM, otherwise AM. Returns the 24-hour clock
        hour.

        Raises :exc:`chrono.error.HourError` if *hour* is invalid.
        """

        hour = utility.int_hour(hour)

        cls.validate_hour(hour)

        if hour == 12:
            hour = 0

        if pm:
            hour += 12

        return hour

    @classmethod
    def validate(cls, hour, minute, second):
        """
        Validates a time: *hour* must be in range 1-12, *minute* in range
        0-59, and *second* in range 0-59.

        Raises :exc:`chrono.error.HourError`, :exc:`chrono.error.MinuteError`,
        or :exc:`chrono.error.SecondError` if *hour*, *minute*, or *second*
        is invalid.
        """

        return clock.Clock.validate(hour, minute, second)

    @classmethod
    def validate_hour(cls, hour):
        """
        Validates an hour: must be in range 1-12.

        Raises :exc:`chrono.error.HourError` if *hour* is invalid.
        """

        if not 1 <= utility.int_hour(hour) <= 12:
            raise error.HourError("Hour '{0}' not in range 1-12".format(hour))
