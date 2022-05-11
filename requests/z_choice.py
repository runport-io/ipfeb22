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
class Choice:
    """

    Class supports choosing items from a menu of options. You can specify one or
    more results.
    """
    
    SEP = ","
    
    def __init__(self, default=None, options=list()):
        self._value = list()
        if default:
            self._value.append(default)
            
        self._default = default
        self._options = options
        self._cache = list()
        self._limit = 1

    def get_default(self):
        """

        get_default() -> obj

        Method returns the value for the default selection.         
        """
        return self._default
    
    def get_dict(self, encode=True):
        """

        get_dict() -> dict

        Method returns the name:value pair for the parameter. If you specify
        that encode is True, the method will encode URL entities in the value.
        """        
        name, value = self.get_tuple(encode=encode)
        return {name:value}

        # this should be pulled out to a core req object
        

    def get_limit(self):
        """

        get_limit() -> int

        Method returns the maximum permitted number of selections. By default,
        this is 1. 
        """
        return self._max

    def get_name(self):
        """

        get_name() -> str

        Method returns the name of the parameter.
        """
        return self._name

    def get_options(self):
        """

        get_options() -> list

        Method returns the list of choices you can make for the instance. 
        """
        return self._options

    def get_list_of_tuples(self, encode=True):
        """

        get_list_of_tuples() -> tuple

        Method returns the tuple of the name and value of the parameter. If you
        turn on encoding, method will pass both to urllib.parse.urlencode first. 
        """
        name = self.get_name()
        items = self.get_value()
        value = self.SEP.join(items)
        
        if encode:
            value = urllib.parse.urlencode(value, safe=self.SEP)
            name = urllib.parse.urlencode(name)

        result = (name, value)
        return result

    def get_value(self):
        """

        get_value() -> list

        Method returns the value for the instance.
        """
        if not self._value:
            self._value.append(self._default)
            
        return self._value

    def reset(self):
        """

        reset() -> None

        Method removes items from the instance.        
        """
        self._value.clear()

    def select(self, *choices, force=False):
        """

        select() -> None

        Method resets the value of the instance and then adds choices to the
        value, up to the limit specified for the instance. If force is True, you
        can add choices that do not match the options, otherwise method will
        throw an exception. 
        """
        self.reset()
        limit = self.get_limit()
        
        for c in choices[:limit]:
            if force or (c in self._options):
                self._value.append(c)
            else:
                raise Exception

    def set_default(self, value, check=False):
        """

        set_default() -> None

        Method sets the default selection for the instance. If you set check to
        True, method will append the value to options if it is not there.
        """
        if check:
            if not value in self._options:
                self._options.append(value)
                
        self._default = value

    def set_limit(self, num):
        """

        set_limit() -> None

        Method sets the maximum number of entries for the instance. 
        """
        self._limit = num

    def set_name(self, name):
        """

        set_name() -> None

        Method sets the name for the parameter.
        """
        self._name = name
        
    def set_options(self, options):
        """

        set_options() -> None

        Method sets the menu for the instance. 
        """
        self._options = options
