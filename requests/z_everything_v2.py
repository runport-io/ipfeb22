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
class Everything:

    ENDPOINT = "https://newsapi.org/v2/everything?"

    LANGUAGES = ["ar", "de", "en", "es", "fr", "he", "it", "nl", "no", "pt",
                 "ru", "sv", "ud", "zh"]
    
                # From NewsAPI.org, as of May 10, 2022.
                # See https://newsapi.org/docs/endpoints/everything

    SEARCH_IN = ["title", "description", "content"]
    SORT_BY = ["relevancy", "popularity", "publishedAT"]
    
    def __init__(self):
        
        self.date_to = Date(name="dateTO")
        self.date_from = Date(name="dateFROM")
        
        self.domains = Domains()

        self.language = Choice(name="language")
        self.language.set_options(self.LANGUAGES)
       
        self.page = Number(name="page")
        self.page.set_floor(1)
        
        self.page_size = Number(name="pageSize")
        self.page_size.set_ceiling(100)
        # per docs

        self.q = Query(name="q")

        self.search_in = Choice(name="searchIn")'
        self.search_in.set_choices(self.SEARCH_IN)
        
        self.sort = Choice(name="sortBy")
        self.sort.set_choices(self.SORT_BY)
        self.sort.set_default(SORT_BY[2])
        # I am setting the default to match the NewsAPI docs
        
        self.sources = Choice(name="SOURCES")
        self.sources.set_limit(20)
        # Not currently using
        
        self.headers = dict()
    
class Handler:
    AUTH_KEY = ""
    
    def get_params(self, request):
        
        result = dict()
        for attr_name in request.__dict__:
            if attr_name[0].islower():
                attr = getattr(request, attr_name)
                params = attr.get_dict()
                result.update(params)

        return result
    
    def get_endpoint(self, request):
        result = request.ENDPOINT
        return result
    
    def get_url(self, request):
        endpoint = self.get_endpoint(request)
        params = self.get_params(request)

        query = urllib.parse.urlencode(params)
        # need to get the actual query? or have Query have a get_dict()?
        
        result = endpoint + query
        return result

    def get_request(self, request):
        headers = self.get_headers(request)
        headers = self.add_security(headers)
        url = self.get_url(request)
        
        result = urllib.request.Request(url, headers=headers)
        return result

    def add_security(self, headers, key):
        headers[self.AUTH_KEY] = key
        return headers
    

# I could make this:
#   x = add_core(x)
#   x = add_everything(x)


    
    
    
    
