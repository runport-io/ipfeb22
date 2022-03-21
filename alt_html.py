# Copyright Port. Prerogative Club ("the Club")
#
# 
# This file is part of Port. 2.0. ("Port.")
#
# Port. is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Port. is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Port. If not, see <https://www.gnu.org/licenses/>.
#
# Questions? Contact hi@runport.io.

# Imports
# 1) Built-ins
import pickle

# 2) Port.
import references

# 3) Constants
ARROW_LEFT = "<"
ARROW_RIGHT = ">"

COLON = ":"
EQUALS = "="

HTML_START = "<html>"
HTML_END = "</html>"

QUOTATION = '"'

SLASH = "/"
SPACE = " "
STYLE_START = "<style"
STYLE_END = "</style>"
TABLE = "table"


# 4) Functions
def parse_body_as_html(string):
    html = extract_html(string)
    # pass
    # extract html
    # extract style
    # extract table

def do_nothing(element):
    result = element
    return result

def construct_start(element):
    result = ARROW_LEFT + element
    return result

def construct_end(element):
    result = ARROW_LEFT + SLASH + element + ARROW_RIGHT
    return result

def remove_tag(string, tag):
    start_tag = construct_start(tag)
    end_tag = construct_end(tag)
    result = remove_elements(string, start_tag, end_tag)
    return result

def parse_image(element):
    """
    -> 
    """
    pass

def parse_tag(tag):
    """
    -> dict

    Function returns a dictionary of attributes. 
    """
    # let's say I only get here with the substantive tag, so <table ... >
    # or <img ...>. I have to remove the closing tag, if any, elsewhere.

    # should I return the tag plus the data? I think so.

    result = dict()
    adj_tag = references.clean_string(tag) #<--------------------------------------- moved lower
    # I do this now because otherwise, the colons may be escaped. I am removing
    # any embedded, escaped new lines here.
    contents = remove_arrows(adj_tag)
    # keep this

    pairs = contents.split()
    for pair in pairs:
        if pair.startswith(EXCLAMATION_MARK):
            data = parse_comment(pair)
            result.update(data)
        elif EQUALS in pair:
            attribute, value = pair.split(EQUALS)
            result[attribute] = value
            # need to protect against implicit overwrites.
        else:
            attribute = pair
            # for the tag itself
            result[attribute] = None
            
    return result
    
    # to do:
    ## 1) strip arrows - done
    ## 2) strip quotes
    ## 3) do something with comments, either take them as is, or replace.
    ## 4) add logic to detect if this is a single tag or an open / closed pair.

def remove_quotes(string):
    pass

def extract_tokens(tag):
    """
    -> list

    Function picks out each token in the tag. 
    """
    result = list()
    
    adj_tag = remove_arrows(tag)
    # get rid of "<" and ">"
    contents = references.clean_string(tag)
    # remove escapes

    # i need to pick out things like the tag name
    # that's the first token, I should strip out left of first space
    name = contents
    # should work for <br>, <td>, and so on
    
    first_space = contents.find(SPACE)
    # -1 here means that I did not find the query. 
    if first_space != -1:
        name = contents[:first_space]
        contents = contents[first_space:]
    name_token = (name, None)
    result.append(name_token)
    # should be its own routine. extract_name

    attrs = list()
    for i in range(len(contents)):
        pass
        # here, i have to attr to attr, and keep parsing until i hit the quote
        char = contents[i]
          
        if char is SPACE:
            continue
        else:
            pass
            # add to token if it exists
            # start new token if it does not

            # if char is alphanumeric:
                # if i haven't finished the attr_name, then this is part of the
                # attr_name

                # if i have finished the attr_name, then this is the value until
                # i hit the end quote.

    # I can also take a shortcut and parse "style" separately. So find "style",
    # then take =, then start parsing and keep going until I reach the quote
    # again. Extract that. then split remainder.

def parse_string(string):
    tokens = list()
    wip = string
    length = len(wip)

    parsing = False
    token = ""
    quotes = 0 #I don't use this
    
    for i in range(length):
        char = wip[i]
        if not parsing:
            if char == SPACE:
                continue
            else:
                parsing = True
                # start parsing
                token += char
                # simple, won't differentiate
                continue
        else:
            token += char
            if char == QUOTATION:
                quotes += 1
                if quotes == 2:
                    
                    parsing = False
                    tokens.append(token)
                    quotes = 0
                    token = ""
                    # can move the append and token reset to the start op
                    
    return tokens

