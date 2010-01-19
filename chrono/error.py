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

"""
This module contains various exceptions used by python-chrono.

.. note::

   These exceptions are imported into the main :mod:`chrono` module,
   and can therefore be referenced both via (for example)
   :class:`chrono.error.YearError` and :class:`chrono.YearError`.

The exception tree is structured as follows:

* :class:`Exception`

  * :class:`chrono.error.NoDateTimeError`

    * :class:`chrono.error.NoDateError`
    * :class:`chrono.error.NoTimeError`

  * :class:`ValueError`

    * :class:`chrono.error.DateTimeError`

      * :class:`chrono.error.DateError`

        * :class:`chrono.error.DayError`
        * :class:`chrono.error.MonthError`
        * :class:`chrono.error.WeekError`
        * :class:`chrono.error.YearError`

      * :class:`chrono.error.TimeError`

        * :class:`chrono.error.HourError`
        * :class:`chrono.error.MinuteError`
        * :class:`chrono.error.SecondError`

    * :class:`chrono.error.ParseError`
"""


class DateTimeError(ValueError):
    "Error for invalid date and/or time."
    pass


class DateError(DateTimeError):
    "Error for invalid date."
    pass


class YearError(DateError):
    "Error for invalid year."
    pass


class MonthError(DateError):
    "Error for invalid month."
    pass


class WeekError(DateError):
    "Error for invalid week."
    pass


class DayError(DateError):
    "Error for invalid day."
    pass


class TimeError(DateTimeError):
    "Error for invalid time."
    pass


class HourError(TimeError):
    "Error for invalid hour."
    pass


class MinuteError(TimeError):
    "Error for invalid minute."
    pass


class SecondError(TimeError):
    "Error for invalid second."
    pass


class NoDateTimeError(Exception):
    "Error for missing date/time data."
    pass


class NoDateError(NoDateTimeError):
    "Error for missing date."
    pass


class NoTimeError(NoDateTimeError):
    "Error for missing time."
    pass


class ParseError(ValueError):
    "Error for parse failures."
    pass
