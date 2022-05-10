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
    """

    Class supports parameters for dates. Class does NOT support parameters for
    time.     
    """
    def __init__(self, name, value=None):
        self._name = name
        self._value = value
        self._default = None

    def get_dict(self, encode=True):
        """

        get_dict() -> dict

        Method returns a name:value dictionary of the parameter if the value is
        defined. You get an empty dictionary if the value is False.
        """
        name, value = self.get_tuple(encode=encode)
        result = {name: value}
        if not value:
            result = dict()
            
        return result
    
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
        
    def get_name(self):
        """

        get_name() -> str

        Method returns the name of the parameter.
        """
        return self._name

    def get_tuple(self, encode=True):
        """

        get_tuple() -> tuple

        Method returns a tuple of (name, value) for the instance. If you disable
        encoding, the results will come back raw, otherwise, method will pass 
        them to urllib.parse.urlencode first.
        """

        name = self.get_name()
        value = self.get_iso()
        
        if encode:
            name = urllib.parse.urlencode(name)
            value = urllib.parse.urlencode(value)

        result = (name, value)
        return result
    
    def get_value(self):
        """
        
        get_value() -> datetime.time

        Method returns the value of the instance. 
        """
        return self._value

    def reset(self):
        """

        reset() -> None

        Method sets the value of the instance to the default. 
        """
        self._value = self._default
    
    def set_name(self, name):
        """

        set_name() -> None

        Method sets the name for the instance. 
        """
        self._name = name

    def set_value(self, value, check=True):
        """

        set_value() -> None

        Method sets the value for the instance. If the value does not support an
        isoformat() method, the call with throw an exception unless you turn off
        "check".
        """
        if check: 
            value.isoformat()
            
        self._value = value
