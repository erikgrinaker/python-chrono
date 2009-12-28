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


class ISOCalendarTest(unittest.TestCase):

	def test__subclass(self):
		"ISOCalendar is subclass of Calendar"

		self.assertTrue(issubclass(chrono.calendar.ISOCalendar, chrono.calendar.Calendar))


class ISOCalendar_weekTest(unittest.TestCase):

	def test_2009_01_01(self):
		"ISOCalendar.week() returns 1 for 2009-01-01"

		self.assertEquals(chrono.calendar.ISOCalendar.week(2009, 1, 1), 1)

	def test_2009_07_15(self):
		"ISOCalendar.week() returns 29 for 2009-07-15"

		self.assertEquals(chrono.calendar.ISOCalendar.week(2009, 7, 15), 29)

	def test_2009_12_31(self):
		"ISOCalendar.week() returns 53 for 2009-12-31"

		self.assertEquals(chrono.calendar.ISOCalendar.week(2009, 12, 31), 53)

	def test_2010_01_01(self):
		"ISOCalendar.week() returns 53 for 2010-01-01"

		self.assertEquals(chrono.calendar.ISOCalendar.week(2010, 1, 1), 53)

	def test_2010_01_04(self):
		"ISOCalendar.week() returns 1 for 2010-01-04"

		self.assertEquals(chrono.calendar.ISOCalendar.week(2010, 1, 4), 1)

	def test_2010_12_31(self):
		"ISOCalendar.week() returns 52 for 2010-12-31"

		self.assertEquals(chrono.calendar.ISOCalendar.week(2010, 12, 31), 52)

	def test_invalid(self):
		"ISOCalendar.week() raises ValueError on invalid date"

		self.assertRaises(ValueError, chrono.calendar.ISOCalendar.week, 2009, 2, 29)

	def test_none(self):
		"ISOCalendar.week() raises TypeError on None input"

		self.assertRaises(TypeError, chrono.calendar.ISOCalendar.week, None, 8, 14)
		self.assertRaises(TypeError, chrono.calendar.ISOCalendar.week, 2009, None, 14)
		self.assertRaises(TypeError, chrono.calendar.ISOCalendar.week, 2009, 8, None)

	def test_nonnumeric(self):
		"ISOCalendar.week() raises ValueError on non-numeric input"

		self.assertRaises(ValueError, chrono.calendar.ISOCalendar.week, "abc", 8, 14)
		self.assertRaises(ValueError, chrono.calendar.ISOCalendar.week, 2009, "abc", 14)
		self.assertRaises(ValueError, chrono.calendar.ISOCalendar.week, 2009, 8, "abc")

	def test_string(self):
		"ISOCalendar.week() accepts string input"

		self.assertEquals(chrono.calendar.ISOCalendar.week("2009", "7", "15"), 29)


class ISOCalendar_weekdayTest(unittest.TestCase):

	def test_invalid(self):
		"ISOCalendar.weekday() raises ValueError on invalid date"

		self.assertRaises(ValueError, chrono.calendar.ISOCalendar.weekday, 2009, 2, 29)

	def test_monday(self):
		"ISOCalendar.weekday() returns 1 for 2009-12-28"

		self.assertEquals(chrono.calendar.ISOCalendar.weekday(2009, 12, 28), 1)

	def test_none(self):
		"ISOCalendar.weekday() raises TypeError on None input"

		self.assertRaises(TypeError, chrono.calendar.ISOCalendar.weekday, None, 8, 14)
		self.assertRaises(TypeError, chrono.calendar.ISOCalendar.weekday, 2009, None, 14)
		self.assertRaises(TypeError, chrono.calendar.ISOCalendar.weekday, 2009, 8, None)

	def test_nonnumeric(self):
		"ISOCalendar.weekday() raises ValueError on non-numeric input"

		self.assertRaises(ValueError, chrono.calendar.ISOCalendar.weekday, "abc", 8, 14)
		self.assertRaises(ValueError, chrono.calendar.ISOCalendar.weekday, 2009, "abc", 14)
		self.assertRaises(ValueError, chrono.calendar.ISOCalendar.weekday, 2009, 8, "abc")

	def test_string(self):
		"ISOCalendar.weekday() accepts string input"

		self.assertEquals(chrono.calendar.ISOCalendar.weekday("2009", "12", "27"), 7)

	def test_sunday(self):
		"ISOCalendar.weekday() returns 7 for 2009-12-27"

		self.assertEquals(chrono.calendar.ISOCalendar.weekday(2009, 12, 27), 7)


