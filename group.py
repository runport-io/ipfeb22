# Group
# (c) Port. Prerogative Club 2022

class Group:
    def __init__(self):
        self._contents = list()
        # is this supposed to be ordered? probably not

    def get_contents(self, copy=False):
        result = self._contents
        if copy:
            result = self._contents.copy()
        return result

    def add(self, brand):
        self._contents.append(brand)

    def get_uniques(self):
        result = set(self._contents)
        return result

    
        
        
