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

from .calendar import Calendar

import calendar
import datetime


class ISOCalendar(Calendar):
	"""
	An ISO calendar, with functionality conforming to the ISO 8601 standard

	Characteristics of the ISO calendar, compared to the Gregorian:

	* Weeks start on Monday
	* The first week of a year is the week containing the first Thursday

	All methods accept either integers or strings as parameters, and raises
	:exc:`TypeError` on invalid type for parameters, and :exc:`ValueError` on
	invalid parameter values (such as non-numeric strings or invalid dates).
	"""

	@classmethod
	def validate_week(cls, year, week):
		"""
		Validates a week: *week* must be in range 1-53, depending on *year*.
		"""

		year = int(year)
		week = int(week)

		cls.validate_year(year)

		weeks = cls.weeks(year)

		if not 1 <= week <= weeks:
			raise ValueError(
				"Week number '{0}' not in valid range 1-{1} for year '{2}'"
				.format(week, weeks, year)
			)

	@classmethod
	def validate_weekdate(cls, year, week, weekday):
		"""
		Validates a weekdate: *week* must be in range 1-53, depending on *year*,
		and *weekday* must be in range 1-7.
		"""

		cls.validate_week(year, week)
		cls.validate_weekday(weekday)

	@classmethod
	def week(cls, year, month, day):
		"""
		Returns the ISO week number containing the given date.
		"""

		year = int(year)
		month = int(month)
		day = int(day)

		cls.validate(year, month, day)

		return datetime.date(year, month, day).isocalendar()[1]

	@classmethod
	def weekday(cls, year, month, day):
		"""
		Returns the weekday of the given date (1 = Monday, 7 = Sunday).
		"""

		year = int(year)
		month = int(month)
		day = int(day)

		cls.validate(year, month, day)

		return calendar.weekday(year, month, day) + 1

	@classmethod
	def weeks(cls, year):
		"""
		Returns the number of weeks in *year*.
		"""

		if cls.leapyear(year) and cls.weekday(year, 1, 1) == 3:
			return 53

		elif not cls.leapyear(year) and cls.weekday(year, 1, 1) == 4:
			return 53

		else:
			return 52

	@classmethod
	def weekyear(cls, year, month, day):
		"""
		Returns the year that "owns" the week containing the date
		(for dates where the week number might belong to a different year).
		"""

		year = int(year)
		month = int(month)
		day = int(day)

		cls.validate(year, month, day)

		return datetime.date(year, month, day).isocalendar()[0]

