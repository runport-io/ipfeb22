# blog
# (c) Port. Prerogative Club 2022

class Blog:
    """
    Where we store a record of changes.
    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    contents            list of entries
    hook
    
    FUNCTIONS:
    add_entry           requires timestamp, content, author
    get_log()
    ------------------  --------------------------------------------------------
    pass

# consider whether to support introspecvtion into authors out of the box.
# YAGNI. test: add entry, content, author. check contents length. should
# increase by 1. remove_entry should fail explicitly.
