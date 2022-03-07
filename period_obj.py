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

# 2) Port.
import utilities

class Period:
    def __init__(self, start=None):
        self._start = start
        self._stop = None
        self._contents = list()

    def __hash__(self):
        result = (self._start, self._stop)
        return result
        
    def __str__(self):
        lines = self.get_lines()
        string = "".join(lines)
        return string

    def append_to_contents(self, obj):
        """

        -> None
        """
        self._contents.append(obj)

    def check_timestamp(self, timestamp):
        """

        check_timestamp() -> bool

        Method returns True if the timestamp falls in the interval defined by
        [period.start, period.stop).
        """
        result = False
        if self._start <= timestamp < self._stop:
            result = True
        return result

    def get_contents(self):
        result = self._contents
        return result
    
    def get_start(self):
        result = self._start
        return result

    def get_stop(self):
        result = self._stop
        return result
    
    def get_length(self):
        length = self._stop - self._start
        return length

    def get_lines(self):
        result = list()
        line1 = "Period " + repr(self) + "\n"
        result.append(line1)
        
        line2 = "Start: " + self.get_start_as_string() + "\n"
        result.append(line2)

        line3 = "Stop: " + self.get_stop_as_string() + "\n"
        result.append(line3)

        line4 = "Contents: \n" + str(self._contents)
        result.append(line4)

        return result
        
    def get_start_as_local(self):
        result = time.localtime(self._start)
        return result

    def get_stop_as_local(self):
        result = time.localtime(self._stop)
        return result

    def get_start_as_string(self):
        result = time.ctime(self._start)
        return result

    def get_stop_as_string(self):
        result = time.ctime(self._stop)
        return result
        
    def set_length(self, length):
        """
        -> None
        """
        self._stop = self._start + length
        return self._stop
