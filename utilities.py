# Copyright Port. Prerogative Club ("the Club")
#
# 
# This file is part of Port. 2 ("Port.")
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
import os
import webbrowser

# 2) Port.
import constants
import exceptions

def add_attributes_to_skip(obj, name=None, value=None, override=False):
    if not name:
        name = constants.SKIP_ATTRIBUTES
    if not value:
        value = list()
    set_with_override(obj, name=name, value=value, override=override)

def clear_screen():
    """

    clear_screen() -> None

    Function clears the screen.
    """
    # credit to link {1} 
    command = "cls"
    if os.name != "nt":
        command = "clear"
    os.system(command)

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
    
    new = obj.from_flat(data=data)
    return new

def flatten(obj, recur=False):
    result = dict()
    wip = dict()
    wip.update(obj.__dict__)

    # remove attributes we don't like
    skip_attrs = getattr(obj, SKIP)
    for attr in skip_attrs:
        wip.pop(attr)

    if recur:
        # walk the attributes and flatten them
        for key, value in wip.items():
            f = getattr(value, "flatten")
            adj_value = f()
            if not f:
                adj_value = flatten(value, recur=True)
            result[k] = adj_value

    return result
   

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
        header = str(type(obj))
        lines.append(header)
    
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

def make_string(obj, glue=None):
    """

    make_string(obj) -> string

    Function returns a view of the object. Function attempts to call
    obj.get_lines() and falls back on str if the object does not define that
    routine.
    """
    result = ""
    lines = list()

    # attempt to retrieve the view defined by the object
    try:
        lines = obj.get_lines()
    except AttributeError:
        pass

    # if we got lines, put them together, otherwise, return the system view
    if lines:
        if not glue:
            glue = constants.NEW_LINE
        result = glue.join(lines)
    else:
        result = str(obj)
        
    return result

def open_link(url, new_tab=True):
    """

    open_link() -> bool

    Function opens the url in the browser. If you turn off "new_tab", you will
    see the results in the window you have open.
    """
    result = False
    if new_tab:
        result = webbrowser.open_new_tab(url)
    else:
        result = webbrowser.open(url, new=0)

    return result    
    
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

def set_with_force(*pargs, **kwargs):
    """

    set_with_force(*pargs, **kwargs) -> obj

    Wrapper for set_with_override. Returns result from that function.
    """
    result = set_with_override(*pargs, **kwargs)
    return result

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



     

# Links
# 1: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
