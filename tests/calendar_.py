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

from chrono.calendar import Calendar
from chrono.calendar import ISOCalendar
import test

class CalendarTest(test.TestCase):

	def test_leap(self):
		"Calendar.leap() returns True for 2008"

		self.assertTrue(Calendar.leap(2008))

	def test_leap__not(self):
		"Calendar.leap() returns False for 2007"

		self.assertFalse(Calendar.leap(2007))

	def test_monthdays(self):
		"Calendar.monthdays() returns 31 for 2009-01"

		self.assertEquals(Calendar.monthdays(2009, 1), 31)

	def test_monthdays__april(self):
		"Calendar.monthdays() returns 30 for 2009-04"

		self.assertEquals(Calendar.monthdays(2009, 4), 30)

	def test_monthdays__february(self):
		"Calendar.monthdays() returns 28 for 2009-02"

		self.assertEquals(Calendar.monthdays(2009, 2), 28)

	def test_monthdays__february_leap(self):
		"Calendar.monthdays() returns 29 for 2008-02"

		self.assertEquals(Calendar.monthdays(2008, 2), 29)

	def test_validate(self):
		"Calendar.validate() accepts 2009-12-27"

		Calendar.validate(2009, 12, 27)

	def test_validate__2008_02_29(self):
		"Calendar.validate() accepts 2008-02-29"

		Calendar.validate(2008, 2, 29)

	def test_validate__2009_02_29(self):
		"Calendar.validate() raises ValueError for 2009-02-29"

		self.assertRaises(ValueError, Calendar.validate, 2009, 2, 29)

	def test_validate__nonnumeric(self):
		"Calendar.validate() raises TypeError for non-numeric string"

		self.assertRaises(ValueError, Calendar.validate, "abc", 12, 27)
		self.assertRaises(ValueError, Calendar.validate, 2009, "abc", 27)
		self.assertRaises(ValueError, Calendar.validate, 2009, 12, "abc")

	def test_validate__type(self):
		"Calendar.validate() raises TypeError for invalid types"

		self.assertRaises(TypeError, Calendar.validate, None, 12, 27)
		self.assertRaises(TypeError, Calendar.validate, 2009, None, 27)
		self.assertRaises(TypeError, Calendar.validate, 2009, 12, None)

	def test_validate_month(self):
		"Calendar.validate_month() accepts 7"

		Calendar.validate_month(7)

	def test_validate_month__0(self):
		"Calendar.validate_month() raises ValueError for 0"

		self.assertRaises(ValueError, Calendar.validate_month, 0)

	def test_validate_month__13(self):
		"Calendar.validate_month() raises ValueError for 13"

		self.assertRaises(ValueError, Calendar.validate_month, 13)

	def test_validate_month__nonnumeric(self):
		"Calendar.validate_month() raises TypeError for non-numeric string"

		self.assertRaises(ValueError, Calendar.validate_month, "abc")

	def test_validate_month__type(self):
		"Calendar.validate_month() raises TypeError for invalid types"

		self.assertRaises(TypeError, Calendar.validate_month, None)

	def test_validate_year(self):
		"Calendar.validate_year() accepts 2009"

		Calendar.validate_year(2009)

	def test_validate_year__0(self):
		"Calendar.validate_year() raises ValueError for 0"

		self.assertRaises(ValueError, Calendar.validate_year, 0)

	def test_validate_year__10000(self):
		"Calendar.validate_year() raises ValueError for 10000"

		self.assertRaises(ValueError, Calendar.validate_year, 10000)

	def test_validate_year__nonnumeric(self):
		"Calendar.validate_year() raises TypeError for non-numeric string"

		self.assertRaises(ValueError, Calendar.validate_year, "abc")

	def test_validate_year__type(self):
		"Calendar.validate_year() raises TypeError for invalid types"

		self.assertRaises(TypeError, Calendar.validate_year, None)

	def test_week(self):
		"Calendar.week() raises NotImplementedError"

		self.assertRaises(NotImplementedError, Calendar.week, 2009, 12, 28)

	def test_weekday(self):
		"Calendar.weekday() raises NotImplementedError"

		self.assertRaises(NotImplementedError, Calendar.weekday, 2009, 12, 28)

	def test_weeks(self):
		"Calendar.weeks() raises NotImplementedError"

		self.assertRaises(NotImplementedError, Calendar.weeks, 2009)

	def test_weekyear(self):
		"Calendar.weekyear() raises NotImplementedError"

		self.assertRaises(NotImplementedError, Calendar.weekyear, 2009, 12, 28)

	def test_yearday(self):
		"Calendar.yearday() returns 5 for 2009-01-05"

		self.assertEquals(Calendar.yearday(2009, 1, 5), 5)

	def test_yearday__last(self):
		"Calendar.yearday() returns 365 for 2009-12-31"

		self.assertEquals(Calendar.yearday(2009, 12, 31), 365)

	def test_yearday__leap(self):
		"Calendar.yearday() returns 366 for 2008-12-31"

		self.assertEquals(Calendar.yearday(2008, 12, 31), 366)

	def test_yeardays(self):
		"Calendar.yeardays() returns 365 for 2007"

		self.assertEquals(Calendar.yeardays(2007), 365)

	def test_yeardays__leap(self):
		"Calendar.yeardays() returns 366 for 2008"

		self.assertEquals(Calendar.yeardays(2008), 366)


