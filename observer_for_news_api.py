# Imports
# 1) Built-ins
import json
import urllib
import urllib.request

# 3) Constants
EVERYTHING_ENDPOINT = "https://newsapi.org/v2/everything?"
CHAR_LIMIT = 500
KEY_LENGTH = 32

PARAMETER_QUERY = "q"
PARAMETER_KEY = "apiKey"

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

def get_chunk(brands, char_limit=CHAR_LIMIT, sep=QUERY_SEP, trace=True):
    """

    get_chunk() -> chunk, remainder

    Function returns a list where the total length of items is no more than
    "length". You should use a flat container for "brands."
    """
    chunk = list()
    wip = sorted(brands)

    chars_left = char_limit
    
    for i in range(len(wip)):

        next_brand = wip[0]
        next_brand_as_url = urllib.parse.quote(next_brand)
        # I check whether this fits in the url before taking it out of wip
        
        length_of_next_brand = len(next_brand_as_url)
        if chars_left >= length_of_next_brand:
            wip.pop(0)
            chunk.append(next_brand_as_url)
            chars_left = chars_left - (length_of_next_brand + len(sep))
            
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

def get_limit(char_limit=CHAR_LIMIT):
    """

    -> int

    Function computes the limit for a the query portion of a url. 
    """
    prefix = get_prefix()
    base_query = get_query()
    # I use this to figure out how much space the scaffolding takes
    result = char_limit - len(prefix) - len(base_query)
    return result

def get_params(q="",key=None):
    """

    -> list()
    
    """
    if key is None:
        key = KEY_LENGTH * "K"
        
    result = [(PARAMETER_QUERY, q),
              (PARAMETER_KEY, key)]

    return result

def get_prefix(endpoint=EVERYTHING_ENDPOINT):
    """

    -> string

    Function returns the base of the url.
    """
    result = endpoint
    return result

def get_query(params=None):
    """

    -> string

    Params is supposed to be a list of tuples of parameter, value. 
    """
    if not params:
        params = get_params()
        # I always have at least these
        
    result = urllib.parse.urlencode(params, safe=QUERY_SEP)
    return result

def get_response(req):
    """
    -> response
    
    """
    response = urllib.request.urlopen(req)
    return response

def make_request(chunk, key, put_key_in_url=True):
    """

    -> request

    
    """
    url = ""
    values = dict()
    
    if put_key_in_url:
        url = make_url_with_key(chunk, key)
    else:
        url = make_url_without_key(chunk)
        values[HEADER_KEY] = key

    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")
    #<--------------- data should be in bytes?
    # this should be its own function
    
    req = urllib.request.Request(url, data)
    return req

def make_string(brands, sep=QUERY_SEP):
    """

    make_string -> string

    Function joins brands separated by sep.
    """
    result = sep.join(brands)
    return result

def make_url_with_key(chunk, key, endpoint=EVERYTHING_ENDPOINT, sep=QUERY_SEP):
    """

    -> string

    """
    q = sep.join(chunk)
    
    params = get_params(q, key)
    query = get_query(params)
    
    result = endpoint + query
    return result

def parse_response(response):
    """
    -> dict
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

def run_test3():
    # get data
    result = get_response(query)
    # this should be in python already? or in json? if json means i don't waste
    # cycles
    return result
    # sort of done

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

