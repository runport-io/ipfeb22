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
        # may be explicitly delete on override?
    else:
        raise exceptions.OverrideError

def set_with_force(*pargs, **kwargs):
    result = set_with_override(*pargs, **kwargs)
    return result

def add_attributes_to_skip(obj, name=None, value=None, override=False):
    if not name:
        name = constants.SKIP_ATTRIBUTES
    if not value:
        value = list()
    set_with_override(obj, name=name, value=value, override=override)

def get_lines(obj, include_header=True, width=None, indent=None):
    """

    get_lines() -> list
    
    Returns list of strings that represent the object.
    """
    lines = list()
    if not width:
        width = constants.STANDARD_WIDTH
    target_width = width
    
    if include_header:
        wip = str(type(obj))
        list.append(wip)
    
    skip = getattr(obj, constants.SKIP_ATTRIBUTES, [])
    
    items = None
    try:
        items = obj.__dict__.items()
        # Built-ins don't have a "__dict__" attribute
    except AttributeError:
        items = obj.items()
        # works for printing dictionaries

    if not items:
        line = str(obj)
        lines.append(line)
        
    else:
        for k, v in items:
            
            if k in skip:
                continue

            else:
                label = ""
                start = str(k)
                current_width = len(start)
                gap = target_width - current_width
                if gap > 0:
                    start = start + constants.SPACE * gap
                label = start
                lines.append(label)

                value = str(v)
                lines.append(value)
        
    return lines

def deepcopy(obj, recur=False):
    wip = obj.__dict__.copy()
    data = dict()
    # need recursion to deal with attributes that are themselves objects
    if recur:
        for k, v in wip:
            replacement = v
            try:
                replacement = v.copy()
            except AttributeError:
                pass
            data[k] = v
    
    new = obj.new(data=data)
    return new
    
    
    

