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
##import email_observer
# For testing <-------------------------------------------------------------------- remove dependency

# 3) Constants
HTML_START = "<html>"
HTML_END = "</html>"

STYLE_START = "<style"
STYLE_END = "</style>"
TABLE = "table"
ARROW_LEFT = "<"
ARROW_RIGHT = ">"
SLASH = "/"

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
    
    """
    pass
    result = dict()
    adj_tag = references.clean_html(tag)
    attrs = adj_tag.split()
    for attr in attrs:
        if COLON in attr:
            k, v = attr.split(COLON)
            result[k] = v
            # need to protect against implicit overwrites.
            
    return result
    
    
    # pass to the clean html
    # split by space
    # built attr dict by splitting by colon
    # return 

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
##E = email_observer.run_test1()
##messages = E.connector.get_messages(offset=0, count=10)
##m2 = messages[2]
##h2 = m2.get("subject")
##print(h2)

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

def _run_test4(html):
    """

    _run_test4(html) ->

    Pull out all images. Return a string with images replaced by some sort of a
    placeholder for images. 
    """
    pass

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

    return s2, d2

if __name__ == "__main__":
    _run_test(ubs_body)
    



