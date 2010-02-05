#!/usr/bin/env python

import chrono
import datetime
import unittest
import time


class Date__eqTest(unittest.TestCase):

    def test_date(self):
        "Date.__eq__() handles Date objects"

        self.assertTrue(chrono.Date("2009-12-27") == chrono.Date("2009-12-27"))
        self.assertFalse(
            chrono.Date("2009-12-27") == chrono.Date("2009-12-28")
        )

    def test_datetime(self):
        "Date.__eq__() handles DateTime objects"

        self.assertTrue(
            chrono.Date("2009-12-27") == \
            chrono.DateTime("2009-12-27 00:00:00")
        )
        self.assertFalse(
            chrono.Date("2009-12-27") == \
            chrono.DateTime("2009-12-27 16:27:43")
        )

    def test_none(self):
        "Date.__eq__() handles None"

        self.assertTrue(chrono.Date() == None)
        self.assertFalse(chrono.Date("2010-07-23") == None)

    def test_string(self):
        "Date.__eq__() handles strings"

        self.assertTrue(chrono.Date("2009-12-27") == "2009-12-27")
        self.assertFalse(chrono.Date("2010-07-23") == "2010-07-22")


class Date__geTest(unittest.TestCase):

    def test_date(self):
        "Date.__ge__() handles Date objects"

        self.assertTrue(chrono.Date("2009-12-28") >= chrono.Date("2009-12-27"))
        self.assertTrue(chrono.Date("2009-12-28") >= chrono.Date("2009-12-28"))
        self.assertFalse(
            chrono.Date("2009-12-28") >= chrono.Date("2009-12-29")
        )

    def test_datetime(self):
        "Date.__ge__() handles DateTime objects"

        self.assertTrue(
            chrono.Date("2009-12-28") >= chrono.DateTime("2009-12-27 16:27:43")
        )
        self.assertTrue(
            chrono.Date("2009-12-28") >= chrono.DateTime("2009-12-28 00:00:00")
        )
        self.assertFalse(
            chrono.Date("2009-12-28") >= chrono.DateTime("2009-12-28 16:27:43")
        )

    def test_none(self):
        "Date.__ge__() handles None"

        self.assertTrue(chrono.Date("2009-12-28") >= None)
        self.assertTrue(chrono.Date() >= None)

    def test_string(self):
        "Date.__ge__() handles strings"

        self.assertTrue(chrono.Date("2009-12-29") >= "2009-12-28")
        self.assertTrue(chrono.Date("2009-12-28") >= "2009-12-28")
        self.assertFalse(chrono.Date("2009-12-27") >= "2009-12-28")


class Date__gtTest(unittest.TestCase):

    def test_date(self):
        "Date.__gt__() handles Date objects"

        self.assertTrue(chrono.Date("2009-12-28") > chrono.Date("2009-12-27"))
        self.assertFalse(chrono.Date("2009-12-28") > chrono.Date("2009-12-28"))
        self.assertFalse(chrono.Date("2009-12-28") > chrono.Date("2009-12-29"))

    def test_datetime(self):
        "Date.__gt__() handles DateTime objects"

        self.assertTrue(
            chrono.Date("2009-12-28") > chrono.DateTime("2009-12-27 16:27:43")
        )
        self.assertFalse(
            chrono.Date("2009-12-28") > chrono.DateTime("2009-12-28 00:00:00")
        )
        self.assertFalse(
            chrono.Date("2009-12-28") > chrono.DateTime("2009-12-28 16:27:43")
        )

    def test_none(self):
        "Date.__gt__() handles None"

        self.assertFalse(chrono.Date() > None)
        self.assertTrue(chrono.Date("2009-12-27") > None)

    def test_string(self):
        "Date.__gt__() handles strings"

        self.assertTrue(chrono.Date("2009-12-28") > "2009-12-27")
        self.assertFalse(chrono.Date("2009-12-28") > "2009-12-28")
        self.assertFalse(chrono.Date("2009-12-28") > "2009-12-29")


