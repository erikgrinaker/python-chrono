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


class Clock_validateTest(unittest.TestCase):

    def test_hour(self):
        "Clock.validate() raises HourError on invalid hour"

        self.assertRaises(
            chrono.HourError, chrono.clock.Clock.validate, 25, 37, 43
        )

    def test_minute(self):
        "Clock.validate() raises MinuteError on invalid minute"

        self.assertRaises(
            chrono.MinuteError, chrono.clock.Clock.validate, 16, 65, 43
        )

    def test_second(self):
        "Clock.validate() raises SecondError on invalid second"

        self.assertRaises(
            chrono.SecondError, chrono.clock.Clock.validate, 16, 37, 84
        )

    def test_valid(self):
        "Clock.validate() returns None for valid times"

        self.assertEqual(chrono.clock.Clock.validate(16, 27, 43), None)


class Clock_validate_hourTest(unittest.TestCase):

    def test_0(self):
        "Clock.validate_hour() accepts 0"

        chrono.clock.Clock.validate_hour(0)

    def test_23(self):
        "Clock.validate_hour() accepts 23"

        chrono.clock.Clock.validate_hour(23)

    def test_24(self):
        "Clock.validate_hour() raises HourError on 24"

        self.assertRaises(
            chrono.HourError, chrono.clock.Clock.validate_hour, 24
        )

    def test_negative(self):
        "Clock.validate_hour() raises HourError on negative values"

        self.assertRaises(
            chrono.HourError, chrono.clock.Clock.validate_hour, -1
        )


class Clock_validate_minuteTest(unittest.TestCase):

    def test_0(self):
        "Clock.validate_minute() accepts 0"

        chrono.clock.Clock.validate_minute(0)

    def test_59(self):
        "Clock.validate_minute() accepts 59"

        chrono.clock.Clock.validate_minute(59)

    def test_60(self):
        "Clock.validate_minute() raises MinuteError on 60"

        self.assertRaises(
            chrono.MinuteError, chrono.clock.Clock.validate_minute, 60
        )

    def test_negative(self):
        "Clock.validate_minute() raises MinuteError on negative values"

        self.assertRaises(
            chrono.MinuteError, chrono.clock.Clock.validate_minute, -1
        )


class Clock_validate_secondTest(unittest.TestCase):

    def test_0(self):
        "Clock.validate_second() accepts 0"

        chrono.clock.Clock.validate_second(0)

    def test_59(self):
        "Clock.validate_second() accepts 59"

        chrono.clock.Clock.validate_second(59)

    def test_60(self):
        "Clock.validate_second() raises SecondError on 60"

        self.assertRaises(
            chrono.SecondError, chrono.clock.Clock.validate_second, 60
        )

    def test_negative(self):
        "Clock.validate_second() raises SecondError on negative values"

        self.assertRaises(
            chrono.SecondError, chrono.clock.Clock.validate_second, -1
        )


if __name__ == "__main__":
    unittest.main()
