#Parser

# Imports
# 1) Built-ins
import re

# 2) Port.
from . import element
from . import image

# 3) Constants
re_double = re.compile(r'(?P<element>'
                        r'(?P<start><(?P<name>\b\w+\b)(?P<attrs>.*?)>)'
                        r'(?P<data>.*?)'
                        r'(?P<end></(?P=name)>))',
                        re.DOTALL)

re_single = re.compile(r'(?P<element>'
                       r'(?P<start><(?P<name>\b\w+\b)(?P<attrs>.*?)>))',
                       re.DOTALL)

ARROW_LEFT = "<"
IMAGE = "img"
GROUP_NAME = "name"

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
    name = match.group(GROUP_NAME)
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
    """
    re = select_re(string)
    matches = re.findall(string)

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


        
    
    
    
