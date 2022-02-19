
# Imports
# 1) Built-ins
# n/a

# 2) Port.
import constants
import event as e
import observ2
import parser2

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
        body = observ2.get_body(msg)
        event.set_body(body)
        return event
    
    def add_headline(self, msg, event, overwrite=False):
        """

        Welder.add_headline() -> event

        Returns an event populated with a headline.
        """
        headline = msg.get(constants.EMAIL_LIB_SUBJECT)
        event.set_headline(headline, overwrite=overwrite)
        return event

    def add_original(self):
        pass

    def add_source(self, msg, event, overwrite=False):
        """

        Welder.add_source(msg, event, overwrite=False) -> event

        Method records the sender of the message as the source of the event.
        Method modifies event in place before returning it to you. 
        """
        email_address = msg.get(constants.EMAIL_LIB_FROM)
        source = parser2.extract_domain(email_address)
        existing = event.get_source()
        if existing and not overwrite:
            pass
        else:
            event.set_source(source, overwrite=overwrite)
        
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
        # return
    
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

import pickle
file_name = "emails.pkl"
f = open(file_name, "rb")
results = pickle.load(f)
email0 = results[0]
w = Welder()
event = w.make_event_from_msg(email0)
