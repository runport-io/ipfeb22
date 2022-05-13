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
class Date(parameter.Parameter):
    """

    Class supports parameters for dates. Class does NOT support parameters for
    time.     
    """
    def __init__(self, name, value=None, default=None):
        parameter.Parameter.__init__(self, name=name, value=value,
                                     default=default)
        
    def get_iso(self):
        """

        get_iso() -> string or None

        Method returns a string in ISO 8601 format if the instance has a value,
        or None otherwise.
        """
        result = None
        value = self.get_value()
        if value:
            result = value.isoformat()

        return result

    # Non-Public
        
    def _get_list_of_tuples(self, encode=True):
        """

        _get_list_of_tuples() -> list

        Method returns a tuple of (name, iso) for the instance. If you disable
        encoding, the results will come back raw, otherwise, method will pass 
        them to urllib.parse.urlencode first.
        """

        name = self.get_name()
        value = self.get_iso()
        
        if encode:
            value = urllib.parse.urlencode(value)

        result = [(name, value)]
        return result
    
