# textfield
# (c) Port. Prerogative Club 2022

"""

Module defines the TextField class. A TextField holds a string and information
about that string.

------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:

FUNCTIONS:

CLASSES:
TextField           Container for storing text and information about the text.
------------------  ------------------------------------------------------------
"""

class TextField:
    """
    
    A TextField stores a string and information about its language. The idea is
    to simplify reading in the future. 

    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    
    content             formatted
    language            placeholder, if "" then American English
    raw                 placeholder
    encoding            placeholder
    in_observer
    in_source
    hook                instance of a Hoo.k, to go one level up in the hierarchy
    
    FUNCTIONS:
    copy                returns deep copy of event
    print_contents      returns a string that looks nice when you print it
    json_to             returns a JSON object 
    json_from           (cls) generates an instance of the class from JSON
    check_equivalence   placeholder for exact match
    check_similarity    placeholder for fuzzy match
    ------------------  --------------------------------------------------------
    """
    pass

# tests:
# pass in a headline
# get the version without newlines, get the version with nrewlines
# to json and from json should return the same thing, more or less.
# should eventually build the EQ thing? if content == then same?
# most likely to break: assign permanent (should clear out the temp id?);
# ## i get this thing from the observer, does the observer number it? yes.
# ## do i keep the observer-level id? I should probably. I should also record the UID
# ## within the observer's topic, here the UID. What happens if I reshare this?
# ## i think then the sender sends me their thing with their own numbering?
# hook works only when the whole thing is built








