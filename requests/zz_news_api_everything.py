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

# <--------------------------------------------------------- old, remove

# Imports
# 1) Built-ins
#    N/a

# 2) Port.
#    N/a

# 3) Constants
#    N/a

# 4) Functions
class EverythingRequest:

    ENDPOINT = "www.blah"

    def __init__(self):
        
        self.base = NewsAPIRequest()
        self.dates = Dates()

        self._search_in = None
        self._domains = None
        self._exclude_domains = None

        self._language = None
        self._sort_by = None

    def set_endpoint(self, url):
        self.base.set_sendpoint(url)
        # should delegate down

    def get_params(self, clean=True):
        base = self.base.get_params(clean=clean)
        dates = self.dates.get_params()
        base.update(dates)
        
        # if defined, include it (ie clean anythign that's not?)
        # separate multiple entries with the separator? or comma? #<-------- test
        
    def get_headers(self):
        result = self.base.get_headers()
        return result


    
    
    
    
