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
import time

# 2) Port.
import constants

import event as e
import exceptions
import observ2
import parser2
import parser_for_dates
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
        cleaned = parser2.clean_string(headline)
        event.set_headline(cleaned, force=force)
        return event

    def add_headline_alt(self, msg, event, force=False):
        headline = msg.get(constants.EMAIL_LIB_SUBJECT)
        charsets = msg.get_charsets()
        

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
        existing = event.source.get_sender()
        
        if force or not existing:
            event.set_source(source)
        else:
            raise exceptions.OverrideError
        
        return event
        
        # event.log.record(something)
        # when do i assign the id to the event?? probably after i set the source
        # and the headline

        # ideally, source would be an entity, may be? linked through a URL?

    def add_timestamp(self, msg, event, time_number=None):
        """

        add_timestamp() -> event

        Method extracts the time of receipt from the message ("Date"), converts
        it into a float, and records it on the event. You are changing the
        event in place.
        """
        if time_number is None:
            date = msg.get("Date")
            # date is string
            time_tuple = parser_for_dates.convert_to_tuple(date)
            time_number = time.mktime(time_tuple)
        event.timestamp.set_receipt(time_number)
        return event

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
        event = self.add_timestamp(msg, event)
        # event.assign_id()
        
        return event
    
    def make_events(self, messages):
        events = list()
        for message in messages:
            event = self.make_event_from_msg(message)
            events.append(event)
    
        return events
        
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

    def z_parse_body_by_line(self, msg, parser, trace=False):
        # for parsing html
        parser.reset()
        # to avoid surprises

        result = list()
        
        body = msg.get_body()
        # EmailMessage object

        body_string = body.as_string()
        # long string, sometimes breaks parser.

        body_lines = body_string.splitlines()
        if trace:
            print("Number of lines in body: ", len(body_lines))
            print("\n")

        for raw_line in body_lines():
            output = ""
            try:
                output = parser.feed(raw_line)
            except SomeTypeofException:
                pass
            if output:
                result.append(output)

        # go through lines, skip ones that we can't figure out

        return result

    def z_check_body(self, msg):
        """

        z_check_body() -> bool

        Returns True if body has plain text, false otherwise.
        """
        result = False
        
# Testing
_file_name = "emails.pkl"

def _get_messages(file_name):
    import pickle
    f = open(file_name, "rb")
    messages = pickle.load(f)

    return messages
  
def _run_test(messages):    
    w = Welder()
    result = list()
    for msg in messages:

        event = w.make_event_from_msg(msg)
        result.append(event)
        
        body = event.get_body()
        print("Headline:   ", event.get_headline())
        print("Body:    ",)
        print(body)
        print("\n\n")
    
    return result

def _main():
    messages = _get_messages(_file_name)
    events = _run_test(messages)

if __name__ == "__main__":
    _main()

#*"Well done."
