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
class TopHeadlinesRequest:

    CATEGORIES = ["business", "entertainment", "general", "health", "science",
                  "sports", "technology"]

    ENDPOINT = "https://newsapi.org/v2/top-headlines"
    
    def __init__(self):
        self.base = NewsAPIRequest()
        # need to pass in the query, unless i get the query object? 
        
        self.base.set_endpoint(self.ENDPOINT)
        # this would be like self.endpoint.set(self.ENDPOINT)
        

        self._category = None
        # self.category = CachedAttribute()
        ## really this is not about cached
        ## this is about multiple choice
        ## ValueFromList()
        ## Value()

        # then have rules:
        #   if category, then not sources

        # get params?
        # get_headers?
        # probably outside

        self._country = None
        self._toggle_state = self.CATEGORIES.copy()

    def get_category(self):
        return self._category
    
    def set_category(self, category):
        if category in self.CATEGORIES:
            self._category = category
        else:
            raise Exception

        # does not mix with sources, so have to get rid of that or throw an
        # excpetion <-------------------------------------------------------------------
        # something like, "remove sources", or "reset sources"
        # same above.

    def toggle_category(self):
        if not self._toggle_state:
            self._toggle_state = self.CATEGORIES.copy()

        cat_old = self.get_category()
        cat_new = self._toggle_state.pop(0)
        
        if old_cat in self.CATEGORIES:
            self._toggle_state.append(old_cat)
            # so I can keep cycling

        self.set_category(cat_new)

# min interface:
# get_url
# get_url_details
# get_params
# get_header
# update_params
# update_header
# set_query()
# get_query()


