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

import unittest


main = unittest.main


class TestCase(unittest.TestCase):
	"A TestCase"

	def assertNone(self, object):
		"Asserts that an object is None"

		self.assertSame(object, None)

	def assertSame(self, a, b):
		"Asserts that two object references point to the same object"

		self.assertTrue(a is b)

	def assertSubclass(self, sub, super):
		"Asserts that a class is a subclass of another"

		self.assertTrue(issubclass(sub, super))

	def assertType(self, instance, cl):
		"Asserts that an instance is instance of a class"

		self.assertTrue(isinstance(instance, cl))

