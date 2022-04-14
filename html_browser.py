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

import html_elements.element as element
import html_elements.image as image


# 3) Constants
re_double = alt_html.re_element2
re_single = re.compile(r'(?P<element>'
                       r'(?P<start><(?P<name>\b\w+\b)(?P<attrs>.*?)>))',
                       re.DOTALL)

ARROW_LEFT = "<"
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

def make_element(match):
    """
    -> obj
    """
    name = match.group(NAME)
    processor = element.Element
    if name in PROCESSORS:
        processor = PROCESSORS[name]

    result = processor(match)
    return result

def make_image(span, page):
    """

    -> image
    
    """
    result = Image(span)
    url = result.get_source()
    
    ref = page.um.get_ref(url)
    result.link.set_ref(ref)

    return result
    
def parse_element(string):
    """

    -> element

    Function returns an object that represents the string and supports the
    element interface.
    """
    re = select_re(string)
    iterable = re.finditer(string)
    matches = list(iterable)

    if len(matches) != 1:
        c = "May be losing data"
        raise exceptions.OperationError(c)

    match = matches[0]
    element = make_element(match)

    return element   

def select_re(html):
    """

    -> re

    Function returns the re that is most likely to process the html.
    """
    result = re_double
    if check_startend(html):
        result = re_single
        
    return result

def view2(string):
    """

    -> string

    Function returns a version of the input that Port. optimized for a human
    reader in command line.
    """
    result = string

    if check_element(string):
        element = parse_element(string)
        tag = make(element)
        result = tag.view()

    return result

# Refactor:
# parse_element returns a match
# extact_data(match) -> dict
# make_element(dict) -> obj

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

def _run_test(links):
    _run_test1(links)

## if __name__ == "__main__":
##    _run_test()
## cannot use this
    
    
# Tests:
# 1) check that images in links look right
# 2) check that I can replace all images in the html

# not necessary to have alt_html references here.


        
    
    
    
