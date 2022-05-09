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
    
    def __init__(self, default=None, options=list()):
        self._value = default
        # self._value = list()
        # if default:
        #   self._value.append(default)
        
        self._default = default
        self._options = options
        self._cache = list()
        self._max = 1

    def get_max(self):
        return self._max

    def set_max(self, num):
        self._max = num

    def get_value(self):
        return self._value or self._default

    def select(self, *choices):
        self.reset()
        limit = self.get_max()
        
        for c in choices[:limit]:
            if c in self._options:
                self._value.append(c)
            else:
                raise Exception

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_default(self):
        return self._default

    def set_default(self, value):
        self._default = value
        # <------------------------------------------------ do i care if this is in options?

    def get_options(self):
        return self._options

    def set_options(self, options):
        self._options = options
    
    def reset(self):
        self._value.clear()
    
    def toggle(self):
        """

        Method sets value to the first item in options, puts existing 
        """

        old = self.get_value()
        
        if not self._cache:
            i = self._options.find(old)
            if i != -1:
                cache = self._options.copy()
                cache.pop(i)
            else:
                # If I forced a value that isn't on the menu, then I could have
                # a -1 result
                cache = self._options.copy()
                
            self._cache = cache
            
        new = self._cache.pop(0)
        self._cache.append(old)
        
        self.set_value(new)
        return new

    def get_params(self):
        name = self.get_name()
        choices = self.get_choices()
        value = self.SEP.join(choices)
        
        result = {name:value}
        return result

        #< ---------------------------------------------------------------- encode?
