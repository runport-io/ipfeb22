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
import uuid

# 2) Port.
import constants
import utilities as up

class Number:
    """
    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    
    FUNCTIONS:
    get_name
    set_name
    get_number
    set_number
    get_namespace
    set_namespace
    
    ------------------  --------------------------------------------------------
    """
    def __init__(self):
        self._name = None
        self._number = None
        self._namespace = None

    def set_namespace(self, namespace, force=False):
        up.set_with_force(self, "_namespace", namespace, override=force)

    def get_namespace(self):
        result = self._namespace
        return result

    def set_name(self, name, force=False):
        up.set_with_force(self, "_name", name, override=force)

    def get_name(self):
        return self._name

    def set_number(self, namespace=None, name=None):
        if namespace:
            self.set_namespace(namespace)
        else:
            namespace = self.get_namespace()
        
        if name:
            self.set_name(name)
        else:
            name = self.get_name()
            
        number = generate_number(namespace, name)
        up.set_with_force(self, "_number", number)

        return number
    
    def get_number(self):
        return self._number

    @classmethod
    def make(cls, data=None):
        new = cls()
        if data:
            new.__dict__.update(data)
        return new

    def validate(self):
        result = False
        actual = self.get_number()
        namespace = self.get_namespace()
        name = self.get_name()
        expected = generate_number(namespace, name)
        if actual == expected:
            result = True
        return result

    def get_lines(self, include_header=True):
        lines = up.get_lines(self, include_header=include_header)
        return lines

    def __str__(self):
        lines = self.get_lines()
        glue = constants.NEW_LINE
        string = glue.join(lines)
        return string

def generate_number(namespace, name):
    result = uuid.uuid5(namespace, name)
    return result

skip = list()
setattr(Number, constants.SKIP_ATTRIBUTES, skip)

# Testing
def run_test():
    random = uuid.uuid4()
    print("Random: ")
    print(random)

    a = Number()
    print("a: ", a)
    a.set_namespace(random)
    a.set_name("eggplant")
    print(a)
    a.set_number()
    print(a)

    b = Number()
    print("b: ", b)
    b.set_number(random, "grapefruit")
    print(b)

if __name__ == "__main__":
    run_test()
