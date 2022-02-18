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

# Built-ins

# P2
import utilities as up

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
    number              an instance of Number
    
    FUNCTIONS:
    get_content         returns content from instance
    set_content         sets content for instance, can force overwrite.
    ------------------  --------------------------------------------------------
    """
    SKIP_ATTRIBUTES = []

    @classmethod
    def make(cls, data=None):
        new = cls()
        new.__dict__.update(data)
        # should skip attributes?
        return new
        
    def __init__(self, content=None):
        self._content = content
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







