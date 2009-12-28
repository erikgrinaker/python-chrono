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
	An ISO date parser
	"""

	re_date		= re.compile('^\s*(\d{1,4})-(\d{1,2})-(\d{1,2})\s*$')
	re_date_compact	= re.compile('^\s*(\d{4})(\d{2})(\d{2})\s*$')

	@classmethod
	def date(cls, date):
		"""
		Parses an ISO date (yyyy-mm-dd or yyyymmdd), returns a tuple
		with year, month, and day
		"""

		match = cls.re_date.match(date)

		if not match:
			match = cls.re_date_compact.match(date)

			if not match:
				raise ValueError("Invalid ISO date '{0}'".format(date))

		year, month, day = (
			int(match.group(1)),
			int(match.group(2)),
			int(match.group(3))
		)

		calendar.ISOCalendar.validate(year, month, day)

		return (year, month, day)

