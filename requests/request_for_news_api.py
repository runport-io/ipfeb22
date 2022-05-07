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

class NewsAPIRequest:

    KEY_PAGE = "page"
    KEY_PAGE_SIZE = "pageSize"

    MAX_PAGE_SIZE = 100
    
    def __init__(self):
        self.base = GenericRequest()
        self._page = 1
        self._page_size = 100
        self._sources = list()

    #LCD for NewsApi requests
    def get_params(self):
        base = self.base.get_params()
        base[self.KEY_PAGE] = self._page
        base[self.KEY_PAGE_SIZE] = self._page_size
        # add something for source mgmt?
        
        # get params from base
        # update with data defined here

    def get_headers(self):
        result = self.base.get_headers()
        return result
        # delegate down
        # in place changes?

    def get_url_details(self):
        headers = self.get_headers()
        params = self.get_params()
        result = self.base.get_url_details(params, headers)
        return result


    def get_sources(self):
        result = self._sources
        return result
        # some logic here to match the news_api

    def set_sources(self, sources):
        self._sources = sources

    def reset_sources(self):
        if self._sources:
            cache = self._sources
            self._sources_cache = cache
        self._sources = list()       

    # almost looks like I should pull sources out into its own module? easier
    # to handle dependencies and caching. then can add "get_cache()", and reuse
    # for "country".

    def get_page(self):
        return self._page

    def set_page(self, num):
        self._page = num
        # add logic for checking num in range()

    def increase_page(self):
        starting = self.get_page()
        starting = max(1, starting)
        result = starting + 1
        self.set_page(result)
        return result

    def decrease_page(self):
        starting = self.get_page()
        ending = starting - 1
        ending = max(ending, 1)
        self.set_page(ending)
        return ending

    def get_page_size(self):
        return self._page_size

    def set_page_size(self, num, force=False):
        if num > self.MAX_PAGE_SIZE:
            if force:
                self._page_size = num
            else:
                raise Exception
                # need to put the exception module on the path?
                # no, but what to do about typed exceptions?
                # catch them at the op level - the op module should
                # know what to do with these.
        else:
            self._page_size = num

    # I could consider adding a Pages object
    # then I could add pages to the higher-level request, without the base. So
    # higher level object could have
    # self.dates
    # self.pages
    # self.sources
    # self.countries
    # self.generic
    # self.query
    #
    # this approach would make the object flat, rather than nested.

    

        