class Date__initTest(unittest.TestCase):

    def test_calendar(self):
        "Date.__init__() takes calendar as input"

        c = chrono.calendar.USCalendar

        self.assertEqual(chrono.Date(None, None, c).calendar, c)

    def test_calendar_default(self):
        "Date.__init__() defaults to ISOCalendar"

        self.assertEqual(chrono.Date().calendar, chrono.calendar.ISOCalendar)

    def test_date(self):
        "Date.__init__() with Date instance parameter copies attributes"

        self.assertEquals(
            chrono.Date(chrono.Date("2009-12-27")).get(),
            (2009, 12, 27)
        )

    def test_datetime_date(self):
        "Date.__init__() with datetime.date instance parameter copies attrs"

        self.assertEquals(
            chrono.Date(datetime.date(2009, 12, 27)).get(),
            (2009, 12, 27)
        )

    def test_datetime_datetime(self):
        "Date.__init__() with datetime.datetime instance copies attrs"

        self.assertEquals(
            chrono.Date(datetime.datetime(2009, 12, 27, 16, 27, 43)).get(),
            (2009, 12, 27)
        )

    def test_default(self):
        "Date.__init__() without parameters sets up empty date"

        self.assertRaises(chrono.error.NoDateTimeError, chrono.Date().get)

    def test_integer(self):
        "Date.__init__() with integer parameter assumes UNIX timestamp"

        self.assertEquals(chrono.Date(1261892718).get(), (2009, 12, 27))

    def test_kwargs(self):
        "Date.__init__() accepts keyword arguments"

        self.assertEquals(
            chrono.Date(year=2009, month=12, day=27).get(),
            (2009, 12, 27)
        )

    def test_kwargs_date(self):
        "Date.__init__() uses date over kwargs"

        self.assertEquals(
            chrono.Date("2009-12-27", year=2009, month=12, day=26).get(),
            (2009, 12, 27)
        )

    def test_kwargs_partial(self):
        "Date.__init__() raises proper error on partial kwargs"

        self.assertRaises(chrono.YearError, chrono.Date, month=7, day=23)
        self.assertRaises(chrono.MonthError, chrono.Date, year=2010, day=23)
        self.assertRaises(chrono.DayError, chrono.Date, year=2010, month=7)

    def test_none(self):
        "Date.__init__() with none sets up empty date"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.Date(None).get
        )

    def test_parser(self):
        "Date.__init__() takes parser as input"

        p = chrono.parser.ISOParser

        d = chrono.Date("2009-07-23", p)

        self.assertEqual(d.get(), (2009, 7, 23))
        self.assertEqual(d.parser, p)

    def test_parser_default(self):
        "Date.__init__() defaults to CommonParser"

        d = chrono.Date("2009-07-23")

        self.assertEqual(d.get(), (2009, 7, 23))
        self.assertEqual(d.parser, chrono.parser.CommonParser)

    def test_string(self):
        "Date.__init__() parses strings"

        self.assertEquals(chrono.Date("2009-12-27").get(), (2009, 12, 27))

    def test_struct_time(self):
        "Date.__init__() accepts struct_time input"

        self.assertEquals(
            chrono.Date(time.localtime(1261892718)).get(),
            (2009, 12, 27)
        )

    def test_true(self):
        "Date.__init__() with True parameter uses current date"

        dt = datetime.date.today()

        self.assertEquals(
            chrono.Date(True).get(),
            (dt.year, dt.month, dt.day)
        )

    def test_unknown(self):
        "Date.__init__() raises TypeError on unknown type"

        self.assertRaises(TypeError, chrono.Date, [])


