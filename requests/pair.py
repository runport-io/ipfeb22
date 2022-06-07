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
class Pair:
    """

    Class provides an object for storing matching requests and responses.
    """    
    def __init__(self, request=None, response=None):
        self._request = request
        self._response = response

    def get_request(self):
        """

        get_request() -> obj

        Method returns the request stored on the instance.
        """
        return self._request

    def get_response(self):
        """

        get_response() -> obj

        Method returns the response stored on the instance.
        """
        return self._response

    def set_request(self, request):
        """

        set_request() -> None

        Method stores the request on the instance.
        """
        self._request = request

    def set_response(self, response):
        """

        set_response() -> None

        Method stores the response on the instance.
        """
        self._response
