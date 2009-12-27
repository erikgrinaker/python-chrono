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

import datetime


class Date(object):
	"Date class"

	day	= None
	month	= None
	year	= None

	def __init__(self, date = None):
		"Creates a Date object"

		if date is True:
			self.set_now()


	def set_now(self):
		"Sets the date to the current date"

		d = datetime.date.today()

		self.year = d.year
		self.month = d.month
		self.day = d.day

