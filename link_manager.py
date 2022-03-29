# link manager

class LinkManager:
    def __init__(self):
        self._by_ref = dict()
        # k is a string, v is the url
        self._by_url = dict()
        # k is a string (the url), v is a list of integers
        self._links = list()
        # ssot, list of strings
        self._refs = list()
        # list of strings too

        self._repeat_refs = True
        # if false, then a link that appears twice on the page will get two
        # different references

        self.handle = str
        
    def get_link(self, ref):
        result = self._by_ref.get(ref, None)
        return result

    def get_links(self, copy=True):
        result = self._by_ref
        if copy:
            result = self._by_ref.copy()
        return result

    def add_link(self, url):
        """

        -> string
        
        returns a reference
        
        """
        result = ""
        existing = self.get_ref(url)

        self._links.append(url)
        
        if existing:
            # I already have the url in my links
            
            if self.repeat_refs():
                result = existing
    
            else:
                # assign new ref
                result = self.make_ref(url)
        
        else:
            result = self.make_ref(url)
        # this block can be _get_ref(), but I already use this routine... 

        i = self._append_ref(result)
        locations = self._by_ref.setdefault(result, list())
        # could route through _get_locations()
        locations.append(i)

    def get_ref(self, url):
        result = self._by_url.get(url, None)
        return result

    def get_refs(self, copy=True):
        result = self._refs
        if copy:
            result = result.copy()
        return result       
        
    def check_repeats(self):
        result = self._repeat_refs
        return result
    
    def disable_repeats(self):
        self._repeat_refs = False
    
    def enable_repeats(self):
        self._repeat_refs = True    
    
    def make_ref(self, url):
        i = len(self._refs)
        result = self.handle(i)
        return result

    def change_ref(self, old, new):
        # in the ref:url dictionary, i need to remove the old and replace it
        # with the new
        # i then need to go through each place where the ref takes place and
        # replace it in _refs

        url = self._by_ref.pop(old)
        # think about how this works with uniques? should work automatically
        
        self._by_ref[new] = url
        locations = self._by_url[url]
        for location in locations:
            self._refs[location] = new

    # Non-public
    def _append_ref(self, ref):
        self._refs.append(ref)
        return len(self._refs)

class View:
    def __init__(self):
        self.links = LinkManager()

    def print(self):
        pass
        # easy to print as a string

yahoo = "www.yahoo.com"
bing = "www.bing.com"
link3 = yahoo
link4 = "www.chase.com"
links = [yahoo, bing, link3, link4]

def _run_test1():
    lm = LinkManager()
    return lm

def _run_test2(lm, *links):
    for link in links:
        lm.add_link(link)
    result = lm.get_refs()
    return result

def run_test():
    lm = _run_test1()
    refs = _run_test2(lm, *links)
    print(refs)
    
if __name__ == "__main__":
    run_test()
    
