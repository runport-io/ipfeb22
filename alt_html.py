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
import re

# 2) Port.
import references

import html_elements.link
import url_manager

# 3) Constants
ARROW_LEFT = "<"
ARROW_RIGHT = ">"

COLON = ":"
EQUALS = "="

HTML_START = "<html>"
HTML_END = "</html>"
LINK = "a"

QUOTATION = '"'

SLASH = "/"
SPACE = " "
STYLE_START = "<style"
STYLE_END = "</style>"
TABLE = "table"

# 4) Functions
def construct_end(element):
    """

    construct_end() -> str

    Function returns a tag that closes the element in HTML.
    """
    result = ARROW_LEFT + SLASH + element + ARROW_RIGHT
    return result

def construct_start(element):
    """

    construct_start() -> str

    Function returns the start of a tag that opens the element. The result omits
    the closing arrow for the tag to allow you to match the output against
    strings of html.
    """
    result = ARROW_LEFT + element
    return result

def detect_tokens(string):
    """

    detect_tokens() -> list

    Returns a list of tokens in the string, where the string follows the
    convention for assigning values in HTML (ie, 'key1="value1" key2="value2"').
    """
    tokens = list()
    wip = string
    length = len(wip)

    parsing = False
    token = ""
    quotes = 0
    
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
    # Use the re logic instead.

def do_nothing(element):
    """

    do_nothing() -> obj

    Function returns the input without changes.
    """
    result = element
    return result

def extract_content(element):
    """

    extract_content() -> content, start, end
    
    Removes one layer of tag, returns the inside 
    """
    start_tag, remainder = find_first(element)
    remainder, end_tag = find_last(remainder)

    result = (remainder, start_tag, end_tag)
    return result

def extract_html(string):
    """

    extract_html() -> string

    Function pulls out the contents between <html> and </html>. You may get
    problems if you input a string that lacks one or both of these elements.
    """
    html_start = HTML_START
    html_end = HTML_END

    start = string.find(html_start)
    end = string.rfind(html_end)

    result = string[start:end]
    return result  

def extract_name(string):
    """

    extract_name() -> string, string

    Function takes the contents of a tag without arrows and pulls out the value
    of the first argument. 
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

def find_first(string):
    """

    find_first() -> string, string

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

    find_last() -> string, string

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

def parse_attributes(string, strip_quotes=True):
    """

    parse_attributes() -> dict

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

## <-------------------------------------------------------------------------------- remove this routine?

def parse_attributes2(string, strip_quotes=True):
    """

    parse_attributes2() -> dict

    Function uses re to parse attributes. You should use modify the re if you
    expect to use assignment other than through "=" or other than double quotes
    around the attribute values.
    """
    result = dict()
    cleaned = references.clean_string(string)
    # without cleaning the re doesn't work as well. I use the re to look for
    # equals signs, and some of those appear more than once in escapes.
    
    attributes = re_attr.finditer(cleaned)
    # single use iterator
    #<----------------------------------------------------------------------------------------- improve re to include single quotes.
    
    for attribute in attributes:
        key = attribute.group("key") #embedded into re
        value = attribute.group("value")
        if strip_quotes:
            value = remove_quotes(value)

        result[key] = value

    return result

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
    
def remove_elements(string, start, end=ARROW_RIGHT, replace=False):
    """

    remove_elements() -> (string, list)
    
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
        start_ends = start_position + start_length
        
        end_begins = wip.find(end, start_ends)
        if end_begins != -1:
            end_position = end_begins + end_length
            # if start = "<table", this moves forward 6 characters
        else:
            end_position = end_begins
            # "end_begins" comes back as -1, meaning it is not in the string.
            # I want to avoid wrapping around, which would happen if I turn the
            # -1 into a positive integer by adding a length, and return an empty
            # slice when the start_position > end_position

        element = wip[start_position:end_position]
        if not element:
            c = "element is empty"
            print("Elements has a length of %s" % len(elements))
            raise exceptions.OperationError(c)
        
        if trace:
            print(element)

        elements.append(element)
        
        before = wip[:start_position]
        after = wip[end_position:]

        if replace:
            template = "{{%s}}"
            placeholder = template % len(elements)
            before = before + placeholder

        cleaned += before
        
        wip = after
        # repeat

    cleaned += wip
    # wip will be the tail, after the last tag

    result = (cleaned, elements)
    return result

def remove_quotes(string):
    """

    remove_quotes() -> string

    Function takes the input and strips starting and ending quotation marks. You
    can use this to clean the values of attributes in a string of HTML.
    """
    result = string
    if result.startswith(QUOTATION):
        result = result[1:]
    if result.endswith(QUOTATION):
        result = result[:-1]
    # can replace logic with detection of the char, etc. 
    
    return result

