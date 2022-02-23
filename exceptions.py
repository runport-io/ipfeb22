# Exceptions
# (c) Port. Prerogative Club 2022

class PortError(Exception):
    pass
    # parent 

class OverrideError(PortError):    
    pass

class PlaceholderError(PortError):
    """

    Flag for operations that I have not yet defined.
    """
    pass

class ParameterError(PortError):
    """

    Flag for something beinng wrong with inputs.
    """
    pass
