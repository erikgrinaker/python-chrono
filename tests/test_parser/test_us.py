#!/usr/bin/env python

import chrono
import unittest


class USParserTest(unittest.TestCase):

    def test_subclass(self):
        "USParser subclasses Parser"

        self.assertTrue(issubclass(
            chrono.parser.USParser, chrono.parser.parser.Parser
        ))


class USParser_dashdateTest(unittest.TestCase):

    def test_invalid_date(self):
        "USParser.dashdate() raises error on invalid date"

        self.assertRaises(
            chrono.DayError, chrono.parser.USParser.dashdate, "02-29-2009"
        )

    def test_invalid_format(self):
        "USParser.dashdate() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.USParser.dashdate, "yy-xx-zzzz"
        )

    def test_none(self):
        "USParser.dashdate() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.USParser.dashdate, None)

    def test_nozero(self):
        "USParser.dashdate() parses dates without leading zeroes (7-3-2009)"

        self.assertEquals(
            chrono.parser.USParser.dashdate("7-3-2009"),
            (2009, 7, 3)
        )

    def test_parse(self):
        "USParser.dashdate() parses proper dates (mm-dd-yyyy)"

        self.assertEquals(
            chrono.parser.USParser.dashdate("12-27-2009"),
            (2009, 12, 27)
        )

    def test_shortyear(self):
        "USParser.dashdate() handles two-digit years"

        self.assertEquals(
            chrono.parser.USParser.dashdate("12-27-09"),
            (2009, 12, 27)
        )


class USParser_dateTest(unittest.TestCase):

    def test_invalid_date(self):
        "USParser.date() raises error on invalid date"

        self.assertRaises(
            chrono.DayError, chrono.parser.USParser.date, "02/29/2009"
        )

    def test_invalid_format(self):
        "USParser.date() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.USParser.date, "yy/xx/zzzz"
        )

    def test_none(self):
        "USParser.date() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.USParser.date, None)

    def test_nozero(self):
        "USParser.date() parses dates without leading zeroes (7/3/2009)"

        self.assertEquals(
            chrono.parser.USParser.date("7/3/2009"),
            (2009, 7, 3)
        )

    def test_parse(self):
        "USParser.date() parses proper dates (mm/dd/yyyy)"

        self.assertEquals(
            chrono.parser.USParser.date("12/27/2009"),
            (2009, 12, 27)
        )

    def test_shortyear(self):
        "USParser.date() handles two-digit years"

        self.assertEquals(
            chrono.parser.USParser.date("12/27/09"),
            (2009, 12, 27)
        )


class USParser_dotdateTest(unittest.TestCase):

    def test_invalid_date(self):
        "USParser.dotdate() raises error on invalid date"

        self.assertRaises(
            chrono.DayError, chrono.parser.USParser.dotdate, "02.29.2009"
        )

    def test_invalid_format(self):
        "USParser.dotdate() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.USParser.dotdate, "yy.xx.zzzz"
        )

    def test_none(self):
        "USParser.dotdate() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.USParser.dotdate, None)

    def test_nozero(self):
        "USParser.dotdate() parses dates without leading zeroes (7.3.2009)"

        self.assertEquals(
            chrono.parser.USParser.dotdate("7.3.2009"),
            (2009, 7, 3)
        )

    def test_parse(self):
        "USParser.dotdate() parses proper dates (mm.dd.yyyy)"

        self.assertEquals(
            chrono.parser.USParser.dotdate("12.27.2009"),
            (2009, 12, 27)
        )

    def test_shortyear(self):
        "USParser.dotdate() handles two.digit years"

        self.assertEquals(
            chrono.parser.USParser.dotdate("12.27.09"),
            (2009, 12, 27)
        )


class USParser_namedateTest(unittest.TestCase):

    def test_invalid_date(self):
        "USParser.namedate() raises error on invalid date"

        self.assertRaises(
            chrono.DayError, chrono.parser.USParser.namedate, "29-FEB-2009"
        )

    def test_invalid_format(self):
        "USParser.namedate() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.USParser.namedate, "xx-yyy-zzzz"
        )

    def test_invalid_month(self):
        "USParser.namedate() raises error on invalid month"

        self.assertRaises(
            chrono.MonthError, chrono.parser.USParser.namedate, "29-XYZ-2009"
        )

    def test_months(self):
        "USParser.namedate() handles all months"

        months = (
            "JAN", "FEB", "MAR", "APR",
            "MAY", "JUN", "JUL", "AUG",
            "SEP", "OCT", "NOV", "DEC"
        )

        for i, month in enumerate(months):
            self.assertEquals(
                chrono.parser.USParser.namedate("3-{0}-2009".format(month)),
                (2009, i + 1, 3)
            )

    def test_none(self):
        "USParser.namedate() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.USParser.namedate, None)

    def test_nozero(self):
        "USParser.namedate() parses dates without leading zeroes (3-JUL-2009)"

        self.assertEquals(
            chrono.parser.USParser.namedate("3-JUL-2009"),
            (2009, 7, 3)
        )

    def test_parse(self):
        "USParser.namedate() parses proper dates (dd-mmm-yyyy)"

        self.assertEquals(
            chrono.parser.USParser.namedate("27-DEC-2009"),
            (2009, 12, 27)
        )

    def test_shortyear(self):
        "USParser.namedate() handles two-digit years"

        self.assertEquals(
            chrono.parser.USParser.namedate("27-DEC-09"),
            (2009, 12, 27)
        )


