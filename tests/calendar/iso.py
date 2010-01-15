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


class ISOCalendar_validate_weekTest(unittest.TestCase):

	def test_invalid(self):
		"ISOCalendar.validate_week() raises WeekError for 2008-W53"

		self.assertRaises(chrono.WeekError, chrono.calendar.ISOCalendar.validate_week, 2008, 53)

	def test_leap(self):
		"ISOCalendar.validate_week() accepts 2009-W53"

		chrono.calendar.ISOCalendar.validate_week(2009, 53)

	def test_max(self):
		"ISOCalendar.validate_week() accepts 2008-W52"

		chrono.calendar.ISOCalendar.validate_week(2008, 52)

	def test_nonnumeric(self):
		"ISOCalendar.validate_week() raises proper error for non-numeric string"

		self.assertRaises(chrono.YearError, chrono.calendar.ISOCalendar.validate_week, "abc", 32)
		self.assertRaises(chrono.WeekError, chrono.calendar.ISOCalendar.validate_week, 2009, "abc")

	def test_none(self):
		"ISOCalendar.validate_week() raises proper error for None"

		self.assertRaises(chrono.YearError, chrono.calendar.ISOCalendar.validate_week, None, 32)
		self.assertRaises(chrono.WeekError, chrono.calendar.ISOCalendar.validate_week, 2009, None)

	def test_week(self):
		"ISOCalendar.validate_week() accepts 2009-W32"

		chrono.calendar.ISOCalendar.validate_week(2009, 32)

	def test_string(self):
		"ISOCalendar.validate_week() accepts string inputs"

		chrono.calendar.ISOCalendar.validate_week("2009", "32")


class ISOCalendar_validate_weekdateTest(unittest.TestCase):

	def test_invalid_week(self):
		"ISOCalendar.validate_weekdate() raises WeekError for 2008-W53-3"

		self.assertRaises(chrono.WeekError, chrono.calendar.ISOCalendar.validate_weekdate, 2008, 53, 3)

	def test_invalid_weekday(self):
		"ISOCalendar.validate_weekdate() raises DayError for 2009-W32-8"

		self.assertRaises(chrono.DayError, chrono.calendar.ISOCalendar.validate_weekdate, 2009, 32, 8)

	def test_invalid_year(self):
		"ISOCalendar.validate_weekdate() raises YearError for 10000-W32-4"

		self.assertRaises(chrono.YearError, chrono.calendar.ISOCalendar.validate_weekdate, 10000, 32, 4)

	def test_leap(self):
		"ISOCalendar.validate_weekdate() accepts 2009-W53-4"

		chrono.calendar.ISOCalendar.validate_weekdate(2009, 53, 4)

	def test_max(self):
		"ISOCalendar.validate_weekdate() accepts 2008-W52-7"

		chrono.calendar.ISOCalendar.validate_weekdate(2008, 52, 7)

	def test_nonnumeric(self):
		"ISOCalendar.validate_weekdate() raises proper error for non-numeric string"

		self.assertRaises(chrono.YearError, chrono.calendar.ISOCalendar.validate_weekdate, "abc", 32, 4)
		self.assertRaises(chrono.WeekError, chrono.calendar.ISOCalendar.validate_weekdate, 2009, "abc", 4)
		self.assertRaises(chrono.DayError, chrono.calendar.ISOCalendar.validate_weekdate, 2009, 32, "abc")

	def test_none(self):
		"ISOCalendar.validate_weekdate() raises proper error for None"

		self.assertRaises(chrono.YearError, chrono.calendar.ISOCalendar.validate_weekdate, None, 32, 4)
		self.assertRaises(chrono.WeekError, chrono.calendar.ISOCalendar.validate_weekdate, 2009, None, 4)
		self.assertRaises(chrono.DayError, chrono.calendar.ISOCalendar.validate_weekdate, 2009, 32, None)

	def test_weekdate(self):
		"ISOCalendar.validate_weekdate() accepts 2009-W32-4"

		chrono.calendar.ISOCalendar.validate_weekdate(2009, 32, 4)

	def test_string(self):
		"ISOCalendar.validate_weekdate() accepts string inputs"

		chrono.calendar.ISOCalendar.validate_weekdate("2009", "32", "4")


