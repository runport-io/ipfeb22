# controller 2

# launch observers
# have a function called get_events()
# get the events
# put them in the cache

# bad version - send them across as is
# no unpacking or repacking

import cache
import email_observer

import observ2
# I am importing this just for the credentials

marketing = email_observer.EmailObserver()
temp = cache.Cache()

guest, token = observ2.load_credentials()
marketing.activate(token)
# need to have a flag of some sort here: marketing.is_active() -> bool

def get_events(count, offset):
    events = marketing.get_events(offset=offset, count=count)
    # < --- change this
    return events
    # list how many events, that kind of thing

def store_events(events):
    cache.add_events(events)
    # return length of cache

def update(count=20, offset=0):
    events = get_events(count, offset)
    offset = temp.add_events(events)
    # offset is None, current implementation does not track offsets across
    # channels.
    result = (offset, events)
    return result

# for simplicity, visualize starting at 0
# that's on the observer. starting offset = 0
# then can load a later offset.




    
