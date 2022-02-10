# Library
# (c) Port. Prerogative Club 2022

import os




singleton = os.path()
# tracks brand : [event_ids]
# matches topic id?

stacks = os.path(2)
# the library tracks events by id: id: event (attrs in columns)
# the library records all events

topics = {}
size_limit = 100

def start(watchlist=None):
    pass
    # open singleton (location should not change session to session)
    
    # for brand in watchlist:
        # open_or_start_topic(brand)

def get_recent(count=100):
    pass
    # returns x most recent events
    # i = 0
    # result = list() 
    # while i < count:
    #   event = stacks.read_last()
    #   result.append(event)
    #
    # return result

def create_topic(name):
    # open file
    # topics[name] = obj
    # do nothing? print success?

def open_topic(name):
    # create file
    # check for naming collisions

def save_events(events):
    # for e in events:
    #   record e in library
    #   record e for each of the brands mentioned in e.brands in singleton
    #   record e in each topic?
    ## [verbose = writes the headline of e in the topic]

def watch(brands):
    # ? is it necessary?

def check_limits():
    result = None
    if size(stacks) >= size_limit * 80%:
        print(something)
        result = Exception
    else:
        result = ?


    
    

