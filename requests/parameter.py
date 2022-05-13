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
import urllib.parse

# 2) Port.
#    N/a

# 3) Constants
#    N/a

# 4) Functions
class Parameter:
    """

    Class provides an object for managing data that goes into a parameter on
    an HTTP request. Usually, you would use this object one-to-one with a
    parameter, but sometimes that's not the case, such as when you want to
    manage two related parameters together. 
    """
    def __init__(self, name, value=None, default=None):
        self._name = name
        self._value = value
        self._default = default

    def get_default(self):
        """

        get_default() -> obj

        Method returns the instance's default value. 
        """
        return self._default

    def get_dict(self, tuples=[], encode=True, include_blanks=False):
        """

        get_dict() -> dict

        Method returns a dictionary of the name and value of any parameters the
        instance covers. If include_blanks is off, the method will omit any
        params that do not have a True value.
        """
        result = dict()
        if not tuples:
            tuples = self._get_list_of_tuples(encode=encode)
            
        for k, v in tuples:
            if include_blanks:
                result[k] = v
            else:
                if v:
                    result[k] = v
                
        return result
    
    def get_name(self):
        """

        get_name() -> str

        Method returns the name of the parameter. 
        """
        return self._name

    def get_value(self):
        """

        get_value() -> obj

        Method returns the value for the instance.
        """
        return self._value

    def reset(self):
        """

        reset() -> None

        Method sets the value to the default. 
        """
        default = self.get_default()
        self.set_value(default)
        
    def set_default(self, default):
        """

        set_default() -> None

        Method sets the default for the instance.
        """
        self._default = default

    def set_name(self, name):
        """

        set_name() -> None

        Method sets the name of the parameter that this instance represents.
        """
        self._name = name

    def set_value(self, value):
        """

        set_value() -> None

        Method sets the value for the parameter that the instance represents.
        """
        self._value = value

    # Non-Public

    def _get_list_of_tuples(self, encode=True):
        """

        _get_list_of_tuples() -> list

        Method delivers the parameter or parameters that the instance represents
        as a list of tuples of (parameter name, parameter value). If you turn
        off encoding, names and values may include unescaped entities.
        """
        name = self.get_name()
        value = self.get_value()
        if encode:
            name = urllib.parse.urlencode(name)
            value = urllib.parse.urlencode(value)

        result = [(name, value)]
        return result
        
