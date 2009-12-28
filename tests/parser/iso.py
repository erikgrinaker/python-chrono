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

	def test_subclass(self):
		"ISOParser subclasses Parser"

		self.assertTrue(issubclass(chrono.parser.ISOParser, chrono.parser.parser.Parser))


class ISOParser_compactdateTest(unittest.TestCase):

	def test_invalid_date(self):
		"ISOParser.compactdate() raises ValueError on invalid date"

		self.assertRaises(ValueError, chrono.parser.ISOParser.compactdate, "20090229")

	def test_invalid_format(self):
		"ISOParser.compactdate() raises ValueError on invalid format"

		self.assertRaises(ValueError, chrono.parser.ISOParser.compactdate, "090229")

	def test_none(self):
		"ISOParser.compactdate() raises TypeError on None"

		self.assertRaises(TypeError, chrono.parser.ISOParser.compactdate, None)

	def test_parse(self):
		"ISOParser.compactdate() parses proper ISO compact dates (yyyymmdd)"

		self.assertEquals(
			chrono.parser.ISOParser.compactdate("20091227"),
			(2009, 12, 27)
		)


class ISOParser_dateTest(unittest.TestCase):

	def test_invalid_date(self):
		"ISOParser.date() raises ValueError on invalid date"

		self.assertRaises(ValueError, chrono.parser.ISOParser.date, "2009-02-29")

	def test_invalid_format(self):
		"ISOParser.date() raises ValueError on invalid format"

		self.assertRaises(ValueError, chrono.parser.ISOParser.date, "xx-yy-zz")

	def test_none(self):
		"ISOParser.date() raises TypeError on None"

		self.assertRaises(TypeError, chrono.parser.ISOParser.date, None)

	def test_nozero(self):
		"ISOParser.date() parses dates without leading zeroes (2009-7-3)"

		self.assertEquals(
			chrono.parser.ISOParser.date("2009-7-3"),
			(2009, 7, 3)
		)

	def test_parse(self):
		"ISOParser.date() parses proper ISO dates (yyyy-mm-dd)"

		self.assertEquals(
			chrono.parser.ISOParser.date("2009-12-27"),
			(2009, 12, 27)
		)


class ISOParser_yearTest(unittest.TestCase):

	def test_invalid_year(self):
		"ISOParser.year() raises ValueError on invalid year"

		self.assertRaises(ValueError, chrono.parser.ISOParser.year, "10000")

	def test_invalid_format(self):
		"ISOParser.year() raises ValueError on invalid format"

		self.assertRaises(ValueError, chrono.parser.ISOParser.year, "abc")

	def test_none(self):
		"ISOParser.year() raises TypeError on None"

		self.assertRaises(TypeError, chrono.parser.ISOParser.year, None)

	def test_parse(self):
		"ISOParser.year() parses proper ISO compact dates (yyyymmdd)"

		self.assertEquals(chrono.parser.ISOParser.year("2009"), 2009)


if __name__ == "__main__":
	unittest.main()
