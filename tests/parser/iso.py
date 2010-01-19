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


class ISOParserTest(unittest.TestCase):

    def test_subclass(self):
        "ISOParser subclasses Parser"

        self.assertTrue(issubclass(
            chrono.parser.ISOParser, chrono.parser.parser.Parser
        ))


class ISOParser_compactdateTest(unittest.TestCase):

    def test_invalid_date(self):
        "ISOParser.compactdate() raises error for invalid date"

        self.assertRaises(
            chrono.DayError, chrono.parser.ISOParser.compactdate, "20090732"
        )

    def test_invalid_format(self):
        "ISOParser.compactdate() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.ISOParser.compactdate, "090229"
        )

    def test_none(self):
        "ISOParser.compactdate() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.ISOParser.compactdate, None)

    def test_parse(self):
        "ISOParser.compactdate() parses proper ISO compact dates (yyyymmdd)"

        self.assertEquals(
            chrono.parser.ISOParser.compactdate("20091227"),
            (2009, 12, 27)
        )


class ISOParser_compactordinalTest(unittest.TestCase):

    def test_invalid_compactordinal(self):
        "ISOParser.compactordinal() raises error on invalid date"

        self.assertRaises(
            chrono.DayError, chrono.parser.ISOParser.compactordinal, "2009366"
        )

    def test_invalid_format(self):
        "ISOParser.compactordinal() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError,
            chrono.parser.ISOParser.compactordinal, "2009abc"
        )

    def test_none(self):
        "ISOParser.compactordinal() raises TypeError on None"

        self.assertRaises(
            TypeError, chrono.parser.ISOParser.compactordinal, None
        )

    def test_parse(self):
        "ISOParser.compactordinal() parses proper ISO compactordinal dates (yyyyddd)"

        self.assertEquals(
            chrono.parser.ISOParser.compactordinal("2009202"),
            (2009, 202)
        )


class ISOParser_compacttimeTest(unittest.TestCase):

    def test_invalid_format(self):
        "ISOParser.compacttime() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.ISOParser.compacttime, "16xy"
        )

    def test_invalid_time(self):
        "ISOParser.compacttime() raises error on invalid time"

        self.assertRaises(
            chrono.HourError, chrono.parser.ISOParser.compacttime, "242743"
        )

    def test_full(self):
        "ISOParser.compacttime() accepts full time"

        self.assertEquals(
            chrono.parser.ISOParser.compacttime("162743"),
            (16, 27, 43)
        )

    def test_nominutes(self):
        "ISOParser.compacttime() accepts missing minutes"

        self.assertEquals(
            chrono.parser.ISOParser.compacttime("16"),
            (16, 0, 0)
        )

    def test_none(self):
        "ISOParser.compacttime() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.ISOParser.compacttime, None)

    def test_noseconds(self):
        "ISOParser.compacttime() accepts missing seconds"

        self.assertEquals(
            chrono.parser.ISOParser.compacttime("1627"),
            (16, 27, 0)
        )


class ISOParser_compactweekTest(unittest.TestCase):

    def test_invalid_date(self):
        "ISOParser.compactweek() raises error on invalid date"

        self.assertRaises(chrono.WeekError, chrono.parser.ISOParser.compactweek, "2008W53")

    def test_invalid_format(self):
        "ISOParser.compactweek() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.ISOParser.compactweek, "2009Wxx"
        )

    def test_lowercase(self):
        "ISOParser.compactweek() accepts lowercase input"

        self.assertEquals(
            chrono.parser.ISOParser.compactweek("2009w12"),
            (2009, 12)
        )

    def test_none(self):
        "ISOParser.compactweek() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.ISOParser.compactweek, None)

    def test_nozero(self):
        "ISOParser.compactweek() accepts weeks without leading zeroes"

        self.assertEquals(
            chrono.parser.ISOParser.compactweek("2009W7"),
            (2009, 7)
        )

    def test_parse(self):
        "ISOParser.compactweek() parses proper compact ISO week dates (yyyyWww)"

        self.assertEquals(
            chrono.parser.ISOParser.compactweek("2009W12"),
            (2009, 12)
        )


