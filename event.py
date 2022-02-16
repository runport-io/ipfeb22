# event
# (c) Port. Prerogative Club 2022

# imports
# from . import header
# from . import content
# from . import timestamp
# from . import log

"""

Module defines the Event class. Events record observations in time.

------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:

FUNCTIONS:

CLASSES:
Event               Organizes information detected by observers or created
                    elsewhere in Port.
------------------  ------------------------------------------------------------
"""

class Event:
    """
    
    Events record observations at one or more points in time.

    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    ATTRS
    number              instance of Number? 
    source              instance of Source, tracks where the event came from
    brands              instance of Brands, tracks brands mentioned in event.
    headline            instance of TextField, tracks the headline
    body                instance of TextField, tracks the body
    timestamp           instance of TimeStamp, shows when event took place? this may not be necessary. kind of duplicates log, because log can be a list of tuples (time, note)
    blog                instance of Blog, tracks modifications to the object.
    
    FUNCTIONS:
    copy                returns deep copy of event
    print_contents      returns a string that looks nice when you print it
    email_from          (cls) generates an instance of the class from an email
    [json_to             returns a JSON object 
    json_from           (cls) generates an instance of the class from JSON]
    get_fields          returns list of fields for instance
    get_field_names     returns list of field names for instance
   
    ------------------  --------------------------------------------------------
    """
    ATTRS = list()

    @classmethod
    def from_email(cls, email):
        new = cls()

        #
        headline = email.get(HEADLINE)
        new.set_headline(headline)

        return new

    @classmethod
    def from_flat(cls):
        pass
    
    def __init__(self, headline=None, body=None):
        self.body = TextField(body)
        self.headline = TextField(headline)
        self.source = Source()
        self.timestamp = TimeStamp()

        # self.number.assign()
        # # or something like that

        # when creating an instance:
        # if headline:
        #   that's the name for the number
        #   assign number on that basis
        #   namespace should be the source
        #   the source's namespace should be the observer
        #   ## can also assign id based on full body
        
    def get_fields(self, decouple=False):
        """
        event.get_fields() --> list
        
        Returns list of fields. Items in list link to contents on the event
        unless "Decouple" is True. 
        """
        pass

    def get_field_names(self):
        """
        Returns list of field names
        """
        pass
        
    def walk_content():
        pass

    def get_card():
        pass
        # returns: event name
        # event headline
        # event number
        # event namespace
        # event source
        # event date
        # first couple lines of event body?
        # how is this different than just print() or print_short()?
    
# tests
# make event
# send to json
# get json result, make event again
# compare


