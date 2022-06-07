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
class ResponseForNewsAPI:
    def __init__(self):
        self._response = None
        # the wrapper
        self._articles = None
        # list
        self._count = None
        # int, total number of matches for request
        self._status = None
        # NewsAPI specific, string

    def get_articles(self):
        return self._articles

    def set_articles(self, articles):
        self._articles = articles

    def get_count(self):
        # returns number of matches
        return self._count

    def set_count(self, count):
        self._count = count
    
    def get_response(self):
        # get the raw thing
        return self._response

    def set_response(self, response):
        self._response = response

    def get_string(self, response=None):
        """

         -> dict

        Takes the response and assigns the contents to the isntance. 
        """
        if response is None:
            response = self.get_response()

        binary_content = response.read()
        result = binary_content.decode()
        return result

    def get_data(self, string=None):
        if string is None:
            string = self.get_string()

        result = json.loads(string)
        return result

    def get_values(self, data=None):
        if data is None:
            data = self.get_data()

        articles = data[self.ARTICLES]
        count = data[self.COUNT]
        status = data[self.STATUS]

    def set_attributes(self, values=None):
        if values is None:
            values = self.get_values()

        articles, count, status = values
        self.set_articles(articles)
        self.set_count(count)
        self.set_status(status)
        
    
    

    
        
        

        
