# Utilities
# (c) Port. Prerogative Club 2022

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
    if not getattr(obj, name):
        # attribute not defined
        safe = True
    if safe or override:
        setattr(obj, name, value)
    else:
        raise exceptions.OverrideError

def pretty_print_smarter():
    pass
    # placeholder for walking the attr tree

def add_attributes_to_skip():
    pass

def add_attributes_to_print():
    pass

