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

class Query:

    SEP = " OR "
    
    def __init__(self):
        self._elements = list()
        self._sep = ""

    def get_elements(self):
        """

        get_elements() -> list

        Method returns the elements on the instance. 
        """
        result = self._elements
        return result

    def get_value_as_string(self):
        """

        get_value_as_string() -> string

        Method joins each of the elements with the separator and returns the
        string. 
        """
        result = self.SEP.join(self._elements)
        return result
