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

Module contains routines that turn data from NewsAPI into an Event. 
------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:

FUNCTIONS:
make_event()

CLASSES:

------------------  ------------------------------------------------------------
"""
# Imports
# 1) Built-ins
# N/a
# 2) Port.
import event as e

# Constants
AUTHOR = "author"
CONTENT = "content"
PUBLISHED_AT = "publishedAt"
SOURCE = "source"
SOURCE_NAME = "name"
TITLE = "title"
URL = "url"

# Functions
def make_event(article):
    """

    Function returns an Event with details from the article. An article is a
    dictionary that follows the NewsAPI format for responses.    
    """
    event = e.Event()

    event = add_title(event, article)
    event = add_body(event, article)
    event = add_date(event, article)
    event = add_source(event, article)

    event.set_number()
    return event

def add_title(event, article):
    title = article[TITLE]
    event.set_headline(title)
    return event

def add_body(event, article):
    summary = article[CONTENT]
    url = article[URL]

    response = urllib.open(url)
    content = response.decode()
    event.set_raw(content)
    
    mini = summary[:40]
    if mini in content:
        event.set_body(content)

    return event
    # also checks for errors
    # and set raw

def add_date(event, article):
    published = article[PUBLISHED]
    seconds = parse_timestamp(published)
    event.timestamp.set_published(seconds)

    now = time.time()
    event.timestamp.set_receipt(now)
    return event

def add_source(event, article):
    source = article[SOURCE][SOURCE_NAME]
    event.set_source(source)

    author = article[AUTHOR]
    event.source.set_author(author)
    
    return revent

    
    # implies that the source object should have some detail:
        # author
        # publication
        # and that each one of these may be should have an id
        # so that i can see if they match or do verification or something
        # though unclear why that's better than just comparing the string
    
# add the number?
# add the something else?

# ideally, ID would be driven by both an author and a source

def parse_timestamp(string):
    """

    -> number

    Expects a timestamp in "YYYY-MM-DDTHH:MM:SSZ" format.
    """
    time_tuple = get_tuple(string)
    seconds = get_seconds(time_tuple)
    return seconds

def get_tuple(string):
    string = string.rstrip("Z")
    parts = string.split("T")
    year, month, day = parts[0].split("-")
    hours, minutes, seconds = parts[1].split(":")
    result = (year, month, day, hours, minutes, seconds)
    return result
    
def get_seconds(tt):
    result = time.mktime(tt)
    return result
    
    

