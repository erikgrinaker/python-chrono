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
	NotImplementedError if called directly in this base class
	"""

	def leap(self, year):
		"""
		Returns **True** if *year* is a leap year
		"""

		return calendar.isleap(year)

	def monthdays(self, year, month):
		"""
		Returns the number of days in a given month (*year* is needed
		to handle leap years
		"""

		return calendar.monthrange(year, month)[1]

	def week(self, year, month, day):
		"""
		Returns the week number containing the given date
		"""

		raise NotImplementedError()

	def weekday(self, year, month, day):
		"""
		Returns the week day of the date
		"""

		raise NotImplementedError()

	def weeks(self, year):
		"""
		Returns the number of weeks in *year*
		"""

		raise NotImplementedError()

	def weekyear(self, year, month, day):
		"""
		Returns the year that "owns" the week containing the date
		(for dates where the week number might belong to a different year)
		"""

		raise NotImplementedError()

	def yearday(self, year, month, day):
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

		if self.leap(year):
			offset += 1

		return offset + day

	def yeardays(self, year):
		"""
		Returns the number of days in a year
		"""

		return self.leap(year) and 366 or 365


class ISOCalendar(Calendar):
	"""
	An ISO calendar, as specified in ISO 8601

	Characteristics of the ISO calendar, in relation to the Gregorian:

	* Weeks start on Monday
	* The first week of a year is the week containing the first Thursday
	"""

	def week(self, year, month, day):
		"""
		Returns the week number containing the given date
		"""

		return datetime.date(year, month, day).isocalendar()[1]

	def weekday(self, year, month, day):
		"""
		Returns the week day of the date (1 = Monday, 7 = Sunday)
		"""

		return calendar.weekday(year, month, day) + 1

	def weeks(self, year):
		"""
		Returns the number of weeks in *year*
		"""

		if self.leap(year) and self.weekday(year, 1, 1) == 3:
			return 53

		elif not self.leap(year) and self.weekday(year, 1, 1) == 4:
			return 53

		else:
			return 52

	def weekyear(self, year, month, day):
		"""
		Returns the year that "owns" the week containing the date
		(for dates where the week number might belong to a different year)
		"""

		return datetime.date(year, month, day).isocalendar()[0]

