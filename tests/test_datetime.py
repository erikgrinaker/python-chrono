#!/usr/bin/env python

import chrono
import datetime
import unittest
import time


class DateTime__cmpTest(unittest.TestCase):

    def test_equal(self):
        "DateTime.__cmp__() handles equality"

        self.assertTrue(
                chrono.DateTime("2009-12-27 16:27:43") == \
                chrono.DateTime("2009-12-27 16:27:43")
        )

    def test_gt(self):
        "DateTime.__cmp__() handles > comparison"

        self.assertTrue(
                chrono.DateTime("2009-12-28 16:27:43") > \
                chrono.DateTime("2009-12-27 16:27:43")
        )

    def test_lt(self):
        "DateTime.__cmp__() handles < comparison"

        self.assertTrue(
            chrono.DateTime("2009-12-27 16:27:43") < \
            chrono.DateTime("2009-12-27 17:27:43")
        )

    def test_none_equal(self):
        "DateTime.__cmp__() handles equality with None"

        self.assertTrue(chrono.DateTime() == None)

    def test_none_gt(self):
        "DateTime.__cmp__() handles > comparison with None"

        self.assertTrue(chrono.DateTime("2009-12-28 16:26:47") > None)

    def test_none_lt(self):
        "DateTime.__cmp__() handles < comparison with None"

        self.assertFalse(chrono.DateTime() < None)

    def test_string_equal(self):
        "DateTime.__cmp__() handles equality with strings"

        self.assertTrue(
            chrono.DateTime("2009-12-27 16:27:43") == "2009-12-27 16:27:43"
        )

    def test_string_gt(self):
        "DateTime.__cmp__() handles > comparison with strings"

        self.assertTrue(
            chrono.DateTime("2009-12-28 16:27:43") > "2009-12-27 16:26:43"
        )

    def test_string_lt(self):
        "DateTime.__cmp__() handles < comparison with strings"

        self.assertTrue(
            chrono.DateTime("2009-12-26 16:27:43") < "2009-12-27 16:27:44"
        )


