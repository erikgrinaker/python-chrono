#!/usr/bin/env python

import chrono
import unittest


class USCalendarTest(unittest.TestCase):

    def test__subclass(self):
        "USCalendar is subclass of Calendar"

        self.assertTrue(
            issubclass(chrono.calendar.USCalendar, chrono.calendar.Calendar)
        )


class USCalendar_weekdateTest(unittest.TestCase):

    def test_2009_01_01(self):
        "USCalendar.weekdate() returns 2009-W01-5 for 2009-01-01"

        self.assertEquals(
            chrono.calendar.USCalendar.weekdate(2009, 1, 1),
            (2009, 1, 5)
        )

    def test_2009_07_15(self):
        "USCalendar.weekdate() returns 2009-W29-4 for 2009-07-15"

        self.assertEquals(
            chrono.calendar.USCalendar.weekdate(2009, 7, 15),
            (2009, 29, 4)
        )

    def test_2009_12_31(self):
        "USCalendar.weekdate() returns 2010-W01-5 for 2009-12-31"

        self.assertEquals(
            chrono.calendar.USCalendar.weekdate(2009, 12, 31),
            (2010, 1, 5)
        )

    def test_2010_01_01(self):
        "USCalendar.weekdate() returns 2010-W01-6 for 2010-01-01"

        self.assertEquals(
            chrono.calendar.USCalendar.weekdate(2010, 1, 1),
            (2010, 1, 6)
        )

    def test_2010_01_04(self):
        "USCalendar.weekdate() returns 2010-W02-2 for 2010-01-04"

        self.assertEquals(
            chrono.calendar.USCalendar.weekdate(2010, 1, 4),
            (2010, 2, 2)
        )

    def test_2010_12_31(self):
        "USCalendar.weekdate() returns 2011-W01-6 for 2010-12-31"

        self.assertEquals(
            chrono.calendar.USCalendar.weekdate(2010, 12, 31),
            (2011, 1, 6)
        )

    def test_invalid(self):
        "USCalendar.weekdate() raises proper error on invalid input"

        self.assertRaises(
            chrono.YearError,
            chrono.calendar.USCalendar.weekdate, 10000, 7, 23
        )
        self.assertRaises(
            chrono.MonthError,
            chrono.calendar.USCalendar.weekdate, 2010, 13, 23
        )
        self.assertRaises(
            chrono.DayError,
            chrono.calendar.USCalendar.weekdate, 2010, 7, 32
        )

    def test_string(self):
        "USCalendar.weekdate() accepts string input"

        self.assertEquals(
            chrono.calendar.USCalendar.weekdate("2009", "7", "15"),
            (2009, 29, 4)
        )


class USCalendar_weekdate_to_dateTest(unittest.TestCase):

    def test_2007_W01_3(self):
        "USCalendar.weekdate_to_date() returns 2007-01-02 for 2007-W01-3"

        self.assertEquals(
            chrono.calendar.USCalendar.weekdate_to_date(2007, 1, 3),
            (2007, 1, 2)
        )

    def test_2008_W29_1(self):
        "USCalendar.weekdate_to_date() returns 2008-07-14 for 2008-W29-1"

        self.assertEquals(
            chrono.calendar.USCalendar.weekdate_to_date(2008, 29, 1),
            (2008, 7, 13)
        )

    def test_2009_W01_3(self):
        "USCalendar.weekdate_to_date() returns 2008-12-30 for 2009-W01-3"

        self.assertEquals(
            chrono.calendar.USCalendar.weekdate_to_date(2009, 1, 3),
            (2008, 12, 30)
        )

    def test_2009_W32_5(self):
        "USCalendar.weekdate_to_date() returns 2009-08-06 for 2009-W32-5"

        self.assertEquals(
            chrono.calendar.USCalendar.weekdate_to_date(2009, 32, 5),
            (2009, 8, 6)
        )

    def test_2011_W01_3(self):
        "USCalendar.weekdate_to_date() returns 2010-12-28 for 2011-W01-3"

        self.assertEquals(
            chrono.calendar.USCalendar.weekdate_to_date(2011, 1, 3),
            (2010, 12, 28)
        )

    def test_2016_W53_7(self):
        "USCalendar.weekdate_to_date() returns 2016-12-31 for 2016-W53-7"

        self.assertEquals(
            chrono.calendar.USCalendar.weekdate_to_date(2016, 53, 7),
            (2016, 12, 31)
        )

    def test_invalid(self):
        "USCalendar.weekdate_to_date() raises proper error on invalid input"

        self.assertRaises(
            chrono.YearError,
            chrono.calendar.USCalendar.weekdate_to_date, 10000, 32, 5
        )
        self.assertRaises(
            chrono.WeekError,
            chrono.calendar.USCalendar.weekdate_to_date, 2010, 54, 5
        )
        self.assertRaises(
            chrono.DayError,
            chrono.calendar.USCalendar.weekdate_to_date, 2010, 52, 8
        )

    def test_string(self):
        "USCalendar.weekdate_to_date() accepts string inputs"

        self.assertEquals(
            chrono.calendar.USCalendar.weekdate_to_date("2009", "32", "5"),
            (2009, 8, 6)
        )


class USCalendar_weekdaynameTest(unittest.TestCase):

    def test_full(self):
        "USCalendar.weekdayname() returns full weekday name"

        self.assertEquals(
            chrono.calendar.USCalendar.weekdayname(4), "Wednesday"
        )

    def test_short(self):
        "USCalendar.weekdayname() returns short weekday name if requested"

        self.assertEquals(
            chrono.calendar.USCalendar.weekdayname(4, True), "Wed"
        )

    def test_invalid(self):
        "USCalendar.weekdayname() raises DayError on invalid weekday"

        self.assertRaises(
            chrono.DayError, chrono.calendar.USCalendar.weekdayname, 8
        )


class USCalendar_weeksTest(unittest.TestCase):

    def test_2010(self):
        "USCalendar.weeks() returns 52 for 2010"

        self.assertEquals(chrono.calendar.USCalendar.weeks(2010), 52)

    def test_2011(self):
        "USCalendar.weeks() returns 53 for 2011"

        self.assertEquals(chrono.calendar.USCalendar.weeks(2011), 53)

    def test_2016(self):
        "USCalendar.weeks() returns 53 for 2016"

        self.assertEquals(chrono.calendar.USCalendar.weeks(2016), 53)

    def test_invalid(self):
        "USCalendar.weeks() raises YearError on invalid year"

        self.assertRaises(
            chrono.YearError,
            chrono.calendar.USCalendar.weeks, 10000
        )

    def test_string(self):
        "USCalendar.weeks() accepts string input"

        self.assertEquals(chrono.calendar.USCalendar.weeks("2010"), 52)


if __name__ == "__main__":
    unittest.main()
