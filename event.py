# Event
# (c) Port. Prerogative Club 2022

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

# Imports
# 1) Built-ins

# 2) Port.
import utilities as up

from source import Source
from textfield import TextField

# Functions
class Event:
    """
    
    Events record observations at one or more points in time.

    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    number              instance of Number? 
    source              instance of Source, tracks where the event came from
    brands              instance of Brands, tracks brands mentioned in event.
    headline            instance of TextField, tracks the headline
    body                instance of TextField, tracks the body
    timestamp           instance of TimeStamp, shows when event took place? this may not be necessary. kind of duplicates log, because log can be a list of tuples (time, note)
    
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
    @classmethod
    def from_flat(cls):
        pass

    def __init__(self, headline=None, body=None):
        self.body = TextField(body)
        self.headline = TextField(headline)
        self.source = Source()
        self.timestamp = TimeStamp()
        self._raw = None

        # self.number.assign()
        # # or something like that

        # when creating an instance:
        # if headline:
        #   that's the name for the number
        #   assign number on that basis
        #   namespace should be the source
        #   the source's namespace should be the observer
        #   ## can also assign id based on full body

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

    def set_headline(self, headline):
        self.headline.set_content(headline)

    def get_headline(self):
        return self.headline.get_content()

    def set_source(self):
        pass

    def set_body(self, string):
        self.body.set_content(string)

    def get_body(self):
        return self.body.get_content()
    
    def get_source(self):
        source = self.source.get_publisher()
        return source
        # source is updates@nytimes.com
        #   i have to match that to an entity called NYTimes
        #   is it also the reporter?
        #   is it the online edition?

    def get_lines(self):
        alt = self.__dict__.copy()
        alt.pop("_raw")
        lines = up.get_lines(alt)
        return lines


    def __str__(self):
        string = up.make_string(self)
        return string   
    
    def get_number(self):
        return self.number.get_number()
        
    def set_number(self):
        
        namespace = self.source.number.get_number()
        # source should get its number from observer + string
        name = self.headline.get_content()
        number = self.number.set_number(namespace, name)

        return number
        # or can have the event be the product of source and whatever. the problem
        # there is that the id gets really long.
        # I could write some functions that take a number and convert it into a
        # base 64 or base 85 integer. that shrinks them a lot. then i would have
        # a way to trace inheritance, and would have product = descendant, and
        # that kind of stuff.
    
    # can experiment with the number approach later.
    # number approach:
    # generate an id, randomly, or something like that. or based on a seed. either alone,
    # or in a namespace. 
    # multiply the id by the inheritance tree.
    # voila

# tests
# make event
# send to json
# get json result, make event again
# compare


