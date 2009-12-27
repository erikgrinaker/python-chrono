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

import calendar
import datetime
import time
from . import parser


class Date(object):
	"""
	Represents a date
	
	Valid values for *date* can be:

	* **None**: creates a date with empty attributes
	* **True**: sets the date to the current date

	The class can also be initialized using the keyword arguments
	*year*, *month*, and *day*, like this::

		Date(year = 2000, month = 10, day = 16)

	When initializing using keywords, all keywords must be specified.
	If both *date* and keywords are specified, keywords take precedence.
	"""

	day = None
	"Day number, 1 - 31 depending on month"

	month = None
	"Month number, 1 - 12"

	year = None
	"Year number, 0000 - 9999"

	def __cmp__(self, other):

		if isinstance(other, Date):
			return cmp(self.isodate(), other.isodate())

		elif isinstance(other, str):
			return cmp(self.isodate(), other)

		elif other is None:
			return cmp(self.isodate(), other)

		else:
			raise TypeError("Invalid type '{0}' for comparison".format(type(other)))

	def __init__(self, date = None, **kwargs):

		if "year" in kwargs and "month" in kwargs and "day" in kwargs:
			self.year = kwargs["year"]
			self.month = kwargs["month"]
			self.day = kwargs["day"]

		elif isinstance(date, Date) or isinstance(date, datetime.date):
			self.year = date.year
			self.month = date.month
			self.day = date.day

		elif date is True:
			self.set_now()

		elif isinstance(date, int):
			self.set_unix(date)

		elif isinstance(date, str):
			self.set_iso(date)

	def __repr__(self):

		if self.is_set():
			return "chrono.Date('{0}')".format(self.isodate())

		else:
			return "chrono.Date()"

	def __str__(self):

		return self.isodate() or ""

	def datetime(self):
		"""
		Returns a datetime.date instance based on the current date, or **None**
		if date isn't set
		"""

		if self.is_set():
			return datetime.date(self.year, self.month, self.day)

	def format(self, format):
		"""
		Formats the date, according to formatting rules for :func:`time.strftime`
		"""

		if self.is_set():
			return self.datetime().strftime(format)

	def is_set(self):
		"""
		Checks if a date is set, ie if the attributes *year*, *month*,
		and *day* are not None
		"""

		return self.year != None and self.month != None and self.day != None

	def isodate(self):
		"""
		Formats the date as an ISO date (yyyy-mm-dd)
		"""

		return self.format("%Y-%m-%d")

	def isomonth(self):
		"""
		Formats the date as an ISO month (yyyy-mm)
		"""

		return self.format("%Y-%m")

	def isoyear(self):
		"""
		Formats the date as an ISO year (yyyy)
		"""

		return self.format("%Y")

	def leap(self):
		"""
		Returns True if the date is in a leap year
		"""

		if self.is_set():
			return calendar.isleap(self.year)

	def monthdays(self):
		"""
		Returns the number of days in the set month
		"""

		if self.is_set():
			return calendar.monthrange(self.year, self.month)[1]

	def set_iso(self, date):
		"""
		Sets the date from an ISO date string (yyyy-mm-dd)

		Raises :exc: ValueError on invalid value
		"""

		self.year, self.month, self.day = parser.isodate(date)

	def set_now(self):
		"""
		Sets the date to the current date
		"""

		d = datetime.date.today()

		self.year = d.year
		self.month = d.month
		self.day = d.day

	def set_unix(self, secs):
		"""
		Sets the date from an integer UNIX timestamp
		"""

		dt = datetime.date.today()

		self.year = dt.year
		self.month = dt.month
		self.day = dt.day

	def struct_time(self):
		"""
		Returns a struct_time for the date, as expected by many Python functions
		"""

		if self.is_set():
			return time.struct_time(self.datetime.timetuple())

	def week(self):
		"""
		Returns the week number of the set date (weeks starting monday)
		"""

		if self.is_set():
			return int(self.datetime().isocalendar()[1])

	def weekday(self):
		"""
		Returns the week day of the set date (1 is Monday, 7 is Sunday)
		"""

		if self.is_set():
			return calendar.weekday(self.year, self.month, self.day) + 1

	def weekyear(self):
		"""
		Returns the year that the current week belongs to (for dates where
		the week number belongs to a different year)
		"""

		if self.is_set():
			return self.datetime().isocalendar()[0]

	def yearday(self):
		"""
		Returns the day number of the date in the set year
		"""

		if not self.is_set():
			return

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

		offset = offsets[self.month - 1]

		if self.leap():
			offset += 1

		return offset + self.day

	def yeardays(self):
		"""
		Returns the number of days in the year
		"""

		if self.is_set():
			return self.leap() and 366 or 365

