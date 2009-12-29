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

from . import calendar
from . import parser

import datetime
import time


class Date(object):
	"""
	Valid values for *date* can be:

	* string: parses string using :attr:`chrono.Date.parser`, by default set to :class:`chrono.parser.ISOParser`
	* **True**: sets the date to the current date
	* integer: assumes input is a UNIX timestamp, sets date accordingly
	* :class:`chrono.Date`: sets date from another Date object
	* :class:`datetime.date`: sets date from a :class:`datetime.date` object
	* :class:`time.struct_time`: sets date from a :class:`time.struct_time` object
	* **None**: creates a date with empty attributes
	* **False**: creates a date with empty attributes

	The class can also be initialized using the keyword arguments
	*year*, *month*, and *day*, like this::

		Date(year = 2000, month = 10, day = 16)

	If both *date* and keywords are specified, *date* takes precedence.

	All methods will generally raise :exc:`TypeError` on invalid types for date
	input, and :exc:`ValueError` on invalid dates (such out-of-range values,
	or values which cannot be parsed to a proper value)
	"""

	calendar = calendar.ISOCalendar()
	"""
	Calendar to be used for calendar-related operations. Should be a
	subclass of :class:`chrono.calendar.Calendar`.
	"""

	parser = parser.ISOParser()
	"""
	Parser to be used for parsing strings to dates in :meth:`set_string`.
	Should be a subclass of :class:`chrono.parser.Parser`.
	"""

	day = None
	"Day number, range 1-31 depending on :attr:`month` and :attr:`year`"

	month = None
	"Month number, range 1-12"

	year = None
	"Year number, range 0001-9999"

	def __cmp__(self, other):

		if not isinstance(other, Date):
			other = Date(other)

		if self.year != other.year:
			return cmp(self.year, other.year)

		elif self.month != other.month:
			return cmp(self.month, other.month)

		else:
			return cmp(self.day, other.day)

	def __init__(self, date = None, **kwargs):

		if isinstance(date, str):
			self.set_string(date)

		elif date is True:
			self.set_now()

		elif isinstance(date, int):
			self.set_unix(date)

		elif isinstance(date, Date):
			self.set(date.year, date.month, date.day)

		elif isinstance(date, datetime.date):
			self.set_datetime(date)

		elif isinstance(date, time.struct_time):
			self.set_struct_time(date)

		elif not date and ("year" in kwargs or "month" in kwargs or "day" in kwargs):
			y = kwargs.get("year")
			m = kwargs.get("month")
			d = kwargs.get("day")

			if y and m and d:
				self.set(y, m, d)

			else:
				self.year = y
				self.month = m
				self.day = d

		elif date is False:
			pass

		elif date is None:
			pass

		else:
			raise TypeError("Invalid type for Date parameter")

	def __repr__(self):

		args = []

		if self.year:
			args.append("year = {0}".format(self.year))

		if self.month:
			args.append("month = {0}".format(self.month))

		if self.day:
			args.append("day = {0}".format(self.day))

		return "chrono.Date({0})".format(", ".join(args))

	def __str__(self):

		return self.get_iso() or ""

	def clear(self):
		"""
		Clears the date, by setting :attr:`year`, :attr:`month` and
		:attr:`day` to **None**.
		"""

		self.year	= None
		self.month	= None
		self.day	= None

	def format(self, format):
		"""
		Formats the date using the template *format*, according to the
		formatting rules for :func:`time.strftime`.
		"""

		if self.is_set():
			return self.get_datetime().strftime(format)

	def get(self):
		"""
		Returns the date as a tuple of year, month, and day, or **None**
		if no date is set.
		"""

		if self.is_set():
			return (self.year, self.month, self.day)

	def get_datetime(self):
		"""
		Returns a datetime.date instance based on the current date, or **None**
		if date isn't set.
		"""

		if self.is_set():
			return datetime.date(self.year, self.month, self.day)

	def get_iso(self):
		"""
		Returns a ISO date (*yyyy-mm-dd*) representation of the date, or None
		if date isn't set.
		"""

		return self.format("%Y-%m-%d")

	def get_iso_month(self):
		"""
		Returns a ISO month (*yyyy-mm*) representation of the date, or None
		if date isn't set.
		"""

		return self.format("%Y-%m")

	def get_iso_year(self):
		"""
		Returns a ISO year (*yyyy*) representation of the date, or None
		if date isn't set.
		"""

		return self.format("%Y")

	def get_struct_time(self):
		"""
		Returns a :class:`time.struct_time` representation of the date
		(expected as input to many Python functions), or **None** if date
		isn't set.
		"""

		if self.is_set():
			return time.struct_time(self.get_datetime().timetuple())

	def get_unix(self):
		"""
		Returns a UNIX timestamp  representation of the date, or **None**
		if not set.
		"""

		if self.is_set():
			return int(time.mktime(self.get_struct_time()))

	def is_set(self):
		"""
		Returns **True** if a date is set, ie if the attributes :attr:`year`,
		:attr:`month`, and :attr:`day` are not **None**.
		"""

		return self.year != None and self.month != None and self.day != None

	def leapyear(self):
		"""
		Returns **True** if the date is in a leap year.
		"""

		return self.is_set() and self.calendar.leapyear(self.year) or False

	def monthdays(self):
		"""
		Returns the number of days in the set month, or **None** if no
		date is set.
		"""

		if self.is_set():
			return self.calendar.monthdays(self.year, self.month)

	def ordinal(self):
		"""
		Returns the ordinal day (day number in the year) of the set date,
		or **None** if no date is set.
		"""

		if self.is_set():
			return self.calendar.ordinal(self.year, self.month, self.day)

	def set(self, year, month, day):
		"""
		Sets the date.
		"""

		year = int(year)
		month = int(month)
		day = int(day)

		self.calendar.validate(year, month, day)

		self.clear()

		self.year = year
		self.month = month
		self.day = day

	def set_datetime(self, datetime):
		"""
		Sets the date from a :class:`datetime.date` object.
		"""

		self.set(datetime.year, datetime.month, datetime.day)

	def set_iso(self, date):
		"""
		Sets the date from an ISO date string. See :class:`chrono.parser.ISOParser`
		for valid formats.
		"""

		y, m, d = parser.ISOParser.parse_date(date)

		self.set(y, m, d)

	def set_now(self):
		"""
		Sets the date to the current date
		"""

		d = datetime.date.today()

		self.set(d.year, d.month, d.day)

	def set_string(self, string):
		"""
		Sets the date from a string parsed with Date.parser
		"""

		y, m, d = self.parser.parse_date(string)

		self.set(y, m, d)

	def set_struct_time(self, struct_time):
		"""
		Sets the date from a :class:`time.struct_time` (as returned by
		various Python functions)
		"""

		self.set(
			struct_time.tm_year,
			struct_time.tm_mon,
			struct_time.tm_mday
		)

	def set_unix(self, timestamp):
		"""
		Sets the date from an integer UNIX timestamp.
		"""

		dt = datetime.date.fromtimestamp(int(timestamp))

		self.set(dt.year, dt.month, dt.day)

	def week(self):
		"""
		Returns the week of the set date as a tuple with year and week
		number, or **None** if no date is set.
		"""

		if self.is_set():
			return self.calendar.week(self.year, self.month, self.day)

	def weekdate(self):
		"""
		Returns the week date of the set date as a tuple with year,
		week, and weekday, or **None** if no date is set.
		"""

		if self.is_set():
			return self.calendar.weekdate(self.year, self.month, self.day)

	def weekday(self):
		"""
		Returns the week day of the set date, or **None** if no
		date is set.
		"""

		if self.is_set():
			return self.calendar.weekday(self.year, self.month, self.day)

	def weeks(self):
		"""
		Returns the number of weeks in the set year, or **None** if no
		date is set.
		"""

		if self.is_set():
			return self.calendar.weeks(self.year)

	def yeardays(self):
		"""
		Returns the number of days in the year, or **None** if no date
		is set.
		"""

		if self.is_set():
			return self.calendar.yeardays(self.year)