class DateTime__initTest(unittest.TestCase):

    def test_datetime(self):
        "DateTime.__init__() with DateTime parameter copies attributes"

        self.assertEquals(
            chrono.DateTime(chrono.DateTime("2009-12-27 16:27:43")).get(),
            (2009, 12, 27, 16, 27, 43)
        )

    def test_datetime_datetime(self):
        "DateTime.__init__() with datetime.datetime parameter copies attrs"

        self.assertEquals(
            chrono.DateTime(datetime.datetime(2010, 7, 23, 16, 27, 43)).get(),
            (2010, 7, 23, 16, 27, 43)
        )

    def test_default(self):
        "DateTime.__init__() without parameters sets up empty datetime"

        self.assertRaises(chrono.error.NoDateTimeError, chrono.DateTime().get)

    def test_integer(self):
        "DateTime.__init__() with integer parameter assumes UNIX timestamp"

        self.assertEquals(
            chrono.DateTime(1261892718).get(),
            (2009, 12, 27, 12, 45, 18)
        )

    def test_kwargs(self):
        "DateTime.__init__() accepts keyword arguments"

        self.assertEquals(
            chrono.DateTime(
                year=2010, month=7, day=23, hour=16, minute=27, second=43
            ).get(),
            (2010, 7, 23, 16, 27, 43)
        )

    def test_kwargs_datetime(self):
        "DateTime.__init__() uses date over kwargs"

        self.assertEquals(
            chrono.DateTime(
                "2010-07-23 16:27:43",
                year=2010, month=1, day=20, hour=1, minute=48, second=21
            ).get(),
            (2010, 7, 23, 16, 27, 43)
        )

    def test_kwargs_partial(self):
        "DateTime.__init__() raises proper error on partial kwargs"

        self.assertRaises(
            chrono.YearError,
            chrono.DateTime, month=7, day=23, hour=16, minute=27, second=43
        )

        self.assertRaises(
            chrono.MonthError,
            chrono.DateTime, year=2010, day=23, hour=16, minute=27, second=43
        )

        self.assertRaises(
            chrono.DayError,
            chrono.DateTime, year=2010, month=7, hour=16, minute=27, second=43
        )

        self.assertRaises(
            chrono.HourError,
            chrono.DateTime, year=2010, month=7, day=23, minute=27, second=43
        )

        self.assertRaises(
            chrono.MinuteError,
            chrono.DateTime, year=2010, month=7, day=23, hour=16, second=43
        )

        self.assertRaises(
            chrono.SecondError,
            chrono.DateTime, year=2010, month=7, day=23, hour=16, minute=27
        )

    def test_none(self):
        "DateTime.__init__() with none sets up empty date"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.DateTime(None).get
        )

    def test_string(self):
        "DateTime.__init__() parses strings"

        self.assertEquals(
            chrono.DateTime("2010-07-23 16:27:43").get(),
            (2010, 7, 23, 16, 27, 43)
        )

    def test_struct_time(self):
        "DateTime.__init__() accepts struct_time input"

        self.assertEquals(
            chrono.DateTime(time.localtime(1261892718)).get(),
            (2009, 12, 27, 12, 45, 18)
        )

    def test_true(self):
        "DateTime.__init__() with True parameter uses current date"

        dt = datetime.datetime.now()

        self.assertEquals(
            chrono.DateTime(True).get(),
            (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
        )

    def test_unknown(self):
        "DateTime.__init__() raises TypeError on unknown type"

        self.assertRaises(TypeError, chrono.DateTime, [])


class DateTime__reprTest(unittest.TestCase):

    def test_empty(self):
        "DateTime.__repr__() handles empty dates"

        self.assertEquals(repr(chrono.DateTime()), "chrono.DateTime()")

    def test_partial(self):
        "DateTime.__repr__() handles partial dates"

        d = chrono.DateTime("2010-07-23 16:27:43")
        d.month = None

        self.assertEquals(
            repr(d),
            "chrono.DateTime(year=2010, day=23, hour=16, minute=27, second=43)"
        )

    def test_repr(self):
        "DateTime.__repr__() shows code to recreate object"

        self.assertEquals(
            repr(chrono.DateTime("2010-07-23 16:27:43")),
            "chrono.DateTime(year=2010, month=7, day=23, hour=16, " + \
            "minute=27, second=43)"
        )


class DateTime__setattrTest(unittest.TestCase):

    def test_day_negative(self):
        "DateTime.__setattr__() handles month rollunder for negative days"

        d = chrono.DateTime("2009-07-15 16:27:43")
        d.day -= 20

        self.assertEquals(d.get(), (2009, 6, 25, 16, 27, 43))

    def test_day_negative_doublemonth(self):
        "DateTime.__setattr__() handles double rollunder for negative days"

        d = chrono.DateTime("2009-07-15 16:27:43")
        d.day -= 50

        self.assertEquals(d.get(), (2009, 5, 26, 16, 27, 43))

    def test_day_negative_leap(self):
        "DateTime.__setattr__() handles leap years for negative days"

        d = chrono.DateTime("2008-03-01 16:27:43")
        d.day -= 2

        self.assertEquals(d.get(), (2008, 2, 28, 16, 27, 43))

    def test_day_negative_year(self):
        "DateTime.__setattr__() handles year rollunder for negative days"

        d = chrono.DateTime("2009-02-03 16:27:43")
        d.day -= 90

        self.assertEquals(d.get(), (2008, 11, 5, 16, 27, 43))

    def test_day_overflow(self):
        "DateTime.__setattr__() handles month rollover for day overflow"

        d = chrono.DateTime("2009-07-15 16:27:43")
        d.day += 20

        self.assertEquals(d.get(), (2009, 8, 4, 16, 27, 43))

    def test_day_overflow_doublemonth(self):
        "DateTime.__setattr__() handles double month rollover for day overflow"

        d = chrono.DateTime("2009-07-15 16:27:43")
        d.day += 50

        self.assertEquals(d.get(), (2009, 9, 3, 16, 27, 43))

    def test_day_overflow_leap(self):
        "DateTime.__setattr__() handles leap years for day overflow"

        d = chrono.DateTime("2008-02-28 16:27:43")
        d.day += 2

        self.assertEquals(d.get(), (2008, 3, 1, 16, 27, 43))

    def test_day_overflow_year(self):
        "DateTime.__setattr__() handles year rollover for day overflow"

        d = chrono.DateTime("2009-11-15 16:27:43")
        d.day += 90

        self.assertEquals(d.get(), (2010, 2, 13, 16, 27, 43))

    def test_day_zero(self):
        "DateTime.__setattr__() handles rollunder for zero-days"

        d = chrono.DateTime("2008-06-01 16:27:43")
        d.day = 0

        self.assertEquals(d.get(), (2008, 5, 31, 16, 27, 43))

    def test_day_zero_leap(self):
        "DateTime.__setattr__() handles leap years for zero-days"

        d = chrono.DateTime("2008-03-01 16:27:43")
        d.day = 0

        self.assertEquals(d.get(), (2008, 2, 29, 16, 27, 43))

    def test_day_zero_year(self):
        "DateTime.__setattr__() handles year rollunder for zero-days"

        d = chrono.DateTime("2009-01-20 16:27:43")
        d.day = 0

        self.assertEquals(d.get(), (2008, 12, 31, 16, 27, 43))

    def test_hour_negative(self):
        "DateTime.__setattr__() handles hour rollunder"

        d = chrono.DateTime("2010-07-23 16:27:43")
        d.hour -= 20

        self.assertEquals(d.get(), (2010, 7, 22, 20, 27, 43))

    def test_hour_negative_double(self):
        "DateTime.__setattr__() handles double hour rollunder"

        d = chrono.DateTime("2010-07-23 16:27:43")
        d.hour -= 44

        self.assertEquals(d.get(), (2010, 7, 21, 20, 27, 43))

    def test_hour_overflow(self):
        "DateTime.__setattr__() handles hour rollover"

        d = chrono.DateTime("2010-07-23 16:27:43")
        d.hour += 10

        self.assertEquals(d.get(), (2010, 7, 24, 2, 27, 43))

    def test_hour_overflow_double(self):
        "DateTime.__setattr__() handles double hour rollover"

        d = chrono.DateTime("2010-07-23 16:27:43")
        d.hour += 34

        self.assertEquals(d.get(), (2010, 7, 25, 2, 27, 43))

    def test_minute_negative(self):
        "DateTime.__setattr__() handles hour rollunder for negative minutes"

        d = chrono.DateTime("2010-07-23 16:27:43")
        d.minute -= 30

        self.assertEquals(d.get(), (2010, 7, 23, 15, 57, 43))

    def test_minute_negative_doublehour(self):
        "DateTime.__setattr__() handles double rollunder for negative minutes"

        d = chrono.DateTime("2010-07-23 16:27:43")
        d.minute -= 120

        self.assertEquals(d.get(), (2010, 7, 23, 14, 27, 43))

    def test_minute_overflow(self):
        "DateTime.__setattr__() handles hour rollover for minute overflow"

        d = chrono.DateTime("2010-07-23 16:27:43")
        d.minute += 45

        self.assertEquals(d.get(), (2010, 7, 23, 17, 12, 43))

    def test_minute_overflow_doublehour(self):
        "DateTime.__setattr__() handles double rollover for minute overflow"

        d = chrono.DateTime("2010-07-23 16:27:43")
        d.minute += 120

        self.assertEquals(d.get(), (2010, 7, 23, 18, 27, 43))

    def test_month_dayoverflow(self):
        "DateTime.__setattr__() handles days outside new month range"

        d = chrono.DateTime("2009-07-31 16:27:43")
        d.month -= 1

        self.assertEquals(d.get(), (2009, 7, 1, 16, 27, 43))

    def test_month_negative(self):
        "DateTime.__setattr__() handles year rollunder for negative months"

        d = chrono.DateTime("2009-04-15 16:27:43")
        d.month -= 6

        self.assertEquals(d.get(), (2008, 10, 15, 16, 27, 43))

    def test_month_negative_doublemonth(self):
        "DateTime.__setattr__() handles double rollunder for negative months"

        d = chrono.DateTime("2009-07-15 16:27:43")
        d.month -= 30

        self.assertEquals(d.get(), (2007, 1, 15, 16, 27, 43))

    def test_month_negative_leap(self):
        "DateTime.__setattr__() handles leap years for negative months"

        d = chrono.DateTime("2008-02-29 16:27:43")
        d.month -= 12

        self.assertEquals(d.get(), (2007, 3, 1, 16, 27, 43))

    def test_month_overflow(self):
        "DateTime.__setattr__() handles year rollover for month overflow"

        d = chrono.DateTime("2009-07-15 16:27:43")
        d.month += 10

        self.assertEquals(d.get(), (2010, 5, 15, 16, 27, 43))

    def test_month_overflow_doubleyear(self):
        "DateTime.__setattr__() handles double rollover for month overflow"

        d = chrono.DateTime("2009-03-15 16:27:43")
        d.month += 30

        self.assertEquals(d.get(), (2011, 9, 15, 16, 27, 43))

    def test_month_overflow_leap(self):
        "DateTime.__setattr__() handles leap years for month overflow"

        d = chrono.DateTime("2008-02-29 16:27:43")
        d.month += 12

        self.assertEquals(d.get(), (2009, 3, 1, 16, 27, 43))

    def test_month_zero(self):
        "DateTime.__setattr__() handles rollunder for zero-months"

        d = chrono.DateTime("2008-06-21 16:27:43")
        d.month = 0

        self.assertEquals(d.get(), (2007, 12, 21, 16, 27, 43))

    def test_second_negative(self):
        "DateTime.__setattr__() handles minute rollunder for negative seconds"

        d = chrono.DateTime("2010-07-23 16:27:43")
        d.second -= 60

        self.assertEquals(d.get(), (2010, 7, 23, 16, 26, 43))

    def test_second_negative_doubleminute(self):
        "DateTime.__setattr__() handles double rollunder for negative secs"

        d = chrono.DateTime("2010-07-23 16:27:43")
        d.second -= 120

        self.assertEquals(d.get(), (2010, 7, 23, 16, 25, 43))

    def test_second_negative_hour(self):
        "DateTime.__setattr__() handles hour rollunder for negative seconds"

        d = chrono.DateTime("2010-07-23 16:27:43")
        d.second -= 1800

        self.assertEquals(d.get(), (2010, 7, 23, 15, 57, 43))

    def test_second_overflow(self):
        "DateTime.__setattr__() handles minute rollover for second overflow"

        d = chrono.DateTime("2010-07-23 16:27:43")
        d.second += 45

        self.assertEquals(d.get(), (2010, 7, 23, 16, 28, 28))

    def test_second_overflow_doubleminute(self):
        "DateTime.__setattr__() handles double rollover for second overflow"

        d = chrono.DateTime("2010-07-23 16:27:43")
        d.second += 120

        self.assertEquals(d.get(), (2010, 7, 23, 16, 29, 43))

    def test_second_overflow_hour(self):
        "DateTime.__setattr__() handles hour rollover for second overflow"

        d = chrono.DateTime("2010-07-23 16:27:43")
        d.second += 3600

        self.assertEquals(d.get(), (2010, 7, 23, 17, 27, 43))

    def test_year_invalid(self):
        "DateTime.__setattr__() raises YearError on year outside range 1-9999"

        d = chrono.DateTime("2008-12-27 16:27:43")

        self.assertRaises(chrono.YearError, setattr, d, "year", 10000)

    def test_year_leap(self):
        "DateTime.__setattr__() handles leap years when changing year"

        d = chrono.DateTime("2008-02-29 16:27:43")
        d.year = 2009

        self.assertEquals(d.get(), (2009, 3, 1, 16, 27, 43))


class DateTime__strTest(unittest.TestCase):

    def test_empty(self):
        "DateTime.__str__() handles empty dates"

        self.assertEquals(str(chrono.DateTime()), "")

    def test_str(self):
        "DateTime.__str__() returns iso date"

        self.assertEquals(
            str(chrono.DateTime("2009-12-27 16:27:43")),
            "2009-12-27 16:27:43"
        )


class Time_assert_setTest(unittest.TestCase):

    def test_empty(self):
        "DateTime.assert_set() raises NoDateTimeError on empty date"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.DateTime().assert_set
        )

    def test_full(self):
        "DateTime.assert_set() doesn't raise exception on date"

        chrono.DateTime("2010-07-23 16:27:43").assert_set()

    def test_partial(self):
        "DateTime.assert_set() raises NoDateTimeError on partial date"

        d = chrono.DateTime("2010-07-23 16:27:43")
        d.day = None

        self.assertRaises(chrono.error.NoDateTimeError, d.assert_set)


