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
# N/a

# 3) Constants
# N/a

# 4) Functions
class Moment:
    """

    Class provides an adapter to the built-in time library. You can modify
    formats if you want to adjust the output.
    
    """
    DATE_ONLY = "%Y-%m-%d"
    DATE_TIME = DATE_ONLY+"T%H:%M:%S"
    
    # Formats follow ISO 8601, as requested by NewsAPI. 
    
    def __init__(self, seconds=None):
        if seconds is None:
            seconds = time.time()
            
        self._seconds = seconds
        self._date_only = DATE_ONLY
        self._date_time = DATE_TIME
        # rewrite in case I want to modify these later without forgetting the
        # default

    def get_date_only_format(self):
        """

        get_date_only_format() -> string

        Method returns the string used to format output for
        get_string_of_date(). 
        """
        return self._date_only

    def get_date_time_format(self):
        """

        get_date_only_format() -> string

        Method returns the string the instance uses to format output when you
        call get_string(). 
        """
        return self._date_time
        
    def get_seconds(self):
        """

        get_seconds() -> float

        Method returns the point in time the instance represents as the number
        of seconds since the Epoch. 
        """
        return self._seconds

    def get_string(self, time_tuple=None, format=None):
        """

        get_string() -> string

        Method returns a string that shows the year, date, hours, minutes, and
        so on.
        """
        if time_tuple is None:
            time_tuple = self.get_tuple()

        if format is None:
            format = self.get_date_time_format()
            
        result = time.strftime(format, time_tuple)
        return result       

    def get_tuple(self):
        """

        get_tuple() -> tuple

        Method returns a container that describes the instance as 7 numbers.
        """
        seconds = self.get_seconds()
        result = time.localtime(seconds)
        return result

        # should be local or gmt, depending on toggle
        # gmt by default

    def get_string_of_date(self, time_tuple=None, format=None):
        if time_tuple is None:
            time_tuple = self.get_tuple()

        if format is None:
            format = self.get_date_only_format()
            
        result = time.strftime(format, time_tuple)
        return result    

    def set_seconds(self, seconds):
        """

        set_seconds() -> None

        Method sets the value for the time in seconds since the Epoch that the
        instance represents. 
        """
        self._seconds = seconds

    def set_date_only_format(self, string):
        self._date_only = string

    def set_date_time_format(self, string):
        self._date_time = string