class ISOCalendar_weekTest(unittest.TestCase):

	def test_2009_01_01(self):
		"ISOCalendar.week() returns 2009-W01 for 2009-01-01"

		self.assertEquals(chrono.calendar.ISOCalendar.week(2009, 1, 1), (2009, 1))

	def test_2009_07_15(self):
		"ISOCalendar.week() returns 2009-W29 for 2009-07-15"

		self.assertEquals(chrono.calendar.ISOCalendar.week(2009, 7, 15), (2009, 29))

	def test_2009_12_31(self):
		"ISOCalendar.week() returns 2009-W53 for 2009-12-31"

		self.assertEquals(chrono.calendar.ISOCalendar.week(2009, 12, 31), (2009, 53))

	def test_2010_01_01(self):
		"ISOCalendar.week() returns 2009-W53 for 2010-01-01"

		self.assertEquals(chrono.calendar.ISOCalendar.week(2010, 1, 1), (2009, 53))

	def test_2010_01_04(self):
		"ISOCalendar.week() returns 2010-W01 for 2010-01-04"

		self.assertEquals(chrono.calendar.ISOCalendar.week(2010, 1, 4), (2010, 1))

	def test_2010_12_31(self):
		"ISOCalendar.week() returns 2010-W52 for 2010-12-31"

		self.assertEquals(chrono.calendar.ISOCalendar.week(2010, 12, 31), (2010, 52))

	def test_invalid(self):
		"ISOCalendar.week() raises DayError on invalid date"

		self.assertRaises(chrono.DayError, chrono.calendar.ISOCalendar.week, 2009, 2, 29)

	def test_none(self):
		"ISOCalendar.week() raises propet error on None input"

		self.assertRaises(chrono.YearError, chrono.calendar.ISOCalendar.week, None, 8, 14)
		self.assertRaises(chrono.MonthError, chrono.calendar.ISOCalendar.week, 2009, None, 14)
		self.assertRaises(chrono.DayError, chrono.calendar.ISOCalendar.week, 2009, 8, None)

	def test_nonnumeric(self):
		"ISOCalendar.week() raises proper error on non-numeric input"

		self.assertRaises(chrono.YearError, chrono.calendar.ISOCalendar.week, "abc", 8, 14)
		self.assertRaises(chrono.MonthError, chrono.calendar.ISOCalendar.week, 2009, "abc", 14)
		self.assertRaises(chrono.DayError, chrono.calendar.ISOCalendar.week, 2009, 8, "abc")

	def test_string(self):
		"ISOCalendar.week() accepts string input"

		self.assertEquals(chrono.calendar.ISOCalendar.week("2009", "7", "15"), (2009, 29))


class ISOCalendar_week_to_dateTest(unittest.TestCase):

	def test_2007_W01(self):
		"ISOCalendar.week_to_date() returns 2007-01-01 for 2007-W01"

		self.assertEquals(
			chrono.calendar.ISOCalendar.week_to_date(2007, 1),
			(2007, 1, 1)
		)

	def test_2009_W01(self):
		"ISOCalendar.week_to_date() returns 2008-12-29 for 2009-W01"

		self.assertEquals(
			chrono.calendar.ISOCalendar.week_to_date(2009, 1),
			(2008, 12, 29)
		)

	def test_2009_W32(self):
		"ISOCalendar.week_to_date() returns 2009-08-03 for 2009-W32"

		self.assertEquals(
			chrono.calendar.ISOCalendar.week_to_date(2009, 32),
			(2009, 8, 3)
		)

	def test_invalid(self):
		"ISOCalendar.week_to_date() raises WeekError for invalid week dates"

		self.assertRaises(chrono.WeekError, chrono.calendar.ISOCalendar.week_to_date, 2008, 53)

	def test_last(self):
		"ISOCalendar.week_to_date() returns 2009-12-28 for 2009-W53"

		self.assertEquals(
			chrono.calendar.ISOCalendar.week_to_date(2009, 53),
			(2009, 12, 28)
		)

	def test_leap(self):
		"ISOCalendar.week_to_date() returns 2008-07-14 for 2008-W29"

		self.assertEquals(
			chrono.calendar.ISOCalendar.week_to_date(2008, 29),
			(2008, 7, 14)
		)

	def test_none(self):
		"ISOCalendar.week_to_date() raises proper error for None"

		self.assertRaises(chrono.YearError, chrono.calendar.ISOCalendar.week_to_date, None, 29)
		self.assertRaises(chrono.WeekError, chrono.calendar.ISOCalendar.week_to_date, 2009, None)

	def test_nonnumeric(self):
		"ISOCalendar.week_to_date() raises proper error for non-numeric values"

		self.assertRaises(chrono.YearError, chrono.calendar.ISOCalendar.week_to_date, "abc", 29)
		self.assertRaises(chrono.WeekError, chrono.calendar.ISOCalendar.week_to_date, 2009, "abc")

	def test_string(self):
		"ISOCalendar.week_to_date() accepts string inputs"

		self.assertEquals(
			chrono.calendar.ISOCalendar.week_to_date("2009", "32"),
			(2009, 8, 3)
		)


