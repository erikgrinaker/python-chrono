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

	def setUp(self):
		unittest.TestCase.setUp(self)

		self.f = chrono.formatter.Formatter(2010, 8, 4, 1, 2, 3)

	def test_012hour(self):
		"Formatter.format() handles $012hour"

		self.f.hour = 15

		self.assertEqual(self.f.format("$012hour"), "03")

	def test_0day(self):
		"Formatter.format() handles $0day"

		self.assertEqual(self.f.format("$0day"), "04")

	def test_0hour(self):
		"Formatter.format() handles $0hour"

		self.assertEqual(self.f.format("$0hour"), "01")

	def test_0minute(self):
		"Formatter.format() handles $0minute"

		self.assertEqual(self.f.format("$0minute"), "02")

	def test_0month(self):
		"Formatter.format() handles $0month"

		self.assertEqual(self.f.format("$0month"), "08")

	def test_0second(self):
		"Formatter.format() handles $0second"

		self.assertEqual(self.f.format("$0second"), "03")

	def test_0week(self):
		"Formatter.format() handles $0week"

		self.f.month = 2

		self.assertEqual(self.f.format("$0week"), "05")

	def test_0year(self):
		"Formatter.format() handles $0year"

		self.f.year = 492

		self.assertEqual(self.f.format("$0year"), "0492")

	def test_12hour(self):
		"Formatter.format() handles $12hour"

		self.f.hour = 15

		self.assertEqual(self.f.format("$12hour"), "3")

	def test_ampm(self):
		"Formatter.format() handles $ampm"

		self.assertEqual(self.f.format("$ampm"), "AM")

		self.f.hour = 12

		self.assertEqual(self.f.format("$ampm"), "PM")

	def test_day(self):
		"Formatter.format() handles $day"

		self.assertEqual(self.f.format("$day"), "4")

	def test_hour(self):
		"Formatter.format() handles $hour"

		self.assertEqual(self.f.format("$hour"), "1")

	def test_minute(self):
		"Formatter.format() handles $minute"

		self.assertEqual(self.f.format("$minute"), "2")

	def test_month(self):
		"Formatter.format() handles $month"

		self.assertEqual(self.f.format("$month"), "8")

	def test_monthname(self):
		"Formatter.format() handles $monthname"

		self.assertEqual(self.f.format("$monthname"), "August")

	def test_second(self):
		"Formatter.format() handles $second"

		self.assertEqual(self.f.format("$second"), "3")

	def test_shortmonthname(self):
		"Formatter.format() handles $shortmonthname"

		self.assertEqual(self.f.format("$shortmonthname"), "Aug")

	def test_shortweekdayname(self):
		"Formatter.format() handles $shortweekdayname"

		self.assertEqual(self.f.format("$shortweekdayname"), "Wed")

	def test_shortyear(self):
		"Formatter.format() handles $shortyear"

		self.assertEqual(self.f.format("$shortyear"), "10")

	def test_week(self):
		"Formatter.format() handles $week"

		self.assertEqual(self.f.format("$week"), "31")

	def test_weekday(self):
		"Formatter.format() handles $weekday"

		self.assertEqual(self.f.format("$weekday"), "3")

	def test_weekdayname(self):
		"Formatter.format() handles $weekdayname"

		self.assertEqual(self.f.format("$weekdayname"), "Wednesday")

	def test_year(self):
		"Formatter.format() handles $year"

		self.assertEqual(self.f.format("$year"), "2010")


if __name__ == "__main__":
	unittest.main()
