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

import re
import string


class Formatter(object):
	"""
	Date/time template formatter. Template variables are defined as *{name}*,
	for example: *{year}-{0month}-{0day}* is formatted as *2010-01-11*.

	Valid variable names:

	* year
	* month
	* day
	"""

	year	= None
	month	= None
	day	= None
	hour	= None
	minute	= None
	second	= None

	re_replace = re.compile('''
		\$(?:					# starting variable delimiter
		(?P<escaped>\$)			|	# escape sequence (two delimiters)
		(?P<named>[a-z0-9_]+)		|	# delimiter and identifier
		\{(?P<braced>[a-z0-9_]+)\}	|	# delimiter and braced identifier
		(?P<invalid>)				# invalid delimiter expression
		)
	''', re.VERBOSE | re.IGNORECASE)

	def __init__(self, year = None, month = None, day = None, hour = None, minute = None, second = None):

		self.year	= year
		self.month	= month
		self.day	= day
		self.hour	= hour
		self.minute	= minute
		self.second	= second

	def __re_replace(self, match):
		"Callback function for replacing variables in a template"

		# handle escaped delimiters
		if match.group("escaped") is not None:
			return "$"

		# handle invalid identifiers
		elif match.group("invalid") is not None:
			return match.group(0)

		# otherwise, find name to use
		name = match.group("named") or match.group("braced")

		# handle year formatting
		if name == "year":
			return self.year and str(self.year) or ""

		elif name == "0year":
			return self.year and str(self.year).zfill(4) or ""

		elif name == "shortyear":
			return self.year and str(self.year)[-2:] or ""

		# handle month formatting
		elif name == "month":
			return self.month and str(self.month) or ""

		elif name == "0month":
			return self.month and str(self.month).zfill(2) or ""

		# handle day formatting
		elif name == "day":
			return self.day and str(self.day) or ""

		elif name == "0day":
			return self.day and str(self.day).zfill(2) or ""

		# handle hour formatting
		elif name == "hour":
			return self.hour is not None and str(self.hour) or ""

		elif name == "0hour":
			return self.hour is not None and str(self.hour).zfill(2) or ""

		# handle minute formatting
		elif name == "minute":
			return self.minute is not None and str(self.minute) or ""

		elif name == "0minute":
			return self.minute is not None and str(self.minute).zfill(2) or ""

		# handle second formatting
		elif name == "second":
			return self.second is not None and str(self.second) or ""

		elif name == "0second":
			return self.second is not None and str(self.second).zfill(2) or ""

	def format(self, template):
		"Formats a template"

		return self.re_replace.sub(self.__re_replace, template)

