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


class Calendar_leapyearTest(unittest.TestCase):

	def test_invalid(self):
		"Calendar.leapyear() raises YearError for invalid years"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.leapyear, 10000)

	def test_leapyear(self):
		"Calendar.leapyear() returns True for 2008"

		self.assertTrue(chrono.calendar.Calendar.leapyear(2008))

	def test_noleapyear(self):
		"Calendar.leapyear() returns False for 2007"

		self.assertFalse(chrono.calendar.Calendar.leapyear(2007))

	def test_none(self):
		"Calendar.leapyear() raises YearError on None"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.leapyear, None)

	def test_string(self):
		"Calendar.leapyear() handles string input"

		self.assertTrue(chrono.calendar.Calendar.leapyear("2008"))

	def test_text(self):
		"Calendar.leapyear() raises YearError for text input"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.leapyear, "abc")


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

	def test_invalid(self):
		"Calendar.monthdays() raises YearError and MonthError for invalid years and months"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.monthdays, 10000, 1)
		self.assertRaises(chrono.MonthError, chrono.calendar.Calendar.monthdays, 2009, 13)

	def test_january(self):
		"Calendar.monthdays() returns 31 for 2009-01"

		self.assertEquals(chrono.calendar.Calendar.monthdays(2009, 1), 31)

	def test_none(self):
		"Calendar.monthdays() raises YearError and MonthError on None"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.monthdays, None, 1)
		self.assertRaises(chrono.MonthError, chrono.calendar.Calendar.monthdays, 2009, None)

	def test_string(self):
		"Calendar.monthdays() accepts string input"

		self.assertEquals(chrono.calendar.Calendar.monthdays("2009", "1"), 31)

	def test_text(self):
		"Calendar.monthdays() raises YearError and MonthError on text input"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.monthdays, "abc", 1)
		self.assertRaises(chrono.MonthError, chrono.calendar.Calendar.monthdays, 2009, "abc")


class Calendar_monthnameTest(unittest.TestCase):

	def test_full(self):
		"Calendar.monthname() returns full month name"

		self.assertEquals(chrono.calendar.Calendar.monthname(4), "April")

	def test_short(self):
		"Calendar.monthname() returns short month name on short-parameter"

		self.assertEquals(chrono.calendar.Calendar.monthname(4, True), "Apr")

	def test_invalid(self):
		"Calendar.monthname() raises MonthError on invalid month"

		self.assertRaises(chrono.MonthError, chrono.calendar.Calendar.monthname, 13)


class Calendar_ordinalTest(unittest.TestCase):

	def test_2009_01_05(self):
		"Calendar.ordinal() returns 5 for 2009-01-05"

		self.assertEquals(chrono.calendar.Calendar.ordinal(2009, 1, 5), 5)

	def test_invalid(self):
		"Calendar.ordinal() raises DayError for invalid day"

		self.assertRaises(chrono.DayError, chrono.calendar.Calendar.ordinal, 2009, 7, 32)

	def test_last(self):
		"Calendar.ordinal() returns 365 for 2009-12-31"

		self.assertEquals(chrono.calendar.Calendar.ordinal(2009, 12, 31), 365)

	def test_leap(self):
		"Calendar.ordinal() returns 366 for 2008-12-31"

		self.assertEquals(chrono.calendar.Calendar.ordinal(2008, 12, 31), 366)

	def test_none(self):
		"Calendar.ordinal() raises proper errors for None"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.ordinal, None, 7, 21)
		self.assertRaises(chrono.MonthError, chrono.calendar.Calendar.ordinal, 2009, None, 21)
		self.assertRaises(chrono.DayError, chrono.calendar.Calendar.ordinal, 2009, 7, None)

	def test_string(self):
		"Calendar.ordinal() accepts string inputs"

		self.assertEquals(chrono.calendar.Calendar.ordinal("2009", "7", "21"), 202)

	def test_text(self):
		"Calendar.ordinal() raises proper error for text values"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.ordinal, "abc", 7, 21)
		self.assertRaises(chrono.MonthError, chrono.calendar.Calendar.ordinal, 2009, "abc", 21)
		self.assertRaises(chrono.DayError, chrono.calendar.Calendar.ordinal, 2009, 7, "abc")


