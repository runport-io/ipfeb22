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
class Choice(parameter.Parameter):
    """

    A parameter that supports selection from a list. You can specify whether you
    want to permit one or more selections. 
    """
    SEP = ","
    
    def __init__(self):
        parameter.Parameter.__init__(self)

        self._limit = 1
        self._sep = None
        self._menu = list()
        self._choices = list()

    def get_limit(self):
        """

        get_limit() -> int

        Method returns the limit on the number of choices the instance supports.
        You can override the default of 1 to enable multiple selections.
        """
        return self._limit

    def get_menu(self):
        """

        get_menu() -> list

        Method returns the menu of options that the instance supports.
        """
        return self._menu

    def get_selection(self):
        """

        get_selection() -> list

        Method returns the items the instance selected.
        """
        return self._selection
        
    def get_sep(self):
        """

        get_sep() -> string

        Method returns the separator used to join the values.
        """
        return self._sep or self.SEP

    def get_value(self):
        """

        get_value() -> string

        Method returns a string by delegating to get_value_as_string().
        """
        result = get_value_as_string()
        return result
    
    def get_value_as_string(self, encode=True):
        """

        get_value_as_string() -> str

        Method prepares a string that represents the selections. You can choose
        whether to encode the items in URL format through "encode".
        """
        selection = self.get_selection()
        sep = self.get_sep()
        result = sep.join(selection)
        
        if encode:
            result = urllib.parse.urlendcode(result, safe=sep)
        return result

    def reset(self):
        """

        reset() -> None

        Method clears the list of selections for the instance. If you specified
        a value for default, and that value is True, reset() will add the value
        to selection. 
        """
        self._choices.clear()
        default = self.get_default()
        if default:
            self._choices.append(default)

    def select(self, *selections, force=False):
        """

        select() -> None

        Method records selections if there are fewer of them than the limit, or
        the instance does not define a limit, and throws an exception otherwise.
        If "force" is off, you can only add selections that are on the menu. 
        """
        # could also have controls for reset and truncate #<----------------------------------- revisit
        limit = self.get_limit()
        if limit is not None:
            if len(selections) > limit:
                c = "The number of selections exceeds the instance limit: %s"
                c = c % len(selections)
                raise Exception(c)

            else:
                menu = self.get_menu()
                self._selections.reset()
                if menu:
                    for selection in selections:
                        # go one by one
                        if force or (selection in menu):
                            self._selections.append(selection)
                else:
                    # menu is empty, anything goes
                    self._selections.extend(selections)

    def set_menu(self, *options, reset=True):
        """

        set_menu() -> None

        Method extends the menu with the options. If you turn off "reset",
        method will keep the options already on the menu. 
        """
        if reset:
            self.reset()

        self._menu.extend(options)

    def set_value(self, value, force=False):
        """

        set_value() -> Exception

        Method throws exception when called. You should use select() to choose
        items from the menu. 
        """
        raise Exception
    
