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
# 1) Built-ins
import time

# 2) Port.
# N/a

# 3) Constants
# N/a

# 4) Functions
def convert_to_tuple(string, trace=False):
    """

    -> time tuple
    """
    tokens = string.split()

    if trace:
        print(tokens)

    day = tokens[0]
    day = day.strip(",")
    
    if trace:
        print("Day: ", day)
        
    date = tokens[1]
    month = tokens[2]
    year = tokens[3]
    hhmmss = tokens[4]
    # skips the time zone for now
    
    alt_tokens = [day, month, date, hhmmss, year]
    if trace:
        print("Alt tokens: \n", alt_tokens)
    
    alt_string = " ".join(alt_tokens)
    if trace:
        print("Alt string: \n", alt_string)

    result = time.strptime(alt_string)
    return result


    
    
