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

"""
Various utility functions used by the other modules.
"""


from __future__ import absolute_import

from . import error


def cmp(a, b):
    """
    Compares a to b, returns -1 if smaller, 0 if equal, and 1 if greater.
    """

    if a > b:
        return 1

    elif a == b:
        return 0

    else:
        return -1


def int_day(value):
    """
    Converts a day value to an integer. If *value* is invalid
    (non-numeric string, or invalid type), :exc:`chrono.error.DayError`
    is raised.
    """

    try:
        return int(value)

    except (TypeError, ValueError):
        raise error.DayError("Invalid day value '{0}'".format(value))


def int_hour(value):
    """
    Converts an hour value to an integer. If *value* is invalid
    (non-numeric string, or invalid type), :exc:`chrono.error.HourError`
    is raised.
    """

    try:
        return int(value)

    except (TypeError, ValueError):
        raise error.HourError("Invalid hour value '{0}'".format(value))


def int_minute(value):
    """
    Converts a minute value to an integer. If *value* is invalid
    (non-numeric string, or invalid type), :exc:`chrono.error.MinuteError`
    is raised.
    """

    try:
        return int(value)

    except (TypeError, ValueError):
        raise error.MinuteError("Invalid minute value '{0}'".format(value))


def int_month(value):
    """
    Converts a month value to an integer. If *value* is invalid
    (non-numeric string, or invalid type), :exc:`chrono.error.MonthError`
    is raised.
    """

    try:
        return int(value)

    except (TypeError, ValueError):
        raise error.MonthError("Invalid month value '{0}'".format(value))


def int_second(value):
    """
    Converts a second value to an integer. If *value* is invalid
    (non-numeric string, or invalid type), :exc:`chrono.error.SecondError`
    is raised.
    """

    try:
        return int(value)

    except (TypeError, ValueError):
        raise error.SecondError("Invalid second value '{0}'".format(value))


def int_week(value):
    """
    Converts a week value to an integer. If *value* is invalid
    (non-numeric string, or invalid type), :exc:`chrono.error.WeekError`
    is raised.
    """

    try:
        return int(value)

    except (TypeError, ValueError):
        raise error.WeekError("Invalid week value '{0}'".format(value))


def int_year(value):
    """
    Converts a year value to an integer. If *value* is invalid
    (non-numeric string, or invalid type), :exc:`chrono.error.YearError`
    is raised.
    """

    try:
        return int(value)

    except (TypeError, ValueError):
        raise error.YearError("Invalid year value '{0}'".format(value))


def integer(value):
    """
    Converts *value* to an integer. If *value* is a sequence or
    dictionary, members will be recursively converted to integers.
    Raises :exc:`TypeError` if *value* (or members) isn't a string or
    integer, or :exc:`ValueError` if *value* couldn't be converted.
    """

    if value is None:
        return None

    elif type(value) == list:
        value = [integer(v) for v in value]

    elif type(value) == tuple:
        value = tuple([integer(v) for v in value])

    elif type(value) == dict:
        for k, v in value.items():
            value[k] = integer(v)

    else:
        value = int(value)

    return value