class Date__leTest(unittest.TestCase):

    def test_date(self):
        "Date.__le__() handles Date objects"

        self.assertTrue(chrono.Date("2009-12-26") <= chrono.Date("2009-12-27"))
        self.assertTrue(chrono.Date("2009-12-27") <= chrono.Date("2009-12-27"))
        self.assertFalse(
            chrono.Date("2009-12-28") <= chrono.Date("2009-12-27")
        )

    def test_datetime(self):
        "Date.__le__() handles DateTime objects"

        self.assertTrue(
            chrono.Date("2009-12-26") <= chrono.DateTime("2009-12-26 00:00:00")
        )
        self.assertTrue(
            chrono.Date("2009-12-26") <= chrono.DateTime("2009-12-26 16:27:43"))
        self.assertFalse(
            chrono.Date("2009-12-27") <= chrono.DateTime("2009-12-26 16:26:43")
        )

    def test_none(self):
        "Date.__le__() handles None"

        self.assertTrue(chrono.Date() <= None)
        self.assertFalse(chrono.Date("2009-12-27") <= None)

    def test_string(self):
        "Date.__le__() handles strings"

        self.assertTrue(chrono.Date("2009-12-27") <= "2009-12-27")
        self.assertTrue(chrono.Date("2009-12-27") <= "2009-12-28")
        self.assertFalse(chrono.Date("2009-12-27") <= "2009-12-26")


class Date__ltTest(unittest.TestCase):

    def test_date(self):
        "Date.__lt__() handles Date objects"

        self.assertTrue(chrono.Date("2009-12-26") < chrono.Date("2009-12-27"))
        self.assertFalse(chrono.Date("2009-12-27") < chrono.Date("2009-12-27"))
        self.assertFalse(chrono.Date("2009-12-28") < chrono.Date("2009-12-27"))

    def test_datetime(self):
        "Date.__lt__() handles DateTime objects"

        self.assertTrue(
            chrono.Date("2009-12-26") < chrono.DateTime("2009-12-26 16:27:43")
        )
        self.assertFalse(
            chrono.Date("2009-12-27") < chrono.DateTime("2009-12-27 00:00:00")
        )
        self.assertFalse(
            chrono.Date("2009-12-28") < chrono.DateTime("2009-12-27 16:27:43")
        )

    def test_none(self):
        "Date.__lt__() handles None"

        self.assertFalse(chrono.Date("2009-12-27") < None)
        self.assertFalse(chrono.Date() < None)

    def test_string(self):
        "Date.__lt__() handles strings"

        self.assertTrue(chrono.Date("2009-12-26") < "2009-12-27")
        self.assertFalse(chrono.Date("2009-12-27") < "2009-12-27")
        self.assertFalse(chrono.Date("2009-12-28") < "2009-12-27")


class Date__neTest(unittest.TestCase):

    def test_date(self):
        "Date.__ne__() handles Date objects"

        self.assertTrue(chrono.Date("2009-12-27") != chrono.Date("2009-12-26"))
        self.assertFalse(
            chrono.Date("2009-12-27") != chrono.Date("2009-12-27")
        )

    def test_datetime(self):
        "Date.__ne__() handles DateTime objects"

        self.assertTrue(
            chrono.Date("2009-12-27") != chrono.DateTime("2009-12-27 16:27:43")
        )
        self.assertFalse(
            chrono.Date("2009-12-27") != chrono.DateTime("2009-12-27 00:00:00")
        )

    def test_none(self):
        "Date.__ne__() handles None"

        self.assertTrue(chrono.Date("2009-12-27") != None)
        self.assertFalse(chrono.Date() != None)

    def test_string(self):
        "Date.__ne__() handles strings"

        self.assertTrue(chrono.Date("2009-12-27") != "2009-12-26")
        self.assertFalse(chrono.Date("2009-12-27") != "2009-12-27")


class Date__reprTest(unittest.TestCase):

    def test_empty(self):
        "Date.__repr__() handles empty dates"

        self.assertEquals(repr(chrono.Date()), "chrono.Date()")

    def test_partial(self):
        "Date.__repr__() handles partial dates"

        d = chrono.Date("2010-07-23")
        d.month = None

        self.assertEquals(repr(d), "chrono.Date(year=2010, day=23)")

    def test_repr(self):
        "Date.__repr__() shows code to recreate object"

        self.assertEquals(
            repr(chrono.Date("2009-12-27")),
            "chrono.Date(year=2009, month=12, day=27)"
        )


