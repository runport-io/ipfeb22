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
class Value:
    """

    Class defines objects that provides a get/set interface for their value.
    The idea is to use instances to provide consistency in how to access
    parts of an HTTP request.
    """
    def __init__(self, value=None):
        self._value = value

    def get(self):
        """

        get() -> obj

        Method returns the value for the instance.
        """
        return self._value

    def set(self, value):
        """

        set() -> None

        Method sets the value for the instance.
        """
        self._value = value

    def reset(self):
        """

        reset() -> None

        Method sets the value to None. 
        """
        self.set(None)