class ISOParser_compactweekdateTest(unittest.TestCase):

    def test_invalid_date(self):
        "ISOParser.compactweekdate() raises DayError on invalid weekdate"

        self.assertRaises(
            chrono.DayError,
            chrono.parser.ISOParser.compactweekdate, "2008W528"
        )

    def test_invalid_format(self):
        "ISOParser.compactweekdate() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError,
            chrono.parser.ISOParser.compactweekdate, "2009Wxxy"
        )

    def test_lowercase(self):
        "ISOParser.compactweekdate() accepts lowercase input"

        self.assertEquals(
            chrono.parser.ISOParser.compactweekdate("2009w124"),
            (2009, 12, 4)
        )

    def test_none(self):
        "ISOParser.compactweekdate() raises TypeError on None"

        self.assertRaises(
            TypeError, chrono.parser.ISOParser.compactweekdate, None
        )

    def test_parse(self):
        "ISOParser.compactweekdate() parses proper ISO weekdate dates (yyyyWwwd)"

        self.assertEquals(
            chrono.parser.ISOParser.compactweekdate("2009W123"),
            (2009, 12, 3)
        )


class ISOParser_dateTest(unittest.TestCase):

    def test_invalid_date(self):
        "ISOParser.date() raises error on invalid date"

        self.assertRaises(
            chrono.DayError, chrono.parser.ISOParser.date, "2009-02-29"
        )

    def test_invalid_format(self):
        "ISOParser.date() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.ISOParser.date, "xx-yy-zz"
        )

    def test_none(self):
        "ISOParser.date() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.ISOParser.date, None)

    def test_nozero(self):
        "ISOParser.date() parses dates without leading zeroes (2009-7-3)"

        self.assertEquals(
            chrono.parser.ISOParser.date("2009-7-3"),
            (2009, 7, 3)
        )

    def test_parse(self):
        "ISOParser.date() parses proper ISO dates (yyyy-mm-dd)"

        self.assertEquals(
            chrono.parser.ISOParser.date("2009-12-27"),
            (2009, 12, 27)
        )


class ISOParser_monthTest(unittest.TestCase):

    def test_invalid_date(self):
        "ISOParser.month() raises error on invalid date"

        self.assertRaises(
            chrono.MonthError, chrono.parser.ISOParser.month, "2009-13"
        )
 
    def test_invalid_format(self):
        "ISOParser.month() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.ISOParser.month, "2009-xyz"
        )

    def test_none(self):
        "ISOParser.month() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.ISOParser.month, None)

    def test_parse(self):
        "ISOParser.month() parses proper ISO month dates (yyyy-mm)"

        self.assertEquals(
            chrono.parser.ISOParser.month("2009-12"),
            (2009, 12)
        )


class ISOParser_ordinalTest(unittest.TestCase):

    def test_invalid_date(self):
        "ISOParser.ordinal() raises error on invalid ordinal date"

        self.assertRaises(
            chrono.DayError, chrono.parser.ISOParser.ordinal, "2009-366"
        )

    def test_invalid_format(self):
        "ISOParser.ordinal() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.ISOParser.ordinal, "2009-abc"
        )

    def test_none(self):
        "ISOParser.ordinal() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.ISOParser.ordinal, None)

    def test_parse(self):
        "ISOParser.ordinal() parses proper ISO ordinal dates (yyyy-ddd)"

        self.assertEquals(
            chrono.parser.ISOParser.ordinal("2009-202"),
            (2009, 202)
        )


class ISOParser_parse_dateTest(unittest.TestCase):

    def test_compactdate(self):
        "ISOParser.parse_date() parses compact ISO dates (yyyymmdd)"

        self.assertEquals(
            chrono.parser.ISOParser.parse_date("20091227"),
            (2009, 12, 27)
        )

    def test_compactordinal(self):
        "ISOParser.parse_date() parses compact ISO ordinal dates (yyyyddd)"

        self.assertEquals(
            chrono.parser.ISOParser.parse_date("2009202"),
            (2009, 7, 21)
        )

    def test_compactweek(self):
        "ISOParser.parse_date() parses compact ISO week dates (yyyyWww)"

        self.assertEquals(
            chrono.parser.ISOParser.parse_date("2009W32"),
            (2009, 8, 3)
        )

    def test_compactweekdate(self):
        "ISOParser.parse_date() parses compact ISO weekdates (yyyyWwwd)"

        self.assertEquals(
            chrono.parser.ISOParser.parse_date("2009W324"),
            (2009, 8, 6)
        )

    def test_date(self):
        "ISOParser.parse_date() parses ISO dates (yyyy-mm-dd)"

        self.assertEquals(
            chrono.parser.ISOParser.parse_date("2009-12-27"),
            (2009, 12, 27)
        )

    def test_invalid(self):
        "ISOParser.parse_date() raises error on invalid date"

        self.assertRaises(
            chrono.MonthError,
            chrono.parser.ISOParser.parse_date, "2009-13-27"
        )

    def test_month(self):
        "ISOParser.parse_date() parses ISO month dates (yyyy-mm)"

        self.assertEquals(
            chrono.parser.ISOParser.parse_date("2009-07"),
            (2009, 7, 1)
        )

    def test_none(self):
        "ISOParser.parse_date() raises TypeError on None"

        self.assertRaises(
            TypeError, chrono.parser.ISOParser.parse_date, None
        )

    def test_ordinal(self):
        "ISOParser.parse_date() parses ISO ordinal dates (yyyy-ddd)"

        self.assertEquals(
            chrono.parser.ISOParser.parse_date("2009-202"),
            (2009, 7, 21)
        )

    def test_unknown(self):
        "ISOParser.parse_date() raises ParseError for unknown date formats"

        self.assertRaises(
            chrono.ParseError, chrono.parser.ISOParser.parse_date, "abc"
        )

    def test_week(self):
        "ISOParser.parse_date() parses ISO week dates (yyyy-Www)"

        self.assertEquals(
            chrono.parser.ISOParser.parse_date("2009-W32"),
            (2009, 8, 3)
        )

    def test_weekdate(self):
        "ISOParser.parse_date() parses ISO weekdates (yyyy-Www-d)"

        self.assertEquals(
            chrono.parser.ISOParser.parse_date("2009-W32-4"),
            (2009, 8, 6)
        )

    def test_year(self):
        "ISOParser.parse_date() parses ISO year dates (yyyy)"

        self.assertEquals(
            chrono.parser.ISOParser.parse_date("2009"),
            (2009, 1, 1)
        )