class ISOCalendar_weekdateTest(unittest.TestCase):

	def test_2009_01_01(self):
		"ISOCalendar.weekdate() returns 2009-W01-4 for 2009-01-01"

		self.assertEquals(
			chrono.calendar.ISOCalendar.weekdate(2009, 1, 1),
			(2009, 1, 4)
		)

	def test_2009_07_15(self):
		"ISOCalendar.weekdate() returns 2009-W29-3 for 2009-07-15"

		self.assertEquals(
			chrono.calendar.ISOCalendar.weekdate(2009, 7, 15),
			(2009, 29, 3)
		)

	def test_2009_12_31(self):
		"ISOCalendar.weekdate() returns 2009-W53-4 for 2009-12-31"

		self.assertEquals(
			chrono.calendar.ISOCalendar.weekdate(2009, 12, 31),
			(2009, 53, 4)
		)

	def test_2010_01_01(self):
		"ISOCalendar.weekdate() returns 2009-W53-5 for 2010-01-01"

		self.assertEquals(
			chrono.calendar.ISOCalendar.weekdate(2010, 1, 1),
			(2009, 53, 5)
		)

	def test_2010_01_04(self):
		"ISOCalendar.weekdate() returns 2010-W01-1 for 2010-01-04"

		self.assertEquals(
			chrono.calendar.ISOCalendar.weekdate(2010, 1, 4),
			(2010, 1, 1)
		)

	def test_2010_12_31(self):
		"ISOCalendar.weekdate() returns 2010-52-5 for 2010-12-31"

		self.assertEquals(
			chrono.calendar.ISOCalendar.weekdate(2010, 12, 31),
			(2010, 52, 5)
		)

	def test_invalid(self):
		"ISOCalendar.weekdate() raises DayError on invalid date"

		self.assertRaises(chrono.DayError, chrono.calendar.ISOCalendar.weekdate, 2009, 2, 29)

	def test_none(self):
		"ISOCalendar.weekdate() raises proper error on None input"

		self.assertRaises(chrono.YearError, chrono.calendar.ISOCalendar.weekdate, None, 8, 14)
		self.assertRaises(chrono.MonthError, chrono.calendar.ISOCalendar.weekdate, 2009, None, 14)
		self.assertRaises(chrono.DayError, chrono.calendar.ISOCalendar.weekdate, 2009, 8, None)

	def test_nonnumeric(self):
		"ISOCalendar.weekdate() raises proper error on non-numeric input"

		self.assertRaises(chrono.YearError, chrono.calendar.ISOCalendar.weekdate, "abc", 8, 14)
		self.assertRaises(chrono.MonthError, chrono.calendar.ISOCalendar.weekdate, 2009, "abc", 14)
		self.assertRaises(chrono.DayError, chrono.calendar.ISOCalendar.weekdate, 2009, 8, "abc")

	def test_string(self):
		"ISOCalendar.weekdate() accepts string input"

		self.assertEquals(
			chrono.calendar.ISOCalendar.weekdate("2009", "7", "15"),
			(2009, 29, 3)
		)


