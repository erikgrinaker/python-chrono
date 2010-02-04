#!/usr/bin/env python

import chrono
import unittest


class EuroParserTest(unittest.TestCase):

    def test_subclass(self):
        "EuroParser subclasses Parser"

        self.assertTrue(issubclass(
            chrono.parser.EuroParser, chrono.parser.parser.Parser
        ))


class EuroParser_compactdateTest(unittest.TestCase):

    def test_invalid_date(self):
        "EuroParser.compactdate() raises error on invalid date"

        self.assertRaises(
            chrono.DayError, chrono.parser.EuroParser.compactdate, "29022009"
        )

    def test_invalid_format(self):
        "EuroParser.compactdate() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.EuroParser.compactdate, "xxyyzzzz"
        )

    def test_none(self):
        "EuroParser.compactdate() raises TypeError on None"

        self.assertRaises(
            TypeError, chrono.parser.EuroParser.compactdate, None
        )

    def test_parse(self):
        "EuroParser.compactdate() parses proper dates (ddmmyyyy)"

        self.assertEquals(
            chrono.parser.EuroParser.compactdate("27122009"),
            (2009, 12, 27)
        )

    def test_shortyear(self):
        "EuroParser.compactdate() handles two-digit years"

        self.assertEquals(
            chrono.parser.EuroParser.compactdate("271209"),
            (2009, 12, 27)
        )


class EuroParser_compacttimeTest(unittest.TestCase):

    def test_invalid_format(self):
        "EuroParser.compacttime() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.EuroParser.compacttime, "16xy"
        )

    def test_invalid_time(self):
        "EuroParser.compacttime() raises error on invalid time"

        self.assertRaises(
            chrono.HourError, chrono.parser.EuroParser.compacttime, "242743"
        )

    def test_full(self):
        "EuroParser.compacttime() accepts full time"

        self.assertEquals(
            chrono.parser.EuroParser.compacttime("162743"),
            (16, 27, 43)
        )

    def test_nominutes(self):
        "EuroParser.compacttime() accepts missing minutes"

        self.assertEquals(
            chrono.parser.EuroParser.compacttime("16"),
            (16, 0, 0)
        )

    def test_none(self):
        "EuroParser.compacttime() raises TypeError on None"

        self.assertRaises(
            TypeError, chrono.parser.EuroParser.compacttime, None
        )

    def test_noseconds(self):
        "EuroParser.compacttime() accepts missing seconds"

        self.assertEquals(
            chrono.parser.EuroParser.compacttime("1627"),
            (16, 27, 0)
        )


class EuroParser_dashdateTest(unittest.TestCase):

    def test_invalid_date(self):
        "EuroParser.dashdate() raises error on invalid date"

        self.assertRaises(
            chrono.DayError, chrono.parser.EuroParser.dashdate, "29-02-2009"
        )

    def test_invalid_format(self):
        "EuroParser.dashdate() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.EuroParser.dashdate, "xx-yy-zzzz"
        )

    def test_none(self):
        "EuroParser.dashdate() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.EuroParser.dashdate, None)

    def test_nozero(self):
        "EuroParser.dashdate() parses dates without leading zeroes (3-7-2009)"

        self.assertEquals(
            chrono.parser.EuroParser.dashdate("3-7-2009"),
            (2009, 7, 3)
        )

    def test_parse(self):
        "EuroParser.dashdate() parses proper dates (dd-mm-yyyy)"

        self.assertEquals(
            chrono.parser.EuroParser.dashdate("27-12-2009"),
            (2009, 12, 27)
        )

    def test_shortyear(self):
        "EuroParser.dashdate() handles two-digit years"

        self.assertEquals(
            chrono.parser.EuroParser.dashdate("27-12-09"),
            (2009, 12, 27)
        )


