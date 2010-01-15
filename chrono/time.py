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

from . import clock
from . import error
from . import formatter
from . import parser
from . import utility

import datetime
import time as timemod


class Time(object):
	"""
	Valid values for *time* can be:

	* string: parses string using :attr:`chrono.Date.parser`, by default set to :class:`chrono.parser.ISOParser`
	* **True**: sets the time to the current time
	* :class:`chrono.Time`: sets time from another Time object
	* :class:`datetime.time`: sets time from a :class:`datetime.time` object
	* :class:`datetime.datetime`: sets time from a :class:`datetime.datetime` object
	* :class:`time.struct_time`: sets time from a :class:`time.struct_time` object
	* **None**: creates a time with empty attributes
	* **False**: creates a time with empty attributes

	The class can also be initialized using the keyword arguments
	*hour*, *minute*, and *second*, like this::

		Time(hour = 16, minute = 27, second = 43)

	If both *time* and keywords are specified, *time* takes precedence.
	"""

	hour = None
	"Hour number, range 0-23"

	minute = None
	"Minute number, range 0-59"

	second = None
	"Second number, range 0-59"

	def __cmp__(self, other):

		if not isinstance(other, Time):
			other = Time(other)

		if self.hour != other.hour:
			return cmp(self.hour, other.hour)

		elif self.minute != other.minute:
			return cmp(self.minute, other.minute)

		else:
			return cmp(self.second, other.second)

	def __init__(self, time = None, **kwargs):

		if isinstance(time, str):
			self.set_string(time)

		elif time is True:
			self.set_now()

		elif isinstance(time, Time):
			self.set(time.hour, time.minute, time.second)

		elif isinstance(time, datetime.time):
			self.set_datetime(time)

		elif isinstance(time, datetime.datetime):
			self.set_datetime(time)

		elif isinstance(time, timemod.struct_time):
			self.set_struct_time(time)

		elif ("hour" in kwargs or "minute" in kwargs or "second" in kwargs):
			h = kwargs.get("hour")
			m = kwargs.get("minute")
			s = kwargs.get("second")

			if h and m and s:
				self.set(h, m, s)

			else:
				self.hour = h
				self.minute = m
				self.second = s

		elif time is False:
			pass

		elif time is None:
			pass

		else:
			raise TypeError("Invalid type for Time parameter")

	def __repr__(self):

		args = []

		if self.hour != None:
			args.append("hour = {0}".format(self.hour))

		if self.minute != None:
			args.append("minute = {0}".format(self.minute))

		if self.second != None:
			args.append("second = {0}".format(self.second))

		return "chrono.Time({0})".format(", ".join(args))

	def __setattr__(self, name, value):

		# set None values directly
		if value is None:
			object.__setattr__(self, name, value)

		# normalize hour
		elif name == "hour":

			# validate hour
			if not 0 <= utility.int_hour(value) <= 23:
				raise error.HourError("Hour '{0}' not in range 0-23".format(value))

			# set the value if value
			object.__setattr__(self, name, value)

		# normalize minute
		elif name == "minute":

			# handle hour rollover
			h = self.hour or 0

			while value >= 60:
				h += 1
				value -= 60

			while value < 0:
				h -= 1
				value += 60

			# set hour, but only if already set
			if self.hour is not None:
				self.hour = h

			# set minute
			object.__setattr__(self, "minute", value)

		# normalize second
		elif name == "second":

			# handle minute rollover
			m = self.minute or 0

			while value >= 60:
				m += 1
				value -= 60

			while value < 0:
				m -= 1
				value += 60

			# set minute, but only if already set
			if self.minute is not None:
				self.minute = m

			# set second
			object.__setattr__(self, "second", value)

		# set other attributes directly
		else:
			object.__setattr__(self, name, value)

	def clear(self):
		"""
		Clears the time, by setting :attr:`hour`, :attr:`minute` and
		:attr:`second` to **None**.
		"""

		self.hour = None
		self.minute = None
		self.second = None

	def format(self, template):
		"""
		Formats the time using *template*, replacing variables as
		supported by :class:`formatter.Formatter`.
		"""

		if self.is_set():
			return formatter.Formatter(None, None, None, self.hour, self.minute, self.second).format(template)

	def get(self):
		"""
		Returns the time as a tuple of hour, minute, and second, or
		**None** if no time is set.
		"""

		if self.is_set():
			return (self.hour, self.minute, self.second)

	def get_datetime(self):
		"""
		Returns a :class:`datetime.time` instance based on the time, or
		**None** if time isn't set.
		"""

		if self.is_set():
			return datetime.time(self.hour, self.minute, self.second)

	def get_iso(self):
		"""
		Returns an ISO time (*hh:mm:ss*) representation of the time, or
		**None** if time isn't set.
		"""

		return self.format("$0hour:$0minute:$0second")

	def is_set(self):
		"""
		Returns **True** if a time is set, ie if the attributes :attr:`hour`,
		:attr:`minute`, and :attr:`second` are not **None**.
		"""

		return self.hour != None and self.minute != None and self.second != None

	def set(self, hour, minute, second):
		"""
		Sets the time.
		"""

		hour = int(hour)
		minute = int(minute)
		second = int(second)

		clock.Clock.validate(hour, minute, second)

		self.clear()

		self.hour = hour
		self.minute = minute
		self.second = second

	def set_datetime(self, datetime):
		"""
		Sets the time from a :class:`datetime.time` or :class:`datetime.datetime` object.
		"""

		self.set(datetime.hour, datetime.minute, datetime.second)

	def set_iso(self, time):
		"""
		Sets the time from an ISO time string, See :class:`chrono.parser.ISOParser`
		for valid formats.
		"""

		h, m, s = parser.ISOParser.parse_time(time)

		self.set(h, m, s)

	def set_now(self):
		"""
		Sets the time to the current time.
		"""

		t = datetime.datetime.now()

		self.set(t.hour, t.minute, t.second)

	def set_string(self, string):
		"""
		Sets the time from a string parsed with :attr:`Time.parser`.
		"""

		h, m, s = parser.ISOParser.parse_time(string)

		self.set(h, m, s)

	def set_struct_time(self, struct_time):
		"""
		Sets the time from a :class:`time.struct_time` (as returned by
		various Python functions)
		"""

		self.set(
			struct_time.tm_hour,
			struct_time.tm_min,
			struct_time.tm_sec
		)

