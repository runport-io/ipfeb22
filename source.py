# source
# (c) Port. Prerogative Club 2022

# Built-ins
# N/a

# Port.
import constants
import exceptions
import number
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
    number              instance of Number
    
    FUNCTIONS:
    get_sender()        
    set_sender()        Takes string for now.
    ------------------  --------------------------------------------------------
    """
    def __init__(self, name=None):
        self.number = number.Number()
        self._sender = None
        if name:
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
import uuid
test_namespace = uuid.UUID(constants.TEST_STRING)

s1 = Source("ilya")
print(s1)
s1.set_number(test_namespace)

s2 = Source("somebody")
print(s2)
s2.set_number(test_namespace)
