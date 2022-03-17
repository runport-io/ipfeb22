# Copyright Port. Prerogative Club ("the Club")
#
# 
# This file is part of Port. 2 ("Port.")
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
# N/a

# 2) Port.
import alternator
import cache
import camera
import event_wrapper
import gui
import scanner
import scheduler
import watchlist

# 3) Constants
# N/A

# 4) Functions
class Shell:
    def __init__(self):
        self._offset = 0
        self._saved_offsets = list()
        self.alternator = alternator.Alternator()
        # manages the cycle for retrieval
        self.cache = cache.Cache()
        self.scanner = scanner.Scanner()
        self.scheduler = scheduler.Scheduler()
        self.watchlist = watchlist.Watchlist()
       
    def brand_events(self, events, trace=False):
        """

        Shell.brand_events() -> container

        Method returns the container of events with brands attached to each one.
        """
        brands = self.watchlist.get_uniques()
        
        for event in events:
            matches = self.scanner.scan(event, brands)

            if trace:
                print(matches)
            
            for brand, locations in matches.items():
                for start, end in locations:
                    event.body.index.add_location(brand, start, end)

        return events

##    def exit(self):
##        pass
##        # for event in cache:
##            # if event.has_metadata():
##            #   event.save
##            
##        # performs the burn operation
##        # clear cache completely
##        # <----------------------------------------------------remove for now?

    def filter_events(self, events, brands=None):
        """

        Shell.filter_events() -> list

        Method returns the subset of events, if any, that contain brands from
        the watchlist. You should brand events before passing them in.
        """
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

    def get_offset(self):
        """

        Shell.get_offset() -> int

        Method returns the offset for the instance.
        """
        result = self._offset
        return result
    
    def get_saved_offsets(self):
        """

        Shell.get_saved_offsets() -> list

        Method returns a list of offsets from the past.
        """        
        result = self._saved_offsets
        return result
        # this whole thing should be moved to an offsets attribute.

    def increment_offset(self, value):
        """

        Shell.increment_offset() -> int

        Method increases the offset by the value and returns the result.
        """
        old_offset = self.get_offset()
        new_offset = old_offset + value
        self.set_offset(new_offset)
        return new_offset
    
    def load_events(self, count=20, offset=None):
        """

        Shell.load_events() -> list

        Method returns a list of events from the alternator.
        """
        if offset is None:
            offset = self.get_offset()
        events = self.alternator.pull(count=count, offset=offset)
        self.increment_offset(count)
        return events
        # <---------------------------------check_brands?

    def load_offset(self, i=-1, save=True):
        """

        Shell.load_offset() -> 

        Method reverts the shell to an offset. By default, you go back to the
        last offset.
        """
        saved_offsets = self.get_saved_offsets()
        offset = saved_offsets[i]
        self.set_offset(offset,save=save)
        return offset
    
    def print_headlines(self, events):
        """

        Shell.print_headlines() -> None

        Method prints the headline for each event.
        """
        for event in events:
            print(event.get_headline())
        
    def refresh_brands(self):
        """
        NOT DONE

        Shell.refresh_brands() -> ?

        Method updates each event to match the watchlist. You run this after
        you make changes to the watchlist.
        """
        flat_watchlist = self.watchlist.flatten()
        events = self.get_events()
        for event in events:
            new = event.brands.get_new(flat_watchlist)
            # returns flat_watchlist - brands in index
            result = self.scanner.scan(event, new)
            # modifies event?
            # if not: event.brands.record_location(result)

    def reset_offset(self, save=True):
        """

        Shell.reset_offset() -> None

        Method sets the offset to 0.
        """
        self.set_offset(0, save=save)
        
    def save_offset(self, value):
        """

        Shell.save_offset() -> None

        Method saves the value in the container for offsets.        
        """
        self._saved_offsets.append(value)
        
    def set_offset(self, value, save=True):
        """

        Shell.set_offset() -> None

        Method sets the offset to the value. You can specify whether you want to
        remember the value that was in place before the change. 
        """
        if save:
            current = self.get_offset()
            self._saved_offsets.append(current)

        self._offset = value
    
    def update(self):
        """
        NOT DONE

        Shell.update() -> list

        Method pulls in events and checks them against the watchlist.
        """
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
        
    def view_all(self):
        """
        NOT DONE

        Shell.view_all() -> ?

        Method shows all events.
        """
        # returns all events
        pass

    def wrap_events(self, events):
        """

        Shell.wrap_events() -> list

        Method wraps each event in events in an EventWrapper.
        """
        result = list()
        for event in events:
            wrapper = event_wrapper.EventWrapper(event)
            result.append(wrapper)
        return result

# Testing
def run_test1():
    s = Shell()
    return s

def run_test2(shell, trace=False):
    shell.watchlist.add_brand("yo")
    shell.watchlist.add_brand("nike")
    events = shell.load_events(count=10)
    shell.cache.add_events(events)

    if trace:
        print("length of events:")
        print(len(events))
        print("first event")
        print(events[0])
    
    branded_events = shell.brand_events(events)
    # is this an in-place change? yes.
    
    filtered_events = shell.filter_events(branded_events)
    if trace:
        print ("Filtered events: ")
        print(filtered_events)
    
    return filtered_events
    # branded events are likely the same as filtered events

def run_test3(shell, events, trace=False):
    DAY = shell.scheduler.DAY
    periods = shell.scheduler.split_events_into_periods(events, DAY, sort=True)
    if trace:
        print("First period: ")
        print(periods[0])
    return periods
    
    # events come presorted by time. <-------------------------------- preserve?

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
        # need to manage that somehow <-----------------------------------------
        for line in lines: print(line)

def run_test4(shell, periods):
    _print_as_dots(shell, periods)
    _print_as_tiles(shell, periods)

def _test_batches(shell, count, offset, cycles):

    existing_offset = shell.get_offset()

    print("\n\n")
    print("Existing offset: ", existing_offset)

    shell.set_offset(offset)
    print("Starting offset: ", offset)
    
    batches = list()

    for i in range(cycles):
        print("Cycle #", str(i))
        print("\n")
        events = _test_batch(shell, count)
        batches.append(events)
    
    return batches

def _test_batch(shell, count):
    offset = shell.get_offset()
    print("**************************")
    print("Starting offset: ", offset)
    print("\n")

    events = shell.load_events(count=count)
    shell.print_headlines(events)
    
    offset = shell.get_offset()
    print("Offset after pull: ", offset)
    print("\n")

    return events

def run_test5(shell):
    batches = _test_batches(shell, count=4, offset=20, cycles=2)
    return batches

def run_test6(shell):
    batches = _test_batches(shell, count=4, offset=-20, cycles=2)
    return batches

def _run_test7():
    pass
    # load real watchlist, go through 100 events, see what comes up

def run_test():
    shell = run_test1()
    filtered_events = run_test2(shell)
    # populates cache #<----------------------------------------------- refactor
    events = shell.cache.get_events()
    periods = run_test3(shell, events)
    lines = run_test4(shell, periods)    
    
if __name__ == "__main__":
    run_test()
    


        

    
    
