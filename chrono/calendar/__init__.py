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

"""
This module contains various classes that provide calendar-related
functionality, such as week numbers, leap years, validation, etc.

:class:`chrono.calendar.Calendar` is a base class which implements methods
common to all gregorian-based calendars, while calendar-specific methods will
raise :exc:`NotImplementedError`, and be implemented in subclasses.
"""

from __future__ import absolute_import

from .calendar import Calendar
from .iso import ISOCalendar
