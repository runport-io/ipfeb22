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

"""

Module defines a class for making Events out of articles from NewsAPI.org.
----------------------- --------------------------------------------------------
Attribute               Description
----------------------- --------------------------------------------------------

DATA:
N/a

FUNCTIONS:
class WelderForNewsAPI  What do you say when you turn an article into an event?*
----------------------  --------------------------------------------------------

*"Well done!"
"""

class WelderForNewsAPI:
    """

    Object constructs Events out of articles from NewsAPI. 
    """

    SOURCE = "source"
    AUTHOR = "author"
    TITLE = "title"
    DESCRIPTION = "description"
    URL = "url"
    URL_TO_IMAGE = "urlToImage"
    PUBLISHED_AT = "publishedAt"
    CONTENT = "content"
    
    def __init__(self):
        pass

    def make_event_from_article(self, article):
        result = Event()

        headline = article[self.TITLE]
        source = article[self.SOURCE]
        timestamp = article[self.PUBLISHED_AT]
        content = article[self.CONTENT]
        
        self.add_headline(result, headline)
        self.add_source(result, source)
        self.add_timestamp(result, timestamp)
        self.add_content(result, content)
        
        return result
    
    def add_headline(self, event, headline):
        event.set_headline(headline)

    def add_source(self, event, source):
        event.set_source(source)
        # could be more involved. 

    def add_timestamp(self, event, date):
        event.timestamp.set_receipt(date)
        # will break, will need to modify this method

    def add_content(self, event, content):
        event.set_body(content)
        # need to get this through url

    def add_body_from_internet(self, event, url):
        pass
        # load url, send through parser, slap that on.
        
    
