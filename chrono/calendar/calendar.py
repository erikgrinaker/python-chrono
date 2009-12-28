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

import calendar
import datetime


class Calendar(object):
	"""
	Base calendar class, with common calendar functionality.

	All methods accept either integers or strings as parameters, and raises
	:exc:`TypeError` on invalid type for parameters, and :exc:`ValueError` on
	invalid parameter values (such as non-numeric strings or invalid dates).

	Calendar-specific (ie ISO, gregorian etc) methods will raise
	:exc:`NotImplementedError` if called directly from this base class.
	"""

	@classmethod
	def leapyear(cls, year):
		"""
		Returns **True** if *year* is a leap year.
		"""

		year = int(year)

		cls.validate_year(year)

		return calendar.isleap(year)

	@classmethod
	def monthdays(cls, year, month):
		"""
		Returns the number of days in *month*. *year* is needed
		to handle leap years.
		"""

		year = int(year)
		month = int(month)

		cls.validate_year(year)
		cls.validate_month(month)

		return calendar.monthrange(year, month)[1]

	@classmethod
	def ordinal(cls, year, month, day):
		"""
		Returns the ordinal date (day number in the year) for the given date.
		"""

		year = int(year)
		month = int(month)
		day = int(day)

		cls.validate(year, month, day)

		ordinal = 0

		for m in range(1, month):
			ordinal += cls.monthdays(year, m)

		ordinal += day

		return ordinal

	@classmethod
	def validate(cls, year, month, day):
		"""
		Validates a date: *year* must be in 1-9999 range, *month* in
		1-12 range, and day in 1-<monthdays> range.
		"""

		day = int(day)

		cls.validate_year(year)
		cls.validate_month(month)

		monthdays = cls.monthdays(year, month)

		if not 1 <= day <= monthdays:
			raise ValueError(
				"Day must be in range 1 to {0} for year {1} month {2}"
				.format(monthdays, year, month)
			)

	@classmethod
	def validate_month(cls, month):
		"""
		Validates *month*: must be in 1-12 range.
		"""

		if not 1 <= int(month) <= 12:
			raise ValueError("Month must be in range 1 - 12")

	@classmethod
	def validate_year(cls, year):
		"""
		Validates *year*: must be in 1-9999 range.
		"""

		if not 1 <= int(year) <= 9999:
			raise ValueError("Year must be in range 1 - 9999")

	@classmethod
	def week(cls, year, month, day):
		"""
		Returns the week number containing the given date.

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
	def weekyear(cls, year, month, day):
		"""
		Returns the year that "owns" the week containing the date (for
		dates where the week number might belong to a different year).

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