class ISOCalendar_weekdate_to_dateTest(unittest.TestCase):

	def test_2007_W01(self):
		"ISOCalendar.weekdate_to_date() returns 2007-01-03 for 2007-W01-3"

		self.assertEquals(
			chrono.calendar.ISOCalendar.weekdate_to_date(2007, 1, 3),
			(2007, 1, 3)
		)

	def test_2009_W01(self):
		"ISOCalendar.weekdate_to_date() returns 2008-12-31 for 2009-W01-3"

		self.assertEquals(
			chrono.calendar.ISOCalendar.weekdate_to_date(2009, 1, 3),
			(2008, 12, 31)
		)

	def test_2009_W32(self):
		"ISOCalendar.weekdate_to_date() returns 2009-08-07 for 2009-W32-5"

		self.assertEquals(
			chrono.calendar.ISOCalendar.weekdate_to_date(2009, 32, 5),
			(2009, 8, 7)
		)

	def test_invalid(self):
		"ISOCalendar.weekdate_to_date() raises DayError for invalid weekdate dates"

		self.assertRaises(chrono.DayError, chrono.calendar.ISOCalendar.weekdate_to_date, 2008, 52, 8)

	def test_last(self):
		"ISOCalendar.weekdate_to_date() returns 2010-01-03 for 2009-W53-7"

		self.assertEquals(
			chrono.calendar.ISOCalendar.weekdate_to_date(2009, 53, 7),
			(2010, 1, 3)
		)

	def test_leap(self):
		"ISOCalendar.weekdate_to_date() returns 2008-07-14 for 2008-W29-1"

		self.assertEquals(
			chrono.calendar.ISOCalendar.weekdate_to_date(2008, 29, 1),
			(2008, 7, 14)
		)

	def test_none(self):
		"ISOCalendar.weekdate_to_date() raises proper error for None"

		self.assertRaises(chrono.YearError, chrono.calendar.ISOCalendar.weekdate_to_date, None, 29, 3)
		self.assertRaises(chrono.WeekError, chrono.calendar.ISOCalendar.weekdate_to_date, 2009, None, 3)
		self.assertRaises(chrono.DayError, chrono.calendar.ISOCalendar.weekdate_to_date, 2009, 29, None)

	def test_nonnumeric(self):
		"ISOCalendar.weekdate_to_date() raises proper error for non-numeric values"

		self.assertRaises(chrono.YearError, chrono.calendar.ISOCalendar.weekdate_to_date, "abc", 29, 3)
		self.assertRaises(chrono.WeekError, chrono.calendar.ISOCalendar.weekdate_to_date, 2009, "abc", 3)
		self.assertRaises(chrono.DayError, chrono.calendar.ISOCalendar.weekdate_to_date, 2009, 29, "abc")

	def test_string(self):
		"ISOCalendar.weekdate_to_date() accepts string inputs"

		self.assertEquals(
			chrono.calendar.ISOCalendar.weekdate_to_date("2009", "32", "5"),
			(2009, 8, 7)
		)


class ISOCalendar_weekdayTest(unittest.TestCase):

	def test_invalid(self):
		"ISOCalendar.weekday() raises DayError on invalid date"

		self.assertRaises(chrono.DayError, chrono.calendar.ISOCalendar.weekday, 2009, 2, 29)

	def test_monday(self):
		"ISOCalendar.weekday() returns 1 for 2009-12-28"

		self.assertEquals(chrono.calendar.ISOCalendar.weekday(2009, 12, 28), 1)

	def test_none(self):
		"ISOCalendar.weekday() raises proper error on None input"

		self.assertRaises(chrono.YearError, chrono.calendar.ISOCalendar.weekday, None, 8, 14)
		self.assertRaises(chrono.MonthError, chrono.calendar.ISOCalendar.weekday, 2009, None, 14)
		self.assertRaises(chrono.DayError, chrono.calendar.ISOCalendar.weekday, 2009, 8, None)

	def test_nonnumeric(self):
		"ISOCalendar.weekday() raises proper error on non-numeric input"

		self.assertRaises(chrono.YearError, chrono.calendar.ISOCalendar.weekday, "abc", 8, 14)
		self.assertRaises(chrono.MonthError, chrono.calendar.ISOCalendar.weekday, 2009, "abc", 14)
		self.assertRaises(chrono.DayError, chrono.calendar.ISOCalendar.weekday, 2009, 8, "abc")

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
		"ISOCalendar.weeks() raises YearError on invalid year"

		self.assertRaises(chrono.YearError, chrono.calendar.ISOCalendar.weeks, 10000)

	def test_leap(self):
		"ISOCalendar.weeks() returns 53 for 2020"

		self.assertEquals(chrono.calendar.ISOCalendar.weeks(2020), 53)

	def test_none(self):
		"ISOCalendar.weeks() raises YearError on None input"

		self.assertRaises(chrono.YearError, chrono.calendar.ISOCalendar.weeks, None)

	def test_nonnumeric(self):
		"ISOCalendar.weeks() raises YearError on non-numeric input"

		self.assertRaises(chrono.YearError, chrono.calendar.ISOCalendar.weeks, "abc")

	def test_string(self):
		"ISOCalendar.weeks() accepts string input"

		self.assertEquals(chrono.calendar.ISOCalendar.weeks("2008"), 52)

	def test_thursday(self):
		"ISOCalendar.weeks() returns 53 for 2009"

		self.assertEquals(chrono.calendar.ISOCalendar.weeks(2009), 53)


if __name__ == "__main__":
	unittest.main()
