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

"""

Module defines the TextField class. A TextField holds a string and information
about that string.

------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:

FUNCTIONS:

CLASSES:
TextField           Container for storing text and information about the text.
------------------  ------------------------------------------------------------
"""

# Imports
# 1) Built-ins
import json
import time

# 2) Port.
import constants

# 3) Constants
# N/a

# 4) Functions
class TimeStamp:
    """

    Place where we record time. 
    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    START_OF_TIME       reference time in float format
    time_of_observation time in float format
    time_of_receipt     time in float format

    FUNCTIONS:
    get_lines()         returns list of strings with attributes
    json_from()         enriches instance with data from string
    json_to()           returns string that represents data in JSON format
    set_observation()   records time of observation
    set_receipt()       records argument as time of receipt
    print()             prints    
    ------------------  --------------------------------------------------------
    """
    START_OF_TIME = time.mktime(constants.TIME_ZERO)
    
    def __init__(self):
        self.time_of_observation = None
        self.time_of_receipt = None        

    def get_lines(self, header=True):
        """

        TimeStamp.get_lines() -> list()

        Returns list of strings that describe instance.
        
        """
        result = list()

        if header:
            line1 = "TimeStamp  "
            result.append(line1)

        line2 = "Observed:   " + str(self.time_of_observation)
        line3 = "Recorded:   " + str(self.time_of_receipt)
        result.extend([line2, line3])

        return result

    @classmethod
    def from_json(cls, string):
        """

        TimeStamp.from_json() -> TimeStamp

        Expects a JSON string that represents dictionary of
        attributes. Returns instance of class populated with attributes.
        """
        data = json.loads(string)
        new = cls()
        new.__dict__.update(data)
        return new
    
##    def json_from(self, string, override=True):
##        """
##
##        TimeStamp.json_from() -> 
##        """
##        
##        data = json.loads(string)
##        if override:
##            self.__dict__.update(data)
##        else:
##            for k,v in data.items():
##                if k not in self.__dict__:
##                    self.__dict__[k] = v
##                    
##        # should really be a class method
        
    def json_to(self):
        """

        TimeStamp.json_to() -> string

        Returns a string in JSON location that represents a dictionary with
        its attributes. 
        """
        result = json.dumps(self.__dict__)
        return result

        # will have to change this if I start having attributes like hook.
        # how does a hook work if I have no state? probably doesn't. unless I
        # build the event up - first unpack all of the things, then connect
        # them.

    def print(self, glue=constants.NEW_LINE):
        """

        TimeStamp.print() -> None

        Prints data about instance.
        """
        result = ""
        strings = self.get_lines()
        result = glue.join(strings)
        print(result)

    def set_observation(self, trace=False):
        """

        TimeStamp.set_observation() -> time()

        Records the time at call as the time of observation. Returns time.
        """
        now = time.time()
        self.time_of_observation = now
        if trace:
            print(self.time_of_observation)
            
        return now
            
    def set_receipt(self, time):
        """

        TimeStamp.set_receipt() -> None

        Method records the time you specify as the time of receipt.
        """
        self.time_of_receipt = time
        return None

# Testing

def run_test():        
    ts1 = TimeStamp()
    print("ts1: ")
    ts1.print()
    ts2 = TimeStamp()
    print("ts2: ")
    ts2.print()

    ts1.set_observation(trace=True)
    print("ts.set_observation()")
    print("ts1: ")
    ts1.print()

    flat = ts1.json_to()
    print(flat)

    ##ts2.json_from(flat)
    ##ts2.print()

    ts3 = TimeStamp.from_json(flat)
    ts3.print()

if __name__ == "__main__":
    run_test()
