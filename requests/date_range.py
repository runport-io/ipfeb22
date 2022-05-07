# Copyright Port. Prerogative Club ("the Club")
#
# 
# This file is part of Port. 2.0. ("Port.")
#
# Port. is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Port. is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Port. If not, see <https://www.gnu.org/licenses/>.
#
# Questions? Contact hi@runport.io.

# Imports
# 1) Built-ins
#    N/a

# 2) Port.
#    N/a

# 3) Constants
#    N/a

# 4) Functions
class DateRange:

    KEY_TO = "dateTO"
    KEY_FROM = "dateFROM"
    
    def __init__(self):
        self._from = None
        self._to = None

    def get_from(self):
        return self._from

    def get_to(self):
        return self._to

    def set_to(self, date):
        self._to = datetime.date(date)
        # can have error checking here

    def set_from(self, date):
        self._from = datetime.date(date)
        # can check if it is in range
        # will automatically throw an exception if can't convert into right
        # format

    def get_dates(self):
        result = dict()
        result[self.KEY_TO] = self.get_to().isoformat()
        result[self.KEY_FROM] = self.get_from().isoformat()
