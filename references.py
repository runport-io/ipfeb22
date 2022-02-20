# References
# (c) Port. Prerogative Club ("the Club")
# Port. 2.0
# Subject to GPL 3.0, unless agreed to in writing with the Club.

# Imports
# 1) Built-ins
# n/a

# 2) Port.
import constants

def locate_references(string, prefix=constants.EQUALS):
    """

    locate_references(string) -> list

    Returns a list of integers that represent the locations of the handle in the
    string. You should remove newlines from a string before sending.
    """
    result = list()
    i = 0

    while i < length(string):
        if string[i] == prefix:
            result.append(i)
        i = i + 1
    
    return result

# need to handle the "= " empty byte

def identify_tokens(string, references, prefix=constants.EQUALS, length=2):
    """

    identify_tokens() -> dict

    Function picks out the tokens that follow a handle in the string. Expects
    each token to have the length you specify.

    Function treats uniques as a token. 
    """
    tokens = set()
    skip = len(prefix)
    
    for ref in references:
        token = ""
        start_this = ref + skip
        end_this = start_this + length
        this_token = string[start_this:end_this]
        token = this_token
        if token in tokens:
            continue
        else:
            next_token = get_next(remainder, prefix, length)
            token = token + next_token
            # check the one after, and so on
    pass

def get_next(string, prefix, length):
    # goal of this function if to return one token of variable length, as well
    # as the remainder of the string
    result = list()
    remainder = None
    
    skip = len(prefix)
    
    location = string.find(prefix)
    found = False
    if location != -1:
        found = True

    if found:
        start = location + skip
        end = start + length
        token = string[start:end]
        result.append(token)
        remainder = string[end:]

        if remainder[0] == prefix:
            # next step is also a reference potentially
            next_part = get_next(remainder, prefix, length)
            result.extend(next_part[0])

        else:
            pass

    return (result, remainder)

    
            
            
    

    # go through each location
    # for each location, see what's in 2, and what's in 4
    # compare
    # or keep parsing? 