class Date__setattrTest(unittest.TestCase):

    def test_day_negative(self):
        "Date.__setattr__() handles month rollunder for negative days"

        d = chrono.Date("2009-07-15")
        d.day -= 20

        self.assertEquals(d.get(), (2009, 6, 25))

    def test_day_negative_doublemonth(self):
        "Date.__setattr__() handles double month rollunder for negative days"

        d = chrono.Date("2009-07-15")
        d.day -= 50

        self.assertEquals(d.get(), (2009, 5, 26))

    def test_day_negative_leap(self):
        "Date.__setattr__() handles leap years for negative days"

        d = chrono.Date("2008-03-01")
        d.day -= 2

        self.assertEquals(d.get(), (2008, 2, 28))

    def test_day_negative_year(self):
        "Date.__setattr__() handles year rollunder for negative days"

        d = chrono.Date("2009-02-03")
        d.day -= 90

        self.assertEquals(d.get(), (2008, 11, 5))

    def test_day_overflow(self):
        "Date.__setattr__() handles month rollover for day overflow"

        d = chrono.Date("2009-07-15")
        d.day += 20

        self.assertEquals(d.get(), (2009, 8, 4))

    def test_day_overflow_doublemonth(self):
        "Date.__setattr__() handles double month rollover for day overflow"

        d = chrono.Date("2009-07-15")
        d.day += 50

        self.assertEquals(d.get(), (2009, 9, 3))

    def test_day_overflow_leap(self):
        "Date.__setattr__() handles leap years for day overflow"

        d = chrono.Date("2008-02-28")
        d.day += 2

        self.assertEquals(d.get(), (2008, 3, 1))

    def test_day_overflow_year(self):
        "Date.__setattr__() handles year rollover for day overflow"

        d = chrono.Date("2009-11-15")
        d.day += 90

        self.assertEquals(d.get(), (2010, 2, 13))

    def test_day_zero(self):
        "Date.__setattr__() handles rollunder for zero-days"

        d = chrono.Date("2008-06-01")
        d.day = 0

        self.assertEquals(d.get(), (2008, 5, 31))

    def test_day_zero_leap(self):
        "Date.__setattr__() handles leap years for zero-days"

        d = chrono.Date("2008-03-01")
        d.day = 0

        self.assertEquals(d.get(), (2008, 2, 29))

    def test_day_zero_year(self):
        "Date.__setattr__() handles year rollunder for zero-days"

        d = chrono.Date("2009-01-20")
        d.day = 0

        self.assertEquals(d.get(), (2008, 12, 31))

    def test_month_dayoverflow(self):
        "Date.__setattr__() handles days outside new month range"

        d = chrono.Date("2009-07-31")
        d.month -= 1

        self.assertEquals(d.get(), (2009, 7, 1))

    def test_month_negative(self):
        "Date.__setattr__() handles year rollunder for negative months"

        d = chrono.Date("2009-04-15")
        d.month -= 6

        self.assertEquals(d.get(), (2008, 10, 15))

    def test_month_negative_doublemonth(self):
        "Date.__setattr__() handles double year rollunder for negative months"

        d = chrono.Date("2009-07-15")
        d.month -= 30

        self.assertEquals(d.get(), (2007, 1, 15))

    def test_month_negative_leap(self):
        "Date.__setattr__() handles leap years for negative months"

        d = chrono.Date("2008-02-29")
        d.month -= 12

        self.assertEquals(d.get(), (2007, 3, 1))

    def test_month_overflow(self):
        "Date.__setattr__() handles year rollover for month overflow"

        d = chrono.Date("2009-07-15")
        d.month += 10

        self.assertEquals(d.get(), (2010, 5, 15))

    def test_month_overflow_doubleyear(self):
        "Date.__setattr__() handles double year rollover for month overflow"

        d = chrono.Date("2009-03-15")
        d.month += 30

        self.assertEquals(d.get(), (2011, 9, 15))

    def test_month_overflow_leap(self):
        "Date.__setattr__() handles leap years for month overflow"

        d = chrono.Date("2008-02-29")
        d.month += 12

        self.assertEquals(d.get(), (2009, 3, 1))

    def test_month_zero(self):
        "Date.__setattr__() handles rollunder for zero-months"

        d = chrono.Date("2008-06-21")
        d.month = 0

        self.assertEquals(d.get(), (2007, 12, 21))

    def test_year_invalid(self):
        "Date.__setattr__() raises YearError on year outside range (1-9999)"

        d = chrono.Date("2008-12-27")

        self.assertRaises(chrono.YearError, setattr, d, "year", 10000)

    def test_year_leap(self):
        "Date.__setattr__() handles leap years when changing year"

        d = chrono.Date("2008-02-29")
        d.year = 2009

        self.assertEquals(d.get(), (2009, 3, 1))