class Calendar_ordinal_to_dateTest(unittest.TestCase):

	def test_2009_202(self):
		"Calendar.ordinal_to_date() returns 2009-07-16 for 2009-202"

		self.assertEquals(
			chrono.calendar.Calendar.ordinal_to_date(2009, 202),
			(2009, 7, 21)
		)

	def test_invalid(self):
		"Calendar.ordinal_to_date() raises DayError for invalid days"

		self.assertRaises(chrono.DayError, chrono.calendar.Calendar.ordinal_to_date, 2009, 366)

	def test_last(self):
		"Calendar.ordinal_to_date() returns 2009-12-31 for 2009-365"

		self.assertEquals(
			chrono.calendar.Calendar.ordinal_to_date(2009, 365),
			(2009, 12, 31)
		)

	def test_leap(self):
		"Calendar.ordinal_to_date() returns 2008-12-31 for 2008-366"

		self.assertEquals(
			chrono.calendar.Calendar.ordinal_to_date(2008, 366),
			(2008, 12, 31)
		)

	def test_none(self):
		"Calendar.ordinal_to_date() raises proper error for None"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.ordinal_to_date, None, 202)
		self.assertRaises(chrono.DayError, chrono.calendar.Calendar.ordinal_to_date, 2009, None)

	def test_nonnumeric(self):
		"Calendar.ordinal_to_date() raises proper error for non-numeric values"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.ordinal_to_date, "abc", 202)
		self.assertRaises(chrono.DayError, chrono.calendar.Calendar.ordinal_to_date, 2009, "abc")

	def test_string(self):
		"Calendar.ordinal_to_date() accepts string inputs"

		self.assertEquals(
			chrono.calendar.Calendar.ordinal_to_date("2009", "202"),
			(2009, 7, 21)
		)


class Calendar_validateTest(unittest.TestCase):

	def test_2008_02_29(self):
		"Calendar.validate() accepts 2008-02-29"

		chrono.calendar.Calendar.validate(2008, 2, 29)

	def test_2009_02_29(self):
		"Calendar.validate() raises ValueError for 2009-02-29"

		self.assertRaises(chrono.DayError, chrono.calendar.Calendar.validate, 2009, 2, 29)

	def test_2009_12_27(self):
		"Calendar.validate() accepts 2009-12-27"

		chrono.calendar.Calendar.validate(2009, 12, 27)

	def test_nonnumeric(self):
		"Calendar.validate() raises proper error for non-numeric string"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.validate, "abc", 12, 27)
		self.assertRaises(chrono.MonthError, chrono.calendar.Calendar.validate, 2009, "abc", 27)
		self.assertRaises(chrono.DayError, chrono.calendar.Calendar.validate, 2009, 12, "abc")

	def test_none(self):
		"Calendar.validate() raises proper error for None"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.validate, None, 12, 27)
		self.assertRaises(chrono.MonthError, chrono.calendar.Calendar.validate, 2009, None, 27)
		self.assertRaises(chrono.DayError, chrono.calendar.Calendar.validate, 2009, 12, None)

	def test_string(self):
		"Calendar.validate() accepts string inputs"

		chrono.calendar.Calendar.validate("2008", "2", "29")


class Calendar_validate_monthTest(unittest.TestCase):

	def test_0(self):
		"Calendar.validate_month() raises MonthError for 0"

		self.assertRaises(chrono.MonthError, chrono.calendar.Calendar.validate_month, 0)

	def test_13(self):
		"Calendar.validate_month() raises MonthError for 13"

		self.assertRaises(chrono.MonthError, chrono.calendar.Calendar.validate_month, 13)

	def test_july(self):
		"Calendar.validate_month() accepts 7"

		chrono.calendar.Calendar.validate_month(7)

	def test_none(self):
		"Calendar.validate_month() raises MonthError for None"

		self.assertRaises(chrono.MonthError, chrono.calendar.Calendar.validate_month, None)

	def test_nonnumeric(self):
		"Calendar.validate_month() raises MonthError for non-numeric string"

		self.assertRaises(chrono.MonthError, chrono.calendar.Calendar.validate_month, "abc")

	def test_string(self):
		"Calendar.validate_month() accepts strings"

		chrono.calendar.Calendar.validate_month("7")


class Calendar_validate_ordinalTest(unittest.TestCase):

	def test_leap(self):
		"Calendar.validate_ordinal() accepts 2008-366"

		chrono.calendar.Calendar.validate_ordinal(2008, 366)

	def test_max(self):
		"Calendar.validate_ordinal() accepts 2009-365"

		chrono.calendar.Calendar.validate_ordinal(2009, 365)

	def test_nonnumeric(self):
		"Calendar.validate_ordinal() raises proper error for non-numeric string"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.validate_ordinal, "abc", 202)
		self.assertRaises(chrono.DayError, chrono.calendar.Calendar.validate_ordinal, 2009, "abc")

	def test_none(self):
		"Calendar.validate_ordinal() raises proper error for None"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.validate_ordinal, None, 202)
		self.assertRaises(chrono.DayError, chrono.calendar.Calendar.validate_ordinal, 2009, None)

	def test_ordinal(self):
		"Calendar.validate_ordinal() accepts 2009-202"

		chrono.calendar.Calendar.validate_ordinal(2009, 202)

	def test_string(self):
		"Calendar.validate_ordinal() accepts string inputs"

		chrono.calendar.Calendar.validate_ordinal("2009", "202")


class Calendar_validate_weekTest(unittest.TestCase):

	def test_notimplemented(self):
		"Calendar.validate_week() raises NotImplementedError"

		self.assertRaises(NotImplementedError, chrono.calendar.Calendar.validate_week, 2009, 32)


class Calendar_validate_weekdateTest(unittest.TestCase):

	def test_notimplemented(self):
		"Calendar.validate_weekdate() raises NotImplementedError"

		self.assertRaises(NotImplementedError, chrono.calendar.Calendar.validate_weekdate, 2009, 32, 4)


