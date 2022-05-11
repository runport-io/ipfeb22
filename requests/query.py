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
class Query(parameter.Parameter):

    SEP = " OR "
    
    def __init__(self, name):

        parameter.Parameter.__init__(self, name)
        
        self._elements = list()
        self._sep = ""

    def get_elements(self):
        """

        get_elements() -> list

        Method returns the elements on the instance. 
        """
        result = self._elements
        return result

    def get_separator(self):
        return self._sep or self.SEP

    def get_value(self):
        """

        get_value() -> string

        Method joins each of the elements with the separator and returns the
        string. 
        """
        elements = self.get_elements()
        sep = self.get_separator()
        result = sep.join(self._elements)
        return result

    def set_elements(self, elements):
        self._elements = elements

    def set_separator(self, separator):
        self._sep = separator
