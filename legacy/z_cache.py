# cache
# (c) Port. Prerogative Club 2022

class Cache:
    def __init__(self):
        self.hose = list()
        self.topics = dict()
        self.events = dict()

    def update_event(self, event):
        """
        Return none
        """
        existing = self._events[event.id]
        existing.update(event)

    def update_hose(self, eids):
        """
        update_hose(eids) -> eids
        eids should be a list
        return list of event ids that are new
        """

    def update_events(self, *events):
        for event in events:
            self.update_event(event)

    def update(self):
        # get most recent ids from storage
        # fill in the details on those missing
        # get flat list of brands from watchlist
        # for each brand in that list:
            # get event ids from storage
            # update the topic, get back what's missing
            # update the events
        pass

    def update_index(self, eids, trace=False):
        """
        takes a dictionary of brands to events, 
        returns list of missing events
        
        """
        missing = set()
        
        most_recent = eids.pop(None)
        print("Most recent:   ", len(most_recent))
        self.hose = most_recent.copy()
        for event in most_recent:
            if event.id not in self.events.keys():
                missing.append(event.id)
                # will probably break
                print("Missing:   ", event.id)

        for (brand, event_ids) in eids.items():
            missing_for_brand = self.update_topic(brand, event_ids)
            missing = missing + missing_for_brand

        ## what if cache now exceeds size
        self.run_garbage_collection()
        # removes delinked things?
        
        return missing

    def update_topic(self, brand, event_ids):
        """
        Returns None
        automatically creates new topics
        """
        self._topics[brand] = event_ids.copy()


    def collect_garbage(self):
        # find topics that have not been updated
        # delete them
        # find events that are not referenced anywhere
        # delete them

    def collect_events(self, ids_to_collect, trace=False):
        pass
        # for event in self.events.keys():
            # if event.id not in any of the post-lookup things
            # then remove the event

        mapping = self.get_mapping()
        mapped_event_ids = self.get_event_ids(mapping)

        stored_event_ids = self.events.keys()

        stored_but_not_mapped = stored_event_ids - mapped_event_ids
        # set op

        for event_id in stored_but_not_mapped:
            event = self.events.pop(event_id)
            if trace:
                print("Removed: ", event.id)        
                
    def get_event_ids(self, mapping):
        # returns all event ids
        result = set()
        for eids in mapping.values():
            result.extend(eids)
        return result
    
    def get_map(self):
        # returns a map of all topics to events
        result = dict()
        for topic, events in self.topics.items():
            result[topic] = events.copy()
        return result
        
    def connect_storage(self):
        pass
        # ideally would not connect storage.
        

    