class ISOCalendarTest(test.TestCase):

	def test__subclass(self):
		"ISOCalendar is subclass of Calendar"

		self.assertSubclass(ISOCalendar, Calendar)

	def test_week(self):
		"ISOCalendar.week() returns 29 for 2009-07-15"

		self.assertEquals(ISOCalendar.week(2009, 7, 15), 29)

	def test_week__2009_01_01(self):
		"ISOCalendar.week() returns 1 for 2009-01-01"

		self.assertEquals(ISOCalendar.week(2009, 1, 1), 1)

	def test_week__2009_12_31(self):
		"ISOCalendar.week() returns 53 for 2009-12-31"

		self.assertEquals(ISOCalendar.week(2009, 12, 31), 53)

	def test_week__2010_01_01(self):
		"ISOCalendar.week() returns 53 for 2010-01-01"

		self.assertEquals(ISOCalendar.week(2010, 1, 1), 53)

	def test_week__2010_01_04(self):
		"ISOCalendar.week() returns 1 for 2010-01-04"

		self.assertEquals(ISOCalendar.week(2010, 1, 4), 1)

	def test_week__2010_12_31(self):
		"ISOCalendar.week() returns 52 for 2010-12-31"

		self.assertEquals(ISOCalendar.week(2010, 12, 31), 52)

	def test_weekday(self):
		"ISOCalendar.weekday() returns 1 for 2009-12-28"

		self.assertEquals(ISOCalendar.weekday(2009, 12, 28), 1)

	def test_weekday__sunday(self):
		"ISOCalendar.weekday() returns 7 for 2009-12-27"

		self.assertEquals(ISOCalendar.weekday(2009, 12, 27), 7)

	def test_weeks(self):
		"ISOCalendar.weeks() returns 52 for 2008"

		self.assertEquals(ISOCalendar.weeks(2008), 52)

	def test_weeks__leap(self):
		"ISOCalendar.weeks() returns 53 for 2020"

		self.assertEquals(ISOCalendar.weeks(2020), 53)

	def test_weeks__thursday(self):
		"ISOCalendar.weeks() returns 53 for 2009"

		self.assertEquals(ISOCalendar.weeks(2009), 53)

	def test_weekyear(self):
		"ISOCalendar.weekyear() returns 2009 for 2009-07-15"

		self.assertEquals(ISOCalendar.weekyear(2009, 7, 15), 2009)

	def test_weekyear__next(self):
		"ISOCalendar.weekyear() returns 2009 for 2008-12-31"

		self.assertEquals(ISOCalendar.weekyear(2008, 12, 31), 2009)

	def test_weekyear__previous(self):
		"ISOCalendar.weekyear() returns 2009 for 2010-01-01"

		self.assertEquals(ISOCalendar.weekyear(2010, 1, 1), 2009)


if __name__ == "__main__":
	test.main()
