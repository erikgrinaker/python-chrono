#!/usr/bin/env python

import chrono
import unittest


class CommonParserTest(unittest.TestCase):

    def test_subclass(self):
        "CommonParser subclasses Parser"

        self.assertTrue(issubclass(
            chrono.parser.CommonParser, chrono.parser.parser.Parser
        ))


class CommonParser_parse_dateTest(unittest.TestCase):

    def test_euro(self):
        "CommonParser.parse_date() handles european dates (dd.mm.yyyy)"

        self.assertEquals(
            chrono.parser.CommonParser.parse_date("27.08.2010"),
            (2010, 8, 27)
        )

    def test_invalid_date(self):
        "CommonParser.parse_date() raises error on invalid date"

        self.assertRaises(
            chrono.MonthError,
            chrono.parser.CommonParser.parse_date, "27.13.2010"
        )

    def test_invalid_format(self):
        "EuroParser.compactdate() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.CommonParser.parse_date, "xxyyzzzz"
        )

    def test_iso(self):
        "CommonParser.parse_date() handles ISO dates (yyyy-mm-dd)"

        self.assertEquals(
            chrono.parser.CommonParser.parse_date("2010-08-27"),
            (2010, 8, 27)
        )

    def test_iso_month(self):
        "CommonParser.parse_date() handles ISO month dates (yyyy-mm)"

        self.assertEquals(
            chrono.parser.CommonParser.parse_date("2010-08"),
            (2010, 8, 1)
        )

    def test_iso_ordinal(self):
        "CommonParser.parse_date() handles ISO ordinal dates (yyyy-ddd)"

        self.assertEquals(
            chrono.parser.CommonParser.parse_date("2010-165"),
            (2010, 6, 14)
        )

    def test_iso_week(self):
        "CommonParser.parse_date() handles ISO week dates (yyyy-Www)"

        self.assertEquals(
            chrono.parser.CommonParser.parse_date("2010-W32"),
            (2010, 8, 9)
        )

    def test_iso_weekdate(self):
        "CommonParser.parse_date() handles ISO weekdates (yyyy-Www-dd)"

        self.assertEquals(
            chrono.parser.CommonParser.parse_date("2010-W32-5"),
            (2010, 8, 13)
        )

    def test_iso_year(self):
        "CommonParser.parse_date() handles ISO years (yyyy)"

        self.assertEquals(
            chrono.parser.CommonParser.parse_date("2010"),
            (2010, 1, 1)
        )

    def test_us(self):
        "CommonParser.parse_date() handles US dates (mm/dd/yyyy)"

        self.assertEquals(
            chrono.parser.CommonParser.parse_date("08/27/2010"),
            (2010, 8, 27)
        )


class CommonParser_parse_datetimeTest(unittest.TestCase):

    def test_euro(self):
        "CommonParser.parse_datetime() handles european datetimes"

        self.assertEquals(
            chrono.parser.CommonParser.parse_datetime("27.08.2010 16:27:43"),
            (2010, 8, 27, 16, 27, 43)
        )

    def test_iso(self):
        "CommonParser.parse_datetime() handles ISO datetimes"

        self.assertEquals(
            chrono.parser.CommonParser.parse_datetime("2010-08-27 16:27:43"),
            (2010, 8, 27, 16, 27, 43)
        )

    def test_invalid(self):
        "CommonParser.parse_datetime() raises error for invalid datetime"

        self.assertRaises(
            chrono.MonthError,
            chrono.parser.CommonParser.parse_datetime, "13/27/2010 4:27:43 PM"
        )

    def test_unknown(self):
        "CommonParser.parse_datetime() raises ParseError for invalid format"

        self.assertRaises(
            chrono.ParseError,
            chrono.parser.CommonParser.parse_datetime, "xyz abc"
        )

    def test_us(self):
        "CommonParser.parse_datetime() handles US datetimes"

        self.assertEquals(
            chrono.parser.CommonParser.parse_datetime("08/27/2010 4:27:43 PM"),
            (2010, 8, 27, 16, 27, 43)
        )


class CommonParser_parse_timeTest(unittest.TestCase):

    def test_invalid(self):
        "CommonParser.parse_time() raises error for invalid times"

        self.assertRaises(
            chrono.HourError, chrono.parser.CommonParser.parse_time, "24:27:43"
        )

    def test_iso_compacttime(self):
        "CommonParser.parse_time() parses compact ISO times (hhmmss)"

        self.assertEquals(
            chrono.parser.CommonParser.parse_time("162743"),
            (16, 27, 43)
        )

    def test_iso_time(self):
        "CommonParser.parse_time() parses ISO times (hh:mm:ss)"

        self.assertEquals(
            chrono.parser.CommonParser.parse_time("16:27:43"),
            (16, 27, 43)
        )

    def test_none(self):
        "CommonParser.parse_time() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.CommonParser.parse_time, None)

    def test_unknown(self):
        "CommonParser.parse_time() raises ParseError for unknown time formats"

        self.assertRaises(
            chrono.ParseError, chrono.parser.CommonParser.parse_time, "abc"
        )

    def test_us_compacttime(self):
        "CommonParser.parse_time() handles compact times (hhmmss ampm)"

        self.assertEquals(
            chrono.parser.CommonParser.parse_time("042743 PM"),
            (16, 27, 43)
        )

    def test_us_time(self):
        "CommonParser.parse_time() handles normal times (hh:mm:ss ampm)"

        self.assertEquals(
            chrono.parser.CommonParser.parse_time("04:27:43 PM"),
            (16, 27, 43)
        )


if __name__ == "__main__":
    unittest.main()
