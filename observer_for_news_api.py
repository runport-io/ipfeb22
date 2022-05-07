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
import json
import math
import urllib
import urllib.error
import urllib.request

# 2) Port.
# N/A

# 3) Constants
EVERYTHING_ENDPOINT = "https://newsapi.org/v2/everything?"
CHAR_LIMIT = 500
KEY_LENGTH = 32

PARAMETER_KEY = "apiKey"
PARAMETER_QUERY = "q"
PARAMETER_SORTBY = "sortBy"
PARAMETER_PAGESIZE = "pageSize"
PARAMETER_PAGE="page"

# sorting
NEWSAPI_SORT_BY_PUBLISHED_AT = "publishedAt"
NEWSAPI_SORT_BY_POPULARITY = "popularity"
NEWSAPI_SORT_BY_RELEVANCY = "relevancy"

VALUE_MAX_PER_PAGE = 100

NEWSAPI_KEY_FOR_ARTICLES = "articles"
NEWSAPI_KEY_RESULT_COUNT = "totalResults"

HEADER_KEY = "X-Api-Key"
QUERY_SEP = " OR "

# 4) Functions
def chunk_watchlist(watchlist):
    """

    chunk_watchlist() -> list

    Function breaks up the watchlist into a list of chunks that can each be
    submitted as a request.
    """
    result = list()

    limit = get_limit()
    
    remainder = watchlist
    while remainder:
        chunk, remainder = get_chunk(remainder, char_limit=limit)
        result.append(chunk)
        
    return result

def count_chars(brands, sep=QUERY_SEP):
    """

    count_chars() -> int

    Function returns the length of a string that contains the brands separated by sept.
    """
    result = len(make_string(brands, sep=sep))
    return result

def get_articles(data):
    """

    get_articles() -> list

    Function extracts articles from the data NewsAPI sends in its response to a
    query. 
    """
    result = data[NEWSAPI_KEY_FOR_ARTICLES]
    return result

def get_number_of_results(data):
    """

    get_number_of_results() -> int

    Function pulls out the number of results from the data in a NewsAPI response.
    """
    result = data[NEWSAPI_KEY_RESULT_COUNT]
    return result

def get_number_of_calls(results, page_size=VALUE_MAX_PER_PAGE):
    """

    get_number_of_calls() -> int

    Function computes the number of calls it would take to get all of the
    results, if each response contains at most the page_size results. Result
    is the quotient of results over page_size, rounded up to the nearest
    integer.
    """
    result = results / page_size
    result = math.ceil(result)
    result = int(result)
    return result

def get_budget_for_batch(data):
    """

    get_budget_for_batch() -> int

    Function returns the number of calls to NewsAPI necessary to retrieve all
    results.
    """
    number_of_results = get_number_of_results(data)
    result = get_number_of_calls(number_of_results)
    return result

def get_responses_for_request(req, max_pages=10):
    """

    get_responses_for_request() -> list

    Function collects up to a maximum number of pages for the request.
    """
    result = list()
    
    first_response = get_response(req)
    result.append(first_response)
    
    first_data = parse_response(first_response)
    result.append(first_data)
    
    budget = get_budget_for_batch(first_data)
    cap = min(budget, max_pages)

    # start at second page
    for i in range(2, cap):
        req = make_request(page=i)
        # need to make sure this supports pagination, or that i can modify
        # the url
        response = get_response(req)
        result.append(response)

    return result   

def get_budget_for_batches():
    pass
    # should run on data objects. ideally, my implementation should make the
    # batches, get the first response for each, compute the budget, and then
    # get all.

#< add the date restrictions? add the page counter?

def get_chunk(brands, char_limit=CHAR_LIMIT, sep=QUERY_SEP, trace=True):
    """

    get_chunk() -> chunk, remainder

    Function returns a list where the total length of items is no more than
    "length". You should use a flat container for "brands."
    """
    chunk = list()
    wip = sorted(brands)

    chars_left = char_limit
    length_of_separator = len(sep)
    
    for i in range(len(wip)):

        next_brand = wip[0]
        next_brand_as_url = urllib.parse.quote(next_brand)
        # I check whether this fits in the url before taking it out of wip
        
        length_of_next_brand = len(next_brand_as_url)
        
        if chars_left >= length_of_next_brand:
            wip.pop(0)
            chunk.append(next_brand_as_url)
            chars_left = chars_left - (length_of_next_brand +
                                       length_of_separator)
            
            # This logic sometimes will generate a negative chars_left, if the
            # characters left prior to when I add the last brand are long enough
            # to fit the brand, but not long enough to include the separator
            # ("sep").
            #
            #   I view this result as appropriate, since the last brand
            # does not include the separator, but to change the outcome, you can
            # change the condition for adding the brand to chars_left >=
            # (length_of_next_brand + len_of_sepatator)
            
        else:
            if trace:
                print(chars_left)
            break
            # stop when full or close to it
            # saves cycles, but can shift over to smarter routine

    result = chunk, wip
    return result

