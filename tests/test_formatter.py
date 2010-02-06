#!/usr/bin/env python

import chrono
import unittest


class Formatter_formatTest(unittest.TestCase):

    def setUp(self):

        unittest.TestCase.setUp(self)

        self.f = chrono.formatter.Formatter(chrono.calendar.ISOCalendar)

    def test_012hour(self):
        "Formatter.format() handles $012hour"

        self.assertEqual(self.f.format(
            "$012hour", 2010, 8, 4, 0, 2, 3
        ), "12")

        self.assertEqual(self.f.format(
            "$012hour", 2010, 8, 4, 15, 2, 3
        ), "03")

    def test_0day(self):
        "Formatter.format() handles $0day"

        self.assertEqual(self.f.format(
            "$0day", 2010, 8, 4, 1, 2, 3
        ), "04")

    def test_0hour(self):
        "Formatter.format() handles $0hour"

        self.assertEqual(self.f.format(
            "$0hour", 2010, 8, 4, 1, 2, 3
        ), "01")

    def test_0minute(self):
        "Formatter.format() handles $0minute"

        self.assertEqual(self.f.format(
            "$0minute", 2010, 8, 4, 1, 2, 3
        ), "02")

    def test_0month(self):
        "Formatter.format() handles $0month"

        self.assertEqual(self.f.format(
            "$0month", 2010, 8, 4, 1, 2, 3
        ), "08")

    def test_0second(self):
        "Formatter.format() handles $0second"

        self.assertEqual(self.f.format(
            "$0second", 2010, 8, 4, 1, 2, 3
        ), "03")

    def test_0week(self):
        "Formatter.format() handles $0week"

        self.assertEqual(self.f.format(
            "$0week", 2010, 2, 4, 1, 2, 3
        ), "05")

    def test_0year(self):
        "Formatter.format() handles $0year"

        self.assertEqual(self.f.format(
            "$0year", 492, 8, 4, 1, 2, 3
        ), "0492")

    def test_12hour(self):
        "Formatter.format() handles $12hour"

        self.assertEqual(self.f.format(
            "$12hour", 2010, 8, 4, 0, 2, 3
        ), "12")

        self.assertEqual(self.f.format(
            "$12hour", 2010, 8, 4, 15, 2, 3
        ), "3")

    def test_ampm(self):
        "Formatter.format() handles $ampm"

        self.assertEqual(self.f.format(
            "$ampm", 2010, 8, 4, 1, 2, 3
        ), "AM")

        self.assertEqual(self.f.format(
            "$ampm", 2010, 8, 4, 12, 2, 3
        ), "PM")

    def test_day(self):
        "Formatter.format() handles $day"

        self.assertEqual(self.f.format(
            "$day", 2010, 8, 4, 1, 2, 3
        ), "4")

    def test_escape(self):
        "Formatter.format() handles escaped $ signs"

        self.assertEqual(self.f.format(
            "$year$$$month", 2010, 8, 4, 1, 2, 3
        ), "2010$8")

    def test_hour(self):
        "Formatter.format() handles $hour"

        self.assertEqual(self.f.format(
            "$hour", 2010, 8, 4, 1, 2, 3
        ), "1")

    def test_invalid(self):
        "Formatter.format() ignores invalid patterns"

        self.assertEqual(self.f.format(
            "$-}", 2010, 8, 4, 1, 2, 3
        ), "$-}")

    def test_minute(self):
        "Formatter.format() handles $minute"

        self.assertEqual(self.f.format(
            "$minute", 2010, 8, 4, 1, 2, 3
        ), "2")

    def test_missing(self):
        "Formatter.format() returns blank content for variables with no value"

        self.assertEqual(self.f.format(
            "$0year-$0month-$0day", 2010, None, 4, 1, 2, 3
        ), "2010--04")

    def test_month(self):
        "Formatter.format() handles $month"

        self.assertEqual(self.f.format(
            "$month", 2010, 8, 4, 1, 2, 3
        ), "8")

    def test_monthname(self):
        "Formatter.format() handles $monthname"

        self.assertEqual(self.f.format(
            "$monthname", 2010, 8, 4, 1, 2, 3
        ), "August")

    def test_second(self):
        "Formatter.format() handles $second"

        self.assertEqual(self.f.format(
            "$second", 2010, 8, 4, 1, 2, 3
        ), "3")

    def test_shortmonthname(self):
        "Formatter.format() handles $shortmonthname"

        self.assertEqual(self.f.format(
            "$shortmonthname", 2010, 8, 4, 1, 2, 3
        ), "Aug")

    def test_shortweekdayname(self):
        "Formatter.format() handles $shortweekdayname"

        self.assertEqual(self.f.format(
            "$shortweekdayname", 2010, 8, 4, 1, 2, 3
        ), "Wed")

    def test_shortyear(self):
        "Formatter.format() handles $shortyear"

        self.assertEqual(self.f.format(
            "$shortyear", 2010, 8, 4, 1, 2, 3
        ), "10")

    def test_unknown(self):
        "Formatter.format() ignores unknown variables"

        self.assertEqual(self.f.format(
            "$0year-$dummy-$0day", 2010, 8, 4, 1, 2, 3
        ), "2010-$dummy-04")

    def test_week(self):
        "Formatter.format() handles $week"

        self.assertEqual(self.f.format(
            "$week", 2010, 8, 4, 1, 2, 3
        ), "31")

    def test_weekday(self):
        "Formatter.format() handles $weekday"

        self.assertEqual(self.f.format(
            "$weekday", 2010, 8, 4, 1, 2, 3
        ), "3")

    def test_weekdayname(self):
        "Formatter.format() handles $weekdayname"

        self.assertEqual(self.f.format(
            "$weekdayname", 2010, 8, 4, 1, 2, 3
        ), "Wednesday")

    def test_year(self):
        "Formatter.format() handles $year"

        self.assertEqual(self.f.format(
            "$year", 2010, 8, 4, 1, 2, 3
        ), "2010")


if __name__ == "__main__":
    unittest.main()
