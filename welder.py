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

Module defines a class for packaging emails into events
------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:
N/a

FUNCTIONS:
class Welder        What do you say when you turn an email into an event?*
------------------  ------------------------------------------------------------
"""

# Imports
# 1) Built-ins
# n/a

# 2) Port.
import constants
import event as e
import exceptions
import observ2
import parser2
import parser_for_email_body

# 3) Data
# N/a

# 4) Functions
class Welder:
    def __init__(self):
        pass

    def add_body(self, msg, event, overwrite=False):
        """

        Welder.add_body(msg, event, overwrite=False) -> event

        Method adds the message body to the event. Method modifies event in
        place.
        """
        raw_body = observ2.get_body(msg)
        event.body.set_raw(raw_body)
        body, data = parser_for_email_body.parse_body(raw_body)
        event.set_body(body)
        event.body.set_data(data)
        
        return event
    
    def add_headline(self, msg, event, force=False):
        """

        Welder.add_headline(msg, event, force=False) -> event

        Method adds the message subject as the headline of the event. Method
        overwrites any existing headline if you set "force" to True, and throws
        an OverrideException otherwise. 
        """
        headline = msg.get(constants.EMAIL_LIB_SUBJECT)
        existing = event.get_headline()
        
        if force or not existing:
            event.set_headline(headline)
        else:
            raise exceptions.OverrideException
            
        return event

    def add_original(self):
        pass

    def add_source(self, msg, event, force=False):
        """

        Welder.add_source(msg, event, force=False) -> event

        Method records the sender of the message on the event. Method modifies
        the event in place. 

        If you set "overwrite" to True, method will record the source regardless
        of whether the event already has a source. Otherwise, method will only
        record the source if the existing source is blank.
        """
        email_address = msg.get(constants.EMAIL_LIB_FROM)
        source = parser2.extract_domain(email_address)
        existing = event.get_source()
        
        if force or not existing:
            event.set_source(source)
        else:
            raise exceptions.OverrideError
        
        return event
        
        # event.log.record(something)
        # when do i assign the id to the event?? probably after i set the source
        # and the headline

        # ideally, source would be an entity, may be? linked through a URL?

    def make_blank(self):
        """

        Welder.make_blank() -> event

        Method returns an instance of Event. 
        """
        event = e.Event()
        return event
    
        # consider adding headline here.
        # consider adding a timestamp of some sort here too.
        ## should be in the Event constructor

    def make_event_from_msg(self, msg):
        """

        Welder.make_event_from_msg(msg) -> Event

        Method creates an event based on the message. 
        """
        event = self.make_blank()
        event = self.add_source(msg, event)
        event = self.add_headline(msg, event)
        event = self.add_body(msg, event)
        # event.assign_id()
        # add timestamp, original
        
        return event
    
    def record_receipt(self, msg, event, overwrite=False):
        """

        Welder.record_receipt(msg, event, overwrite=False) -> event

        Method timestamps the event with the date from the message. Method
        modifies the event in place.
        """
        timestamp = msg.get(constants.EMAIL_LIB_DATE)
        # convert into what? integer?
        event.record_receipt(timestamp)
        return event

# Testing
def run_test():    
    w = Welder()
    
    import pickle
    file_name = "emails.pkl"
    f = open(file_name, "rb")
    messages = pickle.load(f)

    events = list()
    for msg in messages:
        event = w.make_event_from_msg(msg)
        events.append(event)

        body = event.get_body()
        print("Event:   ", event)
        print("Body:    ",)
        print(body)
        print("\n\n")
    
    result = (messages, events)
    return result

if __name__ == "__main__":
    run_test()

#*"Well done."