class DateTime_clearTest(unittest.TestCase):

    def test_clear(self):
        "DateTime.clear() clears date attributes"

        d = chrono.DateTime("2009-12-27 16:27:43")
        d.clear()

        self.assertEquals(d.year, None)
        self.assertEquals(d.month, None)
        self.assertEquals(d.day, None)
        self.assertEquals(d.hour, None)
        self.assertEquals(d.minute, None)
        self.assertEquals(d.second, None)


class DateTime_formatTest(unittest.TestCase):

    def test_empty(self):
        "DateTime.format() raises NoDateTimeError if no date is set"

        self.assertRaises(
            chrono.error.NoDateTimeError,
            chrono.DateTime().format,
            "$0year-$0month-0day $0hour:$0minute:$0second"
        )

    def test_format(self):
        "DateTime.format() formats date using Formatter"

        self.assertEquals(
            chrono.DateTime(1261892718).format(
                "$0year-$0month-$0day $0hour:$0minute:$0second"
            ),
            "2009-12-27 12:45:18"
        )


class DateTime_getTest(unittest.TestCase):

    def test_empty(self):
        "DateTime.get() raises NoDateTimeError if date isn't set"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.DateTime().get
        )

    def test_get(self):
        "DateTime.get() returns tuple of all attributes"

        self.assertEquals(
                chrono.DateTime("2009-12-27 16:27:43").get(),
            (2009, 12, 27, 16, 27, 43)
        )


