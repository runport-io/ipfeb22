# References
# (c) Port. Prerogative Club ("the Club")
# Port. 2.0
# Subject to GPL 3.0, unless agreed to in writing with the Club.

# Imports
# 1) Built-ins
# n/a

# 2) Port.
# n/a

# 3) Data
EQUALS = "="
HEX_PREFIX = "0x"
STRICT = "strict"
TAB = "\t"
UTF8 = "utf-8"

def locate_references(string, prefix=EQUALS):
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

def adjust_base(string, starting_base=16, ending_base=10,
                prefix=HEX_PREFIX):
    """

    adjust_base() -> int

    Function recomputes the string as an integer in the ending_base. Throws a
    PlaceholderError if you try to compute a result other than in base 10.
    """
    result = None
    
    if ending_base != 10:
        c = "I have defined only transformations into base 10."
        raise exceptions.PlaceholderError(c)
    else:
        adj_string = prefix + string
        result = int(adj_string, starting_base)

    return result

def get_bytes(token, prefix=HEX_PREFIX):
    """

    get_bytes() -> bytestring

    Function changes a token of references into a bytestring. 
    """
    result = bytes()
    seed = get_integers(token)
    result = bytes(seed)
    return result

def get_integers(token, prefix=HEX_PREFIX):
    """

    get_integers -> list

    Function returns a list of integers that correspond to each item in the
    token. 
    """
    result = list()

    for node in token:
        value = adjust_base(node, prefix=prefix)
        result.append(value)

    return result

def turn_tokens_into_bytes(tokens, prefix=HEX_PREFIX):
    """

    turn_tokens_into_bytes() -> dict
    
    Function returns a mapping of each token to a bytestring. You should input
    an iterable for "tokens."
    """
    result = dict()
    for token in tokens:
        result[token] = get_bytes(token)

    return result

def turn_tokens_into_strings(tokens, prefix=HEX_PREFIX, encoding=UTF8,
                             errors=STRICT):
    """

    turn_tokens_into_strings() -> dict

    Function returns a dictionary of each token mapped to the string it
    represents. 
    """
    result = dict()
    for token in tokens:
        wip = get_bytes(token, prefix=prefix)
        value = wip.decode(encoding=encoding, errors=errors)
        result[token] = value
    return result

def clean_string2(string, trace=False, escape=EQUALS):
    """

    clean_string2 -> string

    Function replaces references to bytes in string with the string equivalents. 
    """
    result = string
    tokens = get_tokens(string, prefix=escape)

    if trace:
        print("Tokens:   ", tokens)

    lookup = turn_tokens_into_strings(tokens)

    if trace:
        print("Lookup:   ")
        keys = sorted(lookup.keys())
        for key in keys:
            view = constants.TAB + str(key) + ": " + str(lookup[key])
            print(view)

    for key, value in lookup.items():
        adj_key = escape + escape.join(key)
        # key is now a tuple, need to put in the escapes back in to detect
        # occurences in the string
        
        if trace:
                print("Key:      ", key)
                print("Adj. key: ", adj_key)
        
        result = result.replace(adj_key, value)
        
    return result
  
def extract_and_replace(string, prefix):
    """

    extract_and_replace() -> string

    Function cleans string of references to bytes by replacing the references
    with their unicode equivalents. Expects each reference to start with the
    prefix.
    """
    result = string
    tokens = get_tokens(string, prefix=prefix)
    lookup = transform(tokens)
    print(lookup)
    for token, byte_string in lookup.items():
        adj_token = prefix + prefix.join(token)
        print("Adj. token:", adj_token)
        value = byte_string.decode()
        print("value:     ", value)
        result = result.replace(adj_token, value)

    return result

# to do:
# works ok, but doesn't fix one reference, f0 etc.

# edge cases
# add a little bit of include URLs or not
# escaped new lines
# single blank
    
# replace the escaped new line
# get_tokens() should return a dictionary
# make a new routine that does the job of taking the header out
# 
