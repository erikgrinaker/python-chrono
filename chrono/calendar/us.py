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


class USCalendar(calendar.Calendar):
    """
    A US calendar, also used by Australia, Canada, New Zealand, and the UK.

    Characteristics of the US calendar:

    * Weeks start on Sunday
    * The first week of a year is the week containing January 1
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

        year = utility.int_year(year)
        month = utility.int_month(month)
        day = utility.int_day(day)

        # find the ordinal day number
        ordinal = cls.ordinal(year, month, day)

        # we want ordinal from first sunday in week 1, not from jan 1,
        # so add any extra days
        wd_jan1 = datetime.date(year, 1, 1).isoweekday() + 1

        if wd_jan1 > 7:
            wd_jan1 = 1

        ordinal += wd_jan1 - 1

        # find number of weeks between sunday of week 1 and given date,
        # add 1 since we start in week 1
        week = ordinal / 7 + 1

        # calculate weekday
        weekday = ordinal % 7

        # handle rollover
        weeks = cls.weeks(year)

        if week > weeks:
            year += 1
            week -= weeks

        return (year, week, weekday)

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

        # offset is sunday of first week in year
        wd_jan1 = datetime.date(year, 1, 1).isoweekday() + 1

        if wd_jan1 > 7:
            wd_jan1 = 1

        ordinal = - wd_jan1 + 1

        # find ordinal day from offset
        ordinal = ordinal + (week - 1) * 7 + day

        # if ordinal day is <1, it is in previous year
        if ordinal < 1:
            year -= 1
            ordinal += cls.yeardays(year)

        # convert ordinal to date
        return cls.ordinal_to_date(year, ordinal)

    @classmethod
    def weekdayname(cls, weekday, short=False):
        """
        Returns the weekday name of the given weekday. If *short*
        is **True**, returns the abbreviated weekday name.

        Raises :exc:`chrono.error.DayError` if *weekday* is invalid.
        """

        cls.validate_weekday(weekday)

        d = datetime.date(2010, 1, 2 + utility.int_day(weekday))

        return d.strftime(short and "%a" or "%A")

    @classmethod
    def weeks(cls, year):
        """
        Returns the number of weeks in *year*.

        Raises :exc:`chrono.error.YearError` if *year* is invalid.
        """

        cls.validate_year(year)

        year = utility.int_year(year)

        weekday = datetime.date(year, 1, 1).isoweekday() + 1

        if weekday > 7:
            weekday = 1

        if cls.leapyear(year) and weekday >= 6:
            return 53

        elif not cls.leapyear(year) and weekday == 7:
            return 53

        else:
            return 52
