# source
# (c) Port. Prerogative Club 2022

class Source:
    """

    Place where we record the chain of ownership for information. 
    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    publisher           Entity? a string and a number
    observer            Entity? a string and a number
    other
    hook
    
    FUNCTIONS:
    set_observed()
    set_recorded()
    set_published()
    set_other()
    ------------------  --------------------------------------------------------
    """
    pass

# set_source if id is wrong, should generate a collision?
# file location? visible? probably not? may be shoudl be abstracted? but i
# should be able to retrieve it sometimes.
# establish chain of ownership. each record in chain is from, to, transaction.
# include a cost?
