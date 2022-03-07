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
import period_obj
import utilities

class Scheduler:
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

    def fill_period(self, period, events):
        """

        fill_period() -> tuple

        Method returns a tuple of the period and the events that do not fit
        into the period. You change the period in place.
        """
        remainder = list()
        for event in events:
            timestamp = event.get_timestamp()
            status = period.check_timestamp(timestamp)
            if status:
                period.append_to_contents(event)
            else:
                remainder.append(event)
                # timestamp not in period
        return (period, remainder)


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

    def make_periods(self, start, end, length):
        """

        -> list

        Method returns a list of periods. 
        """
        result = list()
        i = 0

        count = self.count_periods(start, end, length)

        while i < count:
            period = period_obj.Period(start)
            start = period.set_length(length)
            # sets the next starting point to the end of this one
            result.append(period)
            i = i + 1

        return result

    def make_number_of_periods(self, start, count, length=DAY):
        """

        make_number_of_periods() -> list

        Method generates a list of periods starting at the "start" date. If you
        don't specify the length, you default to DAY.
        """
        result = list()           
        start = start
        for i in range(count):
            period = period_obj.Period(start)
            period.set_length(length)
            start = period.end
            
            result.append(period)

        return result
    
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

    def pad_periods(self, periods, target, length=None, append=True):
        """
        -> list()
        
        Method creates a list of periods of length "count", where each blank
        period has the length "length". If you set "append" to "True", the
        list will include the blanks at the end, otherwise method will insert
        them before the periods you provide.
        """
        result = None
        wip = periods[:target]
        # wip can still be shorter than target, because I can do a slice of
        # len-3 list [:8]
        count = len(wip)
        if count == target:
            result = wip
        else:
            gap = target - count
            if length is None:
                length = self.DAY

            if append:
                start = wip[-1].end
                filler = self.make_number_of_periods(start, gap, length)
                result = wip + filler
                
            else:
                first_start = wip[0].start
                start = first_start - gap * length
                filler = self.make_number_of_periods(start, gap, length)
                result = filler + wip

        return result
