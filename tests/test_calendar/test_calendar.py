#!/usr/bin/env python

import chrono
import unittest


class Calendar_fullyearTest(unittest.TestCase):

    def test_0(self):
        "Calendar.fullyear() returns 2000 for 0"

        self.assertEqual(chrono.calendar.Calendar.fullyear(0), 2000)

    def test_29(self):
        "Calendar.fullyear() returns 2029 for 29"

        self.assertEqual(chrono.calendar.Calendar.fullyear(29), 2029)

    def test_30(self):
        "Calendar.fullyear() returns 1930 for 30"

        self.assertEqual(chrono.calendar.Calendar.fullyear(30), 1930)

    def test_100(self):
        "Calendar.fullyear() return 100 for 100"

        self.assertEqual(chrono.calendar.Calendar.fullyear(100), 100)

    def test_full(self):
        "Calendar.fullyear() returns 2010 for 2010"

        self.assertEqual(chrono.calendar.Calendar.fullyear(2010), 2010)

    def test_negative(self):
        "Calendar.fullyear() returns -1 for -1"

        self.assertEqual(chrono.calendar.Calendar.fullyear(-1), -1)

    def test_string(self):
        "Calendar.fullyear() handles strings"

        self.assertEqual(chrono.calendar.Calendar.fullyear("29"), 2029)


class Calendar_leapyearTest(unittest.TestCase):

    def test_invalid(self):
        "Calendar.leapyear() raises YearError for invalid years"

        self.assertRaises(
            chrono.YearError, chrono.calendar.Calendar.leapyear, 10000
        )

    def test_leapyear(self):
        "Calendar.leapyear() returns True for 2008"

        self.assertTrue(chrono.calendar.Calendar.leapyear(2008))

    def test_normal(self):
        "Calendar.leapyear() returns False for 2007"

        self.assertFalse(chrono.calendar.Calendar.leapyear(2007))

    def test_string(self):
        "Calendar.leapyear() handles string input"

        self.assertTrue(chrono.calendar.Calendar.leapyear("2008"))


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
        "Calendar.monthdays() raises proper error for invalid input"

        self.assertRaises(
            chrono.YearError, chrono.calendar.Calendar.monthdays, 10000, 1
        )
        self.assertRaises(
            chrono.MonthError, chrono.calendar.Calendar.monthdays, 2009, 13
        )

    def test_january(self):
        "Calendar.monthdays() returns 31 for 2009-01"

        self.assertEquals(chrono.calendar.Calendar.monthdays(2009, 1), 31)

    def test_string(self):
        "Calendar.monthdays() accepts string input"

        self.assertEquals(chrono.calendar.Calendar.monthdays("2009", "1"), 31)


class Calendar_monthnameTest(unittest.TestCase):

    def test_full(self):
        "Calendar.monthname() returns full month name"

        self.assertEquals(chrono.calendar.Calendar.monthname(4), "April")

    def test_short(self):
        "Calendar.monthname() returns short month name on short-parameter"

        self.assertEquals(chrono.calendar.Calendar.monthname(4, True), "Apr")

    def test_invalid(self):
        "Calendar.monthname() raises MonthError on invalid month"

        self.assertRaises(
            chrono.MonthError, chrono.calendar.Calendar.monthname, 13
        )


class Calendar_ordinalTest(unittest.TestCase):

    def test_2009_01_05(self):
        "Calendar.ordinal() returns 5 for 2009-01-05"

        self.assertEquals(chrono.calendar.Calendar.ordinal(2009, 1, 5), 5)

    def test_invalid(self):
        "Calendar.ordinal() raises proper error for invalid input"

        self.assertRaises(
            chrono.YearError, chrono.calendar.Calendar.ordinal, 10000, 7, 23
        )
        self.assertRaises(
            chrono.MonthError, chrono.calendar.Calendar.ordinal, 2009, 13, 23
        )
        self.assertRaises(
            chrono.DayError, chrono.calendar.Calendar.ordinal, 2009, 7, 32
        )

    def test_last(self):
        "Calendar.ordinal() returns 365 for 2009-12-31"

        self.assertEquals(chrono.calendar.Calendar.ordinal(2009, 12, 31), 365)

    def test_leap(self):
        "Calendar.ordinal() returns 366 for 2008-12-31"

        self.assertEquals(chrono.calendar.Calendar.ordinal(2008, 12, 31), 366)

    def test_string(self):
        "Calendar.ordinal() accepts string inputs"

        self.assertEquals(
            chrono.calendar.Calendar.ordinal("2009", "7", "21"), 202
        )