class EuroParser_dateTest(unittest.TestCase):

    def test_invalid_date(self):
        "EuroParser.date() raises error on invalid date"

        self.assertRaises(
            chrono.DayError, chrono.parser.EuroParser.date, "29.02.2009"
        )

    def test_invalid_format(self):
        "EuroParser.date() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.EuroParser.date, "xx.yy.zzzz"
        )

    def test_none(self):
        "EuroParser.date() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.EuroParser.date, None)

    def test_nozero(self):
        "EuroParser.date() parses dates without leading zeroes (3.7.2009)"

        self.assertEquals(
            chrono.parser.EuroParser.date("3.7.2009"),
            (2009, 7, 3)
        )

    def test_parse(self):
        "EuroParser.date() parses proper dates (27.12.2009)"

        self.assertEquals(
            chrono.parser.EuroParser.date("27.12.2009"),
            (2009, 12, 27)
        )

    def test_shortyear(self):
        "EuroParser.date() handles two-digit years"

        self.assertEquals(
            chrono.parser.EuroParser.date("27.12.09"),
            (2009, 12, 27)
        )


class EuroParser_parse_dateTest(unittest.TestCase):

    def test_compactdate(self):
        "EuroParser.parse_date() handles compact dates (ddmmyyyy)"

        self.assertEquals(
            chrono.parser.EuroParser.parse_date("27082010"),
            (2010, 8, 27)
        )

    def test_dashdate(self):
        "EuroParser.parse_date() handles dash dates (dd-mm-yyyy)"

        self.assertEquals(
            chrono.parser.EuroParser.parse_date("27-08-2010"),
            (2010, 8, 27)
        )

    def test_date(self):
        "EuroParser.parse_date() handles normal dates (dd.mm.yyyy)"

        self.assertEquals(
            chrono.parser.EuroParser.parse_date("27.08.2010"),
            (2010, 8, 27)
        )

    def test_slashdate(self):
        "EuroParser.parse_date() handles slash dates (dd/mm/yyyy)"

        self.assertEquals(
            chrono.parser.EuroParser.parse_date("27/08/2010"),
            (2010, 8, 27)
        )

    def test_invalid(self):
        "EuroParser.parse_date() raises error on invalid date"

        self.assertRaises(
            chrono.MonthError,
            chrono.parser.EuroParser.parse_date, "27.13.2010"
        )


class EuroParser_parse_datetimeTest(unittest.TestCase):

    def test_datetime(self):
        "EuroParser.parse_datetime() parses datetimes"

        self.assertEquals(
            chrono.parser.EuroParser.parse_datetime("23.07.2010 16:27:43"),
            (2010, 7, 23, 16, 27, 43)
        )

    def test_invalid_datetime(self):
        "EuroParser.parse_datetime() raises proper error for invalid values"

        self.assertRaises(
            chrono.YearError,
            chrono.parser.EuroParser.parse_datetime, "23.07.0000 16:27:43"
        )
        self.assertRaises(
            chrono.MonthError,
            chrono.parser.EuroParser.parse_datetime, "23.13.2010 16:27:43"
        )
        self.assertRaises(
            chrono.DayError,
            chrono.parser.EuroParser.parse_datetime, "32.07.2010 16:27:43"
        )
        self.assertRaises(
            chrono.HourError,
            chrono.parser.EuroParser.parse_datetime, "23.07.2010 24:27:43"
        )
        self.assertRaises(
            chrono.MinuteError,
            chrono.parser.EuroParser.parse_datetime, "23.07.2010 16:60:43"
        )
        self.assertRaises(
            chrono.SecondError,
            chrono.parser.EuroParser.parse_datetime, "23.07.2010 16:27:60"
        )

    def test_invalid_format(self):
        "EuroParser.parse_datetime() raises ParseError for invalid format"

        self.assertRaises(
            chrono.ParseError,
            chrono.parser.EuroParser.parse_datetime, "23.07.2010 16:27:43 xyz"
        )

    def test_nominutes(self):
        "EuroParser.parse_datetime() handles times without minutes"

        self.assertEquals(
            chrono.parser.EuroParser.parse_datetime("23.07.2010 16"),
            (2010, 7, 23, 16, 0, 0)
        )

    def test_noseconds(self):
        "EuroParser.parse_datetime() handles times without seconds"

        self.assertEquals(
            chrono.parser.EuroParser.parse_datetime("23.07.2010 16:27"),
            (2010, 7, 23, 16, 27, 0)
        )


