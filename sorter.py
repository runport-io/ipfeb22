# Copyright Port. Prerogative Club ("the Club")
#
# 
# This file is part of Port. 2.0. ("Port.")
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
import math

# 2) Port.
import exceptions
import utilities

class Sorter:
    HOUR = 3600
    DAY = 86400
    WEEK = 604800
    
    def __init__(self):
        pass

    def count_periods(self, start, stop, length):
        """

        count_periods() -> int
        
        """
        distance = stop - start
        count = distance / length
        result = math.ceil(count)
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
            period, remainder = self.fill_period(period, events)
            events = remainder
            
        # should have no events left in events here
        if events:
            c = "Some events not sorted."
            print("Length of events: ", len(events))
            print(events)            
            raise exceptions.OperationError(c)

        return periods
        # consider returning events too?

    def fill_period(self, period, events):
        remainder = list()
        for event in events:
            timestamp = event.get_timestamp()
            status = period.includes(timestamp)
            if status:
                period.append_to_contents(event)
            else:
                remainder.append(event)
                # timestamp not in period
        return (period, remainder)

        
    def sort_events_by_timestamp(self, events):
        """
        -> list
        """
        def by_timestamp(event):
            return event.get_timestamp()

        result = sorted(events, key=by_timestamp)
        return result

    def split_events_into_periods(self, events, period_length, sort=False):
        """

        () -> list

        Returns list of periods
        """      
        if sort:
            events = self.sort_events_by_timestamp(events)
        print(events)
        start = events[0].get_timestamp()
        end = events[-1].get_timestamp()

        periods = self.make_periods(start, end, period_length)
        self.fill_periods_with_events(periods, events)
        # changes periods in place

        return periods

class Period:
    def __init__(self, start=None):
        self.start = start
        self.stop = None
        self.contents = None

    def __str__(self):
        string = utilities.make_string(self)
        return string
        
    def get_lines(self):
        result = list()
        line1 = "Period "
        result.append(line1)
        
        line2 = "Start: " + str(self.start)
        result.append(line2)

        line3 = "Stop: " + str(self.stop)
        result.append(line3)

        line4 = "Contents: \n" + str(self.contents)
        result.append(line4)

        return result

    def append_to_contents(self, obj):
        """

        -> None
        """
        if self.contents is None:
            self.contents = list()
        self.contents.append(obj)
    
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
        if self.start <= timestamp <= self.stop:
            result = True
        return result
        
# could add an alt_sort:

# for event in events:
#   timestamp = event.get_timestamp()
#   if timestamp not in lookup.keys():
#       period = Period(start=something)
#
# go through each event, make a period on the fly
# if the events are sorted, it is easier
# but if not:
# i have to record the hypothetical start
#   bring that down if i find one that is lower
#
# this is all fine and good
# but the thing i am sorting on is days
# units of time
# i could piggyback on the time routine.


    
