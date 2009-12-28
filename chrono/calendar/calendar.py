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
	Base calendar class, with common calendar functionality

	Calendar-specific (ie ISO, gregorian etc) methods will raise
	NotImplementedError if called directly from this base class
	"""

	@classmethod
	def leap(cls, year):
		"""
		Returns **True** if *year* is a leap year
		"""

		return calendar.isleap(year)

	@classmethod
	def monthdays(cls, year, month):
		"""
		Returns the number of days in a given month (*year* is needed
		to handle leap years
		"""

		return calendar.monthrange(year, month)[1]

	@classmethod
	def validate(cls, year, month, day):
		"""
		Validates a date
		"""

		cls.validate_year(year)
		cls.validate_month(month)

		try:
			day = int(day)

		except TypeError:
			raise TypeError("Invalid day type, must be int or string")

		except ValueError:
			raise ValueError("Invalid day value '{0}'".format(day))

		monthdays = cls.monthdays(year, month)

		if not 1 <= day <= monthdays:
			raise ValueError("Day must be in range 1 to {0} for year {1} month {2}".format(
				monthdays,
				year,
				month
			))

	@classmethod
	def validate_month(cls, month):
		"""
		Validates a month
		"""

		try:
			month = int(month)

		except TypeError:
			raise TypeError("Invalid month type, must be int or string")

		except ValueError:
			raise ValueError("Invalid month value '{0}'".format(month))

		if not 1 <= month <= 12:
			raise ValueError("Month must be in range 1 - 12")

	@classmethod
	def validate_year(cls, year):
		"""
		Validates a year
		"""

		try:
			year = int(year)

		except TypeError:
			raise TypeError("Invalid year type, must be int or string")

		except ValueError:
			raise ValueError("Invalid year value '{0}'".format(year))

		if not 1 <= year <= 9999:
			raise ValueError("Year must be in range 1 - 9999")

	@classmethod
	def week(cls, year, month, day):
		"""
		Returns the week number containing the given date
		"""

		raise NotImplementedError()

	@classmethod
	def weekday(cls, year, month, day):
		"""
		Returns the week day of the date
		"""

		raise NotImplementedError()

	@classmethod
	def weeks(cls, year):
		"""
		Returns the number of weeks in *year*
		"""

		raise NotImplementedError()

	@classmethod
	def weekyear(cls, year, month, day):
		"""
		Returns the year that "owns" the week containing the date
		(for dates where the week number might belong to a different year)
		"""

		raise NotImplementedError()

	@classmethod
	def yearday(cls, year, month, day):
		"""
		Returns the day number in a year for a given date
		"""

		offsets = [
			0,
			31,
			59,
			90,
			120,
			151,
			181,
			212,
			243,
			273,
			304,
			334
		]

		offset = offsets[month - 1]

		if cls.leap(year):
			offset += 1

		return offset + day

	@classmethod
	def yeardays(cls, year):
		"""
		Returns the number of days in a year
		"""

		return cls.leap(year) and 366 or 365

