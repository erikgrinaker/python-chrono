#!/usr/bin/env python

import chrono
import datetime
import time
import unittest


class Time__eqTest(unittest.TestCase):

    def test_time(self):
        "Time.__eq__() handles Time objects"

        self.assertTrue(chrono.Time("16:27:43") == chrono.Time("16:27:43"))
        self.assertFalse(chrono.Time("16:27:43") == chrono.Time("16:27:44"))

    def test_none(self):
        "Time.__eq__() handles None"

        self.assertTrue(chrono.Time() == None)
        self.assertFalse(chrono.Time("16:27:43") == None)

    def test_string(self):
        "Time.__eq__() handles strings"

        self.assertTrue(chrono.Time("16:27:43") == "16:27:43")
        self.assertFalse(chrono.Time("16:27:43") == "16:27:42")


class Time__geTest(unittest.TestCase):

    def test_time(self):
        "Time.__ge__() handles Time objects"

        self.assertTrue(chrono.Time("16:27:43") >= chrono.Time("16:27:42"))
        self.assertTrue(chrono.Time("16:27:43") >= chrono.Time("16:27:43"))
        self.assertFalse(chrono.Time("16:27:43") >= chrono.Time("16:27:44"))

    def test_none(self):
        "Time.__ge__() handles None"

        self.assertTrue(chrono.Time() >= None)
        self.assertTrue(chrono.Time("16:27:43") >= None)

    def test_string(self):
        "Time.__ge__() handles strings"

        self.assertTrue(chrono.Time("16:27:43") >= "16:27:42")
        self.assertTrue(chrono.Time("16:27:43") >= "16:27:43")
        self.assertFalse(chrono.Time("16:27:43") >= "16:27:44")


class Time__gtTest(unittest.TestCase):

    def test_time(self):
        "Time.__gt__() handles Time objects"

        self.assertTrue(chrono.Time("16:27:43") > chrono.Time("16:27:42"))
        self.assertFalse(chrono.Time("16:27:43") > chrono.Time("16:27:43"))
        self.assertFalse(chrono.Time("16:27:43") > chrono.Time("16:27:44"))

    def test_none(self):
        "Time.__gt__() handles None"

        self.assertTrue(chrono.Time("16:27:43") > None)
        self.assertFalse(chrono.Time() > None)

    def test_string(self):
        "Time.__gt__() handles strings"

        self.assertTrue(chrono.Time("16:27:43") > "16:27:42")
        self.assertFalse(chrono.Time("16:27:43") > "16:27:43")
        self.assertFalse(chrono.Time("16:27:43") > "16:27:44")


class Time__initTest(unittest.TestCase):

    def test_datetime_datetime(self):
        "Time.__init__() copies time from datetime.datetime objects"

        self.assertEquals(
            chrono.Time(datetime.datetime(2010, 1, 4, 16, 27, 43)).get(),
            (16, 27, 43)
        )

    def test_datetime_time(self):
        "Time.__init__() copies time from datetime.time objects"

        self.assertEquals(
            chrono.Time(datetime.time(16, 27, 43)).get(),
            (16, 27, 43)
        )

    def test_default(self):
        "Time.__init__() without parameters sets up empty date"

        self.assertRaises(chrono.error.NoDateTimeError, chrono.Time().get)

    def test_false(self):
        "Time,__init__() with False sets up empty time"

        self.assertRaises(chrono.error.NoDateTimeError, chrono.Time(False).get)

    def test_kwargs(self):
        "Time.__init__() accepts keyword arguments"

        self.assertEquals(
            chrono.Time(hour=16, minute=27, second=43).get(),
            (16, 27, 43)
        )

    def test_kwargs_partial(self):
        "Time.__init__() raises proper error on partial kwargs"

        self.assertRaises(chrono.HourError, chrono.Time, minute=27, second=43)
        self.assertRaises(chrono.MinuteError, chrono.Time, hour=16, second=43)
        self.assertRaises(chrono.SecondError, chrono.Time, hour=16, minute=27)

    def test_kwargs_precedence(self):
        "Time.__init__() prefers time over kwargs"

        t = chrono.Time("16:27:43", hour=20, second=49)

        self.assertEquals(t.hour, 16)
        self.assertEquals(t.minute, 27)
        self.assertEquals(t.second, 43)

    def test_none(self):
        "Time.__init__() with None sets up empty time"

        self.assertRaises(chrono.error.NoDateTimeError, chrono.Time(None).get)

    def test_parser(self):
        "Time.__init__() takes parser as input"

        p = chrono.parser.ISOParser
        t = chrono.Time("16:27:43", p)

        self.assertEqual(t.get(), (16, 27, 43))
        self.assertEqual(t.parser, p)

    def test_parser_default(self):
        "Time.__init__() defaults to CommonParser"

        t = chrono.Time("16:27:43")

        self.assertEqual(t.get(), (16, 27, 43))
        self.assertEqual(t.parser, chrono.parser.CommonParser)

    def test_string(self):
        "Time.__init__() parses strings using the parser"

        self.assertEquals(chrono.Time("16:27:43").get(), (16, 27, 43))

    def test_struct_time(self):
        "Time.__init__() copies time from time.struct_time objects"

        self.assertEquals(
            chrono.Time(time.localtime(1262621257)).get(),
            (23, 7, 37)
        )

    def test_time(self):
        "Time.__init__() copies time from passed Time object"

        self.assertEquals(
            chrono.Time(chrono.Time("16:27:43")).get(),
            (16, 27, 43)
        )

    def test_true(self):
        "Time.__init__() sets time to current time for True"

        dt = datetime.datetime.now()

        self.assertEquals(
            chrono.Time(True).get(),
            (dt.hour, dt.minute, dt.second)
        )

    def test_unknown(self):
        "Time.__init__() raises TypeError on unknown type"

        self.assertRaises(TypeError, chrono.Time, [])


