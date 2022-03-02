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

Module contains logic for detecting mentions of brands in a string. 

------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:

FUNCTIONS:

CLASSES:
Scanner             Object the finds mentions of brands in a string.
------------------  ------------------------------------------------------------
"""

# Imports
# 1) Built-ins
import re
# 2) Port.
# N/a

class Scanner:
    """
    
    Object finds occurences of substrings.
    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    
    FUNCTIONS:
    index_brand()       Find all mentions of a brand in a string
    index_brands()      Find all mentions of multiple brands in a string
    scan()              Find all mentions of brands in the body of an event.    
    ------------------  --------------------------------------------------------
    """
    def __init__(self):
        pass

    def scan(self, event, brands, match_case=True):
        """

        scan() -> dict

        Method checks the event's body for the location of brands. You get a
        dictionary keyed to brand where the values are list of (start, end)
        tuples. 
        """
        body = event.get_body()
        
        if fold_case:
            body = body.casefold()
            folded_brands = set()
            
            for brand in brands:
                folded = brand.casefold()
                folded_brands.add(folded)

            brands = folded_brands      

        matches = self.index_brands(body, brands)                
        return matches       

    # this is the simple equivalent to the brands detection in parser.
    def index_brand(self, string, brand):
        """

        index_brand() -> list

        Method finds the location of each mention of the brand in the string.
        You get back a list of tuples showing the starting and ending location.
        """
        result = list()
        wip = re.finditer(string, brand)
        # wip is a generator
        for match in wip:
            span = match.span()
            result.append(span)

        return result

    def index_brands(self, string, brands):
        """

        index_brands() -> dict

        Method returns a dictionary of the locations of each brand in the
        string. 
        """
        result = dict()
        for brand in brands:
            spans = self.index_brand(string, brand)
            result[brand] = spans
        return result

    
            
           
