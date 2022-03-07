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
import time

class Period:
    def __init__(self, start=None):
        self.start = start
        self.stop = None
        self.contents = None

    def __hash__(self):
        result = (self.start, self.stop)
        return result
        
    def __str__(self):
        string = utilities.make_string(self)
        return string

    def append_to_contents(self, obj):
        """

        -> None
        """
        if self.contents is None:
            self.contents = list()
        self.contents.append(obj)

    def check_timestamp(self, timestamp):
        """

        check_timestamp() -> bool

        Method returns True if the timestamp falls in the interval defined by
        [period.start, period.stop).
        """
        result = False
        if self.start <= timestamp < self.stop:
            result = True
        return result

    def get_length(self):
        length = self.stop - self.start
        return length

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
        
    def get_start_as_local(self):
        result = time.localtime(self.start)
        return result

    def get_stop_as_local(self):
        result = time.localtime(self.stop)
        return result

    def get_start_as_string(self):
        result = time.ctime(self.start)
        return result

    def get_stop_as_string(self):
        result = time.ctime(self.stop)
        return result
        
    def set_length(self, length):
        """
        -> None
        """
        self.stop = self.start + length
        return self.stop
