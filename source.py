# source
# (c) Port. Prerogative Club 2022

# Built-ins
# N/a

# Port.
import constants
import exceptions
import utilities

# Constants
# N/a

# Functions
class Source:
    """

    Object tracks the handlers of a piece of information.
    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    N/a
    
    FUNCTIONS:
    get_sender()        
    set_sender()        Takes string for now.
    ------------------  --------------------------------------------------------
    """
    def __init__(self, name):
        self._sender = None
        self.set_sender(name)

    def get_sender(self):
        """

        Source.get_sender() -> string
        
        Returns contents of the non-public sender attribute on instance. Does
        not verify type of input.
        """
        result = self._sender
        return result
    
    # sender
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

    #**************************************************************************
    #*                             Non-public                                 *
    #**************************************************************************
    
    def __str__(self):
        lines = self.get_lines()
        result = constants.NEW_LINE.join(lines)
        return result

# add wrap in skip_attrs
# add attributes to print

s1 = Source("ilya")
print(s1)

s2 = Source("somebody")
print(s2)
