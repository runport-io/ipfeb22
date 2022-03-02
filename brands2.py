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

Module defines a container for metadata called Brands.

------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:

FUNCTIONS:

CLASSES:
Brands              A directory of names that a text contains.
------------------  ------------------------------------------------------------
"""

# Imports
# 1) Built-ins
# N/a
# 2) Port.
# N/a

class Brands:
    """
    
    This object records the locations of substrings and provides methods to
    retrieve data about these substrings. 

    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    
    FUNCTIONS:
    add_location        Records the location of a brand in the index
    get_brands          Returns a set of keys from the index          
    get_count           Returns the number of occurences for a brand
    get_counts          Returns a dictionary of brands to occurences
    get_first           Returns the first brand in the inde
    get_inverted        Returns a map of location to brand
    get_locations       Returns all locations for the brand
    get_ranked          Returns a list of brands ordered by number of occurences
    get_snippet         Returns a string of specified length around the brand
    ------------------  --------------------------------------------------------
    """
    def __init__(self):
        self._index = dict()

    def add_location(self, brand, start, end=None):
        """

        add_location() -> None

        Method add a tuple of (start, end) to the set of locations for the
        brand. If you do not specify "end", method computes it as start +
        len(brand). 
        """
        index = self.get_index(copy=False)
        # get the real thing
        locations = index.setdefault(brand, set())
        
        if not end:
            end = start + len(brand)
        span = (start, end)
        if span not in locations:
            locations.add(span)

    def get_brands(self):
        """

        get_brands -> set()
        
        Method returns a set of brands that appear on the event. 
        """
        index = self.get_index()
        brands = index.keys()
        result = set(brands)
        return result

    def get_count(self, brand):
        """

        get_count() -> int

        Method returns the number of occurences for the brand you specify.
        """
        locations = self.get_locations(brand)
        result = len(locations)
        return result

    def get_counts(self):
        """

        get_counts() -> dict

        Method returns a dictionary where the keys are brands and the values are
        the number of locations of that brand.
        """
        result = dict()
        index = self.get_index()
        for k, v in index.items():
            result[k] = len(v)
        return result

    def get_first(self):
        """

        get_first() -> string
        
        Method locates the first brand that appears in the string. 
        """
        by_location = self.get_inverted()

        locations = by_location.keys()
        ordered = sorted(locations)
        
        first = ordered[0]
        brand = by_location[first]
        
        return brand
        
    def get_index(self, copy=True):
        """

        get_index() -> dict

        Method returns the dictionary that maps brands to locations for the
        instance. If you specify "copy" to be True, method copies the
        dictionary before returning it, so you can manipulate it without
        changing the instance.    
        """
        index = self._index
        if copy:
            index = index.copy()
        return index

    def get_inverted(self, brands=None):
        """

        get_inverted() -> dict

        Method returns a map of start:brand for all brands in the index. You can
        input a container of brands as "brands" to see locations only for those
        brands.
        """
        result = dict()
        index = self.get_index()
        
        if not brands:
            brands = self.get_brands()
            
        for brand in brands:
            spans = index[brand]
            for start, end in spans:
                result[start] = brand

        return result      
    
    def get_locations(self, brand):
        """

        get_locations() -> set

        Method returns a list of locations for the brand in the instance, based
        on data you recorded in the index. 
        """
        index = self.get_index()
        locations = index.get(brand, default=set())
        result = locations.copy()
        return result

    def get_ranked(self, length=None):
        """

        get_ranked() -> list

        Method returns a list of tuples of (brand, count), ranked by count. If
        you specify length, method truncates result to that length. 
        """
        counts = self.get_counts()
        ranked = sorted(counts.items(), key=lambda item: item[1])
        # sort by number of occurences
        if length:
            ranked = ranked[:length]
        return ranked