class Calendar_validate_weekdayTest(unittest.TestCase):

	def test_0(self):
		"Calendar.validate_weekday() raises DayError for 0"

		self.assertRaises(chrono.DayError, chrono.calendar.Calendar.validate_weekday, 0)

	def test_8(self):
		"Calendar.validate_weekday() raises DayError for 8"

		self.assertRaises(chrono.DayError, chrono.calendar.Calendar.validate_weekday, 8)

	def test_monday(self):
		"Calendar.validate_weekday() accepts 1"

		chrono.calendar.Calendar.validate_weekday(1)

	def test_none(self):
		"Calendar.validate_weekday() raises DayError for None"

		self.assertRaises(chrono.DayError, chrono.calendar.Calendar.validate_weekday, None)

	def test_nonnumeric(self):
		"Calendar.validate_weekday() raises DayError for non-numeric string"

		self.assertRaises(chrono.DayError, chrono.calendar.Calendar.validate_weekday, "abc")

	def test_string(self):
		"Calendar.validate_weekday() accepts strings"

		chrono.calendar.Calendar.validate_weekday("7")

	def test_sunday(self):
		"Calendar.validate_weekday() accepts 7"

		chrono.calendar.Calendar.validate_weekday(7)


class Calendar_validate_yearTest(unittest.TestCase):

	def test_0(self):
		"Calendar.validate_year() raises YearError for 0"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.validate_year, 0)

	def test_1(self):
		"Calendar.validate_year() accepts 1"

		chrono.calendar.Calendar.validate_year(1)

	def test_10000(self):
		"Calendar.validate_year() raises YearError for 10000"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.validate_year, 10000)

	def test_2009(self):
		"Calendar.validate_year() accepts 2009"

		chrono.calendar.Calendar.validate_year(2009)

	def test_9999(self):
		"Calendar.validate_year() accepts 9999"

		chrono.calendar.Calendar.validate_year(9999)

	def test_none(self):
		"Calendar.validate_year() raises YearError for None"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.validate_year, None)

	def test_nonnumeric(self):
		"Calendar.validate_year() raises YearError for non-numeric string"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.validate_year, "abc")

	def test_string(self):
		"Calendar.validate_year() accepts string"

		chrono.calendar.Calendar.validate_year("2009")


class Calendar_weekTest(unittest.TestCase):

	def test_notimplemented(self):
		"Calendar.week() raises NotImplementedError"

		self.assertRaises(NotImplementedError, chrono.calendar.Calendar.week, 2009, 12, 28)


class Calendar_week_to_dateTest(unittest.TestCase):

	def test_notimplemented(self):
		"Calendar.week_to_date() raises NotImplementedError"

		self.assertRaises(NotImplementedError, chrono.calendar.Calendar.week_to_date, 2009, 32)


class Calendar_weekdateTest(unittest.TestCase):

	def test_notimplemented(self):
		"Calendar.weekdate() raises NotImplementedError"

		self.assertRaises(NotImplementedError, chrono.calendar.Calendar.weekdate, 2009, 32, 4)


class Calendar_weekdate_to_dateTest(unittest.TestCase):

	def test_notimplemented(self):
		"Calendar.weekdate_to_date() raises NotImplementedError"

		self.assertRaises(NotImplementedError, chrono.calendar.Calendar.weekdate_to_date, 2009, 32, 4)


class Calendar_weekdayTest(unittest.TestCase):

	def test_notimplemented(self):
		"Calendar.weekday() raises NotImplementedError"

		self.assertRaises(NotImplementedError, chrono.calendar.Calendar.weekday, 2009, 12, 28)


class Calendar_weekdaynameTest(unittest.TestCase):

	def test_notimplemented(self):
		"Calendar.weekdayname() raises NotImplementedError"

		self.assertRaises(NotImplementedError, chrono.calendar.Calendar.weekdayname, 4)


class Calendar_weeksTest(unittest.TestCase):

	def test_notimplemented(self):
		"Calendar.weeks() raises NotImplementedError"

		self.assertRaises(NotImplementedError, chrono.calendar.Calendar.weeks, 2009)


class Calendar_yeardaysTest(unittest.TestCase):

	def test_2007(self):
		"Calendar.yeardays() returns 365 for 2007"

		self.assertEquals(chrono.calendar.Calendar.yeardays(2007), 365)

	def test_2008(self):
		"Calendar.yeardays() returns 366 for 2008"

		self.assertEquals(chrono.calendar.Calendar.yeardays(2008), 366)

	def test_invalid(self):
		"Calendar.yeardays() raises YearError on invalid year"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.yeardays, 10000)

	def test_none(self):
		"Calendar.yeardays() raises YearError on None"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.yeardays, None)

	def test_nonnumeric(self):
		"Calendar.yeardays() raises YearError on non-numeric input"

		self.assertRaises(chrono.YearError, chrono.calendar.Calendar.yeardays, "abc")

	def test_string(self):
		"Calendar.yeardays() accepts strings"

		self.assertEquals(chrono.calendar.Calendar.yeardays("2008"), 366)


if __name__ == "__main__":
	unittest.main()
