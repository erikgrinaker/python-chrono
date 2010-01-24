# -*- coding: utf-8 -*-
#
# python-chrono - a Python module for easy and convenient date/time handling
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

from .. import error


class Parser(object):
    """
    Base parser class, with utility methods for subclasses.
    """

    @classmethod
    def regexp(cls, regexp, subject):
        """
        Parses *subject* based on the regular expression object *regexp*,
        returns a dict of named captured groups.

        Raises :exc:`chrono.error.ParseError` if the subject doesn't match the
        expression, or :exc:`TypeError` on invalid (ie non-string) subject
        type.
        """

        try:
            match = regexp.match(subject)

        except TypeError:
            raise TypeError("Input is not a string")

        if not match:
            raise error.ParseError(
                "The value '{0}' doesn't match the expected pattern"
                .format(subject)
            )

        if match.groupdict():
            return match.groupdict()

        else:
            return match.groups()
