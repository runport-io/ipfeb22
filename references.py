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

def get_next(string, prefix, length, trace=False):
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
            if trace:
                print(next_part)
                print("\n")
                print("token: ", token)
                print("result: ", result)
                print("next part:  ", next_part[0])
            
            next_tokens = next_part[0]
            if next_tokens[0]!= token:
                result.extend(next_tokens)

            remainder = next_part[1]
        else:
            pass

    return (result, remainder)

def get_tokens(string, prefix, length=2, trace=False):
    result = set()
    rem = string
    while rem:
        token, rem = get_next(rem, prefix, length, trace=trace)
        adj_token = tuple(token)
        result.add(adj_token)

    return result

def transform(tokens):
    # return a dictionary thats a look up table
    result = dict()
    prefix = "0x"
    for token in tokens:
        seed = list()
        for node in token:
            adj_node = prefix + node
            value = int(adj_node, 16)
            seed.append(value)
            
        result[token] = bytes(seed)
    
    return result

def extract_and_replace(string, prefix):
    result = string
    tokens = get_tokens(string, prefix=prefix)
    lookup = transform(tokens)
    print(lookup)
    for token, byte_string in lookup.items():
        adj_token = "=" + "=".join(token)
        print("Adj. token:", adj_token)
        value = byte_string.decode()
        print("value:     ", value)
        result = result.replace(adj_token, value)

    return result

# to do:
# works ok, but doesn't fix one reference, f0 etc.
# pull the parse into char logic into a function, so i could get the result for
# a single function
# check on the reaplcement for that.
# check on othr messages. 

# take a string, and replace everything in the transform
#

# edge cases
# add a little bit of include URLs or not
# escaped new lines
# single blank
    

    # go through each location
    # for each location, see what's in 2, and what's in 4
    # compare
    # or keep parsing? 