def remove_tag(string, tag):
    """

    remove_tag() -> tuple

    Function extracts elements that start and end with the tag from the string.
    You get back a cleaned string and a list of elements.
    """
    start_tag = construct_start(tag)
    end_tag = construct_end(tag)
    result = remove_elements(string, start_tag, end_tag)
    return result
  
# Refactoring
def e_find(string, regex):
    """

    e_find() -> iterable

    Function returns an iterable from re that returns matches. 
    """
    result = regex.finditer(string)
    return result

# Regular expressions
images = re.compile("<img.*?>", re.DOTALL)
re_link = re.compile("<a.*?/a>", re.DOTALL)
re_link2 = re.compile("<a.*?>.*?</a>", re.DOTALL)
re_link3 = re.compile("(?P<start><a(?P<attrs>.*?)>)(?P<data>.*?)(?P<end></a>)",
                      re.DOTALL)
re_link4 = re.compile(r"(?P<start><(?P<name>\ba\b)(?P<attrs>.*?)>)(?P<data>.*?)(?P<end></a>)",
                      re.DOTALL)
re_link4b = re.compile(r"(?P<start><(?P<name>a)(?P<attrs>.*?)>)(?P<data>.*?)(?P<end></a>)",
                      re.DOTALL)

# For more on RE, review this:
# https://docs.python.org/3.8/howto/regex.html#regex-howto

re_link5 = re.compile(r"(?P<element>(?P<start><(?P<name>a)(?P<attrs>.*?)>)(?P<data>.*?)(?P<end></a>))",
                      re.DOTALL)

# to improve this: permit whitespace between "<" and "a"
# also permit whitespace in the end tag

re_element = re.compile(r'(?P<element>'
                        r'(?P<start><(?P<name>\b\w+\b)(?P<attrs>.*?)>)'
                        r'(?P<data>.*?)'
                        r'(?P<end></\b(?P=name)\b>))',
                        re.DOTALL)

# this pulls out body and then stops

re_element2 = re.compile(r'(?P<element>'
                        r'(?P<start><(?P<name>\b\w+\b)(?P<attrs>.*?)>)'
                        r'(?P<data>.*?)'
                        r'(?P<end></(?P=name)>))',
                        re.DOTALL)

# This works very well recursively. Difference vs re_element is that the closing
# tag does not have to be separated by a word.

re_attr = re.compile(r'(?P<key>\b\w+?\b)'
                     r'(?P<equals>=)'
                     r'(?P<value>".*?")', re.DOTALL)

def find_links(string):
    """

    find_links() -> iter

    Function returns an iterator that contains Matches. Each Match should cover
    a link.
    """
    result = e_find(string, re_link5)
    return result

def replace_links(string, um=None):
    """

    replace_links() -> 3-tuple()

    Function returns the string, url manager ("um"), and a dictionary of refs
    to Links.
    """

    matches = find_links(string)

    if not um:
        um = url_manager.UrlManager()
    
    updated = string
    chars_deleted = 0

    link_objects = dict()
    
    for match in matches:
        
        link = make_link(match)
        # later i should do this automatically, based on the data in the tag
        url = link.get_url()
        ref = um.get_ref(url)
        link.set_ref(ref)

        link_objects[ref] = link
        # I am pretending that this implementation is so ugly I will have to
        # think of something better next.
        # <------------------------------------------------------------------------------------------ Refactor!

        replacement = link.view()        
        target = match.group()

        stated_start = match.span()[0]
        adjusted_start = stated_start - chars_deleted
    
        if adjusted_start < 0:
            c = "Something went wrong with finding a location on this string."
            raise exceptions.OperationError(c, match)

        target_length = len(target)
        
        end = adjusted_start + target_length
        span = (adjusted_start, end)
        
        updated = replace(updated, span, replacement)

        abbreviation = target_length - len(replacement)
        chars_deleted = chars_deleted + abbreviation
        # Increase the counter of how much I shortened the string by this
        # iteration.

    return updated, um, link_objects

# could make this into a view object
# really, what this should do is take a web_page object. The web_page object
# should have raw text and then views. The web_page should also include a url
# manager and a cache of some sort.
#
# then a function like this would modify the web_page view and other pieces of
# state, and return the webpage itself.
#
# I can see an argument for why the web_page can pull from the html_elements
# package, namely that I build the webpage from those elements. If so, the
# web_page can sit above the elements.
# <----------------------------------------------------------------------------------------------------

