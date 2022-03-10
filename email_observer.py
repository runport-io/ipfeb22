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
    
    def get_events(self, offset=0, count=10):
        messages = self.connector.get_messages(offset=offset, count=count)
        # self.connector.clear_memory() ## clean the connector
        events = self.transformer.make_events(messages)
        return events
        # consider options for length and offset

# Testing
def run_test():
    results = dict()
    
    e = run_test1()
    results["test1"] = e
    
    batch1 = run_test2(e)
    results["test2"] = batch1

    two_batches = run_test3(e)
    results["test3"] = two_batches

    two_more = run_test4(e)
    results["test4"] = two_more

    return results

def run_test1():
    e1 = EmailObserver()
    print("e1: ", e1)
    
    guest, token = observ2.load_credentials()
    print("token: ", token)
    count = e1.activate(token)
    print("count: ", count)
    #<---------------------------------------------------------------------- add a flag for this

    return e1

def run_test2(email_observer):
    """

    -> events

    Function expects an observer with a connection and authentication.
    """
    events = email_observer.get_events()
    return events

def run_test3(email_observer):
    first_10 = email_observer.get_events(offset=0, count=10)
    next_10 = email_observer.get_events(offset=10, count=10)
    result = (first_10, next_10)
    return result

def run_test4(email_observer):
    e = email_observer
    second_to_last_events = e.get_events(offset=-20, count=10)
    last_events = e.get_events(offset=-10, count=10)
    return (second_to_last_events, last_events)

if __name__ == "__main__":
    run_test()