class DateTime_get_datetimeTest(unittest.TestCase):

    def test_datetime(self):
        "DateTime.get_datetime() returns a datetime.date instance"

        dt = chrono.DateTime("2009-12-27 16:27:43").get_datetime()

        self.assertTrue(isinstance(dt, datetime.date))

        self.assertEquals(dt.year, 2009)
        self.assertEquals(dt.month, 12)
        self.assertEquals(dt.day, 27)
        self.assertEquals(dt.hour, 16)
        self.assertEquals(dt.minute, 27)
        self.assertEquals(dt.second, 43)

    def test_empty(self):
        "DateTime.get_datetime() raises NoDateTimeError on empty date"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.DateTime().get_datetime
        )


class DateTime_get_stringTest(unittest.TestCase):

    def test_empty(self):
        "DateTime.get_string() raises NoDateTimeError on empty date"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.DateTime().get_string
        )

    def test_string(self):
        "DateTime.get_string() returns date string"

        self.assertEquals(
            chrono.DateTime("2009-12-27 16:27:43").get_string(),
            "2009-12-27 16:27:43"
        )


class DateTime_get_struct_timeTest(unittest.TestCase):

    def test_empty(self):
        "DateTime.get_struct_time() raises NoDateTimeError if date isn't set"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.DateTime().get_struct_time
        )

    def test_struct_time(self):
        "DateTime.get_struct_time() returns a proper struct_time"

        s = chrono.DateTime("2009-12-27 16:27:43").get_struct_time()

        self.assertTrue(isinstance(s, time.struct_time))

        self.assertEquals(s.tm_year, 2009)
        self.assertEquals(s.tm_mon, 12)
        self.assertEquals(s.tm_mday, 27)
        self.assertEquals(s.tm_hour, 16)
        self.assertEquals(s.tm_min, 27)
        self.assertEquals(s.tm_sec, 43)
        self.assertEquals(s.tm_wday, 6)
        self.assertEquals(s.tm_yday, 361)
        self.assertEquals(s.tm_isdst, -1)


