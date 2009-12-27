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


class Date(object):
	"""
	Represents a date
	
	Valid values for *date* can be:

	* **None**: creates a date with empty attributes
	* **True**: sets the date to the current date
	"""

	day = None
	"Day number, 1 - 31 depending on month"

	month = None
	"Month number, 1 - 12"

	year = None
	"Year number, 0000 - 9999"

	def __init__(self, date = None):

		if date is True:
			self.set_now()

		elif isinstance(date, int):
			self.set_integer(date)


	def format(self, format):
		"""
		Formats the date, according to formatting rules for :func:`time.strftime`
		"""

		if self.is_set():
			return time.strftime(format, (
				self.year,
				self.month,
				self.day,
				0,
				0,
				0,
				0,
				1,
				0
			))

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

		t = time.localtime(secs)

		self.year = t.tm_year
		self.month = t.tm_mon
		self.day = t.tm_mday

