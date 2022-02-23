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
    
def run_test(string):
    run_test1(string)
    run_test2()

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


    
