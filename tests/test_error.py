#!/usr/bin/env python

import chrono
import unittest


class DateErrorTest(unittest.TestCase):

    def test_subclass(self):
        "DateError is a subclass of DatetimeError"

        self.assertTrue(issubclass(chrono.DateError, chrono.DateTimeError))


class DateTimeErrorTest(unittest.TestCase):

    def test_subclass(self):
        "DateTimeError is a subclass of ValueError"

        self.assertTrue(issubclass(chrono.DateTimeError, ValueError))


class DayErrorTest(unittest.TestCase):

    def test_subclass(self):
        "DayError is a subclass of DateError"

        self.assertTrue(issubclass(chrono.DayError, chrono.DateError))


class HourErrorTest(unittest.TestCase):

    def test_subclass(self):
        "HourError is a subclass of TimeError"

        self.assertTrue(issubclass(chrono.HourError, chrono.TimeError))


class MinuteErrorTest(unittest.TestCase):

    def test_subclass(self):
        "MinuteError is a subclass of TimeError"

        self.assertTrue(issubclass(chrono.MinuteError, chrono.TimeError))


class MonthErrorTest(unittest.TestCase):

    def test_subclass(self):
        "MonthError is a subclass of DateError"

        self.assertTrue(issubclass(chrono.MonthError, chrono.DateError))


class NoDateTimeError(unittest.TestCase):

    def test_subclass(self):
        "NoDateTimeError is subclass of Exception"

        self.assertTrue(issubclass(chrono.NoDateTimeError, Exception))


class ParseErrorTest(unittest.TestCase):

    def test_subclass(self):
        "ParseError is a subclass of ValueError"

        self.assertTrue(issubclass(chrono.ParseError, ValueError))


class SecondErrorTest(unittest.TestCase):

    def test_subclass(self):
        "SecondError is a subclass of TimeError"

        self.assertTrue(issubclass(chrono.SecondError, chrono.TimeError))


class TimeErrorTest(unittest.TestCase):

    def test_subclass(self):
        "TimeError is a subclass of DatetimeError"

        self.assertTrue(issubclass(chrono.TimeError, chrono.DateTimeError))


class WeekErrorTest(unittest.TestCase):

    def test_subclass(self):
        "WeekError is a subclass of DateError"

        self.assertTrue(issubclass(chrono.WeekError, chrono.DateError))


class YearErrorTest(unittest.TestCase):

    def test_subclass(self):
        "YearError is a subclass of DateError"

        self.assertTrue(issubclass(chrono.YearError, chrono.DateError))


if __name__ == "__main__":
    unittest.main()
