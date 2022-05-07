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
#    N/a

# 2) Port.
#    N/a

# 3) Constants
#    N/a

# 4) Functions

class Bundle:
    def __init__(self):
        pass
        # pass in the Query object? or pass in the batch of brands?
        # self._budget = 10

    def get_budget(self):
        return self._budget
        # alternatively, budget could be the lower of the BUDGET or the number
        # needed to complete the requests.

    def set_budget(self):
        pass
    
    def set_query(self):
        pass

    def get_first_request(self):
        pass
        # constructs a request

    def get_first_response(self):
        pass

    def get_requests(self):
        pass
        # make the first request if we can make it
        # get the response
        # create other requests up to budget or need
        # toggle pages

    def get_responses(self):
        pass
        # get responses for each of the requests
   
    
# then we will have the bundle object.
# bundle will create requests: set_query()
# bundle will manage responses
# bundle can also handle uniques, though not necessarily
# that seems better for a constructor of events
# whatever makes events has to be at the level of the Event definition
# should also be able to access storage

# should handle:
#   auth
#   pagination

# bundle.set_query(query)?
# bundle.define(batch)? same thing.


