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

import re


RE_ISODATE = re.compile('^\s*(\d{1,4})-(\d{1,2})-(\d{1,2})\s*$')


class ParserError(ValueError):
	"""
	A parser error
	"""
	pass


def isodate(date):
	"""
	Parses an ISO date (yyyy-mm-dd), returns a tuple with year, month,
	and day
	"""

	match = RE_ISODATE.match(date)

	if not match:
		raise ParserError("Invalid ISO date '{0}'".format(date))

	return (
		int(match.group(1)),
		int(match.group(2)),
		int(match.group(3))
	)

