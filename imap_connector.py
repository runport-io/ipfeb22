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
# N/a

# 2) Port.
import constants
import observ2

# 3) Data
# N/a

# 4) Functions
class ImapConnector:
    def __init__(self, url, guest):
        self._account = guest
        self._offset = 0
        self._service = url
        self._session = None
    
    def check(self, count=10, offset=None, trace=False):
        uniques = self.refresh()

        if offset is None:
            offset = self.get_offset()
        requested_uniques = uniques[offset: (offset+count)]
        # pad with Nones? 
        # for i in uniques[offset: x]:
        #   get message
        #   increment i so that i know where i stopped
        
        messages = list()
        for u in requested_uniques:
            message = self._get_message(u)
            messages.append(message)

        new_offset = offset + count
        self.set_offset(new_off)
        
        return messages

    def connect(self, token):
        self._session = observ2.establish_session(self._service)
        self._session.login(self._account, token)
        result = self._session.select(constants.INBOX, readonly=True)
        return result
        
    def disconnect(self):
        pass

    def refresh(self):
        serials = self._get_serials()
        uniques = self._get_uniques(serials)
        self._uniques = uniques
        # bad structure
        return uniques
    
    def _build_list(self, serials):
        uniques = list()
        for serial in serials:
            unique = self._get_uid(serial)
            uniques.append(unique)
        return uniques
    
    def _get_message(self, uid):
        message = observ2.get_message_by_UID(self._session, uid)
        return message

    def _get_serials(self, trace=False):
        serials = observ2.get_ids(self._session, trace=trace)
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
        
class EmailObserver:
    def __init__(self):
        self.connector = ImapConnector()
        self.worker = Welder()
        
    # something about namespaces?
    # define the main methods of check() and construct(), plus nonpublics.
    
# Testing
url = constants.GMAIL
def run_test(url):
    guest, token = observ2.load_credentials()
    # The EmailObserver should pass those in. The Controller should send them
    # to EmailObserver.
    ct1 = ImapConnector(url=url, guest=guest)
    result = ct1.connect(token)
    print(result)

    uniques = ct1.refresh()
    print("First 10: ", uniques[:10])
    print("Last 10:  ", uniques[-10:])

    msgs = ct1.check()
    print(msgs)
    
    return msgs

if __name__ == "__main__":
    run_test(url)

# figure out how to retrieve in batches only.
# need a routine to go from uid to serial, so i can start looking up from there.
#   then on refresh, i check what position the last unique is in, and get new
#   from there ids from beyond that position.

