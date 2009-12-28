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

from . import parser
from .. import calendar

import re


class ISOParser(parser.Parser):
	"""
	A parser for ISO 8601 date formats
	"""

	re_date = re.compile('''
		^\s*			# ignore whitespace at start
		(?P<year>\d{1,4})	# year
		-(?P<month>\d{1,2})	# month
		-(?P<day>\d{1,2})	# day
		\s*$			# ignore whitespace at end
	''', re.VERBOSE)

	re_date_compact = re.compile('''
		^\s*			# ignore whitespace at start
		(?P<year>\d{4})		# year
		(?P<month>\d{2})	# month
		(?P<day>\d{2})		# day
		\s*$			# ignore whitespace at end
	''', re.VERBOSE)

	@classmethod
	def date(cls, date):
		"""
		Parses an ISO date (*yyyy-mm-dd* or *yyyymmdd*), and returns a tuple
		with year, month, and day.
		"""

		try:
			match = cls.int(cls.regexp(cls.re_date, date))

		except ValueError:
			match = cls.int(cls.regexp(cls.re_date_compact, date))

		calendar.ISOCalendar.validate(
			match["year"],
			match["month"],
			match["day"]
		)

		return (match["year"], match["month"], match["day"])