class Time__leTest(unittest.TestCase):

    def test_time(self):
        "Time.__le__() handles Time objects"

        self.assertTrue(chrono.Time("16:27:43") <= chrono.Time("16:27:44"))
        self.assertTrue(chrono.Time("16:27:43") <= chrono.Time("16:27:43"))
        self.assertFalse(chrono.Time("16:27:43") <= chrono.Time("16:27:42"))

    def test_none(self):
        "Time.__le__() handles None"

        self.assertTrue(chrono.Time() <= None)
        self.assertFalse(chrono.Time("16:27:43") <= None)

    def test_string(self):
        "Time.__le__() handles strings"

        self.assertTrue(chrono.Time("16:27:43") <= "16:27:44")
        self.assertTrue(chrono.Time("16:27:43") <= "16:27:43")
        self.assertFalse(chrono.Time("16:27:43") <= "16:27:42")


class Time__ltTest(unittest.TestCase):

    def test_time(self):
        "Time.__lt__() handles Time objects"

        self.assertTrue(chrono.Time("16:27:43") < chrono.Time("16:27:44"))
        self.assertFalse(chrono.Time("16:27:43") < chrono.Time("16:27:43"))
        self.assertFalse(chrono.Time("16:27:43") < chrono.Time("16:27:42"))

    def test_none(self):
        "Time.__lt__() handles None"

        self.assertFalse(chrono.Time("16:27:43") < None)
        self.assertFalse(chrono.Time() < None)

    def test_string(self):
        "Time.__lt__() handles strings"

        self.assertTrue(chrono.Time("16:27:43") < "16:27:44")
        self.assertFalse(chrono.Time("16:27:43") < "16:27:43")
        self.assertFalse(chrono.Time("16:27:43") < "16:27:42")


class Time__neTest(unittest.TestCase):

    def test_time(self):
        "Time.__ne__() handles Time objects"

        self.assertTrue(chrono.Time("16:27:43") != chrono.Time("16:27:42"))
        self.assertFalse(chrono.Time("16:27:43") != chrono.Time("16:27:43"))

    def test_none(self):
        "Time.__ne__() handles None"

        self.assertTrue(chrono.Time("16:27:43") != None)
        self.assertFalse(chrono.Time() != None)

    def test_string(self):
        "Time.__ne__() handles strings"

        self.assertTrue(chrono.Time("16:27:43") != "16:27:42")
        self.assertFalse(chrono.Time("16:27:43") != "16:27:43")


class Time__reprTest(unittest.TestCase):

    def test_empty(self):
        "Time.__repr__() handles empty times"

        self.assertEquals(repr(chrono.Time()), "chrono.Time()")

    def test_partial(self):
        "Time.__repr__() handles partial times"

        t = chrono.Time()
        t.hour = 16
        t.second = 43

        self.assertEquals(repr(t), "chrono.Time(hour=16, second=43)")

    def test_repr(self):
        "Time.__repr__() shows code to recreate object"

        self.assertEquals(
                repr(chrono.Time("16:27:43")),
            "chrono.Time(hour=16, minute=27, second=43)"
        )


