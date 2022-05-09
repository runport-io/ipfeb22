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

    PARAMS = []
    
    def __init__(self):
        self.endpoint = None
        self.q = Query(name="q")
        
        self.page = Number(name="page")
        self.page.set_floor(1)
        
        self.page_size = Number(name="pageSize")
        self.page_size.set_ceiling(100)
        # per docs
        
        self.date_to = Date(name="dateTO")
        self.date_from = Date(name="dateFROM")
        
        self.sources = Choice(name="SOURCES")
        self.sources.set_max(20)
        # something about handling the options here?
        # what if the options are not defined? <-----------------------------------------------------------
    
        self.domains = Domains()
        
        self.language = Choice(name="language")
        self.language.set_options(LANGUAGES)
        # add "ru" if include_all is TRUE
        
        self.sort = Choice(name="sortBy")
        self.sort.set_choices()
        # add options
                
        self.search_in = Choice(name="searchIn", value=None,
                                choice=["title", "description", "content"])
        self.headers = dict()
        
    def get_params(self):
        # go through each of the attrs, get their params
        # enrich, return. Each attr should deliver the params as is?
        # #<-------------------------------- -----------------------where to put the URL encoding? in the param or not?
        pass

# make sure to handle defaults: e.g., if value is none, return an empty dictionary in Choice
# could really just make this a memo / container, with no ops
# easier to build and supplement.
# harder to save? harder to load? let's not worry about it for now.
    
class Handler:
    def get_params(self):
        pass
    
    def get_url(self):
        pass

        # get endpoint
        # get params
        # glue them together

    def get_request(self):
        pass

        # this stuff I thought about moving to handler
        # so i don't have to repeat myself


# I could make this:
#   x = add_core(x)
#   x = add_everything(x)


    
    
    
    
