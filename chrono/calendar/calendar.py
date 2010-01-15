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


class Calendar(object):
	"""
	Base calendar class, with common calendar functionality.

	Calendar-specific (ie ISO, gregorian etc) methods will raise
	:exc:`NotImplementedError` if called directly from this base class.
	"""

	@classmethod
	def leapyear(cls, year):
		"""
		Returns **True** if *year* is a leap year.
		"""

		cls.validate_year(year)

		return calendar.isleap(utility.int_year(year))

	@classmethod
	def monthdays(cls, year, month):
		"""
		Returns the number of days in *month*. *year* is needed
		to handle leap years.
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
	def ordinal(cls, year, month, day):
		"""
		Returns the ordinal date (day number in the year) for the given date.
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
		Returns a tuple of year, month, and day for the given ordinal date.
		"""

		cls.validate_ordinal(year, day)

		dt = datetime.date(
			year = utility.int_year(year),
			month = 1,
			day = 1
		)

		if day > 1:
			dt += datetime.timedelta(days = utility.int_day(day) - 1)

		return (dt.year, dt.month, dt.day)

	@classmethod
	def validate(cls, year, month, day):
		"""
		Validates a date: *year* must be in 1-9999 range, *month* in
		1-12 range, and day in 1-<monthdays> range.
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
		Validates *month*: must be in 1-12 range.
		"""

		if not 1 <= utility.int_month(month) <= 12:
			raise error.MonthError("Month {0} not in range 1-12".format(month))

	@classmethod
	def validate_ordinal(cls, year, day):
		"""
		Validates an ordinal date: *day* must be in range 1-365, or 366
		if *year* is a leap year.
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
		Validates a week: *week* must be in range 1-53, depending on *year*.

		.. note:: This is a placeholder method which just raises
		   :exc:`NotImplementedError`, it is implemented in
		   calendar-specific subclasses.
		"""

		raise NotImplementedError(
			"This is a calendar-specific method to be handled in subclasses"
		)

	@classmethod
	def validate_weekdate(cls, year, week, weekday):
		"""
		Validates a weekdate: *week* must be in range 1-53, depending on *year*,
		and *weekday* must be in range 1-7.

		.. note:: This is a placeholder method which just raises
		   :exc:`NotImplementedError`, it is implemented in
		   calendar-specific subclasses.
		"""

		raise NotImplementedError(
			"This is a calendar-specific method to be handled in subclasses"
		)

	@classmethod
	def validate_weekday(cls, day):
		"""
		Validates a week day: *day* must be in range 1-7.
		"""

		if not 1 <= utility.int_day(day) <= 7:
			raise error.DayError("Weekday '{0}' not in range 1-7")

	@classmethod
	def validate_year(cls, year):
		"""
		Validates *year*: must be in 1-9999 range.
		"""

		if not 1 <= utility.int_year(year) <= 9999:
			raise error.YearError("Year '{0}' not in range 1-9999".format(year))

	@classmethod
	def week(cls, year, month, day):
		"""
		Returns the week containing the given date as a tuple of year and week.

		.. note:: This is a placeholder method which just raises
		   :exc:`NotImplementedError`, it is implemented in
		   calendar-specific subclasses.
		"""

		raise NotImplementedError(
			"This is a calendar-specific method to be handled in subclasses"
		)

	@classmethod
	def week_to_date(cls, year, week):
		"""
		Returns the date of the first day in the given week as a tuple with
		year, month, and day.

		.. note:: This is a placeholder method which just raises
		   :exc:`NotImplementedError`, it is implemented in
		   calendar-specific subclasses.
		"""

		raise NotImplementedError(
			"This is a calendar-specific method to be handled in subclasses"
		)

	@classmethod
	def weekdate(cls, year, month, day):
		"""
		Returns the weekdate for the given date as a tuple with year, week,
		and weekday.

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
		Returns the number of days in *year* - 365 for normal years,
		366 for leap years.
		"""

		return cls.leapyear(year) and 366 or 365

