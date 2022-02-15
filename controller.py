# Controller
# part of Port. 2.0
# (c) 2022
# 
# Module manages flow of information
#

from . import observer

import time

# launch observers
marketing = observer.GmailObserver("marketing")
# add marketing login

personal = observer.GmailObserver("personal")
# add personal login

# set up storage, one file per co?
# set up delivery interface

memory = dict()
MOST_RECENT = "Most recent"

def do_smtg(x):
	pass
	# results = marketing.check()
	# storage.store(results)
	# results2 = personal.check()
	# storage.store(results2)
	## results should be now stored in SSOT, single timeline, by timestamp, with offset
	## 

def get_events(offset=0, batch=None):
	pass
	# returns batch of events starting at offset

# for observer in observers:
#       events = observer.check()
#       events = normalize(events) #? is this right? should i be normalizing
#       # at the edge
#       storage.record(events)
#       parser.parse(events) # this figures out the brands that are on there,
#       ## may be also a score for significance

def start(offset=None):
        pass
        # launch observers
        # print "Observers launched"
        # launch storage
        # print "Storage launched"
        
        # return offset of most recent event

def get_events(brands, batch=BATCH):
        """
        get_events() -> dict
        
        takes a dictionary of brands:offsets and returns brands:events
        """
        result = dict()

        # first, check cache
        check_storage = set()
        for brand, offset in brands.items:
                if brand in cache:
                        events = cache[brand][offset:(offset+batch)]
                else:
                        check_storage.add(brand)
                result[brand] = events

        # second, check storage?
        for brand in check_storage:
                storage.get_events(brand, offset, batch)

        return result

def monitor(seconds=300):
        """
        monitor() -> None

        Checks VCRs, records, checks trends, prints to stout. Wait, repeat.
        """

        # should give guest interrupt
        timeout = something(seconds)
        while True:
                tapes = list()
                cache = set()
                
                for vcr in vcrs:
                        tape = vcr.retrieve_tape()
                        print(time.time, "collected tape from", vcr)
                        tapes.append(tape)

                for tape in tapes:
                        events = parser.read(tape)
                        print(time.time, "parsed %events from %vcr")
                        # format of events should be: list? probably. not keyed.
                        cache.add(events)

                storage.record(events)
                print(time.time, "recorded x events")

                update_cache()
                # should load the 100 most recent events into cache, plus x by brands

                measure_trends()
                # checks stuff

                comment = input("pause or continue?")
                if comment times out
                timeout.wait()


def measure_trends():
        measure_volume()
        measure_identity()

def measure_volume():
        for brand in watchlist:
                events = library.get_events(start, end)
                if events > trailing_avg * (1+ margin):
                        print "something going on with brand"
                elif events < trailing_avg * (1 - margin):
                        print "something going on with brand"
                else:
                        continue

def update_cache(memory, events):
        """

        Takes processed events, tagged with names and timestamps? Puts them into
        memory. 
        """
        # get 100 most recent
        memory[MOST_RECENT] = library.get_most_recent(DEPTH)
        
        # get for each brand in watchlist
        for brand in watchlist:
                # assumes flat?
                memory[brand] = library.get_brand(brand)

        return memory

# storage management
# I want cache to always have the last 100 events, + up to [20] events by brand,
# up to [200] events, or [x] bytes

# cycle:
# if monitor:
#       for each observer:
#               events = check observer
#               ## returns a bunch of events; now i should map then against the
#               ## watch list and organize them by time.
#               ## to map events against a watchlist, i take the watchlist,
#               ## flatten it, that's set a. Take the event, turn it into one
#               ## string and check what brands are in the string. I can do
#               ## slow: loop through each brand in the watchlist, use
#               ## string.find(x) or something similar. Faster is tokenize the
#               ## event, namely, return a list of strings that represent
#               ## every word. Can also do both: tokenize, check, then check
#               ## against search.

#               # organize the events by time:
#               # use the built in sort function. but really this operation
#               # should take place after I can pull from each of the observers.
#               # or should it? may be i should sort each time i pull

        
        

        

        
        
        








	




