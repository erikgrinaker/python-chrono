#!/usr/bin/env python

import chrono
import unittest


class USClockTest(unittest.TestCase):

    def test__subclass(self):
        "USClock is subclass of Clock"

        self.assertTrue(
            issubclass(chrono.clock.USClock, chrono.clock.Clock)
        )


class USClock_from_24(unittest.TestCase):

    def test_0(self):
        "USClock.from_24() returns 12 AM for 0"

        self.assertEqual(chrono.clock.USClock.from_24(0), (12, False))

    def test_6(self):
        "USClock.from_24() returns 6 AM for 6"

        self.assertEqual(chrono.clock.USClock.from_24(6), (6, False))

    def test_12(self):
        "USClock.from_24() returns 12 PM for 12"

        self.assertEqual(chrono.clock.USClock.from_24(12), (12, True))

    def test_18(self):
        "USClock.from_24() returns 6 PM for 18"

        self.assertEqual(chrono.clock.USClock.from_24(18), (6, True))

    def test_invalid(self):
        "USClock.from_24() raises HourError on invalid hour"

        self.assertRaises(
            chrono.HourError, chrono.clock.USClock.from_24, 24
        )


class USClock_to_24(unittest.TestCase):

    def test_0(self):
        "USClock.to_24() raises HourError on 0"

        self.assertRaises(
            chrono.HourError, chrono.clock.USClock.to_24, 0, False
        )
        self.assertRaises(
            chrono.HourError, chrono.clock.USClock.to_24, 0, True
        )

    def test_6_am(self):
        "USClock.to_24() returns 6 for 6 AM"

        self.assertEqual(chrono.clock.USClock.to_24(6, False), 6)

    def test_6_pm(self):
        "USClock.to_24() returns 18 for 6 PM"

        self.assertEqual(chrono.clock.USClock.to_24(6, True), 18)

    def test_12_am(self):
        "USClock.to_24() returns 0 for 12 AM"

        self.assertEqual(chrono.clock.USClock.to_24(12, False), 0)

    def test_12_pm(self):
        "USClock.to_24() returns 12 for 12 PM"

        self.assertEqual(chrono.clock.USClock.to_24(12, True), 12)


class USClock_validate_hourTest(unittest.TestCase):

    def test_0(self):
        "USClock.validate_hour() raises HourError on 0"

        self.assertRaises(
            chrono.HourError, chrono.clock.USClock.validate_hour, 24
        )

    def test_1(self):
        "USClock.validate_hour() accepts 1"

        chrono.clock.USClock.validate_hour(1)

    def test_12(self):
        "USClock.validate_hour() accepts 12"

        chrono.clock.USClock.validate_hour(12)

    def test_13(self):
        "USClock.validate_hour() raises HourError on 13"

        self.assertRaises(
            chrono.HourError, chrono.clock.USClock.validate_hour, 13
        )


if __name__ == "__main__":
    unittest.main()
