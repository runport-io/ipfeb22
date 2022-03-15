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
import constants
import list_reader as reader
import serializer
import utilities as up

# 3) Constants
# N/a

# 4) Functions
class Watchlist:
    """
    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    N/a
    
    FUNCTIONS:
    add_brand           adds a brand to a group
    add_group           adds a group of brands
    get_group           retrieves a group of brands
    get_lines           gets a list of strings for printing the instance
    get_uniques         returns a set of brands in instance
    from_flat           constructs instance from dictionary
    update              updates instance from dictionary
    ------------------  --------------------------------------------------------
    """
    
    def __init__(self):
        self._groups = dict()

        # self._index = dict()
        # two structures: index, and filters
        # index: brand, keyed by string
        # groups:
        #
        # None: [1, 2]
        # blah: [2, 3]  

    def __str__(self):
        lines = self.get_lines()
        glue = constants.NEW_LINE
        string = glue.join(lines)
        return string
        
    def add_brand(self, brand, group_name=None, trace=False):
        """

        Watchlist.add_brand() -> None

        Method adds brand to the group you name. Delegates to add_group and
        creates the group if it does not exist. 
        """
        group = self.add_group(group_name, brand)
        if trace:
            print(group)
        
        # register brand in the index
        # num = len(self._index)
        #   self._index[brand] = num
        ## what if it is already there?

    def add_group(self, group_name, *brands):
        """

        Watchlist.add_group() -> list

        Adds brands to the group you name in the call. If the group already
        exists, appends brands to the group. 
        """
        new = list()
        group = self._groups.setdefault(group_name, new)
        group.extend(brands)
        
        return group

    def get_group(self, group_name=None):
        """

        Watchlist.get_group() -> group

        Method returns the group (a list) you specify. If you don't specify a
        name, method returns the group "None".
        """
        group = self._groups[group_name]
        return group

    def get_lines(self, include_header=True):
        """

        Watchlist.get_lines() -> list

        Method returns list of strings that represent the instance. Shows only
        the groups.
        """
        data = self._groups
        lines = up.get_lines(data, include_header=False)

        # We will add a header on our own"
        if include_header:
            header = str(type(self))
            lines.insert(0, header)

        return lines

    def get_uniques(self):
        """
 
        Watchlist.get_uniques() -> set

        Method returns a set of the entries in all of the groups.
        """
        result = set()
        for group, brands in self._groups.items():
            uniques = set(brands)
            result.update(uniques)

        return result
        
    @classmethod
    def from_flat(cls, data, keep_data=False):
        """

        Watchlist.from_flat() -> Watchlist

        This is a class method. Constructs instance, fills it with data.
        """
        new = cls()
        new.update(data)
        return new

    @classmethod
    def load(cls, path, keep_data=False):
        """

        Watchlist.load() -> Watchlist

        **Class Method**
        
        Method populates an instance with data from a file. If you turn off
        keep_data, method will discard any details about each brand other than
        its name.
        """

        data = reader.load(path)
        if not keep_data:
            data = reader.simplify(data)

        result = cls()
        result.update(data)

        return result

    def update(self, data):
        """

        Watchlist.update() -> None

        Method updates instance with data. 
        """
        self._groups.update(data)

# Testing
_LOCATION = r"C:\Users\Ilya\Dropbox\Club\Product\Watchlist CSV.csv"

def run_test1():
    w = Watchlist()
    print(w)

    w.add_brand("Birch Coffee")
    print(w)

    w.add_brand("S'well")
    w.add_brand("Piccolina Kids")
    print(w)

    coffee = w.add_group("coffee", "Starbucks", "Birch Coffee", "Variety")
    print(coffee)
    print(w)

    uniques = w.get_uniques()
    print(uniques)

    data = serializer.flatten(w)
    print(data)

    new = w.from_flat(data)
    print(new)

    # adjust pretty print to show the group name in line, or something

def run_test2(path):
    w = Watchlist.load(path)
    return w

def run_test(path=_LOCATION):
    run_test1()

    result = run_test2(path)
    print(result)
    return result

if __name__ == "__main__":
    run_test()
