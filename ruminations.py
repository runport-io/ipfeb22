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

    def draw_strings_as_columns(self, *strings):
        # let's say it's one string
        heights = list()
        adj_columns = list()
        
        for string in strings:
            height = len(string)
            heights.append(height)
            # height can be a property of column
            adj_column = copy.copy(col)
            
        # add block for managing max height
        # cap height at ceiling, say 40
        
        row_count = max(heights)
        rows = list()

        i = 0
        while i < row_count:
            row = list()
            for col in strings:
                pass

    def pad_string(self, string, length, fill=constants.SPACE):
        """
        -> string

        Function returns a string padded to the length you specify. [Function
        will truncate string if string is longer than length].
        """
        result = ""
        starting_length = len(string)
        if starting_length > length:
            raise exceptions.OpError
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

def run_test(string):
    run_test1(string)

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


    
