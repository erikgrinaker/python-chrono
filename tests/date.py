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
import datetime
import test


class DateTest(test.TestCase):

	def test__init(self):
		"Date.__init__() sets up Date"

		d = chrono.Date()

		self.assertNone(d.day)
		self.assertNone(d.month)
		self.assertNone(d.year)

	def test__init_integer(self):
		"Date.__init__() with integer parameter assumes UNIX timestamp"

		d = chrono.Date(1261892718)

		self.assertEquals(d.year,	2009)
		self.assertEquals(d.month,	12)
		self.assertEquals(d.day,	27)

	def test__init_iso(self):
		"Date.__init__() with string parameter assumes ISO date"

		d = chrono.Date("2009-12-27")

		self.assertEquals(d.year,	2009)
		self.assertEquals(d.month,	12)
		self.assertEquals(d.day,	27)

	def test__init_iso_invalid(self):
		"Date.__init__() with invalid string parameter raises ValueError"

		self.assertRaises(ValueError, chrono.Date, "2009-12-")

	def test__init_kwargs(self):
		"Date.__init__() accepts keyword arguments" 

		d = chrono.Date(year = 2009, month = 12, day = 27)

		self.assertEquals(d.year,	2009)
		self.assertEquals(d.month,	12)
		self.assertEquals(d.day,	27)

	def test__init_kwargs_date(self):
		"Date.__init__() uses kwargs over date"

		d = chrono.Date(1261892718, year = 2009, month = 12, day = 26)

		self.assertEquals(d.year,	2009)
		self.assertEquals(d.month,	12)
		self.assertEquals(d.day,	26)

	def test__init_kwargs_date(self):
		"Date.__init__() uses date if kwargs is partial"

		d = chrono.Date(1261892718, year = 2005, month = 8)

		self.assertEquals(d.year,	2009)
		self.assertEquals(d.month,	12)
		self.assertEquals(d.day,	27)

	def test__init_true(self):
		"Date.__init__() with True parameter uses current date"

		d = chrono.Date(True)
		dt = datetime.date.today()

		self.assertEquals(d.year,	dt.year)
		self.assertEquals(d.month,	dt.month)
		self.assertEquals(d.day,	dt.day)

	def test__repr(self):
		"Date.__repr__() shows code to recreate object"

		d = chrono.Date("2009-12-27")

		self.assertEquals(str(d),	"chrono.Date('2009-12-27')")

	def test__repr_empty(self):
		"Date.__repr__() handles empty dates"

		d = chrono.Date()

		self.assertEquals(str(d),	"chrono.Date()")

	def test_format(self):
		"Date.format() formats date according to time.strftime()"

		d = chrono.Date(1261892718)

		self.assertEquals(d.format("%Y-%m-%d"),	"2009-12-27")

	def test_format__nodate(self):
		"Date.format() returns None if no date is set"

		d = chrono.Date()

		self.assertNone(d.format("%Y-%m-%d"))

	def test_is_set(self):
		"Date.is_set() returns True if date is set"

		d = chrono.Date(True)

		self.assertTrue(d.is_set())

	def test_is_set__empty(self):
		"Date.is_set() returns False if no attributes are set"

		d = chrono.Date()

		self.assertFalse(d.is_set())

	def test_is_set__partial(self):
		"Date.is_set() returns False if only some attributes are set"

		d = chrono.Date()
		d.year = 2009
		d.day = 27

		self.assertFalse(d.is_set())

	def test_isodate(self):
		"Date.isodate() returns date in ISO format"

		d = chrono.Date(1261892718)

		self.assertEquals(d.isodate(), "2009-12-27")

	def test_isomonth(self):
		"Date.isomonth() returns month in ISO format"

		d = chrono.Date(1261892718)

		self.assertEquals(d.isomonth(), "2009-12")

	def test_isoyear(self):
		"Date.isoyear() returns month in ISO format"

		d = chrono.Date(1261892718)

		self.assertEquals(d.isoyear(), "2009")

	def test_set_integer(self):
		"Date.set_integer() sets date from UNIX timestamp"

		d = chrono.Date()
		d.set_integer(1261892718)

		self.assertEquals(d.year,	2009)
		self.assertEquals(d.month,	12)
		self.assertEquals(d.day,	27)

	def test_set_iso(self):
		"Date.set_iso() sets date from ISO date"

		d = chrono.Date()
		d.set_iso("2009-12-27")

		self.assertEquals(d.year,	2009)
		self.assertEquals(d.month,	12)
		self.assertEquals(d.day,	27)

	def test_set_iso__invalid(self):
		"Date.set_iso() raises ValueError on invalid format"

		d = chrono.Date()

		self.assertRaises(ValueError, d.set_iso, "2009-12-")

	def test_set_now(self):
		"Date.set_now() sets date to current date"

		d = chrono.Date()
		dt = datetime.date.today()

		d.set_now()

		self.assertEquals(d.year,	dt.year)
		self.assertEquals(d.month,	dt.month)
		self.assertEquals(d.day,	dt.day)


if __name__ == "__main__":
	test.main()
