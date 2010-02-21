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


class Calendar(object):
    """
    Base calendar class, with common calendar functionality.
    """

    @classmethod
    def fullyear(cls, year):
        """
        Converts a short 2-digit year to a full 4-digit year.
        *year* will be interpreted to be in range 1930-2029.

        Raises :exc:`chrono.error.YearError` if *year* is invalid.
        """

        year = utility.int_year(year)

        if year != 0:
            cls.validate_year(year)

        if year > 99:
            return year

        elif year >= 30:
            return 1900 + year

        elif year >= 0:
            return 2000 + year

        else:
            return year

    @classmethod
    def julian(cls, year, month, day):
        """
        Converts a date to a julian day number.

        Raises :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError` or
        :exc:`chrono.error.DayError` if *year*, *month* or *day* is invalid.
        """

        year = utility.int_year(year)
        month = utility.int_month(month)
        day = utility.int_day(day)

        cls.validate(year, month, day)

        a = (14 - month) // 12
        y = year + 4800 - a
        m = month + (12 * a) - 3
        p = day + (((153 * m) + 2) // 5) + (365 * y)
        q = (y // 4) - (y // 100) + (y // 400) - 32045

        return p + q

    @classmethod
    def julian_to_date(cls, julian):
        """
        Converts a julian day number to a date, returns a tuple of year,
        month, and day.

        Raises :exc:`chrono.error.DayError` if *julian* is invalid.
        """

        try:
            julian = int(julian)

        except ValueError:
            raise error.DayError("Invalid julian day '{0}'".format(julian))

        j = julian + 32044
        g = j // 146097
        dg = j % 146097
        c = (dg // 36524 + 1) * 3 // 4
        dc = dg - c * 36524
        b = dc // 1461
        db = dc % 1461
        a = (db // 365 + 1) * 3 // 4
        da = db - a * 365
        y = g * 400 + c * 100 + b * 4 + a
        m = (da * 5 + 308) // 153 - 2
        d = da - (m + 4) * 153 // 5 + 122

        year = int(y - 4800 + (m + 2) // 12)
        month = int((m + 2) % 12 + 1)
        day = int(d + 1)

        return (year, month, day)

    @classmethod
    def leapyear(cls, year):
        """
        Returns **True** if *year* is a leap year, otherwise **False**.

        Raises :exc:`chrono.error.YearError` if *year* is invalid.
        """

        cls.validate_year(year)

        return calendar.isleap(utility.int_year(year))

    @classmethod
    def monthdays(cls, year, month):
        """
        Returns the number of days in *month*. *year* is needed to handle
        leap years.

        Raises :exc:`chrono.error.YearError` or :exc:`chrono.error.MonthError`
        if *year* or *month* is invalid.
        """

        year = utility.int_year(year)
        month = utility.int_month(month)

        cls.validate_year(year)
        cls.validate_month(month)

        return calendar.monthrange(
            utility.int_year(year),
            utility.int_month(month)
        )[1]

    @classmethod
    def monthname(cls, month, short=False):
        """
        Returns the name of *month*, according to the current system locale.
        If *short* is **True**, returns the abbreviated month name.

        Raises :exc:`chrono.error.MonthError` if *month* is invalid.
        """

        month = utility.int_month(month)

        cls.validate_month(month)

        d = datetime.date(2000, month, 1)

        return d.strftime(short and "%b" or "%B")

    @classmethod
    def ordinal(cls, year, month, day):
        """
        Returns the ordinal day for the given date.

        Raises :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError` or
        :exc:`chrono.error.DayError` if *year*, *month* or *day* is invalid.
        """

        cls.validate(year, month, day)

        ordinal = 0

        for m in range(1, utility.int_month(month)):
            ordinal += cls.monthdays(utility.int_year(year), m)

        ordinal += utility.int_day(day)

        return ordinal

    @classmethod
    def ordinal_to_date(cls, year, day):
        """
        Converts an ordinal day to a date, returned as a tuple of year,
        month, and day.

        Raises :exc:`chrono.error.YearError` or :exc:`chrono.error.DayError`
        if *year* or *day* is invalid.
        """

        day = utility.int_day(day)

        cls.validate_ordinal(year, day)

        dt = datetime.date(
            year=utility.int_year(year),
            month=1,
            day=1
        )

        if day > 1:
            dt += datetime.timedelta(days=day - 1)

        return (dt.year, dt.month, dt.day)

    @classmethod
    def validate(cls, year, month, day):
        """
        Validates a date: *year* must be in range 1-9999, *month* in range
        1-12, and *day* in range 1-31, depending on *year* and *month*.

        Raises :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`
        or :exc:`chrono.error.DayError` on invalid input.
        """

        cls.validate_year(year)
        cls.validate_month(month)

        monthdays = cls.monthdays(year, month)

        if not 1 <= utility.int_day(day) <= monthdays:
            raise error.DayError(
                "Day '{0}' not in range 1-{1} for year {2}, month {3}"
                .format(day, monthdays, year, month)
            )

    @classmethod
    def validate_month(cls, month):
        """
        Validates *month*: must be in range 1-12.

        Raises :exc:`chrono.error.MonthError` on invalid input.
        """

        if not 1 <= utility.int_month(month) <= 12:
            raise error.MonthError(
                "Month '{0}' not in range 1-12".format(month)
            )

    @classmethod
    def validate_ordinal(cls, year, day):
        """
        Validates an ordinal date: *year* must be in range 1-9999, *day* must
        be in range 1-365, or 366 if *year* is a leap year.

        Raises :exc:`chrono.error.YearError` or :exc:`chrono.error.DayError` on
        invalid input.
        """

        cls.validate_year(year)

        yeardays = cls.yeardays(year)

        if not 1 <= utility.int_day(day) <= yeardays:
            raise error.DayError(
                "Ordinal day '{0}' not in range 1-{1} for year '{2}'"
                .format(day, yeardays, year)
            )

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
    def validate_weekday(cls, day):
        """
        Validates a week day: *day* must be in range 1-7.

        Raises :exc:`chrono.error.DayError` if *day* is invalid.
        """

        if not 1 <= utility.int_day(day) <= 7:
            raise error.DayError("Weekday '{0}' not in range 1-7")

    @classmethod
    def validate_year(cls, year):
        """
        Validates *year*: must be in range 1-9999.

        Raises :exc:`chrono.error.YearError` if *year* is invalid.
        """

        if not 1 <= utility.int_year(year) <= 9999:
            raise error.YearError(
                "Year '{0}' not in range 1-9999".format(year)
            )

    @classmethod
    def week(cls, year, month, day):
        """
        Returns the week containing the given date as a tuple of year and
        week.

        Raises :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`,
        or :exc:`chrono.error.DayError` if *year*, *month*, or *day* is
        invalid.
        """

        return cls.weekdate(year, month, day)[:2]

    @classmethod
    def week_to_date(cls, year, week):
        """
        Returns the date of the first day in the given week as a tuple of
        year, month, and day.

        Raises :exc:`chrono.error.YearError` or :exc:`chrono.error.WeekError`
        if *year* or *week* is invalid.
        """

        return cls.weekdate_to_date(year, week, 1)

    @classmethod
    def weekdate(cls, year, month, day):
        """
        Returns the weekdate for the given date as a tuple with year, week,
        and weekday.

        Raises :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`,
        or :exc:`chrono.error.DayError` if *year*, *month* or *day* is
        invalid.

        .. note:: This is a placeholder method which just raises
           :exc:`NotImplementedError`, it is implemented in
           calendar-specific subclasses.
        """

        raise NotImplementedError(
            "This is a calendar-specific method to be handled in subclasses"
        )

    @classmethod
    def weekdate_to_date(cls, year, week, day):
        """
        Returns the date of the given weekdate as a tuple with year, month,
        and day.

        Raises :exc:`chrono.error.YearError`, :exc:`chrono.error.WeekError`,
        or :exc:`chrono.error.DayError` if *year*, *week* or *day* is invalid.

        .. note:: This is a placeholder method which just raises
           :exc:`NotImplementedError`, it is implemented in
           calendar-specific subclasses.
        """

        raise NotImplementedError(
            "This is a calendar-specific method to be handled in subclasses"
        )

    @classmethod
    def weekday(cls, year, month, day):
        """
        Returns the weekday of the given date.

        Raises :exc:`chrono.error.YearError`, :exc:`chrono.error.MonthError`,
        or :exc:`chrono.error.DayError` if *year*, *month*, or *day* is
        invalid.
        """

        return cls.weekdate(year, month, day)[2]

    @classmethod
    def weekdayname(cls, weekday, short=False):
        """
        Returns the weekday name of the given weekday. If *short*
        is **True**, returns the abbreviated weekday name.

        Raises :exc:`chrono.error.DayError` if *weekday* is invalid.

        .. note:: This is a placeholder method which just raises
           :exc:`NotImplementedError`, it is implemented in
           calendar-specific subclasses.
        """

        raise NotImplementedError(
            "This is a calendar-specific method to be handled in subclasses"
        )

    @classmethod
    def weeks(cls, year):
        """
        Returns the number of weeks in *year*.

        Raises :exc:`chrono.error.YearError` if *year* is invalid.

        .. note:: This is a placeholder method which just raises
           :exc:`NotImplementedError`, it is implemented in
           calendar-specific subclasses.
        """

        raise NotImplementedError(
            "This is a calendar-specific method to be handled in subclasses"
        )

    @classmethod
    def yeardays(cls, year):
        """
        Returns the number of days in *year*.

        Raises :exc:`chrono.error.YearError` if *year* is invalid.
        """

        return cls.leapyear(year) and 366 or 365