class Calendar_ordinal_to_dateTest(unittest.TestCase):

    def test_2009_202(self):
        "Calendar.ordinal_to_date() returns 2009-07-16 for 2009-202"

        self.assertEquals(
            chrono.calendar.Calendar.ordinal_to_date(2009, 202),
            (2009, 7, 21)
        )

    def test_invalid(self):
        "Calendar.ordinal_to_date() raises proper error for invalid input"

        self.assertRaises(
            chrono.DayError,
            chrono.calendar.Calendar.ordinal_to_date, 2009, 366
        )

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

    def test_string(self):
        "Calendar.ordinal_to_date() accepts string inputs"

        self.assertEquals(
            chrono.calendar.Calendar.ordinal_to_date("2009", "202"),
            (2009, 7, 21)
        )


class Calendar_validateTest(unittest.TestCase):

    def test_invalid(self):
        "Calendar.validate() raises proper error on invalid input"

        self.assertRaises(
            chrono.YearError, chrono.calendar.Calendar.validate, 10000, 7, 23
        )
        self.assertRaises(
            chrono.MonthError, chrono.calendar.Calendar.validate, 2010, 13, 23
        )
        self.assertRaises(
            chrono.DayError, chrono.calendar.Calendar.validate, 2010, 7, 32
        )

    def test_string(self):
        "Calendar.validate() accepts string inputs"

        chrono.calendar.Calendar.validate("2008", "2", "29")

    def test_valid(self):
        "Calendar.validate() returns None for valid dates"

        self.assertEqual(
            chrono.calendar.Calendar.validate(2010, 7, 23), None
        )


class Calendar_validate_monthTest(unittest.TestCase):

    def test_invalid(self):
        "Calendar.validate_month() raises MonthError for invalid month"

        self.assertRaises(
            chrono.MonthError, chrono.calendar.Calendar.validate_month, 13
        )

    def test_string(self):
        "Calendar.validate_month() accepts strings"

        chrono.calendar.Calendar.validate_month("7")

    def test_valid(self):
        "Calendar.validate_month() returns None for valid month"

        self.assertEqual(chrono.calendar.Calendar.validate_month(7), None)


class Calendar_validate_ordinalTest(unittest.TestCase):

    def test_invalid(self):
        "Calendar.validate_ordinal() raises proper error on invalid input"

        self.assertRaises(
            chrono.YearError,
            chrono.calendar.Calendar.validate_ordinal, 10000, 365
        )
        self.assertRaises(
            chrono.DayError,
            chrono.calendar.Calendar.validate_ordinal, 2010, 366
        )

    def test_string(self):
        "Calendar.validate_ordinal() accepts string inputs"

        chrono.calendar.Calendar.validate_ordinal("2009", "202")

    def test_valid(self):
        "Calendar.validate_ordinal() returns None for valid input"

        self.assertEqual(
            chrono.calendar.Calendar.validate_ordinal(2009, 202), None
        )


class Calendar_validate_weekTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        class c(chrono.calendar.Calendar):
            weeks = chrono.calendar.ISOCalendar.weeks

        self.c = c

    def test_invalid(self):
        "Calendar.validate_week() raises proper error on invalid input"

        self.assertRaises(
            chrono.YearError,
            self.c.validate_week, 10000, 52
        )
        self.assertRaises(
            chrono.WeekError,
            self.c.validate_week, 2010, 53
        )

    def test_valid(self):
        "Calendar.validate_week() returns None on valid input"

        self.assertEqual(self.c.validate_week(2009, 32), None)

    def test_string(self):
        "Calendar.validate_week() accepts string inputs"

        self.c.validate_week("2009", "32")


class Calendar_validate_weekdateTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        class c(chrono.calendar.Calendar):
            weeks = chrono.calendar.ISOCalendar.weeks

        self.c = c

    def test_invalid(self):
        "Calendar.validate_weekdate() raises proper error on invalid input"

        self.assertRaises(
            chrono.YearError,
            self.c.validate_weekdate, 10000, 32, 4
        )
        self.assertRaises(
            chrono.WeekError,
            self.c.validate_weekdate, 2008, 53, 3
        )
        self.assertRaises(
            chrono.DayError,
            self.c.validate_weekdate, 2009, 32, 8
        )

    def test_valid(self):
        "Calendar.validate_weekdate() returns None for valid input"

        self.assertEqual(
            self.c.validate_weekdate(2009, 32, 4), None
        )

    def test_string(self):
        "Calendar.validate_weekdate() accepts string inputs"

        self.c.validate_weekdate("2009", "32", "4")


class Calendar_validate_weekdayTest(unittest.TestCase):

    def test_invalid(self):
        "Calendar.validate_weekday() raises DayError for invalid input"

        self.assertRaises(
            chrono.DayError, chrono.calendar.Calendar.validate_weekday, 8
        )

    def test_string(self):
        "Calendar.validate_weekday() accepts strings"

        chrono.calendar.Calendar.validate_weekday("7")

    def test_valid(self):
        "Calendar.validate_weekday() returns None for valid input"

        self.assertEqual(chrono.calendar.Calendar.validate_weekday(7), None)


