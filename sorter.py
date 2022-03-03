# curator
# goal: get emails, display them
# perform filtering
# get emails: controller.get_emails()
# display them:
#  for event in events:
#    view = EventView(event)
#    ## alts: Event.view(); add this to the viewer
#    ## have a function: view_small() ->, view_big() ->

# what else:
#   I want a chart of emails over the last 7 days
#   I want axes labelled

class Sorter:
    def __init__(self):
        pass

    def count_periods(self, start, stop, length):
        """

        count_periods() -> int
        
        """
        distance = start - stop
        count = distance / length
        result = roundup(count)
        return result

    def make_periods(self, start, end, length):
        """

        -> list

        Method returns a list of periods. 
        """
        result = list()
        i = 0

        count = self.count_periods(start, end, length)

        while i < count:
            period = Period(start)
            start = period.set_length(length)
            # sets the next starting point to the end of this one
            result.append(period)
            i = i + 1

        return result
    
    def fill_periods_with_events(self, periods, events, trace=False):
        """

        -> list

        IN PLACE
        """
        # let's pretend events is a list in order
        for period in periods:
            event = events.pop(0)
            timestamp = event.get_timestamp()
            if period.includes(timestamp):
                period.contents.append(event)
                # woah woah
            else:
                continue

        # should have no events left in events here
        if events:
            c = "Some events not sorted."
            raise OperationError(c)

        return periods
        # consider returning events too?

    def sort_events_by_timestamp(self, events):
        """
        -> list
        """
        def by_timestamp(event):
            return event.get_timestamp()

        result = sorted(events, key=by_timestamp)
        return result

    def split_events_into_periods(self, events, period_length, trace=False):
        """

        () -> list

        Returns list of periods
        """      
        ordered_events = self.sort_events_by_timestamp(events)
        start = ordered_events[0].get_timestamp()
        end = ordered_events[-1].get_timestamp()

        periods = self.make_periods(start, end, period_length)
        self.fill_periods_with_events(periods, ordered_events)
        # changes periods in place

        return periods

class Period:
    def __init__(self, start=None):
        self.start = start
        self.stop = None
        self.contents = None

    def set_length(self, length):
        """
        -> None
        """
        self.stop = self.start + length
        return self.stop

    def includes(self, timestamp):
        """
        -> bool
        """
        result = False
        if self.start <= timestamp <= self.end:
            result = True
        return result
        
# if this code works:
  # i need to get the data - in json - make it into something eaiser to handle
  # then sort the events [done]
  # make views for the event:
        # here, that means "*" to start
        # sizes 1 through 4. 1: "*", 2: "br", 3: is the one I have with the box
        # 4 is full screen? 
  # then create a view object:
      # the view object takes a series of events and splits them into screens
      # it has some state, so I can go back and forth

    
    
