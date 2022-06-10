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
# N/a

# 2) Port.
from . import Moment

# 3) Constants
MINUTE = 60
# Expressed in seconds
HOUR = 60 * MINUTE
DAY = 24 * HOUR

# 4) Functions
class Interval:
    """

    Class defines a distance between two points in time. The idea is to simplify
    the generation of Intervals that walk back or forward in time. 
    """
    
    def __init__(self, start=None, default_length=DAY):
        self.start = Moment()
        self.end = Moment()
        self._default_length = default_length
        self.set_start(start)

    def get_length(self):
        start = self.start.get_seconds()
        end = self.end.get_seconds()
        result = end - start
        return result

    def get_seconds(self):
        start = self.start.get_seconds()
        end = self.start.get_seconds()
        result = (start, end)
        return result

    def set_start(self, seconds, length=None):
        self.start.set_seconds(seconds)
        if length is None:
            length = self._default_length
        end = seconds + length
        self.end.set_seconds(end)

    def set_end(self, seconds, length=None):
        self.end.set_seconds(seconds)
        if length is None:
            length = self._default_length
        start = end - length
        self.start.set_seconds(start)

    def set_default_length(self, seconds):
        self._default_length = seconds

    def get_default_length(self):
        return self._default_length

    def copy(self):
        new = Interval()
        new.start = self.start.copy()
        new.end = self.end.copy()
        new.set_default_length(self._default_length)

        return new
        # could have a general purpose copying routine
    
# Testing
# 1) copy an interval
# 2) set start, check end
# 3) set end, check start
# 4) set start, end, check length
# 5) get the dates
# 6) get the dates and times

# time is a float or a series of tuples

# go_back_one_day()
# go_fwd_one_day()
# advance(lengt=DAY)
# retreat(legnth=DAY)

