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
class TopHeadlines:
    def __init__(self):


        PARAMS = ["_categories", "countries", "pages", "sources"]
                  
        CATEGORIES = ["business", "entertainment", "general", "health", "science",
                      "sports", "technology"]

        ENDPOINT = "https://newsapi.org/v2/top-headlines"
        
        self.endpoint = Value(self.ENDPOINT)
        
        self.q = Query()
        
        self.pages = Pages()
        # should deliver a dict
        # get should always deliver a dict of param name to value. #<------------------------
        
        self.countries = Choice()
        self.sources = Choice()
        # need to configure both of these to include the name

        self._categories = Choice(default=None, options=self.CATEGORIES)
        # need to specify, or make into an object: server, var
        # or just keep as Value()
        self.params = Mapping()
        self.headers = Mapping()

    def set_category(self, val):
        sources = self.sources.get()
        if sources:
            raise Exception("cannot have both source and category")
        else:
            self._categories.set(val)

        # could have option to force
      
