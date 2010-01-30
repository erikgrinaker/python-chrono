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

from . import calendar
from .. import error
from .. import utility

import datetime


class ISOCalendar(calendar.Calendar):
    """
    An ISO calendar, with functionality conforming to the ISO 8601 standard.

    Characteristics of the ISO calendar, compared to the Gregorian:

    * Weeks start on Monday
    * The first week of a year is the week containing the first Thursday
    """

    @classmethod
    def weekdate(cls, year, month, day):
        """
        Returns the weekdate for the given date as a tuple with year, week,
        and weekday.

        Raises :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`,
        or :exc:`chrono.error.DayError` if *year*, *month*, or *day* is
        invalid.
        """

        cls.validate(year, month, day)

        return datetime.date(
            utility.int_year(year),
            utility.int_month(month),
            utility.int_day(day)
        ).isocalendar()

    @classmethod
    def weekdate_to_date(cls, year, week, day):
        """
        Returns the date of the given weekdate as a tuple with year, month,
        and day.

        Raises :exc:`chrono.error.YearError`, :exc:`chrono.error.WeekError`,
        or :exc:`chrono.error.DayError` if *year*, *week*, or *day* is
        invalid.
        """

        cls.validate_weekdate(year, week, day)

        year = utility.int_year(year)
        week = utility.int_week(week)
        day = utility.int_day(day)

        d = datetime.date(year, 1, 4)

        if d.isoweekday() > 1:
            d -= datetime.timedelta(d.isoweekday() - 1)

        if week > 1:
            d += datetime.timedelta((week - 1) * 7)

        if day > 1:
            d += datetime.timedelta(day - 1)

        return (d.year, d.month, d.day)

    @classmethod
    def weekdayname(cls, weekday, short=False):
        """
        Returns the weekday name of the given weekday. If *short*
        is **True**, returns the abbreviated weekday name.

        Raises :exc:`chrono.error.DayError` if *weekday* is invalid.
        """

        cls.validate_weekday(weekday)

        d = datetime.date(2000, 1, 2 + utility.int_day(weekday))

        return d.strftime(short and "%a" or "%A")

    @classmethod
    def weeks(cls, year):
        """
        Returns the number of weeks in *year*.

        Raises :exc:`chrono.error.YearError` if *year* is invalid.
        """

        if cls.leapyear(year) and cls.weekday(year, 1, 1) == 3:
            return 53

        elif not cls.leapyear(year) and cls.weekday(year, 1, 1) == 4:
            return 53

        else:
            return 52
