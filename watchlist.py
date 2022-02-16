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
        self._index = dict()
        self._groups = dict()     
        # two structures: index, and filters
        # index: brand, keyed by string
        # groups:
        #
        # None: [1, 2]
        # blah: [2, 3]  

    def add_brand(self, name, group_name=None):
        if group_name not in self._groups.keys():
            group = self.add_group(group_name)
        else:
            group = self.get_group(group_name)

        new = brand.Brand(name)
        group.add(new)
        
        # register brand in the index
        # num = len(self._index)
        #   self._index[brand] = num
        ## what if it is already there?

    def add_group(self, group_name):
        """

        """
        new = group.Group()
        place = self._groups.setdefault(group_name, new)
        return new

    def get_group(self, group_name):
        result = self._groups[group_name]
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