def remove_arrows(string, remove_slash=False):
    """

    remove_arrows() -> string

    Function removes arrows from a tag. If remove_slash is True, function also
    removes the slash that closes tags like "img".
    """
    result = string
    if result.startswith(ARROW_LEFT):
        result = result[1:]
    if result.endswith(ARROW_RIGHT):
        result = result[:-1]

    if remove_slash:
        if result.endswith(SLASH):
            result = result[:-1]

    return result    

def parse_comment(comment):
    result = dict()
    key = comment[:1]
    value = comment[1:]
    result[key] = value
    return result

def extract_html(string):
    """

    -> string
    
    """
    html_start = HTML_START
    html_end = HTML_END

    start = string.find(html_start)
    end = string.rfind(html_end)

    result = string[start:end]
    return result

def render_image(image_tag):
    """
    
    """
    pass
    # should take the tag, pull out alt, and then print it
    # *\nIMAGE: {desc} {Link: x}*\n"
    
def render_link(link_tag):
    """
    """
    pass
    # make "{Caption}{Link: x}", return data of v.
    # How to handle text? # How to handle empty links?
    
    
def remove_elements(string, start, end=ARROW_RIGHT, handler=do_nothing):
    """

    -> (string, list)
    
    Function removes elements between start and end from the string. You get
    back a tuple of (0) the string without the elements and (1) a list of
    outputs from the function you specify as handler, or the elements
    themselves if handler is None.
    """
    trace = True
    cleaned = ""
    elements = list()

    wip = string
    
    start_length = len(start)
    end_length = len(end)
    
    while start in wip:
        start_position = wip.find(start)
        
        end_begins = wip.find(end)
        end_position = end_begins + end_length
        # if start = "<table", this moves forward 6 characters

        element = wip[start_position:end_position]
        if trace:
            print(element)
            
        before = wip[:start_position]
        after = wip[end_position:]

        cleaned += before
        processed_element = handler(element)
        elements.append(processed_element)        

        wip = after
        # repeat

    cleaned += wip
    # wip will be the tail, after the last tag

    result = (cleaned, elements)
    return result

# can and probably should refactor this to generate coordinates, then do with
# those as i wish. almost like a tag type, coordinates. 

# turn break tags into something

# misc:
# 1) I should generalize the process for extracting tags: tag <x, and so on. 
# 2) I should handle <br /> tags and replace them with newlines. I should do
# this after I remove all the whitespace.

# what I really want to do is get rid of all the tabs and new lines, probably,
# and rely only on the html formatting: pars, breaks, etc.


# Tests
p = "ubs_body.pkl"
f = open(p, "rb")
ubs_body = pickle.load(f)
# pass

def _run_test1(string, trace=True):
    html = extract_html(string)
    if trace:
        print(html[:200])        
    return html

def _run_test2(html):
    """

    _run_test2() -> tuple
    
    Function extracts style elements from HTML. You get back a tuple of the
    string and the data. 
    """
    print("Starting length: %s" % len(html))
    string, data = remove_elements(html, STYLE_START, STYLE_END)
    print("Ending length: %s" % len(string))
    return (string, data)

def _run_test3(html):
    """

    _run_test3() -> tuple
    
    Function extacts table elements from html. You get back a tuple of the
    string and the data.
    """
    print("Starting length: %s" % len(html))
    string, data = remove_tag(html, TABLE)
    print("Ending length: %s" % len(string))
    return (string, data)

def _run_test4(tags):
    """

    _run_test4(html) -> list()

    """
    result = list()
    for tag in tags:
        data = parse_tag(tag)
        result.append(data)

    return result

def _run_test5():
    pass

##  Pull out all images. Return a string with images replaced by some sort of a
##  placeholder for images. 

# next, strip out all tables.
def _run_test(string):
    html = _run_test1(string)
    print("Completed test 1.")
    chars_removed = len(string) - len(html)
    print("removed %s characters" % chars_removed)

    s1, d1 = _run_test2(html)
    print("Completed test 2.")
    print(d1)

    s2, d2 = _run_test3(s1)
    print("Completed test 3.")
    print("String: \n%s\n\n" % s2)
    print("Data: \n%s\n\n" % d2)    

    data = _run_test4(d2)
    print("Completed test 4: parsing tags")
    for i in enumerate(data):
        print(i)
    

if __name__ == "__main__":
    _run_test(ubs_body)
    



