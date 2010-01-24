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

from .. import error
from .. import utility
from .calendar import Calendar

import calendar
import datetime


class ISOCalendar(Calendar):
    """
    An ISO calendar, with functionality conforming to the ISO 8601 standard.

    Characteristics of the ISO calendar, compared to the Gregorian:

    * Weeks start on Monday
    * The first week of a year is the week containing the first Thursday
    """

    @classmethod
    def validate_week(cls, year, week):
        """
        Validates a week: *year* must be in range 1-9999, and *week* must be
        in range 1-53, depending on *year*.

        Raises :exc:`chrono.error.YearError` or :exc:`chrono.error.WeekError`
        if *year* or *week* is invalid.
        """

        cls.validate_year(year)

        weeks = cls.weeks(year)

        if not 1 <= utility.int_week(week) <= weeks:
            raise error.WeekError(
                "Week '{0}' not in range 1-{1} for year '{2}'"
                .format(week, weeks, year)
            )

    @classmethod
    def validate_weekdate(cls, year, week, weekday):
        """
        Validates a weekdate: *year* must be in range 1-9999, *week* must be
        in range 1-53, depending on *year*, and *weekday* must be in range
        1-7.

        Raises :exc:`chrono.error.YearError`, :exc:`chrono.error.WeekError`, or
        :exc:`chrono.error.DayError` if *year*, *week*, or *weekday* is
        invalid.
        """

        cls.validate_week(year, week)
        cls.validate_weekday(weekday)

    @classmethod
    def week(cls, year, month, day):
        """
        Returns the week containing the given date as a tuple of year and
        week.

        Raises :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`,
        or :exc:`chrono.error.DayError` if *year*, *month*, or *day* is
        invalid.
        """

        cls.validate(year, month, day)

        return datetime.date(
            utility.int_year(year),
            utility.int_month(month),
            utility.int_day(day)
        ).isocalendar()[0:2]

    @classmethod
    def week_to_date(cls, year, week):
        """
        Returns the date of the first day in the given week as a tuple of
        year, month, and day.

        Raises :exc:`chrono.error.YearError` or :exc:`chrono.error.WeekError`
        if *year* or *month* is invalid.
        """

        cls.validate_week(year, week)

        week = int(week)

        d = datetime.date(utility.int_year(year), 1, 4)

        if d.isoweekday() > 1:
            d -= datetime.timedelta(d.isoweekday() - 1)

        if week > 1:
            d += datetime.timedelta((week - 1) * 7)

        return (d.year, d.month, d.day)

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

        y, m, d = cls.week_to_date(year, week)

        if day > 1:
            dt = datetime.date(y, m, d)
            dt += datetime.timedelta(utility.int_day(day) - 1)

            y = dt.year
            m = dt.month
            d = dt.day

        return (y, m, d)

    @classmethod
    def weekday(cls, year, month, day):
        """
        Returns the weekday of the given date.

        Raises :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`,
        or :exc:`chrono.error.DayError` if *year*, *month*, or *day* is
        invalid.
        """

        cls.validate(year, month, day)

        return calendar.weekday(
            utility.int_year(year),
            utility.int_month(month),
            utility.int_day(day)
        ) + 1

    @classmethod
    def weekdayname(cls, weekday, short=False):
        """
        Returns the weekday name of the given weekday. If *short*
        is **True**, returns the abbreviated weekday name.

        Raises :exc:`chrono.error.DayError` if *weekday* is invalid.
        """

        weekday = utility.int_day(weekday)

        cls.validate_weekday(weekday)

        d = datetime.date(2000, 1, 2 + weekday)

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
