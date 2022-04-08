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
import browser.link
import references

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

def parse_comment(comment):
    result = dict()
    key = comment[:1]
    value = comment[1:]
    result[key] = value
    return result

def parse_element(string, clean=True):
    """

    -> element

    Function expects to receive a string that starts with "<x" and ends with
    "/x>".
    """
    result = browser.element.Element()
    wip = string
    if clean:
        wip = references.clean_string(wip)
        # this removes all line breaks, meaning that if the element contains a
        # lot of information, I cannot then view the formatted results, so I
        # should do this carefully. E.g., in tables. 

    
    # get the start, end, and contents
    # store them
    # parse the attributes in the start, store them
    # do something to the data? probably not

    # Will need to rework to handle images and </br> things?

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

# render all the images cleanly
    
# Refactoring
def e_find(string, regex):
    """

    -> iterable

    Function returns an iterable from re that returns spans. 
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

def replace_links(string, unique=False):
    """

    -> string

    """

    matches = find_links(string)
    
    lm = LinkManager
    if unique:
        lm.disable_repeats()
    
    updated = string
    for match in matches:

        span = match.span()
        # where it is
        
        link = make_link(element)
        # later i should do this automatically, based on the data in the tag
        
        ref = lm.register(link)
        # remove position from link object

        replacement = link.view(ref)
        # modify signature
        
        updated = replace(updated, span, replacement)

    return updated

def make_link(span):
    """

    -> Link

    Function returns a link object.
    """
    if not span.group("name").casefold() == "a":
        c = "This object is not a link."
        raise exceptions.OperationError(c, span)
    
    result = browser.link.Link()

    raw_attrs = span.group("attrs")
    attrs = parse_attributes2(raw_attrs)
    result.set_attrs(attrs)
    
    url = attrs["href"]
    result.set_url(url)
    
    data = span.group("data")
    result.set_data(data)

    # check if data is a caption or something else
    # <------------------------------------------------------------ probably by using re or something
    caption = data
    
    result.set_caption(caption)
    # should clean?
    
    start = span.group("start")
    result.set_start(start)
    
    end = span.group("end")
    result.set_end(end)

    return result    

# when to clean? last?
# run matches on cleaned?

# for each match
#   clean it
#   parse it: get the caption, get the link
#   assign the link a ref
#   replace the match with the pretty view
#   problems: sometimes the data is a tag; i don't have the storage worked out
#   for links, I could use a link object.

# later: review
# add link._data: placeholder for what's inside the link
# can add a constructor: link.construct() returns the HTML element.

# more later:
# Page object should have control for whether you have a unique refs or not? 

def replace(string, span, replacement):
    """

    -> string

    Function returns a string where the span has been replaced with the replacement.
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


    # I could also:
        # precompute replacements and zip them with the matches
        # that also would require a handler function and a counter.
    
    # go through the iterable
    # for span in iterable
    #   match = span.group()
    #   image = render_image(match)
    #   template = blah
    #   replacement = template % counter
    #   string = replace(string, start, end, replacement)
    # The issue is that the locations change once I execute the replacement
    # To mitigate that, I can:
    #   # adjust the position as i go
    #   # execute the replacement one at a time
    #   # compute the location on each iteration through string.find(match)
    #   # do some kind of a modified iteration, though that's like (2)

    # how will this look for tags then:
    #   find a tag
    #   replace the tag
    #   repeat

    # what about paragraphs and breaks
    #   same
    #   what's different:
    #       the replacement

    # so the idea of a replacement function actually makes sense
    # but if i want to find all, I should keep a copy, and copy into that.
    # so as i iterate, i keep track of the last offset. then, I can find all
    # at first.
    #



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

def _run_test5(string):
    link_start = construct_start(LINK)
    link_end = construct_end(LINK)
    result = remove_elements(string, link_start, link_end, replace=True)
    return result



# figure out how to deal with links
# as i parse a string:
# find all instances of links
# replace with "-Text- (Link: AA)"
# this requires me to keep track of positions?
# and to modify the extraction logic to deliver those positions
# I also need a second piece of state called "links", that's a dictionary that
# I pass in. It should key by ref to support things like "-here-, -here-, and
# -here-"

# how do i implement:
# when I pass in a link element and a links object, I should add the link to the
# links object

# so I'd have something like parse_links(html) that finds the links and parses
# them, as well as an add_link() that delivers a substring?

# question: what to do about links that are embedded, such as with images?

# plan: start with a basic element
# make a pretty thing out of it
# deliver the string and the url
# let the client fill in the string with the right ref, such as RR

# then make the parse_links routine if you can. that should go through
# and substitute any links in the whole thing with a clean format?

# really, at that point, i need to make the comprehensive rendering.
# what's my most basic comprehensive rendering:
# new lines for br and p (and a tab)
# parse links and images
# ignore everything else, meaning just drill down to data and show that
# raw.

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

def run_test_something(string):
    # this should be a way of being smart.
    # pull html out, then pull body out
    # in body, keep going in one level ("data")
    # printing and doing something else.
    pass

def _run_testx():
    pass
##  Pull out all images. Return a string with images replaced by some sort of a
##  placeholder for images.

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
    