class Time__setattrTest(unittest.TestCase):

    def test_hour_negative(self):
        "Time.__setattr__() handles hour rollunder"

        t = chrono.Time("16:27:43")
        t.hour -= 20

        self.assertEquals(t.get(), (20, 27, 43))

    def test_hour_negative_double(self):
        "Time.__setattr__() handles double hour rollunder"

        t = chrono.Time("16:27:43")
        t.hour -= 44

        self.assertEquals(t.get(), (20, 27, 43))

    def test_hour_overflow(self):
        "Time.__setattr__() handles hour rollover"

        t = chrono.Time("16:27:43")
        t.hour += 10

        self.assertEquals(t.get(), (2, 27, 43))

    def test_hour_overflow_double(self):
        "Time.__setattr__() handles double hour rollover"

        t = chrono.Time("16:27:43")
        t.hour += 34

        self.assertEquals(t.get(), (2, 27, 43))

    def test_minute_negative(self):
        "Time.__setattr__() handles hour rollunder for negative minutes"

        t = chrono.Time("16:27:43")
        t.minute -= 30

        self.assertEquals(t.get(), (15, 57, 43))

    def test_minute_negative_doublehour(self):
        "Time.__setattr__() handles double hour rollunder for negative minutes"

        t = chrono.Time("16:27:43")
        t.minute -= 120

        self.assertEquals(t.get(), (14, 27, 43))

    def test_minute_overflow(self):
        "Time.__setattr__() handles hour rollover for minute overflow"

        t = chrono.Time("16:27:43")
        t.minute += 45

        self.assertEquals(t.get(), (17, 12, 43))

    def test_minute_overflow_doublehour(self):
        "Time.__setattr__() handles double hour rollover for minute overflow"

        t = chrono.Time("16:27:43")
        t.minute += 120

        self.assertEquals(t.get(), (18, 27, 43))

    def test_second_negative(self):
        "Time.__setattr__() handles minute rollunder for negative seconds"

        t = chrono.Time("16:27:43")
        t.second -= 60

        self.assertEquals(t.get(), (16, 26, 43))

    def test_second_negative_doubleminute(self):
        "Time.__setattr__() handles double minute rollunder for negative secs"

        t = chrono.Time("16:27:43")
        t.second -= 120

        self.assertEquals(t.get(), (16, 25, 43))

    def test_second_negative_hour(self):
        "Time.__setattr__() handles hour rollunder for negative seconds"

        t = chrono.Time("16:27:43")
        t.second -= 1800

        self.assertEquals(t.get(), (15, 57, 43))

    def test_second_overflow(self):
        "Time.__setattr__() handles minute rollover for second overflow"

        t = chrono.Time("16:27:43")
        t.second += 45

        self.assertEquals(t.get(), (16, 28, 28))

    def test_second_overflow_doubleminute(self):
        "Time.__setattr__() handles double minute rollover for second overflow"

        t = chrono.Time("16:27:43")
        t.second += 120

        self.assertEquals(t.get(), (16, 29, 43))

    def test_second_overflow_hour(self):
        "Time.__setattr__() handles hour rollover for second overflow"

        t = chrono.Time("16:27:43")
        t.second += 3600

        self.assertEquals(t.get(), (17, 27, 43))


class Time__strTest(unittest.TestCase):

    def test_empty(self):
        "Time.__str__() returns empty string if no time is set"

        self.assertEqual(str(chrono.Time()), "")

    def test_string(self):
        "Time.__str__() returns string representation of time"

        self.assertEquals(str(chrono.Time("16:27:43")), "16:27:43")


class Time_assert_setTest(unittest.TestCase):

    def test_empty(self):
        "Time.assert_set() raises NoDateTimeError on empty time"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.Time().assert_set
        )

    def test_full(self):
        "Time.assert_set() doesn't raise exception on time"

        chrono.Time("16:27:43").assert_set()

    def test_partial(self):
        "Time.assert_set() raises NoDateTimeError on partial time"

        t = chrono.Time("16:27:43")
        t.minute = None

        self.assertRaises(chrono.error.NoDateTimeError, t.assert_set)


class Time_clearTest(unittest.TestCase):

    def test_clear(self):
        "Time.clear() clears time attributes"

        t = chrono.Time("16:27:43")
        t.clear()

        self.assertEquals(t.hour, None)
        self.assertEquals(t.minute, None)
        self.assertEquals(t.second, None)


class Time_formatTest(unittest.TestCase):

    def test_empty(self):
        "Time.format() raises NoDateTimeError on missing time"

        self.assertRaises(
            chrono.error.NoDateTimeError,
            chrono.Time().format, "$hour:$minute:$second"
        )

    def test_format(self):
        "Time.format() formats template"

        self.assertEqual(
            chrono.Time("16:27:43").format("$hour:$minute:$second"),
            "16:27:43"
        )


class Time_getTest(unittest.TestCase):

    def test_empty(self):
        "Time.get() raises NoDateTimeError if time is not set"

        self.assertRaises(chrono.error.NoDateTimeError, chrono.Time().get)

    def test_get(self):
        "Time.get() returns tuple of hour, minute, and second"

        self.assertEquals(
            chrono.Time(hour=16, minute=27, second=43).get(),
            (16, 27, 43)
        )


