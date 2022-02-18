# number
# (c) Port. Prerogative Club

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

    def set_number(namespace=None, name=None):
        if namespace:
            self.set_namespace(namespace)
        else:
            namespace = self.get_namespace()
        
        if not name:
            self.get_name()
            
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

# to do:
# start with the regular way namespace
# make the exceptions module
# make the pretty print function