# known issues:
# - pop from an empty list [done]
# - if brand is longer than remainder [skip]
# - formatting of brands that include chars and whitespace [done]


# I could refactor this into something that if there is like 5 characters left
# looks through the brands to see if there is a brand that has that length or
# less, to make the most out of the bandwidth
# <-------------------------------------------------------------------------------------------------------------

# smarter routine could sort the items by length. Then pick one or more.

def get_limit(char_limit=CHAR_LIMIT, count_everything=False):
    """

    get_limit() -> int

    Function computes the limit of characters for a the query portion of a url.
    If you specify "count everything", the function will subtract the length of
    the endpoint and authentication parts of the URL from the result.
    """
    result = char_limit
    if count_everything:
        prefix = get_prefix()
        base_query = get_query()
        # I use this to figure out how much space the scaffolding takes
        result = char_limit - len(prefix) - len(base_query)
    return result

def get_params(q="",key=None):
    """

    get_params() -> list()

    Function delivers a list of tuples that includes the name of the parameter
    and the value. Function pulls names from globals.     
    """
    if key is None:
        key = KEY_LENGTH * "K"
        
    result = [(PARAMETER_QUERY, q),
              (PARAMETER_KEY, key)]

    return result

def get_prefix(endpoint=EVERYTHING_ENDPOINT):
    """

    get_prefix() -> string

    Function returns the base of the url.
    """
    result = endpoint
    return result

def get_query(params=None):
    """

    get_query() -> string

    Function composes a query in HTTP format based on the parameters. You should
    pass in a list of tuples of (parameter name, value) as "params".
    """
    if not params:
        params = get_params()
        # I always have at least these
        
    result = urllib.parse.urlencode(params, safe=QUERY_SEP)
    return result

def get_response(req, catch_errors=False):
    """

    get_response() -> response or None

    Function uses the request to return a response. If you turn off error
    catching, function will raise exceptions on failure to connect and other
    URL-specific problems, otherwise, it will print the exception and do nothing.
    """
    response = None
    
    try:
        response = urllib.request.urlopen(req)
        
    except urllib.error.URLError as e:
        if not catch_errors:
            raise e
        else:
            if hasattr(e, "reason"):
                print("We failed to reach a sever.")
                print("Reason: ", e.reason)
            elif hasattr(e, "code"):
                print("The server couldn't fulfill the request.")
                print("Error code: ", e.code)
                # Only HTTPErrors have a "code" attribute. An HTTPError descends
                # from a URLError.

        # I am using the error handling logic Michael Foord recommends here:
        # Error handling from https://docs.python.org/3.8/howto/urllib2.html#id1
        # Thank you.
        
    return response
    # should refactor this into wrapping and not.
    
def make_request(chunk, key, put_key_in_url=False, page=1):
    """

    make_request() -> urllib.request.Request

    Function creates an HTTP request. 
    """        
    if put_key_in_url:
        url = make_url_with_key(chunk, key)
        req = urllib.request.Request(url)
    else:
        url = make_url(chunk, page=page)
        headers = dict()
        headers[HEADER_KEY] = key
        # Can send headers as plain text.
        req = urllib.request.Request(url, headers=headers)
        
    return req

def make_requests(chunk, key, page_start, page_end=10):
    """

    make_requests() -> list of requests

    Function makes a list of requests. You can use this to deal with pagination.
    """
    result = list()
    for i in range(page_start, page_end):
        req = make_request(chunk, key, page=i)
        result.append(req)

    return result

def make_string(brands, sep=QUERY_SEP):
    """

    make_string -> string

    Function joins brands separated by sep.
    """
    result = sep.join(brands)
    return result

def make_url(chunk, endpoint=EVERYTHING_ENDPOINT, sep=QUERY_SEP, page=1,
             sort_by=NEWSAPI_SORT_BY_PUBLISHED_AT):
    """

    make_url() -> string

    Function makes a URL for the NewsAPI endpoint that contains the data you
    specify. 
    """
    q = sep.join(chunk)
    # params = [(PARAMETER_QUERY, q)]
    params = [(PARAMETER_QUERY, q),
              (PARAMETER_SORTBY, sort_by),
              (PARAMETER_PAGESIZE, VALUE_MAX_PER_PAGE),
              (PARAMETER_PAGE, page)]

    # could try sorting by popularity or relevancy?
    # <----------------------------------------------------------------------------- test sort by popularity vs recency
    # picks up 74% new data (36 out of 100 results overlap with first query of 100 articles).
    
    query = get_query(params)
    result = endpoint + query
    return result

    # The joining should take place somewhere else<-------------------------------------------------------
    
