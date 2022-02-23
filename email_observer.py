# Copyright Port. Prerogative Club ("the Club")
#
# 
# This file is part of Port. 2 ("Port.")
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
import imap_connector
import observ2
import welder

# 
class EmailObserver:
    def __init__(self, url=constants.GMAIL, account=constants.USER):
        self.connector = imap_connector.ImapConnector(url, account)
        self.transformer = welder.Welder()
        
    # something about namespaces and numbers
    # define the main methods of check() and construct(), plus nonpublics.

    def activate(self, token, trace=False):
        count = self.connector.connect(token)
        return count
    
    def get_events(self):
        messages = self.connector.get_messages()
        # self.connector.clear_memory() ## clean the connector
        events = self.transformer.make_events(messages)
        return events
        # consider options for length and offset

# Testing
def run_test():
    e1 = EmailObserver()
    print("e1: ", e1)
    
    guest, token = observ2.load_credentials()
    print("token: ", token)
    
    count = e1.activate(token)
    print("count: ", count)
    
    events = e1.get_events()
    print(events)
    return events

if __name__ == "__main__":
    run_test()

