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
import re
import unittest


class Parser_regexpTest(unittest.TestCase):

    re_isodate = re.compile('''
        ^\s*                # ignore whitespace at start
        (?P<year>\d{1,4})   # year
        -(?P<month>\d{1,2}) # month
        -(?P<day>\d{1,2})   # day
        \s*$                # ignore whitespace at end
    ''', re.VERBOSE)

    re_keyval = re.compile('^\s*(.*?)\s*:\s*(.*?)\s*$')

    def test_integer(self):
        "Parser.regexp() raises TypeError for integer subject"

        self.assertRaises(
            TypeError, chrono.parser.Parser.regexp, self.re_isodate, 1
        )

    def test_nomatch(self):
        "Parser.regexp() raises ParseError if input doesn't match expression"

        self.assertRaises(
            chrono.ParseError,
            chrono.parser.Parser.regexp, self.re_isodate, "2009-12-"
        )

    def test_nonamed(self):
        "Parser.regexp() returns a tuple of values if named groups aren't used"

        self.assertEquals(
            chrono.parser.Parser.regexp(self.re_keyval, " key: value "),
            ("key", "value")
        )

    def test_none(self):
        "Parser.regexp() raises TypeError for None subject"

        self.assertRaises(
            TypeError, chrono.parser.Parser.regexp, self.re_isodate, None
        )

    def test_parse(self):
        "Parser.regexp() parses string using regexp, returns named groups"


        self.assertEquals(
            chrono.parser.Parser.regexp(self.re_isodate, "2009-12-27"),
            {"year": "2009", "month": "12", "day": "27"}
        )


if __name__ == "__main__":
    unittest.main()