class Date__strTest(unittest.TestCase):

    def test_empty(self):
        "Date.__str__() handles empty dates"

        self.assertEquals(str(chrono.Date()), "")

    def test_str(self):
        "Date.__str__() returns iso date"

        self.assertEquals(str(chrono.Date("2009-12-27")), "2009-12-27")


class Time_assert_setTest(unittest.TestCase):

    def test_empty(self):
        "Date.assert_set() raises NoDateTimeError on empty date"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.Date().assert_set
        )

    def test_full(self):
        "Date.assert_set() doesn't raise exception on date"

        chrono.Date("2010-07-23").assert_set()

    def test_partial(self):
        "Date.assert_set() raises NoDateTimeError on partial date"

        d = chrono.Date("2010-07-23")
        d.day = None

        self.assertRaises(chrono.error.NoDateTimeError, d.assert_set)


class Date_clearTest(unittest.TestCase):

    def test_clear(self):
        "Date.clear() clears date attributes"

        d = chrono.Date("2009-12-27")
        d.clear()

        self.assertEquals(d.year, None)
        self.assertEquals(d.month, None)
        self.assertEquals(d.day, None)


class Date_formatTest(unittest.TestCase):

    def test_empty(self):
        "Date.format() raises NoDateTimeError if no date is set"

        self.assertRaises(
            chrono.error.NoDateTimeError,
            chrono.Date().format, "$0year-$0month-0day"
        )

    def test_format(self):
        "Date.format() formats date using Formatter"

        self.assertEquals(
            chrono.Date(1261892718).format("$0year-$0month-$0day"),
            "2009-12-27"
        )


class Date_getTest(unittest.TestCase):

    def test_empty(self):
        "Date.get() raises NoDateTimeError if date isn't set"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.Date().get
        )

    def test_get(self):
        "Date.get() returns tuple of year, month, and day"

        self.assertEquals(chrono.Date("2009-12-27").get(), (2009, 12, 27))


class Date_get_datetimeTest(unittest.TestCase):

    def test_datetime(self):
        "Date.get_datetime() returns a datetime.date instance"

        dt = chrono.Date("2009-12-27").get_datetime()

        self.assertTrue(isinstance(dt, datetime.date))

        self.assertEquals(dt.year, 2009)
        self.assertEquals(dt.month, 12)
        self.assertEquals(dt.day, 27)

    def test_empty(self):
        "Date.get_datetime() raises NoDateTimeError on empty date"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.Date().get_datetime
        )


class Date_get_stringTest(unittest.TestCase):

    def test_empty(self):
        "Date.get_string() raises NoDateTimeError on empty date"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.Date().get_string
        )

    def test_string(self):
        "Date.get_string() returns date string"

        self.assertEquals(chrono.Date("2009-12-27").get_string(), "2009-12-27")


