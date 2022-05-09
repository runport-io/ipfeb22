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
class Number:
    """

    
    """
    def __init__(self, name, value=1):
        self._name = name
        self._value = value
        self._min = None
        self._max = None

    def get_min(self):
        return self._min
    
    def set_min(self, num):
        self._min = num

    def get_max(self):
        return self._max
    
    def set_max(self, num):
        self._max = num
    
    def get_value(self):
        return self._value

    def set_value(self, num):
        self._value = num

    def increase(self, amount=1):
        old = self.get_value()
        new = old + amount
        ceiling = self.get_ceiling():

        if ceiling is not None:
            new = min(new, ceiling)
        
        self.set_value(new)
        return new

    def decrease(self, amount):
        old = self.get_value()
        new = old - amount
        floor = self.get_floor()
        if floor is not None:
            new = max(floor, new)
        
        self.set_value(new)
        return new

    def get_dict(self):
        name = self.get_name()
        value = self.get_value()
        result = {name:value}
        return result
        # move this to Handler? 
    
