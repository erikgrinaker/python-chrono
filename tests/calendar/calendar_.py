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


class Calendar_leapTest(unittest.TestCase):

	def test_leap(self):
		"Calendar.leap() returns True for 2008"

		self.assertTrue(chrono.calendar.Calendar.leap(2008))

	def test_noleap(self):
		"Calendar.leap() returns False for 2007"

		self.assertFalse(chrono.calendar.Calendar.leap(2007))


class Calendar_monthdaysTest(unittest.TestCase):

	def test_april(self):
		"Calendar.monthdays() returns 30 for 2009-04"

		self.assertEquals(chrono.calendar.Calendar.monthdays(2009, 4), 30)

	def test_february(self):
		"Calendar.monthdays() returns 28 for 2009-02"

		self.assertEquals(chrono.calendar.Calendar.monthdays(2009, 2), 28)

	def test_february_leap(self):
		"Calendar.monthdays() returns 29 for 2008-02"

		self.assertEquals(chrono.calendar.Calendar.monthdays(2008, 2), 29)

	def test_january(self):
		"Calendar.monthdays() returns 31 for 2009-01"

		self.assertEquals(chrono.calendar.Calendar.monthdays(2009, 1), 31)


class Calendar_validateTest(unittest.TestCase):

	def test_2008_02_29(self):
		"Calendar.validate() accepts 2008-02-29"

		chrono.calendar.Calendar.validate(2008, 2, 29)

	def test_2009_12_27(self):
		"Calendar.validate() accepts 2009-12-27"

		chrono.calendar.Calendar.validate(2009, 12, 27)

	def test_2009_02_29(self):
		"Calendar.validate() raises ValueError for 2009-02-29"

		self.assertRaises(ValueError, chrono.calendar.Calendar.validate, 2009, 2, 29)

	def test_nonnumeric(self):
		"Calendar.validate() raises TypeError for non-numeric string"

		self.assertRaises(ValueError, chrono.calendar.Calendar.validate, "abc", 12, 27)
		self.assertRaises(ValueError, chrono.calendar.Calendar.validate, 2009, "abc", 27)
		self.assertRaises(ValueError, chrono.calendar.Calendar.validate, 2009, 12, "abc")

	def test_none(self):
		"Calendar.validate() raises TypeError for None"

		self.assertRaises(TypeError, chrono.calendar.Calendar.validate, None, 12, 27)
		self.assertRaises(TypeError, chrono.calendar.Calendar.validate, 2009, None, 27)
		self.assertRaises(TypeError, chrono.calendar.Calendar.validate, 2009, 12, None)


class Calendar_validate_monthTest(unittest.TestCase):

	def test_0(self):
		"Calendar.validate_month() raises ValueError for 0"

		self.assertRaises(ValueError, chrono.calendar.Calendar.validate_month, 0)

	def test_13(self):
		"Calendar.validate_month() raises ValueError for 13"

		self.assertRaises(ValueError, chrono.calendar.Calendar.validate_month, 13)

	def test_july(self):
		"Calendar.validate_month() accepts 7"

		chrono.calendar.Calendar.validate_month(7)

	def test_none(self):
		"Calendar.validate_month() raises TypeError for None"

		self.assertRaises(TypeError, chrono.calendar.Calendar.validate_month, None)

	def test_nonnumeric(self):
		"Calendar.validate_month() raises TypeError for non-numeric string"

		self.assertRaises(ValueError, chrono.calendar.Calendar.validate_month, "abc")


class Calendar_validate_yearTest(unittest.TestCase):

	def test_0(self):
		"Calendar.validate_year() raises ValueError for 0"

		self.assertRaises(ValueError, chrono.calendar.Calendar.validate_year, 0)

	def test_10000(self):
		"Calendar.validate_year() raises ValueError for 10000"

		self.assertRaises(ValueError, chrono.calendar.Calendar.validate_year, 10000)

	def test_2009(self):
		"Calendar.validate_year() accepts 2009"

		chrono.calendar.Calendar.validate_year(2009)

	def test_none(self):
		"Calendar.validate_year() raises TypeError for None"

		self.assertRaises(TypeError, chrono.calendar.Calendar.validate_year, None)

	def test_nonnumeric(self):
		"Calendar.validate_year() raises TypeError for non-numeric string"

		self.assertRaises(ValueError, chrono.calendar.Calendar.validate_year, "abc")


class Calendar_weekTest(unittest.TestCase):

	def test_notimplemented(self):
		"Calendar.week() raises NotImplementedError"

		self.assertRaises(NotImplementedError, chrono.calendar.Calendar.week, 2009, 12, 28)


class Calendar_weekdayTest(unittest.TestCase):

	def test_notimplemented(self):
		"Calendar.weekday() raises NotImplementedError"

		self.assertRaises(NotImplementedError, chrono.calendar.Calendar.weekday, 2009, 12, 28)


class Calendar_weeksTest(unittest.TestCase):

	def test_notimplemented(self):
		"Calendar.weeks() raises NotImplementedError"

		self.assertRaises(NotImplementedError, chrono.calendar.Calendar.weeks, 2009)


class Calendar_weekyearTest(unittest.TestCase):

	def test_notimplemented(self):
		"Calendar.weekyear() raises NotImplementedError"

		self.assertRaises(NotImplementedError, chrono.calendar.Calendar.weekyear, 2009, 12, 28)


class Calendar_yeardayTest(unittest.TestCase):

	def test_2009_01_05(self):
		"Calendar.yearday() returns 5 for 2009-01-05"

		self.assertEquals(chrono.calendar.Calendar.yearday(2009, 1, 5), 5)

	def test_last(self):
		"Calendar.yearday() returns 365 for 2009-12-31"

		self.assertEquals(chrono.calendar.Calendar.yearday(2009, 12, 31), 365)

	def test_leap(self):
		"Calendar.yearday() returns 366 for 2008-12-31"

		self.assertEquals(chrono.calendar.Calendar.yearday(2008, 12, 31), 366)


class Calendar_yeardaysTest(unittest.TestCase):

	def test_2007(self):
		"Calendar.yeardays() returns 365 for 2007"

		self.assertEquals(chrono.calendar.Calendar.yeardays(2007), 365)

	def test_2008(self):
		"Calendar.yeardays() returns 366 for 2008"

		self.assertEquals(chrono.calendar.Calendar.yeardays(2008), 366)


if __name__ == "__main__":
	unittest.main()
