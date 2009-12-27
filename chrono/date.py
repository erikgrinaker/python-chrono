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

		elif date is True:
			self.set_now()

		elif isinstance(date, int):
			self.set_integer(date)

		elif isinstance(date, str):
			self.set_iso(date)

	def __repr__(self):

		if self.is_set():
			return "chrono.Date('{0}')".format(self.isodate())

		else:
			return "chrono.Date()"

	def __str__(self):

		return self.isodate() or ""

	def format(self, format):
		"""
		Formats the date, according to formatting rules for :func:`time.strftime`
		"""

		if self.is_set():
			dt = datetime.date(self.year, self.month, self.day)

			return dt.strftime(format)

		else:
			return None

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

	def set_now(self):
		"""
		Sets the date to the current date
		"""

		d = datetime.date.today()

		self.year = d.year
		self.month = d.month
		self.day = d.day

	def set_integer(self, secs):
		"""
		Sets the date from an integer UNIX timestamp
		"""

		dt = datetime.date.today()

		self.year = dt.year
		self.month = dt.month
		self.day = dt.day

	def set_iso(self, date):
		"""
		Sets the date from an ISO date string (yyyy-mm-dd)

		Raises :exc: ValueError on invalid value
		"""

		self.year, self.month, self.day = parser.isodate(date)

	def struct_time(self):
		"""
		Returns a struct_time for the date, as expected by many Python functions
		"""

		if not self.is_set():
			return None

		dt = datetime.date(self.year, self.month, self.day)

		return time.struct_time(dt.timetuple())

