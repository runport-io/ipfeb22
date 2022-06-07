# Copyright Port. Prerogative Club ("the Club")
#
# 
# This file is part of Port. 2 ("Port.")
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
# N/a

# 2) Port.
import constants
import exceptions
import number
import utilities

# 3) Constants
# N/a

# 4) Functions
class Source:
    """

    Object tracks the handlers of a piece of information.
    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    number              instance of Number
    
    FUNCTIONS:
    get_sender()        
    set_sender()        Takes string for now.
    ------------------  --------------------------------------------------------
    """
    def __init__(self, name=None):
        self.number = number.Number()
        self._author = None
        self._sender = None
        
        if name:
            self.set_sender(name)

    def get_author(self):
        """

        get_author() -> string or None

        Method retrieves the author for the instance.
        """
        return self._author
        
    def get_sender(self):
        """

        Source.get_sender() -> string or None
        
        Returns contents of the non-public sender attribute on instance. Does
        not verify type of input.
        """
        result = self._sender
        return result
    
    def set_author(self, string):
        """

        set_author() -> None

        Method records string on instance.
        """
        self._author = string
        
    def set_sender(self, string, override=False):
        """

        Source.set_sender() -> None

        Expects a string as an input, stores on non-public attribute of
        instance. Does not verify type of input.
        """
        utilities.set_with_override(self, "_sender", string, override=override)
        # ideally this would be an object, like NYT, nyt@nyt.com, signature

    def get_lines(self, header=True):
        """

        Source.get_lines() -> list()

        Returns list of strings that show the contents of instance. If "header"
        is True, starts with "Source: "
        """        
        lines = list()
        if header:
            line = "Source:   "
            lines.append(line)

        sender = self.get_sender()
        line = "Sender: " + str(sender)
        lines.append(line)

        return lines

    def set_number(self, namespace):
        name = self.get_sender()
        self.number.set_number(namespace, name)
        

    #**************************************************************************
    #*                             Non-public                                 *
    #**************************************************************************
    
    def __str__(self):
        lines = self.get_lines()
        result = constants.NEW_LINE.join(lines)
        return result

# add wrap in skip_attrs
# add attributes to print

# Tests
def run_test():
    import uuid
    test_namespace = uuid.UUID(constants.TEST_STRING)

    s1 = Source("ilya")
    print(s1)
    s1.set_number(test_namespace)

    s2 = Source("somebody")
    print(s2)
    s2.set_number(test_namespace)

    result = (test_namespace, s1, s2)
    return result

if __name__ == "__main__":
    run_test()
