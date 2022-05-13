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
`
# 2) Port.
from . import choice
from . import date_param
from . import domains
from . import request_for_news_api as news_api

# 3) Constants
#    N/a

# 4) Functions
class RequestForEverything(news_api.RequestForNewsAPI):
    """

    This class provides a place to store data for requests to NewsAPI through
    the "Everything" endpoint. Most requests we send go through this endpoint.
    """
    
    ENDPOINT = "https://newsapi.org/v2/everything?"

    LANGUAGES = ["ar", "de", "en", "es", "fr", "he", "it", "nl", "no", "pt",
                "ru", "sv", "ud", "zh"]
    
    SEARCH_IN = ["title", "description", "content"]

    SORT_BY = ["relevancy", "popularity", "publishedAt"]

    NAME_DATE_FROM = "from"
    NAME_DATE_TO = "to"
    NAME_LANGUAGE = "language"
    NAME_SEARCH_IN = "searchIn"
    NAME_SORT_BY = "sortBy"
    
    def __init__(self):
        news_api.RequestForNewsAPI.__init__(self)
        self.set_sendpoint(self.ENDPOINT)

        
        self.date_from = date_param.Date(self.NAME_DATE_FROM)
        self.date_to = date_param.Date(self.NAME_DATE_TO)

        self.domains = domains.Domains()
        
        self.language = choice.choice(name=self.NAME_LANGUAGE)
        self.language.set_menu(*self.LANGUAGES)
        self.language.set_limit(None)
        # Permit unlimited selections
        
        self.search_in = choice.Choice(name=self.NAME_SEARCH_IN)
        self.search_in.set_menu(*self.SEARCH_IN)
        self.search_in.set_limit(3)
        # Permits multiple.
        
        self.sort_by = choice.Choice(name=self.NAME_SORT_BY,
                                     default=self.SORT_BY[2] # Default per docs
                                     )  
        self.sort_by.set_menu(*self.SORT_BY)

            
