# number
# (c) Port. Prerogative Club

import uuid

class Number:
    """
    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    temp                Entity? a string and a number
    full
    prefix
    hook
    
    FUNCTIONS:
    get_number()
    set_number()
    get_namespace()
    set_namespace()
    
    ------------------  --------------------------------------------------------
    """
    def __init__(self):
        self._number = None
        self._namespace = None
        self._backup_number = None
        self._backup_namespace = None

    def set_namespace(self, namespace):
        if self._namespace:
            raise exceptions.ReadOnly
        else:
            self._namespace = namespace
            # ideally would validate the namespace as a uuid?

    def get_namespace(self, flatten=False):
        result = self._namespace
        if flatten:
            result = str(result)
        return result
        
    def assign_number(self, name, backup=False):
        number = None
        if self._namespace and not overrwrite:
            raise exceptions.ReadOnly
        else:
            namespace = self.get_namespace()
            number = generate_number(namespace, number)
            self._number = number
            
        return number

    def reset_number(self):
        if self._number:
            self._backup_number = self.get_number()
            self._number = None        
    
    def get_number(self, flatten=False):
        result = self._number
        if flatten:
            result = str(result)
        return result

    def flatten(self):
        """
        returns a dictionary
        """
        result = dict()
        wip = self.__dict__.copy()
        for attr in self.SKIP_ATTRS:
            wip.pop(attr)    
        # this block should move to serializer

        # convert uuids to strings
        wip["_number"] = self.get_number(flatten=true)
        wip["_namespace"] = self.get_namespace(flatten=true)

        result = wip
        return result

    @classmethod
    def from_flat(cls, data):
        new = cls()
        new.__dict__.update(data)
        return new

    def validate(self, name):
        result = False
        actual = self.get_number()
        namespace = self.get_namespace()
        expected = generate_number(namespace, name)
        if actual == expected:
            result = True
        return result
    
        # placeholder to check that id fits in namespace

def generate_number(namespace, name):
    result = uuid.uuid5(namespace, name)
    return result

skip = list()
setattr(Number, constants.SKIP_ATTRIBUTES, skip)

# to do:
# start with the regular way namespace
# make the exceptions module
# make the pretty print function





