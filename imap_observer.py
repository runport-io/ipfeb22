# IMAP observer
# (c) Port. Prerogative Club 2022
# Port. 2.0.
# Governed by GPL 3.0, unless agreed otherwise.

"""

Module defines a class for monitoring an email inbox. 
------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:
N/a

FUNCTIONS:
N/a

CLASSES:
IMAPObserver       Observes an inbox via IMAP.
------------------  ------------------------------------------------------------
"""

# Imports
# 1) Built-ins
# n/a

# 2) Port.
import observ2 as kit
import utilities

class IMAPObserver:
    """
    
    A class for monitoring emails you receive. Connects via IMAP. 

    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    
    FUNCTIONS:
    sign_in             connects to server, completes authentication
    sign_out            disconnects from server, destroys session

    get_messages        retrieves emails from server, returns messages
    get_events          retrieves emails from server, turns them into events

    make_event          makes an event from a message
    add_body            adds body to an event based on a message
    add_headline        adds a headline to an event based on a message
    add_timestamp       adds a timestamp to an event based on a message
    add_source          adds a source to an event based on a message
    add_original        adds the contents of the raw message
    flatten_event       turns event into a dictionary
    make_blank          creates a blank event

    set_position        establishes the most recent read message in the inbox
    ------------------  --------------------------------------------------------
    """

    def __init__(self, service=None, offset=None):
        self._service = service
        self._offset = offset
        self._session = None
        self._signed_in = False
        
    def activate(self, service=None, override=False):
        """

        self.activate() -> session

        Establishes a session with the service. Does not perform authentication.
        Uses instance settings if optional parameters are blank
        """
        if not service:
            service = self.get_service()
        else:
            service = self.set_service(service, override=override)

        session = kit.establish_session(service)
        self.set_session(session)
        return session
        # should probably do more here, actually sign in
        # select inbox


    def set_service(self, service, override=False):
        """

        IMAPObserver.set_service() -> None

        Records service on the instance. Raises error if you already defined
        the service, unless you set "override" to True.
        """
        utilities.set_with_override(self, "_service",
                                    service, override=override)

    def get_service(self):
        """

        IMAPObserver.get_service() -> string or None

        Returns service stored on instance.
        """
        return self._service

    def set_offset(self, offset, override=True):
        """

        IMAPObserver.set_offset() -> int

        Records the most recent email you read. Instance will start retrieving
        messages from this point by default in the future.
        """
        utilities.set_with_override(self, "_offset", offset, override=override)

    def get_offset(self, offset):
        """

        IMAPObserver.get_offset() -> int

        Returns offset for instance.
        """
        return self._offset

    def set_session(self, session, override):
        utilities.set_with_override(self, "_session", session, override=override)

    def get_session(self):
        return self._session
        
    def get_events(self, offset, count, flatten=False)
        """

        IMAPObserver.get_events() -> list

        Returns list of length "count" of Events that represent messages
        starting at the offset.
        """
        events = list()
        messages = self.get_messages(offset, count)
        for message in messages:
            event = self.turn_msg_into_event(message)
            if flatten:
                event = event.flatten()
            events.append(event)                

        return events
    
    def get_messages(self, offset, count):
        """

        IMAPObserver.get_messages() -> list

        Returns list of messages of length "count" that start at the offset.
        """
        messages = list()
        muids = self.get_muids(offset, count)

        for identifier in muids:
            message = self.get_message_by_muid(identifier)
            messages.append(message)

        return messages

    def get_message_by_muid(self, muid):
        session = self.get_session()
        message = kit.get_message_by_UID(session, muid)
        return message

    def get_serials(self, offset=0, count=None, trace=False):
        """

        IMAPObserver.get_serials() -> list

        Returns a list of strings that represent the UID for each message,
        starting with the "offset". The list has a length of "count".

        If "offset" is 0, then returns the ids for the first messages. If "count"
        is None, returns ids for all messages.
        """
        session = self.get_session()
        length = None

        if count:
            length = offset + count
        
        serials = kit.get_ids(session, length=length, trace=trace)

        # truncate
        serials = serials[offset:]
        
        return serials

    def get_muids(self, offset=0, count=None, trace=False):
        session = self.get_session()
        serials = self.get_serials(offset, count, trace)
        muids = kit.get_UIDs(session, serials)
        return muids

    def sign_in(self, guest, token=None):
        """

        IMAPObserver.sign_in() -> session

        Returns a session with authentication complete. Sets folder to argument.
        """
        session = self.get_session()
        if self.check_if_signed_in():
            pass
        else:    
            session = kit.authenticate(session, guest, token)
            self.set_session(session, overwrite=True)
            self._signed_in = True

    def check_if_signed_in(self):
        result = self._signed_in
        return result

    def sign_out(self):
        """

        IMAPObserver.sign_out() -> None

        Deauthenticates session. Deletes session reference in memory.
        """
        pass

class Welder:
    def __init__(self):
        pass

    def make_blank(self):
        """

        Welder.make_blank() -> event

        Returns an Event that's blank.
        """
        event = Event()
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
        # event.assign_id()
        # add body, timestamp, original
        # return

def extract_domain(email_address):
    """

    extract_domain(email_address) -> string

    Returns the contents of the email address after the "@". 
    """
    domain = ""
    at = email_address.find(constants.AT)
    if at == -1:
        memo = constants.AT + " not in " + email_address
        raise exceptions.ParsingError(memo)
    else:
        start = at + 1
        domain = email_address[start:]
        
    return domain
    
    
# figure out what to do with read vs unread
## right now i ignore that.
#
# should the get() routines advance the offset? may be. violates statelessness
# to some extent. on deactivate, should I get the offset?

# need a restore method. takes the offset and other metadate. can call it
# "load".

# on refactor:
# create a wrapper for message, or consider it.

# add a check() function, returning timestamp, offset, account, total messages,
# unread messages.

# add a clean_up() routine, to remove messages from memory once I have sent them
# over to controller. 

# need to refactor this somehow. retriever and builder.
# 
