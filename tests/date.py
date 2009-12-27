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

		d = chrono.Date("2009-12-27")

		self.assertEquals(repr(d),	"chrono.Date('2009-12-27')")

	def test__repr_empty(self):
		"Date.__repr__() handles empty dates"

		d = chrono.Date()

		self.assertEquals(repr(d),	"chrono.Date()")

	def test__str(self):
		"Date.__str__() returns iso date"

		d = chrono.Date("2009-12-27")

		self.assertEquals(str(d),	"2009-12-27")

	def test__str_empty(self):
		"Date.__str__() handles empty dates"

		d = chrono.Date()

		self.assertEquals(str(d),	"")

	def test_datetime(self):
		"Date.datetime() returns a datetime.date instance"

		d = chrono.Date("2009-12-27")
		dt = d.datetime()

		self.assertType(dt,		datetime.date)
		self.assertEquals(dt.year,	2009)
		self.assertEquals(dt.month,	12)
		self.assertEquals(dt.day,	27)

	def test_datetime__empty(self):
		"Date.datetime() returns None for empty dates"

		d = chrono.Date()

		self.assertNone(d.datetime())

	def test_datetime__partial(self):
		"Date.datetime() returns None for partial dates"

		d = chrono.Date()
		d.month = 12
		d.day = 27

		self.assertNone(d.datetime())

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

	def test_leap(self):
		"Date.leap() returns True for 2008"

		d = chrono.Date("2008-01-01")

		self.assertTrue(d.leap())

	def test_leap__not(self):
		"Date.leap() returns False for 2007"

		d = chrono.Date("2007-01-01")

		self.assertFalse(d.leap())

	def test_monthdays(self):
		"Date.monthdays() returns 31 for 2009-01"

		d = chrono.Date("2009-01-01")

		self.assertEquals(d.monthdays(), 31)

	def test_monthdays__april(self):
		"Date.monthdays() returns 30 for 2009-04"

		d = chrono.Date("2009-04-01")

		self.assertEquals(d.monthdays(), 30)

	def test_monthdays__february(self):
		"Date.monthdays() returns 28 for 2009-02"

		d = chrono.Date("2009-02-01")

		self.assertEquals(d.monthdays(), 28)

	def test_monthdays__february_leap(self):
		"Date.monthdays() returns 29 for 2008-02"

		d = chrono.Date("2008-02-01")

		self.assertEquals(d.monthdays(), 29)

	def test_monthdays__none(self):
		"Date.monthdays() returns None for empty dates"

		d = chrono.Date()

		self.assertNone(d.monthdays())

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

	def test_set_unix(self):
		"Date.set_unix() sets date from UNIX timestamp"

		d = chrono.Date()
		d.set_unix(1261892718)

		self.assertEquals(d.year,	2009)
		self.assertEquals(d.month,	12)
		self.assertEquals(d.day,	27)

	def test_struct_time(self):
		"Date.struct_time() returns a proper struct_time"

		d = chrono.Date("2009-12-27")
		s = d.struct_time()

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

	def test_struct_time(self):
		"Date.struct_time() returns None with empty date"

		d = chrono.Date()

		self.assertNone(d.struct_time())

	def test_week(self):
		"Date.week() returns 29 for 2009-07-15"

		d = chrono.Date("2009-07-15")

		self.assertEquals(d.week(), 29)

	def test_week(self):
		"Date.week() returns 29 for 2009-07-15"

		d = chrono.Date("2009-07-15")

		self.assertEquals(d.week(), 29)

	def test_week__2009_01_01(self):
		"Date.week() returns 1 for 2009-01-01"

		d = chrono.Date("2009-01-01")

		self.assertEquals(d.week(), 1)

	def test_week__2009_12_31(self):
		"Date.week() returns 53 for 2009-12-31"

		d = chrono.Date("2009-12-31")

		self.assertEquals(d.week(), 53)

	def test_week__2010_01_01(self):
		"Date.week() returns 53 for 2010-01-01"

		d = chrono.Date("2010-01-01")

		self.assertEquals(d.week(), 53)

	def test_week__2010_01_04(self):
		"Date.week() returns 1 for 2010-01-04"

		d = chrono.Date("2010-01-04")

		self.assertEquals(d.week(), 1)

	def test_week__2010_12_31(self):
		"Date.week() returns 52 for 2010-12-31"

		d = chrono.Date("2010-12-31")

		self.assertEquals(d.week(), 52)

	def test_weekday(self):
		"Date.weekday() returns 1 for 2009-12-28"

		d = chrono.Date("2009-12-28")

		self.assertEquals(d.weekday(), 1)

	def test_weekday__none(self):
		"Date.weekday() returns None when date is empty"

		d = chrono.Date()

		self.assertNone(d.weekday())

	def test_weekday__sunday(self):
		"Date.weekday() returns 7 for 2009-12-27"

		d = chrono.Date("2009-12-27")

		self.assertEquals(d.weekday(), 7)

	def test_weekyear(self):
		"Date.weekyear() returns 2009 for 2009-07-15"

		d = chrono.Date("2009-07-15")

		self.assertEquals(d.weekyear(), 2009)

	def test_weekyear__next(self):
		"Date.weekyear() returns 2009 for 2008-12-31"

		d = chrono.Date("2008-12-31")

		self.assertEquals(d.weekyear(), 2009)

	def test_weekyear__previous(self):
		"Date.weekyear() returns 2009 for 2010-01-01"

		d = chrono.Date("2010-01-01")

		self.assertEquals(d.weekyear(), 2009)

	def test_yearday(self):
		"Date.yearday() returns 5 for 2009-01-05"

		d = chrono.Date("2009-01-05")

		self.assertEquals(d.yearday(),	5)

	def test_yearday__last(self):
		"Date.yearday() returns 365 for 2009-12-31"

		d = chrono.Date("2009-12-31")

		self.assertEquals(d.yearday(),	365)

	def test_yearday__leap(self):
		"Date.yearday() returns 366 for 2008-12-31"

		d = chrono.Date("2008-12-31")

		self.assertEquals(d.yearday(),	366)

	def test_yeardays(self):
		"Date.yeardays() returns 366 for 2008"

		d = chrono.Date("2008-01-01")

		self.assertEquals(d.yeardays(),	366)

	def test_yeardays__normal(self):
		"Date.yeardays() returns 365 for 2007"

		d = chrono.Date("2007-01-01")

		self.assertEquals(d.yeardays(),	365)


if __name__ == "__main__":
	test.main()