class DateTime_get_unixTest(unittest.TestCase):

    def test_empty(self):
        "DateTime.get_unix() raises NoDateTimeError if date isn't set"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.DateTime().get_unix
        )

    def test_unix(self):
        "DateTime.get_unix() returns unix timestamp"

        self.assertEquals(
            chrono.DateTime("2009-12-27 16:27:43").get_unix(), 1261906063
        )


class DateTime_is_setTest(unittest.TestCase):

    def test_empty(self):
        "DateTime.is_set() returns False if no attributes are set"

        self.assertFalse(chrono.DateTime().is_set())

    def test_partial(self):
        "DateTime.is_set() returns False if only some attributes are set"

        d = chrono.DateTime("2010-07-23 16:27:43")
        d.hour = None

        self.assertFalse(d.is_set())

    def test_set(self):
        "DateTime.is_set() returns True if date is set"

        self.assertTrue(chrono.DateTime(True).is_set())


class DateTime_leapyearTest(unittest.TestCase):

    def test_empty(self):
        "DateTime.leapyear() raises NoDateTimeError if date isn't set"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.DateTime().leapyear
        )

    def test_leap(self):
        "DateTime.leapyear() returns True for 2008"

        self.assertTrue(chrono.DateTime("2008-01-01 16:27:43").leapyear())

    def test_normal(self):
        "DateTime.leapyear() returns False for 2009"

        self.assertFalse(chrono.DateTime("2009-01-01 16:27:43").leapyear())


