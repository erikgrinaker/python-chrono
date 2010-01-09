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
import datetime
import time
import unittest


class Time__cmpTest(unittest.TestCase):

	def test_equal(self):
		"Time.__cmp__() handles equality"

		self.assertTrue(chrono.Time("16:27:43") == chrono.Time("16:27:43"))

	def test_gt(self):
		"Time.__cmp__() handles > comparison"

		self.assertTrue(chrono.Time("16:27:43") > chrono.Time("16:27:42"))

	def test_lt(self):
		"Time.__cmp__() handles < comparison"

		self.assertTrue(chrono.Time("16:27:43") < chrono.Time("16:28:12"))

	def test_none_equal(self):
		"Time.__cmp__() handles equality with None"

		self.assertTrue(chrono.Time() == None)

	def test_none_gt(self):
		"Time.__cmp__() handles > comparison with None"

		self.assertTrue(chrono.Time("16:27:43") > None)

	def test_none_lt(self):
		"Time.__cmp__() handles < comparison with None"

		self.assertFalse(chrono.Time() < None)

	def test_string_equal(self):
		"Time.__cmp__() handles equality with strings"

		self.assertTrue(chrono.Time("16:27:43") == "16:27:43")

	def test_string_gt(self):
		"Time.__cmp__() handles > comparison with strings"

		self.assertTrue(chrono.Time("16:27:43") > "16:27:42")

	def test_string_lt(self):
		"Time.__cmp__() handles < comparison with strings"

		self.assertTrue(chrono.Time("16:27:43") < "16:28:12")


class Time__initTest(unittest.TestCase):

	def test_datetime_time(self):
		"Time.__init__() copies time from datetime.time objects"

		self.assertEquals(
			chrono.Time(datetime.time(16, 27, 43)).get(),
			(16, 27, 43)
		)

	def test_datetime_datetime(self):
		"Time.__init__() copies time from datetime.datetime objects"

		self.assertEquals(
			chrono.Time(datetime.datetime(2010, 1, 4, 16, 27, 43)).get(),
			(16, 27, 43)
		)

	def test_default(self):
		"Time.__init__() without parameters sets up empty date"

		self.assertEquals(chrono.Time().get(), None)

	def test_false(self):
		"Time,__init__() with False sets up empty time"

		self.assertEquals(chrono.Time(False).get(), None)

	def test_kwargs(self):
		"Time.__init__() accepts keyword arguments"

		self.assertEquals(
			chrono.Time(hour = 16, minute = 27, second = 43).get(),
			(16, 27, 43)
		)

	def test_kwargs_partial(self):
		"Time.__init__() accepts partial kwargs"

		t = chrono.Time(hour = 16, second = 43)

		self.assertEquals(t.hour, 16)
		self.assertEquals(t.minute, None)
		self.assertEquals(t.second, 43)

	def test_none(self):
		"Time.__init__() with None sets up empty time"

		self.assertEquals(chrono.Time(None).get(), None)

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

	def test_unknowntype(self):
		"Time.__init__() raises TypeError on unknown type"

		self.assertRaises(TypeError, chrono.Time, [])


class Time__reprTest(unittest.TestCase):

	def test_empty(self):
		"Time.__repr__() handles empty times"

		self.assertEquals(repr(chrono.Time()), "chrono.Time()")

	def test_partial(self):
		"Time.__repr__() handles partial times"

		self.assertEquals(
			repr(chrono.Time(hour = 16, second = 27)),
			"chrono.Time(hour = 16, second = 27)"
		)

	def test_repr(self):
		"Time.__repr__() shows code to recreate object"

		self.assertEquals(
				repr(chrono.Time("16:27:43")),
			"chrono.Time(hour = 16, minute = 27, second = 43)"
		)


class Time__setattrTest(unittest.TestCase):

	def test_hour_invalid(self):
		"Time.__setattr__() raises ValueError on hour outside range (0-23)"

		t = chrono.Time("16:27:43")

		self.assertRaises(ValueError, setattr, t, "hour", 24)

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
		"Time.__setattr__() handles double minute rollunder for negative seconds"

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


class Time_clearTest(unittest.TestCase):

	def test_clear(self):
		"Time.clear() clears time attributes"

		t = chrono.Time(hour = 16, minute = 27, second = 43)
		t.clear()

		self.assertEquals(t.hour, None)
		self.assertEquals(t.minute, None)
		self.assertEquals(t.second, None)


class Time_getTest(unittest.TestCase):

	def test_empty(self):
		"Time.get() returns None if time is not set"

		self.assertEquals(chrono.Time().get(), None)

	def test_get(self):
		"Time.get() returns tuple of hour, minute, and second"

		self.assertEquals(
			chrono.Time(hour = 16, minute = 27, second = 43).get(),
			(16, 27, 43)
		)


class Time_get_datetimeTest(unittest.TestCase):

	def test_empty(self):
		"Time.get_datetime() returns None if time is not set"

		self.assertEquals(chrono.Time().get_datetime(), None)

	def test_get_datetime(self):
		"Time.get_datetime() returns datetime.time object"

		dt = chrono.Time(hour = 16, minute = 27, second = 43).get_datetime()

		self.assertTrue(isinstance(dt, datetime.time))

		self.assertEquals(dt.hour,	16)
		self.assertEquals(dt.minute,	27)
		self.assertEquals(dt.second,	43)


class Time_is_setTest(unittest.TestCase):

	def test_empty(self):
		"Time.is_set() returns False if no attributes are set"

		self.assertFalse(chrono.Time().is_set())

	def test_partial(self):
		"Time.is_set() returns False if only some attributes are set"

		self.assertFalse(chrono.Time(hour = 16, second = 43).is_set())

	def test_set(self):
		"Time.is_set() returns True if time is set"

		self.assertTrue(chrono.Time(hour = 16, minute = 27, second = 43).is_set())


class Time_setTest(unittest.TestCase):

	def test_invalid_time(self):
		"Time.set() raises ValueError on invalid time"

		t = chrono.Time()

		self.assertRaises(ValueError, t.set, 25, 27, 43)

	def test_invalid_type(self):
		"Time.set() raises TypeError on invalid types"

		t = chrono.Time()

		self.assertRaises(TypeError, t.set, None, 27, 43)

	def test_replace(self):
		"Time.set() replaces set time"

		t = chrono.Time(hour = 16, minute = 27, second = 43)
		t.set(8, 35, 19)

		self.assertEquals(t.get(), (8, 35, 19))

	def test_set(self):
		"Time.set() sets the time"

		t = chrono.Time()
		t.set(16, 27, 43)

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


class Time_set_isoTest(unittest.TestCase):

	def test_time(self):
		"Time.set_iso() sets time from iso string"

		t = chrono.Time()
		t.set_iso("16:27:43")

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
