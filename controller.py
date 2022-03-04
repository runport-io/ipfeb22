# controller 2

# launch observers
# have a function called get_events()
# get the events
# put them in the cache

# bad version - send them across as is
# no unpacking or repacking

import email_observer
import cache


marketing = email_observer.EmailObserver()
temp = cache.Cache()

def get_events(count):
    events = marketing.get_events(count)
    return events
    # list how many events, that kind of thing

def store_events(events):
    cache.add_events(events)
    # return length of cache

def update(count=20):
    events = get_events(count)
    offset = store_events(events)
    result = (offset, events)
    return result

# for simplicity, visualize starting at 0
# that's on the observer. starting offset = 0
# then can load a later offset.




    