class USParser_parse_dateTest(unittest.TestCase):

    def test_dashdate(self):
        "USParser.parse_date() handles dash dates (mm-dd-yyyy)"

        self.assertEquals(
            chrono.parser.USParser.parse_date("08-27-2010"),
            (2010, 8, 27)
        )

    def test_date(self):
        "USParser.parse_date() handles normal dates (mm/dd/yyyy)"

        self.assertEquals(
            chrono.parser.USParser.parse_date("08/27/2010"),
            (2010, 8, 27)
        )

    def test_dotdate(self):
        "USParser.parse_date() handles dot dates (mm.dd.yyyy)"

        self.assertEquals(
            chrono.parser.USParser.parse_date("08.27.2010"),
            (2010, 8, 27)
        )

    def test_invalid(self):
        "USParser.parse_date() raises error on invalid date"

        self.assertRaises(
            chrono.MonthError,
            chrono.parser.USParser.parse_date, "13/27/2010"
        )

    def test_namedate(self):
        "USParser.parse_date() handles named dates (dd-mmm-yyyy)"

        self.assertEquals(
            chrono.parser.USParser.parse_date("27-AUG-2010"),
            (2010, 8, 27)
        )


class USParser_parse_dateTest(unittest.TestCase):

    def test_datetime(self):
        "USParser.parse_datetime() handles normal dates (mm/dd/yyyy)"

        self.assertEquals(
            chrono.parser.USParser.parse_datetime("08/27/2010 4:27:43 PM"),
            (2010, 8, 27, 16, 27, 43)
        )

    def test_invalid(self):
        "USParser.parse_datetime() raises error for invalid datetime"

        self.assertRaises(
            chrono.MonthError,
            chrono.parser.USParser.parse_datetime, "13/27/2010 4:27:43 PM"
        )


class USParser_parse_timeTest(unittest.TestCase):

    def test_time(self):
        "USParser.parse_time() handles normal times (hh:mm:ss ampm"

        self.assertEquals(
            chrono.parser.USParser.parse_time("04:27:43 PM"),
            (16, 27, 43)
        )

    def test_invalid(self):
        "USParser.parse_date() raises error on invalid time"

        self.assertRaises(
            chrono.HourError,
            chrono.parser.USParser.parse_time, "00:27:43 AM"
        )


class USParser_timeTest(unittest.TestCase):

    def test_invalid_ampm(self):
        "USParser.time() raises ParseError on invalid AM/PM"

        self.assertRaises(
             chrono.ParseError, chrono.parser.USParser.time, "4:27:43 PAM"
        )

    def test_invalid_format(self):
        "USParser.time() raises ParseError on invalid format"

        self.assertRaises(
            chrono.ParseError, chrono.parser.USParser.time, "xx:yy:zz PM"
        )

    def test_invalid_time(self):
        "USParser.time() raises error on invalid time"

        self.assertRaises(
                chrono.HourError, chrono.parser.USParser.time, "00:27:43 AM"
        )

    def test_full(self):
        "USParser.time() accepts full time"

        self.assertEquals(
            chrono.parser.USParser.time("4:27:43 PM"),
            (16, 27, 43)
        )

    def test_nominutes(self):
        "USParser.time() accepts missing minutes"

        self.assertEquals(
            chrono.parser.USParser.time("4 PM"),
            (16, 0, 0)
        )

    def test_none(self):
        "USParser.time() raises TypeError on None"

        self.assertRaises(TypeError, chrono.parser.USParser.time, None)

    def test_noseconds(self):
        "USParser.time() accepts missing seconds"

        self.assertEquals(
            chrono.parser.USParser.time("4:27 PM"),
            (16, 27, 0)
        )

    def test_nozero(self):
        "USParser.time() accepts missing zeroes"

        self.assertEquals(
            chrono.parser.USParser.time("8:2:4 AM"),
            (8, 2, 4)
        )


if __name__ == "__main__":
    unittest.main()