class ISOParser_parse_datetimeTest(unittest.TestCase):

    def test_datetime(self):
        "ISOParser.parse_datetime() parses datetimes"

        self.assertEquals(
            chrono.parser.ISOParser.parse_datetime("2010-07-23 16:27:43"),
            (2010, 7, 23, 16, 27, 43)
        )

    def test_invalid_datetime(self):
        "ISOParser.parse_datetime() raises proper error for invalid values"

        self.assertRaises(
            chrono.YearError,
            chrono.parser.ISOParser.parse_datetime, "0000-07-23 16:27:43"
        )
        self.assertRaises(
            chrono.MonthError,
            chrono.parser.ISOParser.parse_datetime, "2010-13-23 16:27:43"
        )
        self.assertRaises(
            chrono.DayError,
            chrono.parser.ISOParser.parse_datetime, "2010-07-32 16:27:43"
        )
        self.assertRaises(
            chrono.HourError,
            chrono.parser.ISOParser.parse_datetime, "2010-07-23 24:27:43"
        )
        self.assertRaises(
            chrono.MinuteError,
            chrono.parser.ISOParser.parse_datetime, "2010-07-23 16:60:43"
        )
        self.assertRaises(
            chrono.SecondError,
            chrono.parser.ISOParser.parse_datetime, "2010-07-23 16:27:60"
        )

    def test_invalid_format(self):
        "ISOParser.parse_datetime() raises ParseError for invalid format"

        self.assertRaises(
            chrono.ParseError,
            chrono.parser.ISOParser.parse_datetime, "2010-07-23 16:27:43 xyz"
        )

    def test_nominutes(self):
        "ISOParser.parse_datetime() handles times without minutes"

        self.assertEquals(
            chrono.parser.ISOParser.parse_datetime("2010-07-23 16"),
            (2010, 7, 23, 16, 0, 0)
        )

    def test_noseconds(self):
        "ISOParser.parse_datetime() handles times without seconds"

        self.assertEquals(
            chrono.parser.ISOParser.parse_datetime("2010-07-23 16:27"),
            (2010, 7, 23, 16, 27, 0)
        )

    def test_t(self):
        "ISOParser.parse_datetime() parses T-separated datetimes"

        self.assertEquals(
            chrono.parser.ISOParser.parse_datetime("2010-07-23T16:27:43"),
            (2010, 7, 23, 16, 27, 43)
        )

    def test_t_lowercase(self):
        "ISOParser.parse_datetime() parses t-separated datetimes"

        self.assertEquals(
            chrono.parser.ISOParser.parse_datetime("2010-07-23t16:27:43"),
            (2010, 7, 23, 16, 27, 43)
        )


class ISOParser_parse_timeTest(unittest.TestCase):

    def test_compacttime(self):
        "ISOParser.parse_time() parses compact ISO times (hhmmss)"

        self.assertEquals(
            chrono.parser.ISOParser.parse_time("162743"),
            (16, 27, 43)
        )

    def test_invalid(self):
        "ISOParser.parse_time() raises error for invalid times"

        self.assertRaises(
            chrono.HourError, chrono.parser.ISOParser.parse_time, "24:27:43"
        )

    def test_none(self):
        "ISOParser.parse_time() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.ISOParser.parse_time, None)

    def test_time(self):
        "ISOParser.parse_time() parses ISO times (hh:mm:ss)"

        self.assertEquals(
            chrono.parser.ISOParser.parse_time("16:27:43"),
            (16, 27, 43)
        )

    def test_unknown(self):
        "ISOParser.parse_time() raises ParseError for unknown time formats"

        self.assertRaises(
            chrono.ParseError, chrono.parser.ISOParser.parse_time, "abc"
        )


