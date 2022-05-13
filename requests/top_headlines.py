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
class RequestForTopHeadlines(news_api.RequestForNewsAPI):
    """

    This class provides a place to store data for requests to NewsAPI through
    the "Top headlines" endpoint. The endpoint provides a high-level overview of
    what's going on to supplement more targeted queries. 
    """
    CATEGORIES = ["business", "entertainment", "general", "health", "science",
                  "sports", "technology"]
    
    COUNTRIES = ["ae", "ar", "at", "au", "be", "bg", "br", "ca", "ch", "cn",
                 "co", "cu", "cz", "de", "eg", "fr", "gb", "gr", "hk", "hu",
                 "id", "ie", "il", "in", "it", "jp", "kr", "lt", "lv", "ma",
                 "mx", "my", "ng", "nl", "no", "nz", "ph", "pl", "pt", "ro",
                 "ru", "rs", "sa", "se", "sg", "si", "sk", "th", "tr", "tw",
                 "ua", "us", "ve", "za"]

    ENDPOINT = "https://newsapi.org/v2/top-headlines?"

    NAME_CATEGORY = "category"
    NAME_COUNTRY = "country"
    
    def __init__(self):
        news_api.RequestForNewsAPI.__init__(self)
        self.set_endpoint(self.ENDPOINT)

        self._category = choice.Choice(name=NAME_CATEGORY)
        self._category.set_menu(*CATEGORIES)
        
        self._country = choice.Choice(name=NAME_COUNTRY)
        self._country.set_menu(*COUNTRIES)
        self._global_coverage = False

    def check_sources(self):
        """

        check_sources() -> bool

        Method returns True if the instance has defined a value for the sources
        parameter, False otherwise. You use this to check for comptability with
        "country" and "category" parameters, since NewsAPI says those cannot
        coexist with "sources".
        """
        result = False
        if self.sources.get_selection():
            result = True

        return result

    def get_params(self, encode=True, include_blanks=False, check_query=True):
        """

        get_params() -> dict

        Method delegates to RequestForNewsAPI.get_params, then adds the params
        for country and category.
        """
        result = news_api.RequestForNewsAPI.get_params(self)
        more_params = [self._category, self._country]
        
        for param in more_params:
            data = param.get_dict(encode=encode, include_blanks=include_blanks,
                                  check_query=check_query)
            result.update(data)

        return result
        
    def select_category(self, *categories, force=False):
        """

        select_category() -> None

        Method sets a value for the category parameter of the request. You will
        get an error if you have previously specified the "source" parameter:
        NewsAPI says these two are mutually exclusive.
        """
        if check_sources():
            c = "NewsAPI prohibits the combination of sources and countries in"
            c += "requests for Top Headlines. "
            c += "See https://newsapi.org/docs/endpoints/top-headlines."
            raise Exception(c)
        else:
            self._category.select(*categories, force=force)

    def select_country(self, *countries, force=False):
        """

        select_category() -> None

        Method sets a value for the category parameter of the request. You will
        get an error if you have previously specified the "source" parameter:
        NewsAPI says these two are mutually exclusive.
        """
        if check_sources():
            c = "NewsAPI prohibits the combination of sources and countries in"
            c += "requests for Top Headlines. "
            c += "See https://newsapi.org/docs/endpoints/top-headlines."
            raise Exception(c)
        else:
            self._country.select(*countries, force=force)
        
    
