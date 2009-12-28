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
import time


class DateTest(test.TestCase):

	def test__cmp_equal(self):
		"Date.__cmp__() handles equality"

		self.assertTrue(chrono.Date("2009-12-27") == chrono.Date("2009-12-27"))

	def test__cmp_gt(self):
		"Date.__cmp__() handles > comparison"

		self.assertTrue(chrono.Date("2009-12-28") > chrono.Date("2009-12-27"))

	def test__cmp_lt(self):
		"Date.__cmp__() handles < comparison"

		self.assertTrue(chrono.Date("2009-12-26") < chrono.Date("2009-12-27"))

	def test__cmp_none_equal(self):
		"Date.__cmp__() handles equality with None"

		self.assertTrue(chrono.Date() == None)

	def test__cmp_none_gt(self):
		"Date.__cmp__() handles > comparison with None"

		self.assertTrue(chrono.Date("2009-12-28") > None)

	def test__cmp_none_lt(self):
		"Date.__cmp__() handles < comparison with None"

		self.assertFalse(chrono.Date() < None)

	def test__cmp_str_equal(self):
		"Date.__cmp__() handles equality with strings"

		self.assertTrue(chrono.Date("2009-12-27") == "2009-12-27")

	def test__cmp_str_gt(self):
		"Date.__cmp__() handles > comparison with strings"

		self.assertTrue(chrono.Date("2009-12-28") > "2009-12-27")

	def test__cmp_str_lt(self):
		"Date.__cmp__() handles < comparison with strings"

		self.assertTrue(chrono.Date("2009-12-26") < "2009-12-27")

	def test__init(self):
		"Date.__init__() sets up Date"

		d = chrono.Date()

		self.assertNone(d.day)
		self.assertNone(d.month)
		self.assertNone(d.year)

	def test__init_date(self):
		"Date.__init__() with Date instance parameter copies attributes"

		d = chrono.Date(chrono.Date("2009-12-27"))

		self.assertEquals(d.year,	2009)
		self.assertEquals(d.month,	12)
		self.assertEquals(d.day,	27)

	def test__init_datetime_date(self):
		"Date.__init__() with datetime.date instance parameter copies attributes"

		d = chrono.Date(datetime.date(2009, 12, 27))

		self.assertEquals(d.year,	2009)
		self.assertEquals(d.month,	12)
		self.assertEquals(d.day,	27)

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

		self.assertEquals(repr(chrono.Date("2009-12-27")), "chrono.Date('2009-12-27')")

	def test__repr_empty(self):
		"Date.__repr__() handles empty dates"

		self.assertEquals(repr(chrono.Date()), "chrono.Date()")

	def test__str(self):
		"Date.__str__() returns iso date"

		self.assertEquals(str(chrono.Date("2009-12-27")), "2009-12-27")

	def test__str_empty(self):
		"Date.__str__() handles empty dates"

		self.assertEquals(str(chrono.Date()), "")

	def test_format(self):
		"Date.format() formats date according to time.strftime()"

		self.assertEquals(chrono.Date(1261892718).format("%Y-%m-%d"), "2009-12-27")

	def test_format__nodate(self):
		"Date.format() returns None if no date is set"

		self.assertNone(chrono.Date().format("%Y-%m-%d"))

	def test_get_datetime(self):
		"Date.get_datetime() returns a datetime.date instance"

		dt = chrono.Date("2009-12-27").get_datetime()

		self.assertType(dt,		datetime.date)
		self.assertEquals(dt.year,	2009)
		self.assertEquals(dt.month,	12)
		self.assertEquals(dt.day,	27)

	def test_get_datetime__empty(self):
		"Date.get_datetime() returns None for empty dates"

		self.assertNone(chrono.Date().get_datetime())

	def test_get_datetime__partial(self):
		"Date.get_datetime() returns None for partial dates"

		d = chrono.Date()
		d.month = 12
		d.day = 27

		self.assertNone(d.get_datetime())

	def test_iso(self):
		"Date.get_iso() returns date in ISO format"

		self.assertEquals(chrono.Date("2009-12-27").get_iso(), "2009-12-27")

	def test_get_iso_month(self):
		"Date.get_iso_month() returns month in ISO format"

		self.assertEquals(chrono.Date("2009-12-27").get_iso_month(), "2009-12")

	def test_get_iso_year(self):
		"Date.get_iso_year() returns month in ISO format"

		self.assertEquals(chrono.Date("2009-12-27").get_iso_year(), "2009")

	def test_get_struct_time(self):
		"Date.get_struct_time() returns a proper struct_time"

		s = chrono.Date("2009-12-27").get_struct_time()

		self.assertType(s,		time.struct_time)
		self.assertEquals(s.tm_year,	2009)
		self.assertEquals(s.tm_mon,	12)
		self.assertEquals(s.tm_mday,	27)
		self.assertEquals(s.tm_hour,	0)
		self.assertEquals(s.tm_min,	0)
		self.assertEquals(s.tm_sec,	0)
		self.assertEquals(s.tm_wday,	6)
		self.assertEquals(s.tm_yday,	361)
		self.assertEquals(s.tm_isdst,	-1)

	def test_get_struct_time__none(self):
		"Date.get_struct_time() returns None with empty date"

		self.assertNone(chrono.Date().get_struct_time())

	def test_get_unix(self):
		"Date.get_unix() returns unix timestamp"

		self.assertEquals(chrono.Date("2009-12-27").get_unix(), 1261846800)

	def test_get_unix__none(self):
		"Date.get_unix() returns None for empty date"

		self.assertNone(chrono.Date().get_unix())

	def test_is_set(self):
		"Date.is_set() returns True if date is set"

		self.assertTrue(chrono.Date(True).is_set())

	def test_is_set__empty(self):
		"Date.is_set() returns False if no attributes are set"

		self.assertFalse(chrono.Date().is_set())

	def test_is_set__partial(self):
		"Date.is_set() returns False if only some attributes are set"

		d = chrono.Date()
		d.year = 2009
		d.day = 27

		self.assertFalse(d.is_set())

	def test_leap(self):
		"Date.leap() returns True for 2008"

		self.assertTrue(chrono.Date("2008-01-01").leap())

	def test_monthdays(self):
		"Date.monthdays() returns 29 for 2008-02"

		self.assertEquals(chrono.Date("2008-02-01").monthdays(), 29)

	def test_set_iso(self):
		"Date.set_iso() sets date from ISO date"

		d = chrono.Date()
		d.set_iso("2009-12-27")

		self.assertEquals(d.year,	2009)
		self.assertEquals(d.month,	12)
		self.assertEquals(d.day,	27)

	def test_set_iso__invalid(self):
		"Date.set_iso() raises ValueError on invalid format"

		self.assertRaises(ValueError, chrono.Date().set_iso, "2009-12-")

	def test_set_now(self):
		"Date.set_now() sets date to current date"

		d = chrono.Date()
		dt = datetime.date.today()

		d.set_now()

		self.assertEquals(d.year,	dt.year)
		self.assertEquals(d.month,	dt.month)
		self.assertEquals(d.day,	dt.day)

	def test_set_unix(self):
		"Date.set_unix() sets date from UNIX timestamp"

		d = chrono.Date()
		d.set_unix(1261892718)

		self.assertEquals(d.year,	2009)
		self.assertEquals(d.month,	12)
		self.assertEquals(d.day,	27)

	def test_week(self):
		"Date.week() returns 53 for 2010-01-01"

		self.assertEquals(chrono.Date("2010-01-01").week(), 53)

	def test_weekday(self):
		"Date.weekday() returns 7 for 2009-12-27"

		self.assertEquals(chrono.Date("2009-12-27").weekday(), 7)

	def test_weeks(self):
		"Date.weeks() returns 53 for 2009"

		self.assertEquals(chrono.Date("2009-07-15").weeks(), 53)

	def test_weekyear(self):
		"Date.weekyear() returns 2009 for 2010-01-01"

		self.assertEquals(chrono.Date("2010-01-01").weekyear(), 2009)

	def test_yearday(self):
		"Date.yearday() returns 366 for 2008-12-31"

		self.assertEquals(chrono.Date("2008-12-31").yearday(), 366)

	def test_yeardays(self):
		"Date.yeardays() returns 366 for 2008"

		self.assertEquals(chrono.Date("2008-01-01").yeardays(), 366)


if __name__ == "__main__":
	test.main()
