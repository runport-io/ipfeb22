# curator

controller = blah
DAY = 0

class Projector:
    """

    Gets events, generates Views
    """
    def __init__(self):
        pass

    def get_view_by_day(self, events):
        """
        -> strings?
        """
        days = sorter.split_events_into_periods(events, period_length=DAY)
        # days are the columns
        # I can turn columns into rows already
        # I want to limit how many columns I print
        # I want to print the first 16 columns
        first_16 = days[:16]
        last_16 = days[-16:]

        # make view
        rows = rumi.turn_90(last_16)
        # rows contain objects
        # now the events are in lists that represent rows
        # I should print each row.
        
        epxanded_rows = list()
        # expanded rows contain lists of strings
        for row in rows:
            expanded_row = list()
            for event in row:
                view = viewer.get_view(event, size=1) # probably not quite
                # view is a list of strings
                expanded_row.append(view)

        return expanded_rows

    def expand_row(self, row):
        """

        -> list

        take list of objects or None, return a list of strings. the list of
        strings should have a length of n, where n is the height of the tallest
        obj.

        initially should break if objects are not all same height or width. 

        if None, should replace with substrings of equal width.
        """
        lines = self.prep_row_for_gluing(row)
        glue = self.glue
        glued = list()
        for line in lines:
            glue.join(line)
        return glued

    def prep_row_for_gluing(self, row, view, blank_char):
        """

        ->
        list of lists
        
        takes a row (list of events or None), expands events into a strings,
        checks that each event has the same width, replaces Nones with blank
        strings of the same width, returns.

        len of list is height of the view. so if the view is one char tall, then
        the len of result is 1. if it is 2 chars tall (br/n:)) then the result
        should be len-2.

        Each item in the result is a list of substrings that can be joined to
        form the row.
        """
        pass    

    # need a place to control the width of what I see. may be. or may be i
    # don't worry about it for now.
    
    def show_by_day_simplified(self, events):
        columns = list()
        
        days = sorter.split_events_into_periods(events, period_length=DAY)
        last_16 = days[-16:]
        for day in last_16:
            pass
            # day is a list of events. for each event, put a dot
            # column = "*" * len(day)
            # columns.append(column)

    def tag(self, event):
        pass
        # gets watchlist from self.
        # takes the body of the event, checks against the watchlist.
        # probably delegate to some sort of a thinking module, Scanner.


class View:
    """

    Holds state for what I am looking it, prints the state. 
    """
    def __init__(self):
        pass

import blah
import scanner
hp = scanner.Scanner()
watchlist = None
# something that gets the events
events = blah.get_events()
# inflate
# can also just try to print the event as is, with the dot

for e in events:
    hp.scan(e, watchlist)

# print the events as dots
# print the bar chart

# get more events
# print events as tiles



    
    
