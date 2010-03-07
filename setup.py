#!/usr/bin/python
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

from distutils.core import setup
from distutils.cmd import Command

import os
import os.path
import subprocess
import sys

sys.path.insert(0, os.path.abspath("."))

import chrono

cmdclass = {}

if "sdist" in sys.argv and not "build_sphinx" in sys.argv:
    sys.argv.insert(1, "build_sphinx")

if "build_sphinx" in sys.argv:
    from sphinx.setup_command import BuildDoc
    cmdclass["build_sphinx"] = BuildDoc


class Test(Command):
    "Command for running unit-tests"

    description = "Run unit-tests"
    user_options = [
        ("python=", "p", "Python command to use (defaults to 'python')"),
    ]
    boolean_options = ()

    def finalize_options(self):
        pass

    def initialize_options(self):
        self.python = "python"

    def run(self):
        sys.exit(subprocess.call([self.python, os.path.dirname(os.path.abspath(__file__)) + "/tests/test.py"], stdout=sys.stdout))


cmdclass["test"] = Test

setup(
    name="python-chrono",
    version=chrono.__version__,
    description="A Python module for simple and convenient date/time handling",
    long_description=open("README").read(),
    license="GNU General Public License 3",
    author="Erik Grinaker",
    author_email="erikg@codepoet.no",
    url="http://oss.codepoet.no/python-chrono/",
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ),
    packages=(
        "chrono",
        "chrono.calendar",
        "chrono.clock",
        "chrono.parser",
    ),
    cmdclass=cmdclass
)
