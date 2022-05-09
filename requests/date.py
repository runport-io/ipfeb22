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
class Date:
    def __init__(self, name, value=None):
        self._name = name
        self._value = value

    def get_name(self):
        return self._name

    def get_value(self):
        return self._value

    def set_name(self, name):
        self._name = name

    def set_value(self, value):
        # if value is not a date, raise error
        # so convert into iso format
                
    def get_tuple(self):
        name = self.get_name()
        value = self.get_value() #< --------------- iso? 
        result = (name, value)
        return result
        # 
        
    def get_dates(self):
        result = dict()
        result[self.KEY_TO] = self.get_to().isoformat()
        result[self.KEY_FROM] = self.get_from().isoformat()

# add default
# if default is None, return nothing
