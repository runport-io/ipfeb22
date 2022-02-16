# Utilities
# (c) Port. Prerogative Club 2022

import constants
import exceptions


def pretty_print(obj, glue=None):
    if not glue:
        glue = constants.NEW_LINE
        
    view = ""
    lines = list()
    try:
        lines = obj.get_lines()
        # ideally would try through getattr
    except AttributeError:
        pass
    if lines:
        view = glue.join(lines)
        print(view)
    else:
        # print system default
        print(obj)

def set_with_override(obj, name, value, override=False):
    safe = False
    if not getattr(obj, name, None):
        # attribute not defined
        safe = True
    if safe or override:
        setattr(obj, name, value)
    else:
        raise exceptions.OverrideError

def add_attributes_to_skip(obj, name=None, value=None, override=False):
    if not name:
        name = constants.SKIP_ATTRIBUTES
    if not value:
        value = list()
    set_with_override(obj, name=name, value=value, override=override)

# def print_smartly(obj):
#   lines = list()
#   skip = getattr(obj, constants.SKIP_ATTRIBUTES)
#   for attr, value in obj.__dict__:
#       if attr not in skip:
#           make a line, add to lines
#           # could use the pretty printing library
    

