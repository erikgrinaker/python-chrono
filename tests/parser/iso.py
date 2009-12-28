#!/usr/bin/python
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

import chrono
import unittest


class ISOParserTest(unittest.TestCase):

	def test_date(self):
		"ISOParser.date() parses proper ISO dates"

		self.assertEquals(
			(2009, 12, 27),
			chrono.ISOParser.date("2009-12-27")
		)

	def test_date__invalid_date(self):
		"ISOParser.date() raises ValueError on invalid date"

		self.assertRaises(ValueError, chrono.ISOParser.date, "2009-02-29")

	def test_date__invalid_format(self):
		"ISOParser.date() raises ValueError on invalid format"

		self.assertRaises(ValueError, chrono.ISOParser.date, "xx-yy-zz")

	def test_date__nozero(self):
		"ISOParser.date() parses dates without leading zeroes"

		self.assertEquals(
			(2009, 7, 3),
			chrono.ISOParser.date("2009-7-3")
		)


if __name__ == "__main__":
	unittest.main()
