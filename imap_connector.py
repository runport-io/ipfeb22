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


# Imports

# 1) Built-ins
from email import policy
from email.parser import BytesParser

# 2) Port.
import constants
import observ2

# 3) Data
ALL = "ALL"
BATCH = 10
READ_ONLY = True
STANDARD_OFFSET = -40

Z_PARSER = BytesParser(policy=policy.default)

# 4) Functions
class ImapConnector:
    def __init__(self, url, guest, batch=BATCH):
        self._account = guest
        self._offset = STANDARD_OFFSET
        self._service = url
        self._session = None

    def check_unread(self):
        # get count
        # subtract offset?
        # probably want to get the uids for those? or not really?
        # return result?
        pass
    
    def connect(self, token):
        """

        ->
        
        Function returns the number of messages in the folder.
        """
        self._session = observ2.establish_session(self._service)
        status = self._session.login(self._account, token)
        print(status)
        count = self.count_messages()
        
        return count

    def count_messages(self, folder=constants.INBOX):
        """

        -> int
        
        Function returns the number of messages in the current folder. 
        """
        response = self._session.select(folder, readonly=READ_ONLY)
        count_string = unpack_response(response)
        result = int(count_string)
        return result

    def disconnect(self):
        pass

    def get_message(self, uid):
        """

        -> returns message obj
        
        """
        message = observ2.get_message_by_UID(self._session, uid)
        return message

    def get_message_content(self, uid):
        """

        get_message_content() -> bytestring
        
        """
        session = self._session
        code, data = session.uid(constants.FETCH, uid, constants.RFC822)
        response = data[0]
        command = response[0]
        content = response[1]

        return content

    def make_message(self, content, parser=Z_PARSER):
        message = parser.parsebytes(content)
        return message

    def get_message_alt(self, uid):
        """
        -> EmailMessage

        """
        content = self.get_message_content(uid)
        message = self.make_message(content)
        return message

    def get_messages(self, offset=None, count=BATCH, trace=False):
        """

        Function returns a list of messages of up to length count, starting at
        the offset. You can use negative offsets.
        """
        messages = list()
        if offset is None:
            # I want to keep the data if offset=0
            offset = self.get_offset()
            
        uniques = self.refresh(offset, count, increment=True)
        for uid in uniques:
            message = self.get_message_alt(uid)
            messages.append(message)
        
        return messages

    def get_new(self):
        pass
        # checks new, returns news

    def get_offset(self):
        result = self._offset
        return result

    def increment_offset(self, number):
        new = self.get_offset() + number
        self.set_offset(new)

    def refresh(self, offset, count, increment=True):
        """

        -> list

        Return a list of uniques for emails after the offset
        """
        serials = self._get_serials()
        # returns all serials

        positioned = serials[offset:]
        sized = positioned[:count]
        
        uniques = self._get_uniques(sized)
        # Think about storing uniques, or storing a map of the uniques or
        # something? map is: serial: unique, serial: unique; omit serials where
        # unique is last unique plus serial - last serial. The purpose of this
        # map would be to figure out what's going on if get new messages?

        if increment:
            length = len(uniques)
            self.increment_offset(length)
        
        return uniques

    def set_offset(self, number):
        self._offset = number

    def _get_serials(self, trace=False):
        """

        _get_serials() -> list

        Function returns a list of strings for all of the messages in the inbox.
        You have to use strings to pass in ids.       
        """
        response = self._session.search(None, ALL)
        serial_string = unpack_response(response)
        serials = serial_string.split()
        # string looks like this: '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16',
        # consists of integers separated by spaces.
        
        return serials

    def _get_uid(self, serial_number):
        uids = observ2.get_UIDs(self._session, [serial_number])
        return uids[0]

    def _get_uniques(self, serials):
        result = list()
        for serial in serials:
            unique = self._get_uid(serial)
            result.append(unique)

        return result

def unpack_response(response):
    """

    unpack_response() -> string

    Function expects a response in the form of ("resp_code", [b'blah blah']). 
    You get the string back, but still need to parse it.
    """
    resp, list_of_one_bytestring = response
    bytestring = list_of_one_bytestring[0]
    string = bytestring.decode()
    return string
    
# Testing
url = constants.GMAIL
def _run_test1(url):
    guest, token = observ2.load_credentials()
    # The EmailObserver should pass those in. The Controller should send them
    # to EmailObserver.
    ct1 = ImapConnector(url=url, guest=guest)
    count = ct1.connect(token)
    print("Count: ", count)

    return ct1

def _run_test2(count, offset, connector): 
    uniques1 = connector.refresh(offset=offset, count=10)
    print("Uniques: ", uniques1)
    
    messages = connector.get_messages()
    print(messages)
    
    return messages

def _run_test(url, offset=-30):
    connector = _run_test1(url)
    messages = _run_test2(count=10, offset=-30, connector=connector)
    return messages

if __name__ == "__main__":
    _run_test(url)

# figure out how to retrieve in batches only.
# need a routine to go from uid to serial, so i can start looking up from there.
#   then on refresh, i check what position the last unique is in, and get new
#   from there ids from beyond that position.

# wishlist:
#  get uniques on first check, or in batches instead of serials
#  retrieve multiple emails at once.
#
# i should be passing in offset and batch size during activation