class Time_get_datetimeTest(unittest.TestCase):

    def test_empty(self):
        "Time.get_datetime() returns None if time is not set"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.Time().get_datetime
        )

    def test_get_datetime(self):
        "Time.get_datetime() returns datetime.time object"

        dt = chrono.Time("16:27:43").get_datetime()

        self.assertTrue(isinstance(dt, datetime.time))

        self.assertEquals(dt.hour, 16)
        self.assertEquals(dt.minute, 27)
        self.assertEquals(dt.second, 43)


class Time_get_julianTest(unittest.TestCase):

    def test_empty(self):
        "Time.get_julian() raises NoDateTimeError if time is not set"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.Time().get_julian
        )

    def test_get(self):
        "Time.get_julian() returns julian time"

        self.assertEquals(
            chrono.Time("16:27:43").get_julian(), 0.6859143518518519
        )


class Time_get_stringTest(unittest.TestCase):

    def test_empty(self):
        "Time.get_string() raises NoDateTimeError if time is not set"

        self.assertRaises(
            chrono.error.NoDateTimeError, chrono.Time().get_string
        )

    def test_get(self):
        "Time.get_string() returns time string"

        self.assertEquals(chrono.Time("16:27:43").get_string(), "16:27:43")


class Time_is_setTest(unittest.TestCase):

    def test_empty(self):
        "Time.is_set() returns False if no attributes are set"

        self.assertFalse(chrono.Time().is_set())

    def test_partial(self):
        "Time.is_set() returns False if only some attributes are set"

        t = chrono.Time("16:27:43")
        t.minute = None

        self.assertFalse(t.is_set())

    def test_set(self):
        "Time.is_set() returns True if time is set"

        self.assertTrue(chrono.Time(hour=16, minute=27, second=43).is_set())


class Time_setTest(unittest.TestCase):

    def test_invalid(self):
        "Time.set() raises proper error on invalid time"

        t = chrono.Time()

        self.assertRaises(chrono.HourError, t.set, 25, 27, 43)
        self.assertRaises(chrono.MinuteError, t.set, 16, 60, 43)
        self.assertRaises(chrono.SecondError, t.set, 16, 27, 60)

    def test_invalid_keep(self):
        "Time.set() keeps the old value when setting invalid values"

        t = chrono.Time("16:27:43")

        self.assertRaises(chrono.HourError, t.set, 26, 12, 34)

        self.assertEqual(t.get(), (16, 27, 43))

    def test_replace(self):
        "Time.set() replaces set time"

        t = chrono.Time("16:27:43")
        t.set(8, 35, 19)

        self.assertEquals(t.get(), (8, 35, 19))

    def test_set(self):
        "Time.set() sets the time"

        t = chrono.Time()
        t.set(16, 27, 43)

        self.assertEquals(t.get(), (16, 27, 43))

    def test_string(self):
        "Time.set() accepts string input"

        t = chrono.Time()
        t.set("16", "27", "43")

        self.assertEquals(t.get(), (16, 27, 43))


class Time_set_datetimeTest(unittest.TestCase):

    def test_datetime(self):
        "Time.set_datetime() sets time from datetime.datetime object"

        t = chrono.Time()
        t.set_datetime(datetime.datetime(2010, 1, 4, 16, 27, 43))

        self.assertEquals(t.get(), (16, 27, 43))

    def test_time(self):
        "Time.set_datetime() sets time from datetime.time object"

        t = chrono.Time()
        t.set_datetime(datetime.time(16, 27, 43))

        self.assertEquals(t.get(), (16, 27, 43))


class Time_set_julianTest(unittest.TestCase):

    def test_julian(self):
        "Time.set_julian() sets time from julian time"

        t = chrono.Time()
        t.set_julian(0.6859143518518519),

        self.assertEquals(t.get(), (16, 27, 43))


class Time_set_nowTest(unittest.TestCase):

    def test_now(self):
        "Time.set_now() sets time to current time"

        t = chrono.Time()
        t.set_now()

        dt = datetime.datetime.now()

        self.assertEquals(t.get(), (dt.hour, dt.minute, dt.second))


class Time_set_stringTest(unittest.TestCase):

    def test_string(self):
        "Time.set_string() sets time from string"

        t = chrono.Time()
        t.set_string("16:27:43")

        self.assertEquals(t.get(), (16, 27, 43))


class Time_set_struct_timeTest(unittest.TestCase):

    def test_struct_time(self):
        "Time.set_struct_time() sets time from a struct_time"

        t = chrono.Time()
        t.set_struct_time(time.localtime(1262621257))

        self.assertEquals(t.get(), (23, 7, 37))


if __name__ == "__main__":
    unittest.main()