class DateTime_monthdaysTest(unittest.TestCase):

    def test_empty(self):
        "DateTime.monthdays() raises NoDateTimeError if date isn't set"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.DateTime().monthdays
        )

    def test_monthdays(self):
        "DateTime.monthdays() returns 29 for 2008-02"

        self.assertEquals(
            chrono.DateTime("2008-02-01 16:27:43").monthdays(), 29
        )


class DateTime_ordinalTest(unittest.TestCase):

    def test_empty(self):
        "DateTime.ordinal() raises NoDateTimeError if date isn't set"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.DateTime().ordinal
        )

    def test_ordinal(self):
        "DateTime.ordinal() returns 366 for 2008-12-31"

        self.assertEquals(
            chrono.DateTime("2008-12-31 16:27:43").ordinal(), 366
        )


class DateTime_setTest(unittest.TestCase):

    def test_invalid_date(self):
        "DateTime.set() raises proper date on invalid date"

        d = chrono.DateTime()

        self.assertRaises(
            chrono.error.YearError, d.set, 10000, 7, 23, 16, 27, 43
        )
        self.assertRaises(
            chrono.error.MonthError, d.set, 2010, 13, 23, 16, 27, 43
        )
        self.assertRaises(
            chrono.error.DayError, d.set, 2010, 7, 32, 16, 27, 43
        )
        self.assertRaises(
            chrono.error.HourError, d.set, 2010, 7, 23, 24, 27, 43
        )
        self.assertRaises(
            chrono.error.MinuteError, d.set, 2010, 7, 23, 16, 60, 43
        )
        self.assertRaises(
            chrono.error.SecondError, d.set, 2010, 7, 23, 16, 27, 60
        )

    def test_replace(self):
        "DateTime.set() replaces set date"

        d = chrono.DateTime("2009-07-21 16:27:43")
        d.set(2009, 12, 27, 12, 34, 56)

        self.assertEquals(d.get(), (2009, 12, 27, 12, 34, 56))

    def test_set(self):
        "DateTime.set() sets the date"

        d = chrono.DateTime()
        d.set(2009, 12, 27, 16, 27, 43)

        self.assertEquals(d.get(), (2009, 12, 27, 16, 27, 43))


class DateTime_set_datetimeTest(unittest.TestCase):

    def test_set(self):
        "DateTime.set_datetime() sets date from datetime.date object"

        d = chrono.DateTime()
        d.set_datetime(datetime.datetime(2009, 12, 27, 16, 27, 43))

        self.assertEquals(d.get(), (2009, 12, 27, 16, 27, 43))


