# serializer
# (c) Port. Prerogative Club 2022

"""

Module provides functions for compressing objects into primitives. 
------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:

FUNCTIONS:
flatten             turns object into dictionary
to_json             turns object into a JSON string      

CLASSES:
N/a
------------------  ------------------------------------------------------------

"""

# Built-ins
import json

# Port.
import constants

# Constants

# Functions
def flatten(obj):
    """

    flatten() -> dict()

    Function returns a copy of the object's attribute dictionary. Function
    ignores attributes listed at obj.SKIP_ATTRIBUTES.
    """
    result = dict()
    wip = dict()
    attrs = obj.__dict__.keys()
    wip = attrs.copy()
    skip = getattr(obj, constants.SKIP_ATTRIBUTES)
    for item in skip:
        wip.pop(item)

    result = wip
    return result

    # consider adding a recursion (if recur=true), walk all the attributes and
    # flatten them

def to_json(obj):
    """

    to_json() -> string
    
    Function returns a string in JSON format for the object.
    """
    result = ""
    flat = flatten(obj)
    result = json.dumps(flat)
    return result
  
    

    
        
