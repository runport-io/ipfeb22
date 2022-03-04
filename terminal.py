import alternator
import cache
import scanner
import watchlist

class Shell:
    def __init__(self):
        self.watchlist = watchlist.Watchlist()
        self.events = None
        # cache
        self.scanner = scanner.Scanner()
        self.alternator = alternator.Alternator()
        # manages the cycle

    def brand_events(self, events):
        brands = self.watchlist.get_uniques()
        self.scanner.scan(events, brands)

    def refresh_brands(self):
        flat_watchlist = self.watchlist.flatten()
        events = self.get_events()
        for event in events:
            new = event.brands.get_new(flat_watchlist)
            # returns flat_watchlist - brands in index
            result = self.scanner.scan(event, new)
            # modifies event?
            # if not: event.brands.record_location(result)

    def load_events(self, count=20):
        events = self.alternator.pull(count)
        return events
        # check_brands?

    def view_all(self):
        # returns all events
        pass

    def filter_events(self, events, watchlist):
        # filters by watchlist
        pass

    def update(self):
        events = self.alternator.pull(n)
        # arrive inflated; should i do that here or there? let's say in there
        branded_events = self.iron(events)
        # inflates and brands
        if not hurry:
            self.acdc.save(branded_events)
            # can be optional
        # print events somehow
        self.hp.print(branded_evens)
            # really want to see these as bars
        return branded_events
    
    def exit(self):
        pass
        # for event in cache:
            # if event.has_metadata():
            #   event.save
            
        # performs the burn operation
        # clear cache completely

    
def run_test1():
    s = Shell()
    return s

def run_test2(shell):
    shell.watchlist.add_brand("yo")
    shell.watchlist.add_brand("nike")
    events = shell.load_events(count=10)
    print("length of events:")
    print(len(events))
    print("first event")
    print(events[0])
    
    branded_events = shell.brand_events(events)
    # is this an in-place change?
    
    events = shell.filter_events()
    return events

def run_test3():
    pass
    # print the events as lines over days. use sorter and graphing.

def run_test():
    shell = run_test1()
    run_test2(shell)
    
if __name__ == "__main__":
    run_test()
    


        

    
    
