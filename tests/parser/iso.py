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


class ISOParser_compactweekTest(unittest.TestCase):

	def test_lowercase(self):
		"ISOParser.compactweek() accepts lowercase input"

		self.assertEquals(
			chrono.parser.ISOParser.compactweek("2009w12"),
			(2009, 12)
		)

	def test_invalid_format(self):
		"ISOParser.compactweek() raises ValueError on invalid format"

		self.assertRaises(ValueError, chrono.parser.ISOParser.compactweek, "2009Wxx")

	def test_invalid_compactweek(self):
		"ISOParser.compactweek() raises ValueError on invalid week"

		self.assertRaises(ValueError, chrono.parser.ISOParser.compactweek, "2008W53")

	def test_invalid_year(self):
		"ISOParser.compactweek() raises ValueError on invalid year"

		self.assertRaises(ValueError, chrono.parser.ISOParser.compactweek, "10000W12")

	def test_none(self):
		"ISOParser.compactweek() raises TypeError on None"

		self.assertRaises(TypeError, chrono.parser.ISOParser.compactweek, None)

	def test_nozero(self):
		"ISOParser.compactweek() accepts weeks without leading zeroes"

		self.assertEquals(
			chrono.parser.ISOParser.compactweek("2009W7"),
			(2009, 7)
		)

	def test_parse(self):
		"ISOParser.compactweek() parses proper compact ISO week dates (yyyyWww)"

		self.assertEquals(
			chrono.parser.ISOParser.compactweek("2009W12"),
			(2009, 12)
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


class ISOParser_monthTest(unittest.TestCase):

	def test_invalid_format(self):
		"ISOParser.month() raises ValueError on invalid format"

		self.assertRaises(ValueError, chrono.parser.ISOParser.month, "2009-xyz")

	def test_invalid_month(self):
		"ISOParser.month() raises ValueError on invalid month"

		self.assertRaises(ValueError, chrono.parser.ISOParser.month, "2009-13")

	def test_invalid_year(self):
		"ISOParser.month() raises ValueError on invalid year"

		self.assertRaises(ValueError, chrono.parser.ISOParser.month, "10000-12")

	def test_none(self):
		"ISOParser.month() raises TypeError on None"

		self.assertRaises(TypeError, chrono.parser.ISOParser.month, None)

	def test_parse(self):
		"ISOParser.month() parses proper ISO month dates (yyyy-mm)"

		self.assertEquals(
			chrono.parser.ISOParser.month("2009-12"),
			(2009, 12)
		)


class ISOParser_ordinalTest(unittest.TestCase):

	def test_invalid_ordinal(self):
		"ISOParser.ordinal() raises ValueError on invalid ordinal date"

		self.assertRaises(ValueError, chrono.parser.ISOParser.ordinal, "2009-366")

	def test_invalid_format(self):
		"ISOParser.ordinal() raises ValueError on invalid format"

		self.assertRaises(ValueError, chrono.parser.ISOParser.ordinal, "2009-abc")

	def test_none(self):
		"ISOParser.ordinal() raises TypeError on None"

		self.assertRaises(TypeError, chrono.parser.ISOParser.ordinal, None)

	def test_parse(self):
		"ISOParser.ordinal() parses proper ISO ordinal dates (yyyy-ddd)"

		self.assertEquals(
			chrono.parser.ISOParser.ordinal("2009-202"),
			(2009, 202)
		)


class ISOParser_weekTest(unittest.TestCase):

	def test_lowercase(self):
		"ISOParser.week() accepts lowercase input"

		self.assertEquals(
			chrono.parser.ISOParser.week("2009-w12"),
			(2009, 12)
		)

	def test_invalid_format(self):
		"ISOParser.week() raises ValueError on invalid format"

		self.assertRaises(ValueError, chrono.parser.ISOParser.week, "2009-Wxx")

	def test_invalid_week(self):
		"ISOParser.week() raises ValueError on invalid week"

		self.assertRaises(ValueError, chrono.parser.ISOParser.week, "2008-W53")

	def test_invalid_year(self):
		"ISOParser.week() raises ValueError on invalid year"

		self.assertRaises(ValueError, chrono.parser.ISOParser.week, "10000-W12")

	def test_none(self):
		"ISOParser.week() raises TypeError on None"

		self.assertRaises(TypeError, chrono.parser.ISOParser.week, None)

	def test_nozero(self):
		"ISOParser.week() accepts weeks without leading zeroes"

		self.assertEquals(
			chrono.parser.ISOParser.week("2009-W7"),
			(2009, 7)
		)

	def test_parse(self):
		"ISOParser.week() parses proper ISO week dates (yyyy-Www)"

		self.assertEquals(
			chrono.parser.ISOParser.week("2009-W12"),
			(2009, 12)
		)


class ISOParser_weekdateTest(unittest.TestCase):

	def test_lowercase(self):
		"ISOParser.weekdate() accepts lowercase input"

		self.assertEquals(
			chrono.parser.ISOParser.weekdate("2009-w12-4"),
			(2009, 12, 4)
		)

	def test_invalid_format(self):
		"ISOParser.weekdate() raises ValueError on invalid format"

		self.assertRaises(ValueError, chrono.parser.ISOParser.weekdate, "2009-Wxx-y")

	def test_invalid_weekdate(self):
		"ISOParser.weekdate() raises ValueError on invalid weekdate"

		self.assertRaises(ValueError, chrono.parser.ISOParser.weekdate, "2008-W52-8")

	def test_none(self):
		"ISOParser.weekdate() raises TypeError on None"

		self.assertRaises(TypeError, chrono.parser.ISOParser.weekdate, None)

	def test_nozero(self):
		"ISOParser.weekdate() accepts weekdates without leading zeroes"

		self.assertEquals(
			chrono.parser.ISOParser.weekdate("2009-W7-3"),
			(2009, 7, 3)
		)

	def test_parse(self):
		"ISOParser.weekdate() parses proper ISO weekdate dates (yyyy-Www-d)"

		self.assertEquals(
			chrono.parser.ISOParser.weekdate("2009-W12-3"),
			(2009, 12, 3)
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
