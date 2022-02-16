# textfield
# (c) Port. Prerogative Club 2022

"""

Module defines the TextField class. A TextField holds a string and information
about that string.

------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:

FUNCTIONS:

CLASSES:
TextField           Container for storing text and information about the text.
------------------  ------------------------------------------------------------
"""

# Built-ins

# P2

# Constants

# Classes
class TextField:
    """
    
    A TextField stores a string and information about its language. The idea is
    to simplify reading in the future. 

    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:

    language            placeholder, if None then American English
    [hook                instance of a Hook, to go one level up in the hierarchy]
    
    FUNCTIONS:
    copy                returns deep copy of event
    print_contents      returns a string that looks nice when you print it
    json_to             returns a JSON object 
    json_from           (cls) generates an instance of the class from JSON
    check_equivalence   placeholder for exact match
    check_similarity    placeholder for fuzzy match
    ------------------  --------------------------------------------------------
    """
    SKIP_ATTRIBUTES = ["hook"]

    @classmethod
    def from_flat(cls, data):
        new = cls()
        new.__dict__.update(data)
        # connect hook? new.hook.establish(parent)
        return new
        
    def __init__(self, string=""):
        self._content = string
        self.language = None
        
    def copy(self):
        new = TextField()
        new.language = self.language
        content = self.get_content()
        new.set_content(content)

        return new
        
    def get_content(self):
        return self._content

    def set_content(self, content, overwrite=False):
        if overwrite:
            self._content = content
        else:
            if self._content:
                raise Exception("Implicit overwrite.")
            else:
                self._content = content

    def print(self):
        content = self.get_content()
        print(content)

f1 = TextField("Something happened somewhere and no one knows.")
print("Field 1:    ")
f1.print()

f2 = f1.copy()
print("Field 2:    ")
f2.print()

try:
    f2.set_content("blah blah")
except Exception:
    # fix this block
    print(Exception)

f2.set_content("blah blah", overwrite=True)
print("Field 2, mod:")
f2.print()







