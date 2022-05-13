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

    SEARCH_IN = ["title", "description", "content"]

    NAME_SEARCH_IN = "searchIn"
    
    
    def __init__(self):
        news_api.RequestForNewsAPI.__init__(self)
        self.set_sendpoint(self.ENDPOINT)

        self.search_in = choice.Choice(name=NAME_SEARCH_IN)
        self.search_in.set_menu(*SEARCH_IN)
        self.search_in.set_limit(3)
        # Permits multiple.

        self.domains = domains.Domains()

        self.date_from = date
        self.date_to = date
        
        self.language = choice
        self.sort_by = choice

            