class Date_get_struct_timeTest(unittest.TestCase):

    def test_empty(self):
        "Date.get_struct_time() raises NoDateTimeError if date isn't set"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.Date().get_struct_time
        )

    def test_struct_time(self):
        "Date.get_struct_time() returns a proper struct_time"

        s = chrono.Date("2009-12-27").get_struct_time()

        self.assertTrue(isinstance(s, time.struct_time))

        self.assertEquals(s.tm_year, 2009)
        self.assertEquals(s.tm_mon, 12)
        self.assertEquals(s.tm_mday, 27)
        self.assertEquals(s.tm_hour, 0)
        self.assertEquals(s.tm_min, 0)
        self.assertEquals(s.tm_sec, 0)
        self.assertEquals(s.tm_wday, 6)
        self.assertEquals(s.tm_yday, 361)
        self.assertEquals(s.tm_isdst, -1)


class Date_get_unixTest(unittest.TestCase):

    def test_empty(self):
        "Date.get_unix() raises NoDateTimeError if date isn't set"

        self.assertRaises(chrono.error.NoDateTimeError, chrono.Date().get_unix)

    def test_unix(self):
        "Date.get_unix() returns unix timestamp"

        self.assertEquals(chrono.Date("2009-12-27").get_unix(), 1261846800)


class Date_is_setTest(unittest.TestCase):

    def test_empty(self):
        "Date.is_set() returns False if no attributes are set"

        self.assertFalse(chrono.Date().is_set())

    def test_partial(self):
        "Date.is_set() returns False if only some attributes are set"

        d = chrono.Date()
        d.year = 2009
        d.day = 27

        self.assertFalse(d.is_set())

    def test_set(self):
        "Date.is_set() returns True if date is set"

        self.assertTrue(chrono.Date(True).is_set())


class Date_leapyearTest(unittest.TestCase):

    def test_empty(self):
        "Date.leapyear() raises NoDateTimeError if date isn't set"

        self.assertRaises(chrono.error.NoDateTimeError, chrono.Date().leapyear)

    def test_leap(self):
        "Date.leapyear() returns True for 2008"

        self.assertTrue(chrono.Date("2008-01-01").leapyear())

    def test_normal(self):
        "Date.leapyear() returns False for 2009"

        self.assertFalse(chrono.Date("2009-01-01").leapyear())


class Date_monthdaysTest(unittest.TestCase):

    def test_empty(self):
        "Date.monthdays() raises NoDateTimeError if date isn't set"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.Date().monthdays
        )

    def test_monthdays(self):
        "Date.monthdays() returns 29 for 2008-02"

        self.assertEquals(chrono.Date("2008-02-01").monthdays(), 29)


class Date_ordinalTest(unittest.TestCase):

    def test_empty(self):
        "Date.ordinal() raises NoDateTimeError if date isn't set"

        self.assertRaises(chrono.error.NoDateTimeError, chrono.Date().ordinal)

    def test_ordinal(self):
        "Date.ordinal() returns 366 for 2008-12-31"

        self.assertEquals(chrono.Date("2008-12-31").ordinal(), 366)


class Date_setTest(unittest.TestCase):

    def test_invalid_date(self):
        "Date.set() raises proper date on invalid date"

        d = chrono.Date()

        self.assertRaises(chrono.error.YearError, d.set, 10000, 7, 23)
        self.assertRaises(chrono.error.MonthError, d.set, 2010, 13, 23)
        self.assertRaises(chrono.error.DayError, d.set, 2010, 7, 32)

    def test_replace(self):
        "Date.set() replaces set date"

        d = chrono.Date("2009-07-21")
        d.set(2009, 12, 27)

        self.assertEquals(d.get(), (2009, 12, 27))

    def test_set(self):
        "Date.set() sets the date"

        d = chrono.Date()
        d.set(2009, 12, 27)

        self.assertEquals(d.get(), (2009, 12, 27))


class Date_set_datetimeTest(unittest.TestCase):

    def test_set(self):
        "Date.set_datetime() sets date from datetime.date object"

        d = chrono.Date()
        d.set_datetime(datetime.date(2009, 12, 27))

        self.assertEquals(d.get(), (2009, 12, 27))


