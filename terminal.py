import alternator
import cache
import camera
import event_wrapper
import gui
import scanner
import scheduler
import watchlist

class Shell:
    def __init__(self):
        self.alternator = alternator.Alternator()
        # manages the cycle for retrieval
        self.cache = cache.Cache()
        self.scanner = scanner.Scanner()
        self.scheduler = scheduler.Scheduler()
        self.watchlist = watchlist.Watchlist()
        
    def brand_events(self, events):
        brands = self.watchlist.get_uniques()
        
        for event in events:
            matches = self.scanner.scan(event, brands)
            print(matches)
            for brand, locations in matches.items():
                for start, end in locations:
                    event.body.index.add_location(brand, start, end)

        return events

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

    def wrap_events(self, events):
        result = list()
        for event in events:
            wrapper = event_wrapper.EventWrapper(event)
            result.append(wrapper)
        return result

    def view_all(self):
        # returns all events
        pass

    def filter_events(self, events, brands=None):
        result = list()
        if brands is None:
            brands = self.watchlist.get_uniques()
        # brands is a set
        for event in events:
            mentions = event.body.index.get_brands()
            overlap = brands & mentions
            if overlap:
                result.append(event)

        return result

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

# Testing

def run_test1():
    s = Shell()
    return s

def run_test2(shell):
    shell.watchlist.add_brand("yo")
    shell.watchlist.add_brand("nike")
    events = shell.load_events(count=10)
    shell.cache.add_events(events)
    
    print("length of events:")
    print(len(events))
    print("first event")
    print(events[0])
    
    branded_events = shell.brand_events(events)
    # is this an in-place change? yes.
    
    filtered_events = shell.filter_events(branded_events)
    print ("Filtered events: ")
    print(filtered_events)
    
    return filtered_events
    # branded events are likely the same as filtered events

def run_test3(shell, events):
    DAY = shell.scheduler.DAY
    periods = shell.scheduler.split_events_into_periods(events, DAY, sort=True)
    print("First period: ")
    print(periods[0])
    return periods
    
    # events come presorted by time. <----------------------------- i ruin that

def _print_as_dots(shell, periods, rows=4):
    """

    -> lines
    
    Function prints each of the events in periods as a line of dots.
    """
    canon = camera.Camera()
    lines = list()
    padded = shell.scheduler.pad_periods(periods, target=rows)
    print("Padded result")
    print(padded)
    print("Length: " + str(len(padded)))
        
    for period in padded:
        line = ""
        for event in period.get_contents():
            dot = canon.get_dot_for_top(event)
            line = line + dot
        line = line + "\n"
        lines.append(line)
    wip = "".join(lines)
    print(wip)
    return lines
    
def _print_as_tiles(shell, periods, rows=4):
    """
    prints periods as rows. if periods < rows, adds periods of equal length
    after.
    
    """
    adjusted_periods = shell.scheduler.pad_periods(periods, target=rows)
    for period in adjusted_periods:
        print("Rendering period ...")
        print(period)
        
        events = period.get_contents()            
        lines = gui.render_row(*events)
        # row will be longer than 80 characters
        # need to manage that somehow <---------------------------------------------------------
        for line in lines: print(line)

def run_test4(shell, periods):
    _print_as_dots(shell, periods)
    _print_as_tiles(shell, periods)
    
def run_test():
    shell = run_test1()
    filtered_events = run_test2(shell)
    # populates cache #<--------------------------------------------------------------- refactor
    events = shell.cache.get_events()
    periods = run_test3(shell, events)
    lines = run_test4(shell, periods)    
    
if __name__ == "__main__":
    run_test()
    


        

    
    
