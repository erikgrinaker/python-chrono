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

"""
This module contains various classes that are used to parse different date/time formats.

:class:`chrono.parser.Parser` is a base class with various utility methods for subclasses.
Actual parsing will always be handled by subclasses, either through a :meth:`parse`
method, or more specialized methods.
"""

from .iso import ISOParser
from .parser import Parser