def make_url_with_key(chunk, key, endpoint=EVERYTHING_ENDPOINT, sep=QUERY_SEP):
    """

    make_url_with_key() -> string

    Function makes a URL for NewsAPI that includes an ApiKey parameter. You
    should not use this routine if you want to maintain security.
    """
    q = sep.join(chunk)
    
    params = get_params(q, key)
    query = get_query(params)
    
    result = endpoint + query
    return result
    
def parse_response(response):
    """

    parse_response() -> dict

    Function takes an HTTP response and turns it into a Python object.
    """
    binary_content = response.read()
    content = binary_content.decode()
    result = json.loads(content)
    return result

# Testing
def run_test1(watchlist):
    result = chunk_watchlist(watchlist)
    return result

def run_test2(chunk, key, trace=False):
    url = make_url_with_key(chunk, key)
    if trace:
        print(url)
    return url

def run_test3(request):
    result = get_response(request)
    return result

def run_test4():
    # parse response
    data = parse_response(response)
    # data should be in python format, a list of dictionaries?
    return data
    # sort of done    

def run_test5():
    # make events
    pass

def run_test6():
    # store events
    pass

# refresh ops:
#   If i get a new list, i should keep track of what i have already called and
#   when. So almost like a dictionary of terms to dates. I should then be able
#   to make that into a list of tuples, from oldest to newest, or something
#   like that. So when I compose the chunks, I should a) get the terms that I
#   haven't seen before, subject to some control, b) refresh older terms, c)
#   refresh newer ones. I can call the order FIFO = bool.

#   generally speaking, I should be able to deliver a list of queries. I should
#   also be able to deliver a schedule of queries (different from a list in that
#   the schedule matches each query against a predetermined point in time).

# spacing / awareness
#   I want to punctuate targeted queries with broad ones that call for all the
#   top headlines, so i don't miss something obvious. 

# As a developer, I want to be able to choose whether the URL has the API key
# in it so that I can maximize bandwidth per day. I can do this through a header
# or something.

w = ["foodprocessing.com",
     "cargill",
     "syngenta",
     "bunge",
     "viterra",
     "vitol",
     "adm",
     "The Archer-Daniels-Midland Company",
     "trafigura",
     "glencore",
     "bayer seeds",
     "food and agriculture organization of the un",
     "farm futures",
     "RiverRock European Capital Partner",
     "Onyx Capital Group",
     "European Federation of Energy Traders",
     "Simmons & Simmons LLP",
     "NERA",
     "Gapuma Group Ltd.",
     "Kimura Capital LLP",
     "EXIM",
     "SITE Intelligence Group",
     "tyson foods",
     "Agence France-Presse",
     "bbc",
     "Institute for the Study of War",
     "Castellum.ai",
     "Shorenstein Center on Media, Politics and Public Policy",
     "First Draft News",
     "SuperYacht Fan",
     "Cultural Heritage Partners",
     "Pryor Cashman",
     "Goodman Law PLLC",
     "jewish journal",
     "UJA-Federation of New York",
     "Meketa Investment Group",
     "German Institute for International and Security Affairs",
     "National Association for Business Economists",
     "Stradley Ronon",
     "Kentik Inc.",
     "GSMA Intelligence",
     "AdaptiveMobile Security",
     "Haun Ventures",
     "Pew Research Center",
     "Montreal AI Ethics Institute",
     "AI consulting firm BNH",
     "Business Talent Group",
     "YotPo",
     "Chatham House",
     "UK Ministry of Defense",
     "Technology Officer Practice Group",
     "RSM US LLP",
     "Notre Dame’s International Security Center",
     "the Nilson Report",
     "ABA Techshow",
     "FocusEconomics",
     "International Monetary Fund",
     "Fed Reserves",
     "Mortgage Bankers Association",
     "Bankrate.com",
     "University of Toronto’s School of Cities",
     "Rotman School of Management",
     "CompTIA",
     "Grant Thornton LLP",
     "Eide Bailly LLP",
     "Paychex",
     "US EIA",
     "Renew America Together",
     "VoteVets",
     "International Institute for Strategic Studies",
     "University of St. Andrews",
     "Royal United Services Institute",
     "Rand Corp",
     "The Federalist",
     "UCLA Burkle Center",
     "PEN America",
     "Florida Citrus Commission",
     "Save Our Children",
     "Sun Sentinel",
     "Survival",
     "Quincy Institute for Responsible Statecraft",
     "Center for a Free Economy",
     "Renew Democracy Initiative",
     "Center for a New American Security",
     "Institute of International Finance",
     "Atlantic Council’s GeoEconomics Center",
     "Institute for the Study of War",
     "Center for Defense Strategies",
     "Hudson Institute",
     "Handout Photos",
     "Planet",
     "Black Sea Institute of Strategic Studies",
     "Halo Trust",
     "Bolt.com"
     ]

w2 = ["Twitter",
      "SpaceX",
      "Blue Origin",
      "Blackstone"]

