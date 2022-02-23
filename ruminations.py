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
# N/a

# Port.
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

# can generalize to draw column, or something like that
# columns = x, bottom of each column, pad to x width

# draw the columns themselves
# let's just say i want the column to be full  of stars
#   *
#   *   *
# * * * *
# * * * *
# * * * *   *
# * * * * * *
# -----------
# M T W T F S
# 21    24
# Feb. 2022

# drawing columns consists of putting white space in the rows
# or the symbol

# this is where a timeline object is useful
# timelines have a length

# i can chart timeline. 


    