class DateTime_set_nowTest(unittest.TestCase):

    def test_now(self):
        "DateTime.set_now() sets date to current date"

        d = chrono.DateTime()
        d.set_now()

        dt = datetime.datetime.now()

        self.assertEquals(
            d.get(), (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
        )


class DateTime_set_stringTest(unittest.TestCase):

    def test_invalid(self):
        "DateTime.set_string() raises proper error on invalid values"

        d = chrono.DateTime()

        self.assertRaises(
            chrono.error.YearError, d.set_string, "0000-07-23 16:27:43"
        )
        self.assertRaises(
            chrono.error.MonthError, d.set_string, "2010-13-23 16:27:43"
        )
        self.assertRaises(
            chrono.error.DayError, d.set_string, "2010-07-32 16:27:43"
        )
        self.assertRaises(
            chrono.error.HourError, d.set_string, "2010-07-23 24:27:43"
        )
        self.assertRaises(
            chrono.error.MinuteError, d.set_string, "2010-07-23 16:60:43"
        )
        self.assertRaises(
            chrono.error.SecondError, d.set_string, "2010-07-23 16:27:60"
        )

    def test_string(self):
        "DateTime.set_string() sets date from string"

        d = chrono.DateTime()

        d.set_string("2010-07-23 16:27:43")

        self.assertEqual(d.get(), (2010, 7, 23, 16, 27, 43))


class DateTime_set_struct_timeTest(unittest.TestCase):

    def test_struct_time(self):
        "DateTime.set_struct_time() sets date from a struct_time"

        d = chrono.DateTime()
        d.set_struct_time(time.localtime(1261892718))

        self.assertEquals(d.get(), (2009, 12, 27, 12, 45, 18))


class DateTime_set_unixText(unittest.TestCase):

    def test_invalid_type(self):
        "DateTime.set_unix() raises TypeError on invalid type"

        self.assertRaises(TypeError, chrono.DateTime().set_unix, None)

    def test_invalid(self):
        "DateTime.set_unix() raises ValueError for invalid values"

        self.assertRaises(ValueError, chrono.DateTime().set_unix, "abc")

    def test_set(self):
        "DateTime.set_unix() sets date from UNIX timestamp"

        d = chrono.DateTime()
        d.set_unix(1261892718)

        self.assertEquals(d.get(), (2009, 12, 27, 12, 45, 18))


class DateTime_weekTest(unittest.TestCase):

    def test_empty(self):
        "DateTime.week() raises NoDateTimeError if date isn't set"

        self.assertRaises(chrono.error.NoDateTimeError, chrono.DateTime().week)

    def test_week(self):
        "DateTime.week() returns 2009-W53 for 2010-01-01"

        self.assertEquals(
            chrono.DateTime("2010-01-01 16:27:43").week(), (2009, 53)
        )


class DateTime_weekdateTest(unittest.TestCase):

    def test_empty(self):
        "DateTime.weekdate() raises NoDateTimeError if date isn't set"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.DateTime().weekdate
        )

    def test_weekdate(self):
        "DateTime.weekdate() returns 2009-W30-2 for 2009-07-21"

        self.assertEquals(
                chrono.DateTime("2009-07-21 16:27:43").weekdate(),
            (2009, 30, 2)
        )


class DateTime_weekdayTest(unittest.TestCase):

    def test_empty(self):
        "DateTime.weekday() raises NoDateTimeError if date isn't set"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.DateTime().weekday
        )

    def test_weekday(self):
        "DateTime.weekday() returns 7 for 2009-12-27"

        self.assertEquals(chrono.DateTime("2009-12-27 16:27:43").weekday(), 7)


class DateTime_weeksTest(unittest.TestCase):

    def test_empty(self):
        "DateTime.weeks() raises NoDateTimeError if date isn't set"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.DateTime().weeks
        )

    def test_weeks(self):
        "DateTime.weeks() returns 53 for 2009"

        self.assertEquals(
                chrono.DateTime("2009-07-15 16:27:43").weeks(), 53
        )


class DateTime_yeardaysTest(unittest.TestCase):

    def test_empty(self):
        "DateTime.yeardays() raises NoDateTimeError if date isn't set"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.DateTime().yeardays
        )

    def test_yeardays(self):
        "DateTime.yeardays() returns 366 for 2008"

        self.assertEquals(
                chrono.DateTime("2008-01-01 16:27:43").yeardays(), 366
        )


if __name__ == "__main__":
    unittest.main()
