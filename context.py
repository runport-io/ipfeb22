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

"""

Module provides functions for quoting text.

------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:
FLAG                character(s) used to highlight a mention
LENGTH              number of characters to sample for context

FUNCTIONS:
add_flag()          adds characters on either side of a string
get_context()       see what's around a span in a text
------------------  ------------------------------------------------------------
"""

# Imports
# 1) Built-ins

FLAG = "*"
LENGTH = 100

def add_flag(string, flag=FLAG):
    """

    add_flag() -> string

    Function adds the flags on either side of the string. 
    """
    flagged = flag + string + flag
    return flagged

def get_context(text, span, length=LENGTH, add_flag=False):
    """

    get_context() -> string

    Function returns a string that samples characters from text on each side of
    the span. If you want, you can add a flag ("this is *a flag*") around the
    span. 
    """
    start, end = span
    mention = text[start:end]
    if add_flag:
        mention = add_flag(mention)

    prefix_start = start - length
    if start >= 0:
        prefix_start = max(0, prefix_start)
        # I am avoiding wrapping around the front unintentionally
    prefix = text[prefix_start:start]

    suffix_end = end + length
    suffix = text[end:suffix_end]

    snippet = prefix + mention + suffix
    return snippet

    

    

    
        
        
    
