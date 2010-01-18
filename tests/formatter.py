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


class Formatter_formatTest(unittest.TestCase):

    def test_012hour(self):
        "Formatter.format() handles $012hour"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$012hour", 2010, 8, 4, 15, 2, 3
        ), "03")

    def test_0day(self):
        "Formatter.format() handles $0day"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$0day", 2010, 8, 4, 1, 2, 3
        ), "04")

    def test_0hour(self):
        "Formatter.format() handles $0hour"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$0hour", 2010, 8, 4, 1, 2, 3
        ), "01")

    def test_0minute(self):
        "Formatter.format() handles $0minute"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$0minute", 2010, 8, 4, 1, 2, 3
        ), "02")

    def test_0month(self):
        "Formatter.format() handles $0month"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$0month", 2010, 8, 4, 1, 2, 3
        ), "08")

    def test_0second(self):
        "Formatter.format() handles $0second"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$0second", 2010, 8, 4, 1, 2, 3
        ), "03")

    def test_0week(self):
        "Formatter.format() handles $0week"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$0week", 2010, 2, 4, 1, 2, 3
        ), "05")

    def test_0year(self):
        "Formatter.format() handles $0year"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$0year", 492, 8, 4, 1, 2, 3
        ), "0492")

    def test_12hour(self):
        "Formatter.format() handles $12hour"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$12hour", 2010, 8, 4, 15, 2, 3
        ), "3")

    def test_ampm(self):
        "Formatter.format() handles $ampm"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$ampm", 2010, 8, 4, 1, 2, 3
        ), "AM")

        self.assertEqual(chrono.formatter.Formatter.format(
            "$ampm", 2010, 8, 4, 12, 2, 3
        ), "PM")

    def test_day(self):
        "Formatter.format() handles $day"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$day", 2010, 8, 4, 1, 2, 3
        ), "4")

    def test_escape(self):
        "Formatter.format() handles escaped $ signs"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$year$$$month", 2010, 8, 4, 1, 2, 3
        ), "2010$8")

    def test_hour(self):
        "Formatter.format() handles $hour"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$hour", 2010, 8, 4, 1, 2, 3
        ), "1")

    def test_invalid(self):
        "Formatter.format() ignores invalid patterns"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$-}", 2010, 8, 4, 1, 2, 3
        ), "$-}")

    def test_minute(self):
        "Formatter.format() handles $minute"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$minute", 2010, 8, 4, 1, 2, 3
        ), "2")

    def test_missing(self):
        "Formatter.format() returns blank content for variables with no value"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$0year-$0month-$0day", 2010, None, 4, 1, 2, 3
        ), "2010--04")

    def test_month(self):
        "Formatter.format() handles $month"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$month", 2010, 8, 4, 1, 2, 3
        ), "8")

    def test_monthname(self):
        "Formatter.format() handles $monthname"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$monthname", 2010, 8, 4, 1, 2, 3
        ), "August")

    def test_second(self):
        "Formatter.format() handles $second"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$second", 2010, 8, 4, 1, 2, 3
        ), "3")

    def test_shortmonthname(self):
        "Formatter.format() handles $shortmonthname"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$shortmonthname", 2010, 8, 4, 1, 2, 3
        ), "Aug")

    def test_shortweekdayname(self):
        "Formatter.format() handles $shortweekdayname"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$shortweekdayname", 2010, 8, 4, 1, 2, 3
        ), "Wed")

    def test_shortyear(self):
        "Formatter.format() handles $shortyear"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$shortyear", 2010, 8, 4, 1, 2, 3
        ), "10")

    def test_unknown(self):
        "Formatter.format() ignores unknown variables"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$0year-$dummy-$0day", 2010, 8, 4, 1, 2, 3
        ), "2010-$dummy-04")

    def test_week(self):
        "Formatter.format() handles $week"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$week", 2010, 8, 4, 1, 2, 3
        ), "31")

    def test_weekday(self):
        "Formatter.format() handles $weekday"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$weekday", 2010, 8, 4, 1, 2, 3
        ), "3")

    def test_weekdayname(self):
        "Formatter.format() handles $weekdayname"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$weekdayname", 2010, 8, 4, 1, 2, 3
        ), "Wednesday")

    def test_year(self):
        "Formatter.format() handles $year"

        self.assertEqual(chrono.formatter.Formatter.format(
            "$year", 2010, 8, 4, 1, 2, 3
        ), "2010")


if __name__ == "__main__":
    unittest.main()
