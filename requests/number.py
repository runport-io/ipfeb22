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
from . import parameter

# 3) Constants
#    N/a

# 4) Functions
class Number(parameter.Parameter):
    """

    A parameter that handles numerical values. The class includes functions
    for increasing and decreasing the value.
    """
    def __init__(self, name, value=None, default=None):
        parameter.Parameter.__init__(self, name, value, default)

        self._ceiling = None
        self._floor = None

    def decrement(self, amount=1):
        """

        decrement() -> None

        Method decreases the value by the amount, but not below the floor. If the
        value plus the amount would be less than the floor, method sets the value
        at the floor.
        """
        old = self.get_value()
        floor = self.get_floor()
        new = old - amount

        if floor is not None:
            new = max(new, floor)

        self.set_value(new)
        
    def get_ceiling(self):
        """

        get_ceiling() -> number

        Method returns the maximum value for the instance. If you do not define
        it explicitly, it is None.
        """
        return self._ceiling
    
    def get_floor(self):
        """

        get_floor() -> number

        Method returns the minimum value for the instance. If you do not define
        it explicitly, it is None.
        """
        return self._floor

    def increment(self, amount=1):
        """

        increment() -> None

        Method increases the value by the amount, up to the ceiling. If the
        value plus the amount would exceed the ceiling, method sets the value at
        the ceiling.
        """
        old = self.get_value()
        ceiling = self.get_ceiling
        new = old + amount
        
        if ceiling is not None:
            new = min(new, ceiling)

        self.set_value(new)
        
    def set_ceiling(self, ceiling):
        """

        set_ceiling() -> None

        Method sets the maximum value for the instance.
        """
        self._ceiling = ceiling

    def set_floor(self, floor):
        """

        set_floor() -> None

        Method sets the minimum value for the instance.
        """
        self._floor = floor

    def set_value(self, value):
        """

        set_value() -> None

        Method sets the instance value. If you have defined the floor or the
        ceiling, method will throw an Exception if the value does not fit in the
        range of [floor, ceiling].
        """
        floor = self.get_floor()
        ceiling = self.get_ceiling()
        if floor is not None:
            if value < floor:
                raise Exception
            
        if ceiling is not None:
            if value > ceiling:
                raise Exception

        parameter.Parameter.set_value(self, value)