class Calendar_validate_yearTest(unittest.TestCase):

    def test_invalid(self):
        "Calendar.validate_year() raises YearError on invalid input"

        self.assertRaises(
            chrono.YearError, chrono.calendar.Calendar.validate_year, 10000
        )

    def test_valid(self):
        "Calendar.validate_year() returns None for valid input"

        self.assertEqual(chrono.calendar.Calendar.validate_year(2010), None)

    def test_string(self):
        "Calendar.validate_year() accepts strings"

        chrono.calendar.Calendar.validate_year("2009")


class Calendar_weekTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        class c(chrono.calendar.Calendar):
            weekdate = chrono.calendar.ISOCalendar.weekdate

        self.c = c

    def test_invalid(self):
        "Calendar.week() raises proper error on invalid input"

        self.assertRaises(
            chrono.YearError,
            self.c.week, 10000, 7, 23
        )
        self.assertRaises(
            chrono.MonthError,
            self.c.week, 2010, 13, 23
        )
        self.assertRaises(
            chrono.DayError,
            self.c.week, 2010, 7, 32
        )

    def test_string(self):
        "Calendar.week() accepts string input"

        self.assertEquals(
            self.c.week("2009", "7", "15"), (2009, 29)
        )

    def test_valid(self):
        "Calendar.week() returns 2009-W29 for 2009-07-15"

        self.assertEquals(
            self.c.week(2009, 7, 15), (2009, 29)
        )


class Calendar_week_to_dateTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        class c(chrono.calendar.Calendar):
            weekdate_to_date = chrono.calendar.ISOCalendar.weekdate_to_date

        self.c = c

    def test_invalid(self):
        "Calendar.week_to_date() raises proper error for invalid input"

        self.assertRaises(
            chrono.YearError,
            self.c.week_to_date, 10000, 32
        )
        self.assertRaises(
            chrono.WeekError,
            self.c.week_to_date, 2008, 53
        )

    def test_string(self):
        "Calendar.week_to_date() accepts string inputs"

        self.assertEquals(
            self.c.week_to_date("2009", "32"),
            (2009, 8, 3)
        )

    def test_valid(self):
        "Calendar.week_to_date() returns 2009-08-03 for 2009-W32"

        self.assertEquals(
            self.c.week_to_date(2009, 32),
            (2009, 8, 3)
        )


class Calendar_weekdateTest(unittest.TestCase):

    def test_notimplemented(self):
        "Calendar.weekdate() raises NotImplementedError"

        self.assertRaises(
            NotImplementedError,
            chrono.calendar.Calendar.weekdate, 2009, 32, 4
        )


class Calendar_weekdate_to_dateTest(unittest.TestCase):

    def test_notimplemented(self):
        "Calendar.weekdate_to_date() raises NotImplementedError"

        self.assertRaises(
            NotImplementedError,
            chrono.calendar.Calendar.weekdate_to_date, 2009, 32, 4
        )


class Calendar_weekdayTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

        class c(chrono.calendar.Calendar):
            weekdate = chrono.calendar.ISOCalendar.weekdate

        self.c = c

    def test_invalid(self):
        "Calendar.weekday() raises proper error on invalid input"

        self.assertRaises(
            chrono.YearError,
            self.c.weekday, 10000, 7, 23
        )
        self.assertRaises(
            chrono.MonthError,
            self.c.weekday, 2010, 13, 23
        )
        self.assertRaises(
            chrono.DayError,
            self.c.weekday, 2010, 7, 32
        )

    def test_string(self):
        "Calendar.weekday() accepts string input"

        self.assertEquals(
            self.c.weekday("2009", "12", "27"), 7
        )

    def test_valid(self):
        "Calendar.weekday() returns 4 for 2009-12-24"

        self.assertEquals(self.c.weekday(2009, 12, 24), 4)


class Calendar_weekdaynameTest(unittest.TestCase):

    def test_notimplemented(self):
        "Calendar.weekdayname() raises NotImplementedError"

        self.assertRaises(
            NotImplementedError,
            chrono.calendar.Calendar.weekdayname, 4
        )


class Calendar_weeksTest(unittest.TestCase):

    def test_notimplemented(self):
        "Calendar.weeks() raises NotImplementedError"

        self.assertRaises(
            NotImplementedError,
            chrono.calendar.Calendar.weeks, 2009
        )


class Calendar_yeardaysTest(unittest.TestCase):

    def test_invalid(self):
        "Calendar.yeardays() raises YearError on invalid year"

        self.assertRaises(
            chrono.YearError,
            chrono.calendar.Calendar.yeardays, 10000
        )

    def test_leap(self):
        "Calendar.yeardays() returns 366 for leap years"

        self.assertEquals(chrono.calendar.Calendar.yeardays(2008), 366)

    def test_normal(self):
        "Calendar.yeardays() returns 365 for normal years"

        self.assertEquals(chrono.calendar.Calendar.yeardays(2007), 365)

    def test_string(self):
        "Calendar.yeardays() accepts strings"

        self.assertEquals(chrono.calendar.Calendar.yeardays("2008"), 366)


if __name__ == "__main__":
    unittest.main()
