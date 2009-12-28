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

class Parser(object):
	"""
	Base parser class, with various utility methods for subclasses
	"""

	@classmethod
	def int(cls, value):
		"""
		Converts *value* to an integer. If *value* is a sequence or
		dictionary, members will be converted to integers. Raises
		:exc:`TypeError` if *value* (or members) isn't a string or
		integer, or :exc:`ValueError` if *value* couldn't be converted.
		"""

		if type(value) == list:
			value = [ int(v) for v in value ]

		elif type(value) == tuple:
			value = tuple([ int(v) for v in value ])

		elif type(value) == dict:
			for k, v in value.items():
				value[k] = int(v)

		else:
			value = int(value)

		return value

	@classmethod
	def regexp(cls, regexp, subject):
		"""
		Parses the string *subject* based on the regular expression object *regexp*,
		and returns a dict of named captured groups. Raises :exc:`ValueError`
		if the subject doesn't match the expression, or :exc:`TypeError` on
		invalid subject type (ie non-string).
		"""

		try:
			match = regexp.match(subject)

		except TypeError:
			raise TypeError("Subject is not a string")

		if not match:
			raise ValueError(
				"The subject '{0}' doesn't match the regular expression"
				.format(subject)
			)

		if match.groupdict():
			return match.groupdict()

		else:
			return match.groups()

