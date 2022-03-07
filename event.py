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
Event               Object organizes information about a moment in time.
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
    
    Events describe a moment in time. Events hash as their Number.

    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    body                instance of TextField, tracks the body
    headline            instance of TextField, tracks the headline
    number              instance of Number
    source              instance of Source, tracks where the event came from       
    timestamp           instance of TimeStamp, shows when event took place  <---------------------------- move to source

    FUNCTIONS:
    from_flat()         CLASS METHOD; generates an instance from a JSON object
    flatten()           turns instance into a JSON object

    get_body()          returns the body of the instance
    get_headline()      returns the headline for the instance
    get_lines()         returns a list of strings that represent the instance
    get_number()        returns the id number for the instance
    get_raw()           returns the data used to construct the instance, if any              
    get_word()          returns a one-word summary of the instance

    set_body()          records text to body
    set_headline()      records text to headline
    set_number()        assigns number to the event #<-------------------------------------------------------change name
    set_raw()           as
    set_source()        sets instance source #<--------------------------------------------------------------------remove
    ------------------  --------------------------------------------------------
    """
    def __init__(self, headline=None, body=None, source=None):
        self.body = TextField(body)
        self.headline = TextField(headline)
        self.number = Number()
        # ideally, this should be a product of all the other attributes' numbers.
        self.source = Source()
        # received_by: id_card (name, parent, id, date, signature) ## e.g., ilya's gmap obs
        # received_from: id_card
        # recorded_by: (x) ## ilya's controller
        # recorded_in: (y) ## ilya's storage x
        # pubished_by: (z) and so on
        # source should really be a list
        self.timestamp = TimeStamp()
        self._raw = None
        # not clear why this is necessary?
        # may be replace with data.
        # data.raw, data.feedback
        
        if source:
            self.set_source(source)
            #<------------------------------------------------------------------------------------------------delegate down

    def __hash__(self):
        result = hash(self.get_number())
        if not result:
            raise exceptions.NumberError("No number defined for object")
        return result
    
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
        #<--------------------------------------------------------------------------------------------------------------------------------------------------------
        # attach the data to raw

    def flatten(self):
        """

        -> dict()

        Method returns a dictionary of primitives. 
        """
        pass
        # does something or other here.
        # should go through each attribute it and flatten it.
        # 
    
        #<--------------------------------------------------------------------------------------------------------------------------------------------------------
    
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
        # consider moving this to camera? keeps this object lighter.  <---------------------------------------------------------------
    
    def get_number(self):
        """

        Event.get_number() -> obj

        Method delegates to instance.number. Method returns the results of
        number.get_number() for the instance.
        """
        result = self.number.get_number()
        return result

##    def get_raw(self):
##        """
##
##        get_raw () -> obj
##
##        Method returns the raw version of the event. You get what you put in. 
##        """
##        result = self._raw
##        return result
##        # unclear if this is valuable <---------------------------------------------------------------
        
    def get_timestamp(self):
        """

        get_timestamp() -> int or None

        Method returns the time of receipt for the instance.
        """
        result = self.timestamp.time_of_receipt
        return result
       
    def get_word(self):
        """

        get_word() -> string

        Method returns a string that describes the instance. Looks to brands by
        default, then headline if no brand is available. 
        """
        ranked_brands = self.body.index.get_ranked()
        if ranked_brands:
            word = ranked_brands[0][0]
        else:
            headline = self.get_headline()
            words = headline.split()
            word = words[0]
            
        return word
    
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

    def set_number(self, force=False):
        """

        Event.set_number() -> uuid

        Method sets the event's number. Method uses the source's number as the
        namespace. 
        """
        if self.get_number():
            if not force:
                c = "Number exists."
                raise exceptions.OverrideError(c)
    
        namespace = self.source.number.get_number()
        # source should get its number from observer + string
        name = self.headline.get_content()
        number = self.number.set_number(namespace, name)
        # could refactor this as: get_number, assign_number(number, force)

        return number

    def set_raw(self, data, force=False):
        """

        set_raw() -> None

        Method records the data in the instance. You will get an OverrideError
        if the instance already has raw data, unless you set "force" to True.
        """
        up.set_with_override(self, "_raw", data, override=force)

    def set_source(self, source):
        """

        Event.set_source() -> None

        Method passes the argument to instance.source for processing and
        recording.
        """
        self.source.set_sender(source)

# should move the timestamp to source, i think. it is on the source that i
# record when i get something, and where i record that info - if its on the
# observer, or something else, is logic that's not obvious from here.
# i can retain event.get_number() and delegate accordingly. 

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

def run_test3():
    container_a = {e1, e2}
    container_b = {e2, "a"}
    intersection = container_a & container_b
    print(intersection)

def run_test4():
    result = e2.flatten()
    print(result)

def run_test5():
    pass
    # get some real events and flatten those

def run_test6():
    pass
    # get the flat events from 5, expand each one
    # do something

if __name__ == "__main__":
    run_test3()