class EuroParser_parse_timeTest(unittest.TestCase):

    def test_compacttime(self):
        "EuroParser.parse_time() parses compact Euro times (hhmmss)"

        self.assertEquals(
            chrono.parser.EuroParser.parse_time("162743"),
            (16, 27, 43)
        )

    def test_invalid(self):
        "EuroParser.parse_time() raises error for invalid times"

        self.assertRaises(
            chrono.HourError, chrono.parser.EuroParser.parse_time, "24:27:43"
        )

    def test_none(self):
        "EuroParser.parse_time() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.EuroParser.parse_time, None)

    def test_time(self):
        "EuroParser.parse_time() parses Euro times (hh:mm:ss)"

        self.assertEquals(
            chrono.parser.EuroParser.parse_time("16:27:43"),
            (16, 27, 43)
        )

    def test_unknown(self):
        "EuroParser.parse_time() raises ParseError for unknown time formats"

        self.assertRaises(
            chrono.ParseError, chrono.parser.EuroParser.parse_time, "abc"
        )


class EuroParser_slashdateTest(unittest.TestCase):

    def test_invalid_slashdate(self):
        "EuroParser.slashdate() raises error on invalid date"

        self.assertRaises(
            chrono.DayError, chrono.parser.EuroParser.slashdate, "29/02/2009"
        )

    def test_invalid_format(self):
        "EuroParser.slashdate() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.EuroParser.slashdate, "xx/yy/zzzz"
        )

    def test_none(self):
        "EuroParser.slashdate() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.EuroParser.slashdate, None)

    def test_nozero(self):
        "EuroParser.slashdate() parses dates without leading zeroes (3/7/2009)"

        self.assertEquals(
            chrono.parser.EuroParser.slashdate("3/7/2009"),
            (2009, 7, 3)
        )

    def test_parse(self):
        "EuroParser.slashdate() parses proper dates (dd/mm/yyyy)"

        self.assertEquals(
            chrono.parser.EuroParser.slashdate("27/12/2009"),
            (2009, 12, 27)
        )

    def test_shortyear(self):
        "EuroParser.slashdate() handles two-digit years"

        self.assertEquals(
            chrono.parser.EuroParser.slashdate("27/12/09"),
            (2009, 12, 27)
        )


class EuroParser_timeTest(unittest.TestCase):

    def test_invalid_format(self):
        "EuroParser.time() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.EuroParser.time, "16:xy"
        )

    def test_invalid_time(self):
        "EuroParser.time() raises error on invalid time"

        self.assertRaises(
            chrono.HourError, chrono.parser.EuroParser.time, "24:27:43"
        )

    def test_full(self):
        "EuroParser.time() accepts full time"

        self.assertEquals(
            chrono.parser.EuroParser.time("16:27:43"),
            (16, 27, 43)
        )

    def test_nominutes(self):
        "EuroParser.time() accepts missing minutes"

        self.assertEquals(
            chrono.parser.EuroParser.time("16"),
            (16, 0, 0)
        )

    def test_none(self):
        "EuroParser.time() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.EuroParser.time, None)

    def test_noseconds(self):
        "EuroParser.time() accepts missing seconds"

        self.assertEquals(
            chrono.parser.EuroParser.time("16:27"),
            (16, 27, 0)
        )

    def test_nozero(self):
        "EuroParser.time() accepts missing zeroes"

        self.assertEquals(
            chrono.parser.EuroParser.time("8:2:4"),
            (8, 2, 4)
        )


if __name__ == "__main__":
    unittest.main()
