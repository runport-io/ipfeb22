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

    def get_events(self, offset, count, flatten=False)
        """

        IMAPObserver.get_events() -> list

        Returns list of length "count" of Events that represent messages
        starting at the offset.
        """
        events = list()
        messages = self.get_messages(offset, count)
        for message in messages:
            event = self.make_event(message)
            if flatten:
                event = event.flatten()
            events.append(event)                

        return events
    
    def get_session(self):
        return self._session
        
    def get_message_by_muid(self, muid):
        session = self.get_session()
        message = kit.get_message_by_UID(session, muid)
        return message

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

    def get_muids(self, offset=0, count=None, trace=False):
        session = self.get_session()
        serials = self.get_serials(offset, count, trace)
        muids = kit.get_UIDs(session, serials)
        return muids

    def get_offset(self, offset):
        """

        IMAPObserver.get_offset() -> int

        Returns offset for instance.
        """
        return self._offset

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

    def get_service(self):
        """

        IMAPObserver.get_service() -> string or None

        Returns service stored on instance.
        """
        return self._service

    def is_authenticated(self):
        result = self._signed_in
        return result

    def is_connected(self):
        pass

    def set_offset(self, offset, override=True):
        """

        IMAPObserver.set_offset() -> int

        Records the most recent email you read. Instance will start retrieving
        messages from this point by default in the future.
        """
        utilities.set_with_override(self, "_offset", offset, override=override)

    
    def set_service(self, service, override=False):
        """

        IMAPObserver.set_service() -> None

        Records service on the instance. Raises error if you already defined
        the service, unless you set "override" to True.
        """
        utilities.set_with_override(self, "_service",
                                    service, override=override)

    def set_session(self, session, override):
        utilities.set_with_override(self, "_session", session, override=override)

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

    def sign_out(self):
        """

        IMAPObserver.sign_out() -> None

        Deauthenticates session. Deletes session reference in memory.
        """
        pass

    
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
