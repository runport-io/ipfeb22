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

def construct_end(element):
    result = ARROW_LEFT + SLASH + element + ARROW_RIGHT
    return result

def construct_start(element):
    result = ARROW_LEFT + element
    return result

def detect_tokens(string):
    """

    -> list

    Returns a list of tokens in the string, where the string follows the
    convention for assigning values in HTML (ie, 'key1="value1" key2="value2"').
    """
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

def do_nothing(element):
    result = element
    return result

def extract_content(element):
    """

    -> content, start, end
    
    Removes one layer of tag, returns the inside 
    """
    start_tag, remainder = find_first(element)
    remainder, end_tag = find_last(remainder)

    result = (remainder, start_tag, end_tag)
    return result

    # find_first() -> tag, remainder
    # find_last() -> tag, remainder
    # return ((first, last), remainder)

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

def extract_name(string):
    """
    -> string, string

    Expects a tag without arrows
    """
    wip = string
    name = wip
    remainder = ""

    first_space = name.find(SPACE)
    if first_space == -1:
        pass
        # no spaces found, the entire string is the name (e.g., "br").
    else:
        name = wip[:first_space]
        start = first_space + len(SPACE)
        remainder = wip[start:]

    return (name, remainder)
    # should work on <br> and <td>, and so forth.
    # consider skipping the first slash

def find_first(string):
    """

    -> string, string

    Function returns a tuple of the tag and the remainder. 
    """
    tag = ""
    remainder = string

    if remainder.startswith(ARROW_LEFT):
        end = len(remainder)
        if ARROW_RIGHT in remainder:
            location = remainder.find(ARROW_RIGHT)
            end = location + 1
            
        tag = remainder[:end]
        remainder = remainder[end:]

    return tag, remainder

def find_last(string):
    """

    -> string, string

    Function returns the remainder and the last tag. 
    """
    tag = ""
    remainder = string

    if remainder[-1] == ARROW_RIGHT:
        if ARROW_LEFT in remainder:
            start = remainder.rfind(ARROW_LEFT)
            tag = remainder[start:]
            remainder = remainder[:start]

    return remainder, tag

    # to do:
    ## 1) strip arrows - done
    ## 2) strip quotes - done
    ## 3) do something with comments, either take them as is, or replace. <--------------------------------------------
        ## for comments, I want to take them out before I break the escapes
        ## that is, while the new lines are still in
        ## cause then I can take any comments that are in a line?
        
    ## 4) add logic to detect if this is a single tag or an open / closed pair.

def parse_attributes(string, strip_quotes=True):
    """

    -> dict

    Function returns a map of names to values.
    """
    result = dict()
    tokens = detect_tokens(string)
    for token in tokens:
        attr, value = token.split(EQUALS)

        if strip_quotes:
            value = remove_quotes(value)
        
        result[attr] = value
        
    return result

def parse_comment(comment):
    result = dict()
    key = comment[:1]
    value = comment[1:]
    result[key] = value
    return result

def parse_element(element):
    """

    -> content, tag_name, tag_data, match

    Gets the first tag and content. Returns the data for the tag.
    """
    pass
    
    # this should probably return the inside of the element with formatting, if
    # any. the formatting should come from the tags: images, etc.

def parse_tag(tag):
    """
    -> tuple

    returns a tuple of name, attributes
    """
    cleaned = references.clean_string(tag) #<--------------- consider cleaning element? 
    content = remove_arrows(cleaned)
    name, remainder = extract_name(content)
    attributes = parse_attributes(remainder)

    return name, attributes
    
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
        if element:
            processed_element = handler(element)
            elements.append(processed_element)        

        wip = after
        # repeat

    cleaned += wip
    # wip will be the tail, after the last tag

    result = (cleaned, elements)
    return result

def remove_quotes(string):
    result = string
    if result.startswith(QUOTATION):
        result = result[1:]
    if result.endswith(QUOTATION):
        result = result[:-1]
    # can replace logic with detection of the char, etc. 
    
    return result

def remove_tag(string, tag):
    start_tag = construct_start(tag)
    end_tag = construct_end(tag)
    result = remove_elements(string, start_tag, end_tag)
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

def _run_test4(elements, trace=True):
    """

    _run_test4(html) -> list()

    see if the tag parsing works. #<--------------------------------------------- improve

    """
    result = list()

    if trace:
        print("Starting test 4....")
    
    for i, element in enumerate(elements):
        if trace:
            print("Element #%s" % i)
            print(element)
        
        content, tag_start, tag_end = extract_content(element)
        if trace:
            print("Start: %s\n" % tag_start)
            print("Content: \n%s\n" % content)
            print("End: %s\n" % tag_end)

        tag_name, tag_data = parse_tag(tag_start)
        if trace:
            print("Tag name: %s" % tag_name)
            print("Tag data: %s\n\n" % sorted(tag_data.items()))
        item = (tag_name, tag_data)
        result.append(item)

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

    elements = d2
    # elements contains a list of the tables I pulled out in test 3
    data = _run_test4(elements)
    print("Completed test 4: parsing tags")
    for i in enumerate(data):
        print(i)
    
if __name__ == "__main__":
    _run_test(ubs_body)
    



