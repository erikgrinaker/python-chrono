#!/usr/bin/env python

import chrono
import unittest


class int_dayTest(unittest.TestCase):

    def test_int(self):
        "int_day() handles integers"

        self.assertEqual(chrono.utility.int_day(10), 10)

    def test_none(self):
        "int_day() raises DayError on None"

        self.assertRaises(chrono.DayError, chrono.utility.int_day, None)

    def test_nonnumeric(self):
        "int_day() raises DayError on non-numeric string"

        self.assertRaises(chrono.DayError, chrono.utility.int_day, "abc")

    def test_string(self):
        "int_day() handles strings"

        self.assertEqual(chrono.utility.int_day("10"), 10)


class int_hourTest(unittest.TestCase):

    def test_int(self):
        "int_hour() handles integers"

        self.assertEqual(chrono.utility.int_hour(10), 10)

    def test_none(self):
        "int_hour() raises HourError on None"

        self.assertRaises(chrono.HourError, chrono.utility.int_hour, None)

    def test_nonnumeric(self):
        "int_hour() raises HourError on non-numeric string"

        self.assertRaises(chrono.HourError, chrono.utility.int_hour, "abc")

    def test_string(self):
        "int_hour() handles strings"

        self.assertEqual(chrono.utility.int_hour("10"), 10)


class int_minuteTest(unittest.TestCase):

    def test_int(self):
        "int_minute() handles integers"

        self.assertEqual(chrono.utility.int_minute(10), 10)

    def test_none(self):
        "int_minute() raises MinuteError on None"

        self.assertRaises(chrono.MinuteError, chrono.utility.int_minute, None)

    def test_nonnumeric(self):
        "int_minute() raises MinuteError on non-numeric string"

        self.assertRaises(chrono.MinuteError, chrono.utility.int_minute, "abc")

    def test_string(self):
        "int_minute() handles strings"

        self.assertEqual(chrono.utility.int_minute("10"), 10)


class int_monthTest(unittest.TestCase):

    def test_int(self):
        "int_month() handles integers"

        self.assertEqual(chrono.utility.int_month(10), 10)

    def test_none(self):
        "int_month() raises MonthError on None"

        self.assertRaises(chrono.MonthError, chrono.utility.int_month, None)

    def test_nonnumeric(self):
        "int_month() raises MonthError on non-numeric string"

        self.assertRaises(chrono.MonthError, chrono.utility.int_month, "abc")

    def test_string(self):
        "int_month() handles strings"

        self.assertEqual(chrono.utility.int_month("10"), 10)


class int_secondTest(unittest.TestCase):

    def test_int(self):
        "int_second() handles integers"

        self.assertEqual(chrono.utility.int_second(10), 10)

    def test_none(self):
        "int_second() raises SecondError on None"

        self.assertRaises(chrono.SecondError, chrono.utility.int_second, None)

    def test_nonnumeric(self):
        "int_second() raises SecondError on non-numeric string"

        self.assertRaises(chrono.SecondError, chrono.utility.int_second, "abc")

    def test_string(self):
        "int_second() handles strings"

        self.assertEqual(chrono.utility.int_second("10"), 10)


class int_weekTest(unittest.TestCase):

    def test_int(self):
        "int_week() handles integers"

        self.assertEqual(chrono.utility.int_week(10), 10)

    def test_none(self):
        "int_week() raises WeekError on None"

        self.assertRaises(chrono.WeekError, chrono.utility.int_week, None)

    def test_nonnumeric(self):
        "int_week() raises WeekError on non-numeric string"

        self.assertRaises(chrono.WeekError, chrono.utility.int_week, "abc")

    def test_string(self):
        "int_week() handles strings"

        self.assertEqual(chrono.utility.int_week("10"), 10)


class int_yearTest(unittest.TestCase):

    def test_int(self):
        "int_year() handles integers"

        self.assertEqual(chrono.utility.int_year(10), 10)

    def test_none(self):
        "int_year() raises YearError on None"

        self.assertRaises(chrono.YearError, chrono.utility.int_year, None)

    def test_nonnumeric(self):
        "int_year() raises YearError on non-numeric string"

        self.assertRaises(chrono.YearError, chrono.utility.int_year, "abc")

    def test_string(self):
        "int_year() handles strings"

        self.assertEqual(chrono.utility.int_year("10"), 10)


class integerTest(unittest.TestCase):

    def test_dict(self):
        "integer() converts dict members to integer"

        self.assertEquals(
            chrono.utility.integer({"a": "123", "b": "456", "c": "789"}),
            {"a": 123, "b": 456, "c": 789}
        )

    def test_dict_none(self):
        "integer() preserves None in dicts"

        self.assertEquals(
            chrono.utility.integer({"a": "123", "b": None, "c": "789"}),
            {"a": 123, "b": None, "c": 789}
        )

    def test_int(self):
        "integer() preserves integers"

        self.assertEquals(chrono.utility.integer(123), 123)

    def test_list(self):
        "integer() converts list members to integer"

        self.assertEquals(
            chrono.utility.integer(["123", "456", "789"]),
            [123, 456, 789]
        )

    def test_list_none(self):
        "integer() preserves None in lists"

        self.assertEquals(
            chrono.utility.integer(["123", None, "789"]),
            [123, None, 789]
        )

    def test_none(self):
        "integer() returns None for None"

        self.assertEquals(chrono.utility.integer(None), None)

    def test_string(self):
        "integer() converts string to integer"

        self.assertEquals(chrono.utility.integer("123"), 123)

    def test_string_nonnumeric(self):
        "integer() raises ValueError for non-numeric string"

        self.assertRaises(ValueError, chrono.utility.integer, "abc")

    def test_tuple(self):
        "integer() converts tuple members to integer"

        self.assertEquals(
            chrono.utility.integer(("123", "456", "789")),
            (123, 456, 789)
        )

    def test_tuple_none(self):
        "integer() preserves None in tuples"

        self.assertEquals(
            chrono.utility.integer(("123", None, "789")),
            (123, None, 789)
        )


if __name__ == "__main__":
    unittest.main()
