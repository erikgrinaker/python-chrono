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


class NoDateError(unittest.TestCase):

    def test_subclass(self):
        "NoDateError is subclass of NoDateTimeError"

        self.assertTrue(issubclass(chrono.NoDateError, chrono.NoDateTimeError))


class NoDateTimeError(unittest.TestCase):

    def test_subclass(self):
        "NoDateError is subclass of Exception"

        self.assertTrue(issubclass(chrono.NoDateTimeError, Exception))


class NoTimeError(unittest.TestCase):

    def test_subclass(self):
        "NoTimeError is subclass of NoDateTimeError"

        self.assertTrue(issubclass(chrono.NoTimeError, chrono.NoDateTimeError))


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
