#!/usr/bin/env python

import chrono
import unittest


class ISOCalendarTest(unittest.TestCase):

    def test__subclass(self):
        "ISOCalendar is subclass of Calendar"

        self.assertTrue(
            issubclass(chrono.calendar.ISOCalendar, chrono.calendar.Calendar)
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
        "ISOCalendar.weekdate() raises proper error on invalid input"

        self.assertRaises(
            chrono.YearError,
            chrono.calendar.ISOCalendar.weekdate, 10000, 7, 23
        )
        self.assertRaises(
            chrono.MonthError,
            chrono.calendar.ISOCalendar.weekdate, 2010, 13, 23
        )
        self.assertRaises(
            chrono.DayError,
            chrono.calendar.ISOCalendar.weekdate, 2010, 7, 32
        )

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

    def test_2009_W29_1(self):
        "ISOCalendar.weekdate_to_date() returns 2008-07-14 for 2008-W29-1"

        self.assertEquals(
            chrono.calendar.ISOCalendar.weekdate_to_date(2008, 29, 1),
            (2008, 7, 14)
        )

    def test_2009_W32_5(self):
        "ISOCalendar.weekdate_to_date() returns 2009-08-07 for 2009-W32-5"

        self.assertEquals(
            chrono.calendar.ISOCalendar.weekdate_to_date(2009, 32, 5),
            (2009, 8, 7)
        )

    def test_2009_W53_7(self):
        "ISOCalendar.weekdate_to_date() returns 2010-01-03 for 2009-W53-7"

        self.assertEquals(
            chrono.calendar.ISOCalendar.weekdate_to_date(2009, 53, 7),
            (2010, 1, 3)
        )

    def test_invalid(self):
        "ISOCalendar.weekdate_to_date() raises proper error on invalid input"

        self.assertRaises(
            chrono.YearError,
            chrono.calendar.ISOCalendar.weekdate_to_date, 10000, 32, 5
        )
        self.assertRaises(
            chrono.WeekError,
            chrono.calendar.ISOCalendar.weekdate_to_date, 2010, 54, 5
        )
        self.assertRaises(
            chrono.DayError,
            chrono.calendar.ISOCalendar.weekdate_to_date, 2010, 52, 8
        )

    def test_string(self):
        "ISOCalendar.weekdate_to_date() accepts string inputs"

        self.assertEquals(
            chrono.calendar.ISOCalendar.weekdate_to_date("2009", "32", "5"),
            (2009, 8, 7)
        )


class ISOCalendar_weekdaynameTest(unittest.TestCase):

    def test_full(self):
        "ISOCalendar.weekdayname() returns full weekday name"

        self.assertEquals(
            chrono.calendar.ISOCalendar.weekdayname(4), "Thursday"
        )

    def test_short(self):
        "ISOCalendar.weekdayname() returns short weekday name if requested"

        self.assertEquals(
            chrono.calendar.ISOCalendar.weekdayname(4, True), "Thu"
        )

    def test_invalid(self):
        "ISOCalendar.weekdayname() raises DayError on invalid weekday"

        self.assertRaises(
            chrono.DayError, chrono.calendar.ISOCalendar.weekdayname, 8
        )


class ISOCalendar_weeksTest(unittest.TestCase):

    def test_2008(self):
        "ISOCalendar.weeks() returns 52 for 2008"

        self.assertEquals(chrono.calendar.ISOCalendar.weeks(2008), 52)

    def test_2009(self):
        "ISOCalendar.weeks() returns 53 for 2009"

        self.assertEquals(chrono.calendar.ISOCalendar.weeks(2009), 53)

    def test_2020(self):
        "ISOCalendar.weeks() returns 53 for 2020"

        self.assertEquals(chrono.calendar.ISOCalendar.weeks(2020), 53)

    def test_invalid(self):
        "ISOCalendar.weeks() raises YearError on invalid year"

        self.assertRaises(
            chrono.YearError,
            chrono.calendar.ISOCalendar.weeks, 10000
        )

    def test_string(self):
        "ISOCalendar.weeks() accepts string input"

        self.assertEquals(chrono.calendar.ISOCalendar.weeks("2008"), 52)


if __name__ == "__main__":
    unittest.main()
