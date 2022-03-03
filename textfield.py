# textfield
# (c) Port. Prerogative Club 2022

"""

Module defines the TextField class. A TextField holds a string.

------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:

FUNCTIONS:

CLASSES:
TextField           Container for storing text and information about the text.
------------------  ------------------------------------------------------------
"""

# Imports
# 1) Built-ins
# n/a

# 2) Port.
import constants
import context
import utilities as up

from brands2 import Index
from number import Number


# Constants

# Classes
class TextField:
    """
    
    A TextField stores a string and information about that string.
    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    index               an instance of Index, tracks mentions in the body.   
    number              an instance of Number
    
    FUNCTIONS:
    get_content         returns content from instance
    set_content         sets content for instance, can force overwrite.
    ------------------  --------------------------------------------------------
    """
    SKIP_ATTRIBUTES = []

    @classmethod
    def from_flat(cls, data=None):
        new = cls()
        new.__dict__.update(data)
        # should skip attributes?
        return new
        
    def __init__(self, content=None):
        self._content = content
        self._data = None
        self._raw = None
        self.index = Index()
        self.number = Number()
    
    def get_content(self):
        return self._content

    def set_content(self, content, force=False):
        up.set_with_override(self, "_content", content, override=force)

    def get_lines(self, header=True):
        lines = list()
        if header:
            line0 = "TextField: "
            lines.append(line0)
        line1 = "Content: "
        lines.append(line1)
        line2 = str(self.get_content())
        lines.append(line2)
        
        number_lines = self.number.get_lines()
        for line in number_lines:
            line = constants.TAB + line
            lines.append(line)

        return lines

    def copy(self):
        new = up.deepcopy(self)
        return new

    def __str__(self):
        lines = self.get_lines()
        glue = constants.NEW_LINE
        string = glue.join(lines)
        return string

    def get_data(self, copy=True):
        """

        get_data() -> obj

        Method returns data from the instance. If you change "copy" to False,
        you get the object itself, otherwise method returns a copy of that
        object so that you can manipulate it.
        """
        result = self._data
        if copy:
            result = result.copy()
        return result

    def get_mentions(self, brand, length=100, flag=True):
        """

        get_mentions() -> dict

        Method returns a dictionary of spans mapped to strings. You can specify
        the number of characters you want from each side of the mention through
        "length" and whether to flag the mention. 
        """
        result = dict()
        body = self.get_content()
        spans = self.index.get_locations(brand)

        for span in spans:
            mention = context.get_context(body, span, length, flag)
            result[span] = mention

        return result

    def get_raw(self):
        """

        get_raw() -> str

        Method returns the format of the instance prior to any transformations.
        You should expect a string.
        """
        result = self._raw
        return result

    def get_snippet(self, line_count=10):
        """

        get_snippet() -> string

        Method returns the number of lines you specify from content.
        """
        content = self.get_content()
        lines = content.splitlines(keepends=True)
        snippet = "".join(lines[:line_count])
        return snippet

    def set_data(self, dictionary):
        """

        set_data() -> None

        Method sets data to the parameter you specify.
        """
        self._data = dictionary

    def set_raw(self, obj):
        """

        set_raw() -> None
        
        Method stores the string version of the object on the instance.
        """
        self._raw = repr(obj)
        # might not be necessary
        
    # consider adding a log attribute
    # every time i make a change, i log it. append only. requires a 
    # signature. probably don't need it right now? could run some logic or
    # something that prints the command
    
f1 = TextField("Something happened somewhere and no one knows.")
print(f1)

f2 = f1.copy()
print(f2)

try:
    f2.set_content("blah blah")
except Exception:
    # fix this block
    print(Exception)

f2.set_content("blah blah", force=True)
print("Field 2, mod:")
print(f2)







