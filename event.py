# Copyright Port. Prerogative Club ("the Club")
#
# 
# This file is part of Port. 2.0. ("Port.")
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

"""

Module defines the Event class. Events record observations in time.

------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:

FUNCTIONS:

CLASSES:
Event               Object organizes information in time.
------------------  ------------------------------------------------------------
"""

# Imports
# 1) Built-ins

# 2) Port.
import utilities as up

from number import Number
from source import Source
from textfield import TextField
from timestamp import TimeStamp

class Event:
    """
    
    Events record observations at one or more points in time.

    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    number              instance of Number
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
    def __init__(self, headline=None, body=None, source=None):
        self.body = TextField(body)
        self.headline = TextField(headline)
        self.number = Number()
        self.source = Source()
        self.timestamp = TimeStamp()
        self._raw = None

        if source:
            self.set_source(source)

    def __str__(self):
        string = up.make_string(self)
        return string
    
    @classmethod
    def from_flat(cls, data):
        """

        Event.from_flat(data) -> Event

        Class method.

        Method returns an instance of Event populated based on the information
        in the parameter. Method delegates to the constructor of each attribute.
        """
        # placeholder code, rewrite.
        new = cls()
        
        # add logic to skip attrs?
        # update for non-object based elements? somehow? e.g. raw?
        
        for attr, value in new.__dict__:
            detail = data[attr]
            new.attr = value.from_flat(detail)

        return new
    
    def get_body(self):
        """

        Event.get_body() -> obj

        Method returns the content of instance.body.
        """
        result = self.body.get_content()
        return result

    def get_headline(self):
        """

        Event.get_headline() -> obj

        Method returns the content from the instance's headline. 
        """
        result = self.headline.get_content()
        return result

    def get_number(self):
        """

        Event.get_number() -> obj

        Method delegates to instance.number. Method returns the results of
        number.get_number() for the instance.
        """
        result = self.number.get_number()
        return result
    
    def get_lines(self, omit_raw=True):
        """

        Event.get_lines(omit_raw=True) -> list

        Method returns a list of strings that represent the instance. Result
        omits raw content. 
        """
        alt = self.__dict__.copy()
        
        if omit_raw:
            alt.pop("_raw")
            
        lines = up.get_lines(alt)
        return lines
    
    def get_source(self):
        """

        Event.get_source() -> obj

        Method returns the instance sender. Method delegates to instance.source.
        """
        source = self.source.get_sender()
        return source

    def get_summary():
        """

        Event.get_summary() -> string

        Method returns a string that summarizes the instance. The string
        truncates the body of the event.
        """
        pass
        # placeholder for abbreviated representation
        #
        # returns: event name
        # event headline
        # event number
        # event namespace
        # event source
        # event date
        # first couple lines of event body?
        # how is this different than just print() or print_short()?

    def set_body(self, content):
        """

        Event.set_body(content) -> None

        Method records the argument as the body of the instance.
        """
        self.body.set_content(content)

    def set_headline(self, content, force=False):
        """

        Event.set_headline(content) -> None

        Method records the argument as the headline of the instance.
        """
        self.headline.set_content(content, force=force)

    def set_number(self):
        """

        Event.set_number() -> uuid

        Method sets the event's number. Method uses the source's number as the
        namespace. 
        """
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

    def set_source(self, source):
        """

        Event.set_source() -> None

        Method passes the argument to instance.source for processing and
        recording.
        """
        self.source.set_sender(source)
        
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

# Testing
e1 = Event()
print("e1: ")
print(e1)
print("\n")

print("e2: ")
e2 = Event(headline="I got a cappucino.", source="me")
print(e2)
print("\n")
