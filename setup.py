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

from distutils.core import setup

setup(
    name="python-chrono",
    version="0.0.0",
    description="a date/time module for python",
    url="http://oss.codepoet.no/python-chrono",
    author="Erik Grinaker",
    author_email="erikg@codepoet.no",
    license="GPL 3",
    keywords="calendar date datetime time",
    packages=(
        "chrono",
        "chrono.calendar",
        "chrono.clock",
        "chrono.parser",
    ),
)
