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

from __future__ import absolute_import

from . import parser
from .. import calendar

import re


class ISOParser(parser.Parser):
	"""
	A parser for ISO 8601 date formats

	All methods raise :exc:`TypeError` on invalid input types,
	and :exc:`ValueError` on invalid input formats (ie, parse failure).
	"""

	re_compactdate = re.compile('''
		^\s*			# ignore whitespace at start
		(?P<year>\d{4})		# year
		(?P<month>\d{2})	# month
		(?P<day>\d{2})		# day
		\s*$			# ignore whitespace at end
	''', re.VERBOSE)

	re_compactweek = re.compile('''
		^\s*			# ignore whitespace at start
		(?P<year>\d{1,4})	# year
		W(?P<week>\d{1,2})	# week
		\s*$			# ignore whitespace at end
	''', re.VERBOSE | re.IGNORECASE)

	re_compactweekdate = re.compile('''
		^\s*			# ignore whitespace at start
		(?P<year>\d{4})		# year
		W(?P<week>\d{2})	# week
		(?P<day>\d)		# day
		\s*$			# ignore whitespace at end
	''', re.VERBOSE | re.IGNORECASE)

	re_date = re.compile('''
		^\s*			# ignore whitespace at start
		(?P<year>\d{1,4})	# year
		-(?P<month>\d{1,2})	# month
		-(?P<day>\d{1,2})	# day
		\s*$			# ignore whitespace at end
	''', re.VERBOSE)

	re_month = re.compile('''
		^\s*			# ignore whitespace at start
		(?P<year>\d{1,4})	# year
		-(?P<month>\d{1,2})	# month
		\s*$			# ignore whitespace at end
	''', re.VERBOSE)

	re_ordinal = re.compile('''
		^\s*			# ignore whitespace at start
		(?P<year>\d{4})		# year
		-(?P<day>\d{3})		# day
		\s*$			# ignore whitespace at end
	''', re.VERBOSE)

	re_week = re.compile('''
		^\s*			# ignore whitespace at start
		(?P<year>\d{1,4})	# year
		-W(?P<week>\d{1,2})	# week
		\s*$			# ignore whitespace at end
	''', re.VERBOSE | re.IGNORECASE)

	re_weekdate = re.compile('''
		^\s*			# ignore whitespace at start
		(?P<year>\d{1,4})	# year
		-W(?P<week>\d{1,2})	# week
		-(?P<day>\d)		# day
		\s*$			# ignore whitespace at end
	''', re.VERBOSE | re.IGNORECASE)

	re_year = re.compile('''
		^\s*			# ignore whitespace at start
		(?P<year>\d{1,4})	# year
		\s*$			# ignore whitespace at end
	''', re.VERBOSE)

	@classmethod
	def compactdate(cls, date):
		"""
		Parses a compact ISO date(*yyyymmdd*), and returns a tuple with
		year, month, and day.
		"""

		match = cls.int(cls.regexp(cls.re_compactdate, date))

		calendar.ISOCalendar.validate(
			match["year"],
			match["month"],
			match["day"]
		)

		return (match["year"], match["month"], match["day"])

	@classmethod
	def compactweek(cls, date):
		"""
		"Parses a compact ISO week (*yyyyWww*), and returns a tuple with year
		and week number. Leading zeroes may be omitted, even though the ISO
		standard requires them.
		"""

		match = cls.int(cls.regexp(cls.re_compactweek, date))

		calendar.ISOCalendar.validate_week(
			match["year"],
			match["week"]
		)

		return (match["year"], match["week"])

	@classmethod
	def compactweekdate(cls, date):
		"""
		"Parses a compact ISO weekdate (*yyyyWwwd*), and returns a tuple with year,
		week, and weekday.
		"""

		match = cls.int(cls.regexp(cls.re_compactweekdate, date))

		calendar.ISOCalendar.validate_weekdate(
			match["year"],
			match["week"],
			match["day"]
		)

		return (match["year"], match["week"], match["day"])

	@classmethod
	def date(cls, date):
		"""
		Parses a ISO date (*yyyy-mm-dd*), and returns a tuple with year,
		month, and day. Leading zeroes may be omitted, even though the ISO
		standard requires them.
		"""

		match = cls.int(cls.regexp(cls.re_date, date))

		calendar.ISOCalendar.validate(
			match["year"],
			match["month"],
			match["day"]
		)

		return (match["year"], match["month"], match["day"])

	@classmethod
	def month(cls, date):
		"""
		Parses an ISO month (*yyyy-mm*), and returns a tuple with year and
		month. Leading zeroes may be omitted, even though the ISO standard
		requires them.
		"""

		match = cls.int(cls.regexp(cls.re_month, date))

		calendar.ISOCalendar.validate_year(match["year"])
		calendar.ISOCalendar.validate_month(match["month"])

		return (match["year"], match["month"])

	@classmethod
	def ordinal(cls, date):
		"""
		Parses an ISO ordinal date (*yyyy-ddd*), and returns a tuple with
		year and ordinal day.
		"""

		match = cls.int(cls.regexp(cls.re_ordinal, date))

		calendar.ISOCalendar.validate_ordinal(
			match["year"],
			match["day"]
		)

		return (match["year"], match["day"])

	@classmethod
	def week(cls, date):
		"""
		"Parses an ISO week (*yyyy-Www*), and returns a tuple with year
		and week number. Leading zeroes may be omitted, even though the ISO
		standard requires them.
		"""

		match = cls.int(cls.regexp(cls.re_week, date))

		calendar.ISOCalendar.validate_week(
			match["year"],
			match["week"]
		)

		return (match["year"], match["week"])

	@classmethod
	def weekdate(cls, date):
		"""
		Parses an ISO weekdate (*yyyy-Www-d*), and returns a tuple with
		year, week, and weekday. Leading zeroes may be omitted, even though
		the ISO standard requires them.
		"""

		match = cls.int(cls.regexp(cls.re_weekdate, date))

		calendar.ISOCalendar.validate_weekdate(
			match["year"],
			match["week"],
			match["day"]
		)

		return (match["year"], match["week"], match["day"])

	@classmethod
	def year(cls, date):
		"""
		Parses an ISO year (*yyyy*), and returns it. Leading zeroes may be
		omitted, even though the ISO standard requires them.
		"""

		match = cls.int(cls.regexp(cls.re_year, date))

		calendar.ISOCalendar.validate_year(match["year"])

		return match["year"]

