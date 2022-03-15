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
# Built-ins
import copy
import textwrap

# Port.
import constants
import event
import exceptions
import gui

class Chartist:
    def __init__(self):
        pass

    def draw_x_axis(self, width=80):
        line1 = "-" * width
        return line1

    def draw_month(self, width):
        result = list()
        line1 = self.draw_x_axis(width)
        # starting day? walk across the days
        # draw date every 4
        # draw month
        return list
        
    def draw_4_days(self, width):
        pass
        # same rows as month?

    def draw_strings_as_columns(self, strings, spacer=constants.SPACE,
                                top_down=True):
        """
        -> list

        Returns list of struings. If top_down is False, the list will start with
        the line that's at the bottom of the chart.
        """
        # let's say it's one string
        heights = list()
        
        for string in strings:
            height = len(string)
            heights.append(height)
            # height can be a property of column
            
        # add block for managing max height
        # cap height at ceiling, say 40
        
        row_count = max(heights)
        adj_columns = list()
        for column in strings:
            adj_column = self.pad_string(column, row_count)
            adj_columns.append(adj_column)
                
        rows = list()
        row_strings = list()

        i = 0
        while i < row_count:
            row = list()
            for column in adj_columns:
                cell = column[i]
                row.append(cell)
                
            rows.append(row)
            # row is a list of strings now
            
            row_string = spacer.join(row)
            row_strings.append(row_string)
            
            i = i + 1

        # no width management, function assumes you are passing in strings of
        # width 1.

        result = row_strings
        if top_down:
            result = result[::-1]
            # Routine creates rows at the bottom of the chart first.

        return result
        # row_strings ship without newlines

    def pad_string(self, string, length, fill=constants.SPACE):
        """

        pad_string() -> string

        Method returns a string padded to length with fill. If you specify a
        string that's longer than length, method will throw a ParameterError.
        """
        result = ""
        starting_length = len(string)
        if starting_length > length:
            c = "String {string} is longer than length {length}"
            lookup = {"string" : string, "length" : length}
            cf = c.format(**lookup)
            raise exceptions.ParameterError(cf)
            # can use textwrap to break into more manageable strings < length
            
        gap = length - starting_length
        length_of_fill = len(fill)
        fill_count = gap // length_of_fill + 1
        result = string + fill * fill_count

        result = result[:length]
        return result

    def pad_list(self, container, length, fill=None):
        """

        -> list

        """
        result = container.copy()
        starting_length = len(container)
        gap = length - starting_length
        if gap < 0:
            c = "Container is longer than length."
            raise exceptions.ParameterError(c)

        i = 0
        while i < gap:
            result.append(fill)
            i = i + 1

        result = result[:length]
        return result        

    def rotate_clockwise(self, rows):
        """

        -> list

        Function returns a list of lists that represent rows rotated 90 degrees.
        For example, if you start with [a, b, c], [d, e], you get [d, a],
        [e, b], [None, c].
        """
        new_rows = list()
        x = 0
        for row in rows:
            length = len(row)
            if length > x:
                x = length
            
        padded_rows = list()
        for row in rows:
            padded_row = self.pad_list(row, length=x)
            padded_rows.append(padded_row)
        # make routine, now all rows are equal length
        reversed_order = padded_rows[::-1]
        print("Reversed order:  \n", reversed_order)
        # [d, e], [a, b, c]

        i = 0
        while i < x:
            new_row = list()
            for starting_row in reversed_order:
                # [d, e]
                item = starting_row[i]
                # d; should work because I padded all rows to the same height.
                new_row.append(item)
                # [d].append(a)
            new_rows.append(new_row)
            #[[d, a]].append([e, b])
            i = i + 1

        return new_rows

    def draw_rows_as_columns(self, rows):
        pass
        # turn rows 3 times
        # for each row, join with spacer. check for width issues.
        #       # also check for height issues
        #       # may be event should return views: small, medium, large, xl?
        #       # a view can be defined as a list of strings
        # get all the strings
        # add legends if necessary
        # return

    def plot_events_over_days(self, events, days=4):

        days = dict()
##        i = 0
##        while i < days:
##            day = list()
##            days.append(day)
##            i = i + 1

        for event in events:
            day_of_event = event.timestamp.to_day()
            if day_of_event not in days.keys():
                days[day_of_event] = list()
                days[day_of_event].append(event)
            else:
                days[day_of_event].append(event)
                # but need to sort then within days
                # ideally would get in order of recency.
                # if not, use sets?

        return days

        # sort into buckets
        # then figure out how many days i want to print
        #   # function of screen size and type of view
        # then get strings or something? sort in some way I want
        # questions:
        #   should periods have markers in them for some reason?
        #   e.g., start
        #   may be there is a better way? 
        
# Testing
s1 = "ilya"
def run_test1(seed):
    dali = Chartist()
    s1a = dali.pad_string(seed, 60)
    print(s1a)
    s2a = dali.pad_string(seed, 60, fill="z")
    print(s2a)
    s1b = dali.pad_string(seed, 60, fill="!z")
    print(s1b)
    s2b = dali.pad_string(seed, 30, fill="abracadabra")
    print(s2b)

line1 = "*" * 4
line2 = "*" * 6
line3 = "*" * 4
line4 = "*" * 5
line5 = "*" * 1
line6 = "*" * 2
lines = [line1, line2, line3, line4, line5, line6]
def run_test2():
    vaka = Chartist()
    chart_lines = vaka.draw_strings_as_columns(lines)
    for line in chart_lines:
        print(line)

class Mock():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

a = Mock("a")
b = Mock("b")
c = Mock("c")
d = Mock("d")
e = Mock("e")
row1 = ["a", "b", "c", "d"]
row2 = ["e", "f"]
row3 = [a, b, c, d]
row4 = [e]
mivr = Chartist()

def run_test3():
    print(row1)
    result1 = mivr.pad_list(row1, 6)
    print(result1)
    
    print(row2)
    result2 = mivr.pad_list(row2, 6)
    print(result2)

def run_test4(rows):
    print(rows)
    result = mivr.rotate_clockwise(rows)
    print(result)
    return result       
    
def run_test(string):
    run_test1(string)
    run_test2()
    run_test3()
    run_test4([row1, row2])

if __name__ == "__main__":
    run_test(s1)      

# can generalize to draw column, or something like that
# columns = x, bottom of each column, pad to x width

# draw the columns themselves
# let's just say i want the column to be full  of stars
#
# 8|
# 7|   6 
# 6|   *   5
# 5| 4 * 4 *
# 4| * * * *
# 3| * * * *   2
# 2| * * * * 1 *
# 1| * * * * * *
#  + -----------
#    M T W T F S
#    21    24
#    Feb. 2022


# drawing columns consists of putting white space in the rows
# or the symbol

# this is where a timeline object is useful
# timelines have a length

# i can chart timeline. 


    
