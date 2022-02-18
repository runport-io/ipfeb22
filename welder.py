
import event as e

class Welder:
    def __init__(self):
        pass

    def make_blank(self):
        """

        Welder.make_blank() -> event

        Returns an Event that's blank.
        """
        event = e.Event()
        return event
    
        # consider adding headline here.
        # consider adding a timestamp of some sort here too.
        ## should be in the Event constructor

    def add_headline(self, msg, event, overwrite=False):
        """

        Welder.add_headline() -> event

        Returns an event populated with a headline.
        """
        headline = msg.get(EMAIL_LIB_SUBJECT)
        event.set_headline(headline, overwrite=overwrite)
        return event

    def add_body(self, event, msg):
        pass

    def add_original(self):
        pass

    def add_source(self, msg, event, overwrite=False):
        email_address = msg.get(EMAIL_LIB_FROM)
        source = extract_domain(email_address)
        event.set_source(source, overwrite)
        
        # event.log.record(something)
        # when do i assign the id to the event?? probably after i set the source
        # and the headline

        # ideally, source would be an entity, may be? linked through a URL?
        
    def record_receipt(self, msg, event, overwrite=False):
        timestamp = msg.get(EMAIL_LIB_DATE)
        # convert into what? integer?
        event.record_receipt(timestamp)
        return event

    def make_event_from_msg(self, msg):
        event = self.make_blank()
        event = self.add_source(msg, event)
        event = self.add_headline(msg, event)
        event = self.add_body(msg, event)
        # event.assign_id()
        # add timestamp, original
        # return

import pickle
file_name = "emails.pkl"
f = open(file_name, "rb")
results = pickle.load(f)
email0 = results[0]
w = Welder()
event = w.make_event_from_msg(email0)