class ISOCalendar_weeksTest(unittest.TestCase):

	def test_2008(self):
		"ISOCalendar.weeks() returns 52 for 2008"

		self.assertEquals(chrono.calendar.ISOCalendar.weeks(2008), 52)

	def test_invalid(self):
		"ISOCalendar.weeks() raises ValueError on invalid year"

		self.assertRaises(ValueError, chrono.calendar.ISOCalendar.weeks, 10000)

	def test_leap(self):
		"ISOCalendar.weeks() returns 53 for 2020"

		self.assertEquals(chrono.calendar.ISOCalendar.weeks(2020), 53)

	def test_none(self):
		"ISOCalendar.weeks() raises TypeError on None input"

		self.assertRaises(TypeError, chrono.calendar.ISOCalendar.weeks, None)

	def test_nonnumeric(self):
		"ISOCalendar.weeks() raises ValueError on non-numeric input"

		self.assertRaises(ValueError, chrono.calendar.ISOCalendar.weeks, "abc")

	def test_string(self):
		"ISOCalendar.weeks() accepts string input"

		self.assertEquals(chrono.calendar.ISOCalendar.weeks("2008"), 52)

	def test_thursday(self):
		"ISOCalendar.weeks() returns 53 for 2009"

		self.assertEquals(chrono.calendar.ISOCalendar.weeks(2009), 53)


class ISOCalendar_weekyearTest(unittest.TestCase):

	def test_invalid(self):
		"ISOCalendar.weekyear() raises ValueError on invalid date"

		self.assertRaises(ValueError, chrono.calendar.ISOCalendar.weekyear, 2009, 2, 29)

	def test_middle(self):
		"ISOCalendar.weekyear() returns 2009 for 2009-07-15"

		self.assertEquals(chrono.calendar.ISOCalendar.weekyear(2009, 7, 15), 2009)

	def test_next(self):
		"ISOCalendar.weekyear() returns 2009 for 2008-12-31"

		self.assertEquals(chrono.calendar.ISOCalendar.weekyear(2008, 12, 31), 2009)

	def test_none(self):
		"ISOCalendar.weekyear() raises TypeError on None input"

		self.assertRaises(TypeError, chrono.calendar.ISOCalendar.weekyear, None, 12, 31)
		self.assertRaises(TypeError, chrono.calendar.ISOCalendar.weekyear, 2008, None, 31)
		self.assertRaises(TypeError, chrono.calendar.ISOCalendar.weekyear, 2008, 12, None)

	def test_nonnumeric(self):
		"ISOCalendar.weekyear() raises ValueError on non-numeric input"

		self.assertRaises(ValueError, chrono.calendar.ISOCalendar.weekyear, "abc", 12, 31)
		self.assertRaises(ValueError, chrono.calendar.ISOCalendar.weekyear, 2008, "abc", 31)
		self.assertRaises(ValueError, chrono.calendar.ISOCalendar.weekyear, 2008, 12, "abc")

	def test_previous(self):
		"ISOCalendar.weekyear() returns 2009 for 2010-01-01"

		self.assertEquals(chrono.calendar.ISOCalendar.weekyear(2010, 1, 1), 2009)

	def test_string(self):
		"ISOCalendar.weekyear() accepts string input"

		self.assertEquals(chrono.calendar.ISOCalendar.weekyear("2010", "1", "1"), 2009)


if __name__ == "__main__":
	unittest.main()