class ISOParser_timeTest(unittest.TestCase):

    def test_invalid_format(self):
        "ISOParser.time() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.ISOParser.time, "16:xy"
        )

    def test_invalid_time(self):
        "ISOParser.time() raises error on invalid time"

        self.assertRaises(
            chrono.HourError, chrono.parser.ISOParser.time, "24:27:43"
        )

    def test_full(self):
        "ISOParser.time() accepts full time"

        self.assertEquals(
            chrono.parser.ISOParser.time("16:27:43"),
            (16, 27, 43)
        )

    def test_nominutes(self):
        "ISOParser.time() accepts missing minutes"

        self.assertEquals(
            chrono.parser.ISOParser.time("16"),
            (16, 0, 0)
        )

    def test_none(self):
        "ISOParser.time() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.ISOParser.time, None)

    def test_noseconds(self):
        "ISOParser.time() accepts missing seconds"

        self.assertEquals(
            chrono.parser.ISOParser.time("16:27"),
            (16, 27, 0)
        )

    def test_nozero(self):
        "ISOParser.time() accepts missing zeroes"

        self.assertEquals(
            chrono.parser.ISOParser.time("8:2:4"),
            (8, 2, 4)
        )


class ISOParser_weekTest(unittest.TestCase):

    def test_invalid_date(self):
        "ISOParser.week() raises error on invalid date"

        self.assertRaises(
            chrono.WeekError, chrono.parser.ISOParser.week, "2008-W53"
        )

    def test_invalid_format(self):
        "ISOParser.week() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.ISOParser.week, "2009-Wxx"
        )

    def test_lowercase(self):
        "ISOParser.week() accepts lowercase input"

        self.assertEquals(
            chrono.parser.ISOParser.week("2009-w12"),
            (2009, 12)
        )

    def test_none(self):
        "ISOParser.week() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.ISOParser.week, None)

    def test_nozero(self):
        "ISOParser.week() accepts weeks without leading zeroes"

        self.assertEquals(
            chrono.parser.ISOParser.week("2009-W7"),
            (2009, 7)
        )

    def test_parse(self):
        "ISOParser.week() parses proper ISO week dates (yyyy-Www)"

        self.assertEquals(
            chrono.parser.ISOParser.week("2009-W12"),
            (2009, 12)
        )


class ISOParser_weekdateTest(unittest.TestCase):

    def test_invalid_date(self):
        "ISOParser.weekdate() raises error on invalid weekdate"

        self.assertRaises(
            chrono.DayError, chrono.parser.ISOParser.weekdate, "2008-W52-8"
        )

    def test_invalid_format(self):
        "ISOParser.weekdate() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.ISOParser.weekdate, "2009-Wxx-y"
        )

    def test_lowercase(self):
        "ISOParser.weekdate() accepts lowercase input"

        self.assertEquals(
            chrono.parser.ISOParser.weekdate("2009-w12-4"),
            (2009, 12, 4)
        )

    def test_none(self):
        "ISOParser.weekdate() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.ISOParser.weekdate, None)

    def test_nozero(self):
        "ISOParser.weekdate() accepts weekdates without leading zeroes"

        self.assertEquals(
            chrono.parser.ISOParser.weekdate("2009-W7-3"),
            (2009, 7, 3)
        )

    def test_parse(self):
        "ISOParser.weekdate() parses proper ISO weekdate dates (yyyy-Www-d)"

        self.assertEquals(
            chrono.parser.ISOParser.weekdate("2009-W12-3"),
            (2009, 12, 3)
        )


class ISOParser_yearTest(unittest.TestCase):

    def test_invalid_date(self):
        "ISOParser.year() raises YearError on invalid year"

        self.assertRaises(
            chrono.YearError, chrono.parser.ISOParser.year, "0"
        )

    def test_invalid_format(self):
        "ISOParser.year() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.ISOParser.year, "abc"
        )

    def test_none(self):
        "ISOParser.year() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.ISOParser.year, None)

    def test_parse(self):
        "ISOParser.year() parses proper ISO compact dates (yyyymmdd)"

        self.assertEquals(chrono.parser.ISOParser.year("2009"), 2009)


if __name__ == "__main__":
    unittest.main()
