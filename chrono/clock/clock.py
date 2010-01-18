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

from .. import error
from .. import utility

import calendar
import datetime


class Clock(object):
    """
    Basic 24-hour clock handling.
    """

    @classmethod
    def validate(cls, hour, minute, second):
        """
        Validates a time: *hour* must be in range 0-23, *minute* in range
        0-59, and *second* in range 0-59. If *hour*, *minute*, or *second*
        is invalid, :exc:`chrono.error.HourError`,
        :exc:`chrono.error.MinuteError`, or :exc:`chrono.error.SecondError`
        will be raised.
        """

        cls.validate_hour(hour)
        cls.validate_minute(minute)
        cls.validate_second(second)

    @classmethod
    def validate_hour(cls, hour):
        """
        Validates an hour: must be in range 0-23, otherwise raises
        :exc:`chrono.error.HourError`.
        """

        if not 0 <= utility.int_hour(hour) <= 23:
            raise error.HourError("Hour '{0}' not in range 0-23".format(hour))

    @classmethod
    def validate_minute(cls, minute):
        """
        Validates a minute: must be in range 0-59, otherwise raises
        :exc:`chrono.error.MinuteError`.
        """

        if not 0 <= utility.int_minute(minute) <= 59:
            raise error.MinuteError(
                "Minute '{0}' not in range 0-59".format(minute)
            )

    @classmethod
    def validate_second(cls, second):
        """
        Validates a second: must be in range 0-59, otherwise raises
        :exc:`chrono.error.SecondError`.
        """

        if not 0 <= utility.int_second(second) <= 59:
            raise error.SecondError(
                "Second '{0}' not in range 0-59".format(second)
            )
