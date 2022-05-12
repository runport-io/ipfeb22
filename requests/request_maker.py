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
import urllib.parse
import urllib.request

# 2) Port.
from . import query

# 3) Constants
#    N/a

# 4) Functions
class RequestMaker:
    """

    Class provides an object with methods for managing the contents of an HTTP
    request.
    """
    
    QUERY_NAME = "q"
    
    def __init__(self, endpoint, query_name=QUERY_NAME):
        self._endpoint = endpoint
        self._headers = dict()
        
        self.query = query.Query(name=query_name)

    def get_endpoint(self):
        """

        get_endpoint() -> str

        Method returns the base URL for the request.
        """
        return self._endpoint

    def get_headers(self, copy=True):
        """

        get_headers() -> dict

        Method returns a dictionary of headers for the instance. If you turn off
        "copy", you get the same object as the one on the instance, so you can
        modify it in place if you wish. 
        """
        result = self._headers
        if copy:
            result = result.copy()
        return result
    
    def get_params(self, encode=True, include_blanks=False):
        """

        get_params() -> dict()

        Method returns a dictionary of name to value for each attribute that
        supports the get_dict() call. If you turn on include_blanks, the result
        will include parameters whose value tests as False.
        """
        result =  dict() 
        for attr_name in self.__dict__:
            if attr_name.startswith("_"):
                continue
            else:
                attr = getattr(self, attr_name)
                data = attr.get_dict(encode=encode,
                                     include_blanks=include_blanks)
                result.update(data)

        return result

    def get_request(self, headers=None):
        """

        get_request() -> urllib.request.Request

        Method creates a request with all of the data. 
        """
        if headers is None:
            headers = self.get_headers()

        url = self.get_url()
        result = urllib.request.Request(url, headers=headers)
        return result

    def get_url(self):
        """

        get_url() -> string

        Method returns a url that includes the parameters the instance defines.
        """
        endpoint = self.get_endpoint()
        tail = self.get_tail()

        result = endpoint + tail
        return result

    def get_tail(self, params=None):
        """

        get_tail() -> string

        Method returns the portion of the URL that contains the query and
        parameters.
        """
        if params is None:
            params = self.get_params()
            
        result = urllib.parse.urlencode(params, safe=self.q.SEP)
        # Consider expanding the logic to permit more than one safe char

        return result
        
    
        
