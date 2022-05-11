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
from . import query

# 3) Constants
#    N/a

# 4) Functions
class GenericRequest:

    KEY_QUERY = "q"
    
    def __init__(self):
        self._endpoint = ""
        # want a rich object here?
        
        self._params = dict()
        self._headers = dict()
        self.q = Query()

    def get_endpoint(self):
        result = self._endpoint
        return result

    def set_endpoint(self, url):
        self._endpoint = url

    def get_params(self):
        """

        -> dict

        Returns a copy. 
        """

        result = self._params.copy()
        query = self.q.get_value_as_string()
        result[self.KEY_QUERY] = query

        return result

    def get_url_details(self):
        params = self.get_params()
        sep = self.q.SEP
        details = urllib.parse.urlencode(params, safe=sep)
        return details

    def get_url(self):
        details = self.get_details()
        endpoint = self.get_endpoint()
        result = endpoint + details
        return result

    def get_request(self):
        headers = self.get_headers()
        url = self.get_url()
        result = urllib.request.Request(url, headers=headers)
        return result

            


        
