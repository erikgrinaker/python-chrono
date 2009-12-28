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
	An ISO calendar, as specified in ISO 8601

	Characteristics of the ISO calendar, in relation to the Gregorian:

	* Weeks start on Monday
	* The first week of a year is the week containing the first Thursday
	"""

	@classmethod
	def week(cls, year, month, day):
		"""
		Returns the week number containing the given date
		"""

		return datetime.date(year, month, day).isocalendar()[1]

	@classmethod
	def weekday(cls, year, month, day):
		"""
		Returns the week day of the date (1 = Monday, 7 = Sunday)
		"""

		return calendar.weekday(year, month, day) + 1

	@classmethod
	def weeks(cls, year):
		"""
		Returns the number of weeks in *year*
		"""

		if cls.leap(year) and cls.weekday(year, 1, 1) == 3:
			return 53

		elif not cls.leap(year) and cls.weekday(year, 1, 1) == 4:
			return 53

		else:
			return 52

	@classmethod
	def weekyear(cls, year, month, day):
		"""
		Returns the year that "owns" the week containing the date
		(for dates where the week number might belong to a different year)
		"""

		return datetime.date(year, month, day).isocalendar()[0]