def make_link(span, trace=False):
    """

    make_link() -> Link

    Function returns a link object.
    """
    if not span.group("name").casefold() == "a":
        c = "This object is not a link."
        raise exceptions.OperationError(c, span)
    
    result = html_elements.link.Link()
    # <----------------------------------------------------------------------------------------- I should modify Link to run
    # on the data packages I build. 

    raw_attrs = span.group("attrs")
    attrs = parse_attributes2(raw_attrs)
    result.set_attrs(attrs)
    
    url = attrs["href"]
    result.set_url(url)
    
    data = span.group("data")
    result.set_data(data)

    # Add a caption to the link
    caption = ""
    wip = data.strip()
    wip = references.clean_string(wip)
##    caption = html_browser.get_view(wip)
##    # <--------------------------------------------------------------------------------------- What I really need to do is
##    # figure out the element nesting. So here data is an element. 

    if wip.startswith(ARROW_LEFT):
        pass
        # do nothing for now, next check if image
        
    else:
        if trace:
            print(span)
            print(wip, "\n")
            
        caption = references.clean_string(data)
        # I want to clean the original, I believe.

    result.set_caption(caption)
    
    # Fill in other attributes
    start = span.group("start")
    result.set_start(start)
    
    end = span.group("end")
    result.set_end(end)

    return result

def check_element(string):
    """

    check_element() -> match or None

    Function identifies whether the string starts with an element of html. If
    so, it returns the first element in the form of a match object.
    """
    result = None
    wip = string.strip()
    if wip.startswith(ARROWLEFT):
        matches = re_element2.finditer(wip)
        result = next(matches)

    return result
    # Do I ever use this? #<--------------------------------------------------------------------------------------

# ---- 

# when to clean? last?
# run matches on cleaned?

# later: review
# add link._data: placeholder for what's inside the link
# can add a constructor: link.construct() returns the HTML element.

# more later:
# Page object should have control for whether you have a unique refs or not? 

# ---
# extract_data(string):
#   pass
#   # if string is html, returns the data if any
#   # else...

# keep it simple stupid
# render contents
# if this is a string, clean it
# if it is a picture, draw the picture thing
# otherwise, do nothing. 

def replace(string, span, replacement):
    """

    replace() -> string

    Function returns a string where the span has been replaced with the
    replacement.
    """
    prefix = string[:span[0]]
    suffix = string[span[1]:]
    result = prefix + replacement + suffix
    return result
    # this should work <---------------------------------------------------------------
    
def e_replace(matches, handler=do_nothing, i=0, data=dict()):
    """

    -> string, index
    """
    result = ""
    source = ""    
    offset = 0
    
    for match in matches:
        
        if not source:
            source = match.string
            # runs once, source is attached to every match

        element = match.group()
        replacement, data = handler(element, i)
        # handler functions should always return this signature
        # <------------------------------------------------------ consider pulling the handlers out into a module

        start, end = match.span()
        # these are coordinates in source, not in result, since result varies
        # in length. 

        prelude = source[offset:start]
        offset = end

        addition = prelude + replacement
        result += addition

    return result, data

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
        #<----------------------------------------------------------------------- consider taking out the escapes and tabs in content here
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
    #< ---------------------------------------------------------------------------------------- consider removing this test?

def _run_test5(string):
    link_start = construct_start(LINK)
    link_end = construct_end(LINK)
    result = remove_elements(string, link_start, link_end, replace=True)
    return result

def _run_test6(html):
    links = e_find(html, re_link5)
    # single use iterator
    
    for i in range(4):
        link = next(links)
        print(link.group("name"))
        print(link.group())
        print("\n")
        print(link.group("start"))
        print("Attrs: %s" % link.group("attrs"))
        print(link.group("data"))
        print(link.group("end"))

    backup = e_find(html, re_link5)

    print("Completed test 6: extract links using re.")
    return backup

def _run_test7(matches):
    links = list()
    for match in matches:
        link = make_link(match)
        links.append(link)

    return links

def _run_test8(links, count=4):
    um = browser.url_manager.UrlManager()
    
    i = 0
    for link in links:
        url = link.get_url()
        ref = um.get_ref(url)
        link.set_ref(ref)
        view = link.view()

        if i < count:
            print(view)
            print("\n")

        i = i + 1
    
    return um

def run_test_something(string):
    # this should be a way of being smart.
    # pull html out, then pull body out
    # in body, keep going in one level ("data")
    # printing and doing something else.
    pass

# next:
# - better table analysis: for each item that's in a table, get the contents.
# -- will require me to parse rows.

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

    sample = html[:10000]
    print("Sample: \n%s" % sample)
    
    cleaned = _run_test5(sample)
    print("Completed test 5: remove and replace")
    print("String: \n%s\n" % result[0])
    print("Links: \n%s\n\n" % result[1])
    
    links = _run_test6(ubs_body)
    
if __name__ == "__main__":
    _run_test(ubs_body)
    