class Date_set_nowTest(unittest.TestCase):

    def test_now(self):
        "Date.set_now() sets date to current date"

        d = chrono.Date()
        d.set_now()

        dt = datetime.date.today()

        self.assertEquals(d.get(), (dt.year, dt.month, dt.day))


class Date_set_stringTest(unittest.TestCase):

    def test_invalid(self):
        "Date.set_string() raises proper error on invalid values"

        d = chrono.Date()

        self.assertRaises(chrono.error.YearError, d.set_string, "0000-07-23")
        self.assertRaises(chrono.error.MonthError, d.set_string, "2010-13-23")
        self.assertRaises(chrono.error.DayError, d.set_string, "2010-07-32")

    def test_string(self):
        "Date.set_string() sets date from string"

        d = chrono.Date()

        d.set_string("2010-07-23")

        self.assertEqual(d.get(), (2010, 7, 23))


class Date_set_struct_timeTest(unittest.TestCase):

    def test_struct_time(self):
        "Date.set_struct_time() sets date from a struct_time"

        d = chrono.Date()
        d.set_struct_time(time.localtime(1261892718))

        self.assertEquals(d.get(), (2009, 12, 27))


class Date_set_unixText(unittest.TestCase):

    def test_invalid_type(self):
        "Date.set_unix() raises TypeError on invalid type"

        self.assertRaises(TypeError, chrono.Date().set_unix, None)

    def test_invalid(self):
        "Date.set_unix() raises ValueError for invalid values"

        self.assertRaises(ValueError, chrono.Date().set_unix, "abc")

    def test_set(self):
        "Date.set_unix() sets date from UNIX timestamp"

        d = chrono.Date()
        d.set_unix(1261892718)

        self.assertEquals(d.get(), (2009, 12, 27))


class Date_weekTest(unittest.TestCase):

    def test_empty(self):
        "Date.week() raises NoDateTimeError if date isn't set"

        self.assertRaises(chrono.error.NoDateTimeError, chrono.Date().week)

    def test_week(self):
        "Date.week() returns 2009-W53 for 2010-01-01"

        self.assertEquals(chrono.Date("2010-01-01").week(), (2009, 53))


class Date_weekdateTest(unittest.TestCase):

    def test_empty(self):
        "Date.weekdate() raises NoDateTimeError if date isn't set"

        self.assertRaises(chrono.error.NoDateTimeError, chrono.Date().weekdate)

    def test_weekdate(self):
        "Date.weekdate() returns 2009-W30-2 for 2009-07-21"

        self.assertEquals(
            chrono.Date("2009-07-21").weekdate(),
            (2009, 30, 2)
        )


class Date_weekdayTest(unittest.TestCase):

    def test_empty(self):
        "Date.weekday() raises NoDateTimeError if date isn't set"

        self.assertRaises(chrono.error.NoDateTimeError, chrono.Date().weekday)

    def test_weekday(self):
        "Date.weekday() returns 7 for 2009-12-27"

        self.assertEquals(chrono.Date("2009-12-27").weekday(), 7)


class Date_weeksTest(unittest.TestCase):

    def test_empty(self):
        "Date.weeks() raises NoDateTimeError if date isn't set"

        self.assertRaises(chrono.error.NoDateTimeError, chrono.Date().weeks)

    def test_weeks(self):
        "Date.weeks() returns 53 for 2009"

        self.assertEquals(chrono.Date("2009-07-15").weeks(), 53)


class Date_yeardaysTest(unittest.TestCase):

    def test_empty(self):
        "Date.yeardays() raises NoDateTimeError if date isn't set"

        self.assertRaises(chrono.error.NoDateTimeError, chrono.Date().yeardays)

    def test_yeardays(self):
        "Date.yeardays() returns 366 for 2008"

        self.assertEquals(chrono.Date("2008-01-01").yeardays(), 366)


if __name__ == "__main__":
    unittest.main()
