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
import re

# 2) Port.
import alt_html
import exceptions

import html_elements.element as element
import html_elements.image as image


# 3) Constants
re_double = alt_html.re_element2
re_single = re.compile(r'(?P<element>'
                       r'(?P<start><(?P<name>\b\w+\b)(?P<attrs>.*?)>))',
                       re.DOTALL)

ARROW_LEFT = "<"
ATTRS = "attrs"
IMAGE = "img"
NAME = "name"

PROCESSORS = dict()
PROCESSORS[IMAGE] = image.Image
# PROCESSORS[BOLD] = make_bold
## This should take the data and add two dots around it

def check_element(string):
    """

    check_element() -> bool

    Function returns True if the string starts with an HTML tag, False
    otherwise.
    """
    result = False
    if string.startswith(ARROW_LEFT):
        result = True
        
    return result

def check_startend(string):
    """

    check_startend() -> bool

    Function returns True if the string contains a single HTML tag, False
    otherwise.
    """
    result = False
    if string.count(ARROW_LEFT) == 1:
        result = True

    return result

def extract_data(match):
    """

    extract_data() -> dict

    Function takes the dictionary of groups from an re.Match and prepares its
    contents for consumption by routines that build elements. For example,
    this routine parses the value for attributes in the group. 
    """
    result = dict()
    wip = match.groupdict()

    attr_string = wip.get(ATTRS, None)
    attrs = dict()

    if attr_string:
        attrs = alt_html.parse_attributes2(attr_string)

    wip[ATTRS] = attrs
    result.update(wip)

    return result
    # Can add the underscore here so I don't have to do annoying stuff in apply_match()
    # logic. Then apply_match() becomes apply_data()<--------------------------------------------------------------------
    
def get_span(string, target):
    """

    get_span() -> tuple

    Function finds the target in the string.
    """
    start = string.find(target)
    if start == -1:
        c = "Not found"
        raise exceptions.OperationError(c)
    else:
        end = start + len(target)

    result = (start, end)
    return result

def make_element(data, default_processor=element.Element):
    """

    make_element() -> Element

    Function constructs a class on the basis of data. 
    """
    name = data.get(NAME)
    
    processor = default_processor
    if name in PROCESSORS:
        processor = PROCESSORS[name]

    result = processor(data)

    return result
    
def parse_string(string):
    """

    parse_string() -> Match

    Function returns an re.Match that contains groups that correspond to parts
    of the string. You can use that match to manipulate the string, such as by
    turning it into data or an object.
    """
    re = select_re(string)
    iterable = re.finditer(string)
    matches = list(iterable)

    if len(matches) != 1:
        c = "May be losing data"
        raise exceptions.OperationError(c)

    match = matches[0]
    return match

def replace(string, target, replacement):
    """

    replace() -> str

    Function replaces the target in the string
    """
    start, end = get_span(string, target)

    prefix = string[:start]
    suffix = string[end:]
    result = prefix + replacement + suffix

    return result

def replace_images(html, trace=True, um=None):
    """

    replace_images() -> str

    Function finds and replaces images on the page.
    """
    result = html
    matches = re_single.finditer(html)
    
    for match in matches:
        if trace:
            print(match.group())
            print(match.group(NAME))
            
        if match.group(NAME) == IMAGE:
            original = match.group()
            replacement = view2(original, um)
            if trace:
                print("replacing")
                print(replacement)
                print("\n\n")
                
            improved = replace(result, original, replacement)
            result = improved
        else:
            if trace:
                print("skip\n")

    return result

    # Figure out what to do with all the objects I make <-----------------------------------------------------
    # Potentially, I could make an object catalog. Catalog could be keyed by the
    # text of the object. If I match the text, then i can get the object. This
    # catalog would be the cache.
    #
    # I could also key it by span, but the thing I should remember is if I do
    # that, the span should be with respect to the original.
   
def select_re(html):
    """

    select_re() -> re

    Function returns the re that is most likely to process the html.
    """
    result = re_double
    if check_startend(html):
        result = re_single
        
    return result

def view2(string, um=None):
    """

    -> string

    Function returns a version of the input that Port. optimized for a human
    reader in command line.
    """
    result = string

    if check_element(string):
        match = parse_string(string)
        data = extract_data(match)
        obj = make_element(data)

        if um:
            url = None
            try:
                url = obj.link.get_url()
            except AttributeError:
                pass
            
            if url:
                ref = um.get_ref(url)
                obj.link.set_ref(ref)
        # I can generalize this to a set_ref(obj, um)
                
        result = obj.view()

    return result

# Testing

def _run_test1(links):
    """

    -> None

    Test checks whether flow works and if links with embedded images print in
    the way their class intends. 
    """    
    for link in links:
        data = link.get_data()
        view = view2(data)
        print(view)

def _run_test2(trace=True):
    import url_manager
    go_blue = url_manager.UrlManager()
    no_pics = replace_images(alt_html.ubs_body, trace=trace, um=go_blue)
    print(len(alt_html.ubs_body))
    print(len(no_pics))
    
    if trace:
        print(no_pics)

    result = alt_html.replace_links(no_pics, go_blue)
    print(len(result[0]))
    if trace:
        print(result[0])        

def _run_test(links):
    _run_test1(links)

## if __name__ == "__main__":
##    _run_test()
## cannot use this
    
# Tests:
# 1) check that images in links look right
# 2) check that I can replace all images in the html

# not necessary to have alt_html references here. though the way I have built
# this module, it is.




        
    
    
    
