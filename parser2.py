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
COLON = ":"
COMMA = ","
EMPTY_STRING = ""
EM_DASH = "-"
EQUALS = "="
FWD_SLASH = "/"
QUESTION_MARK = "?"
SEMICOLON = ";"
SPACE = " "
UNDER = "_"

# Headers
CHARSET = "charset"
CONTENT_ENCODING="Content-Transfer-Encoding"
CONTENT_TYPE = "Content-Type"
FIELDS = [CHARSET, CONTENT_ENCODING, CONTENT_TYPE]

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

def unescape_chars(string, escape=EQUALS, chars=BREAKS, lookup=None):
    """

    unescape_chars() -> string

    Function removes escapes from characters. For example, if you have a string
    where newlines have escapes, you can use this routine to strip the escape
    from the newline without affecting other escaped values.

    If you specify lookup, function will replace the character with the value in
    the lookup. You should provide a dictionary for the lookup.
    """
    result = string
    
    for char in chars:
        query = escape+char
        replacement = char
        if lookup:
            replacement = lookup[char]
            
        result = result.replace(query, replacement)

    return result

# outline
# body, split by newline
# take first two lines
# check for "Content-Type"
# line1: split by semicolon
# check for "Content-Transfer-Encoding"

def extract_encoding:
    pass

def clean_body(string):
    """

    -> string, dict

    Returns cleaned string and dictionary of header and optionally links.
    """
    body = string
    data = ""

    body = unescape_chars(body)
    # clean the new lines
    header, body = strip_header_from_body(body)
    data = parse_header(header)

    # if encoding is utf8
    # <--- should extract encoding and pass it down
    body = html_entities.clean_string(body, encoding=encoding)

    return body, data

def strip_header_from_body(string, line_count=2):
    """

    strip_header_from_body() -> list, string
    """
    result = tuple()
    header = list()
    lines = string.splitlines(NEW_LINE)
    header = lines[:line_count]
    
    remainder = lines[line_count:]
    body = NEW_LINE.join(remainder) 

    result = (header, body)
    return result

def fold_case(iterable):
    """
    -> list
    """
    result = list()
    for item in iterable:
        adj_item = item.casefold()
        result.append(adj_item)
        
    return result
    
def parse_header(header, match_case=False, strip_whitespace=True):
    """

    -> dict

    Function returns a dictionary 
    """
    result = dict()
    wip = dict()
    assignment_operators = [COLON, EQUALS]
    
    if not match_case:
        header = fold_case(header)
        assignment_operators = fold_case(assignment_operators)
    
    for line in header:
        # line1: "Content-Type: text/plain; charset=utf-8"
        segments = line.split(SEMICOLON)
        for segment in segments:
            #segment: "Content-Type: text/plain;"
            operator = ""
            for operator in assignment_operators:
                if operator in segment:
                    key, value = segment.split(operator)
                    wip[key] = value

    if strip_whitespace:
        for k, v in wip.items():
            adjk = k.strip()
            adjv = v.strip()
            result[adjk] = adjv
    else:
        result = wip

    return result

def strip_links(string):
    """

    strip_links() -> dictionary

    Function removes links, replaces them with numbers. Returns dictionary of
    number to link.
    """
    pass
