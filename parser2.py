# parsing tools
# (c) Port. Prerogative Club 2022

# Imports
# 1) Built-ins
import base64

# 2) Port.
import constants

UTF8 = "UTF-8?"
UTF8_LO = "utf-8?"
UTF_PREFIXES = (UTF8, UTF8_LO)
START_ENCODING = "=?"
END_ENCODING = "?="
BREAKS = ("\t", "\r", "\n")

# Encoding
QUOTABLE = "q?"
BASE64 = "b?"
ASCII = "ascii"

# ASCII
APOSTROPHE = "'"
COMMA = ","
EMPTY_STRING = ""
EM_DASH = "-"
FWD_SLASH = "/"
QUESTION_MARK = "?"
SPACE = " "
UNDER = "_"

def detect_encoding(string):
    result = (None, None)
    encoding = None
    wip = string
    if wip.startswith(START_ENCODING):
        wip = wip[2:-2]
        encoding, wip = extract_encoding(wip)

    result = (encoding, wip)
    return result

def extract_domain(email_address):
    """

    extract_domain(email_address) -> string

    Returns the contents of the email address after the "@". 
    """
    domain = ""
    at = email_address.find(constants.AT)
    if at == -1:
        memo = constants.AT + " not in " + email_address
        raise exceptions.ParsingError(memo)
    else:
        start = at + 1
        domain = email_address[start:]
        
    return domain

def extract_encoding(string):
    """
    takes out the encoding prefix
    """
    result = (None, None)
    prefix = ""
    wip = ""
    i = 0
    while i <= len(string):
        if string[i] == QUESTION_MARK:
            wip = string[(i + 1): ]
            break
        else:
            prefix = prefix + string[i]
            i = i + 1

    result = (prefix, wip)
    return result        

def parse_parens(string, trace=False):
    """

    function expects string in format (x y)
    """
    result = dict()
    wip = ""
    start = False
    end = False
    for char in string:
        if trace:
            print(char)
            print("Start: ", start)
            print("End:   ", end)
        
        if char == "(":
            start = True
            if trace:
                print("Starting transcription")
                
            continue
        elif char == ")":
            end = True
            break
        if start and not end:
            wip = wip + char
            if trace:
                print("WIP:  ", wip)
            
    tokens = wip.split()
    result[tokens[0]] = tokens[1]
    
    return result

def remove_breaks(string, chars=BREAKS):
    result = string
    for char in chars:
        result = result.replace(char, EMPTY_STRING)

    return result

def remove_padding(string, char=SPACE):
    result = ""
    wip = string
    padding = SPACE * 2
    while padding in wip:
        wip = wip.replace(padding, SPACE)

    result = wip
    return result

def clean_string(string):
    """
    """
    result = ""
    wip = string
    
    if wip.startswith(START_ENCODING):
        wip = clean_utf(wip)
        # delivers regular way string, may still have linebreaks
    
    wip = remove_breaks(wip)
    wip = remove_padding(wip)
    
    #if no spaces, then replace underscores
    if SPACE not in wip:
        wip = wip.replace(UNDER, SPACE)
    
    result = wip
    return result
    
def clean_utf(string):
    """
    """
    result = ""
    wip = string

    if wip.startswith(START_ENCODING):
        wip = wip[2:-2]
    
    if wip.startswith(UTF_PREFIXES):
        prefix = wip[:6].casefold()
        wip = wip[6:]

        encoding = wip[:2].casefold()
        wip = wip[2:]
        if encoding == QUOTABLE:
            wip = parse_quotable(wip)
        elif encoding == BASE64:
            wip = parse_base64(wip)
    else:
        # reserved for non utf8 encoding, call subroutine
        pass
    
    result = wip
    return result

def parse_quotable(string):
    result = ""
    wip = string

    wip = wip.replace("=2C", COMMA)
    wip = wip.replace("=20", SPACE)
    wip = wip.replace("=E2=80=99", APOSTROPHE)
    wip = wip.replace("=27", APOSTROPHE)
    wip = wip.replace("=2D", EM_DASH)
    wip = wip.replace("=3", QUESTION_MARK)
    wip = wip.replace("=2F", FWD_SLASH)

    result = wip
    return result

def parse_base64(string):
    result = ""
    bytestring = string.encode(ASCII)
    # turns string into bytestring, without changing contents
    
    string_bytes = base64.b64decode(bytestring)
    # changes content of bytestring

    result = string_bytes.decode(ASCII, errors="ignore")
    # turns bytestring into regular string

    return result


