# Watchlist
# (c) Port. Prerogative Club 2022

import group
import brand


class Watchlist:
    """
    ------------------  --------------------------------------------------------
    ------------------  --------------------------------------------------------
    Attribute           Description
    ------------------  --------------------------------------------------------
    DATA:
    
    
    FUNCTIONS:
    
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

    def add_brand(self, brand, group_name=None):
        """

        Watchlist.add_brand() -> None

        Method adds brand to the group you name. Delegates to add_group and
        creates the group if it does not exist. 
        """
        group = self.add_group(group_name, brand)
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

    def get_group(self, group_name):
        group = self._groups[group_name]
        return group

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

    def flatten(self):
        pass
        # result = dict()
        # groups = dict()
        # for k, v in self._groups.items():
        #   groups[k] = v.flatten()
        # index = dict()
        # for k, v in self._index:
        #   index[k] = v.flatten()
        # result["groups"] = groups
        # result["index"] = index
        #
        # return result
        
    def update(self, remove=False):
        pass
        # ops: if items were removed? if items were added
        # start with index:
        #
    
        # takes a flat repr and enriches accordingly

