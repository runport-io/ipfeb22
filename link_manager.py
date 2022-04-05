# link manager

# Imports
# Port.
import list_writer


class LinkManager:
    def __init__(self):
        self._by_ref = dict()
        # k is a string, v is the url
        self._by_url = dict()
        # k is a string (the url), v is a list of integers?
        # or should this be k: to refs? then each ref points to a list of is?
        self._links = list()
        # ssot, list of strings
        self._refs = list()
        # list of strings too

        self._reuse_references = True
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
        reuse = self.check_reuse()
        exists = self.check_url(url)
        
        if reuse and exists:
            ref = self.get_first_ref(url)
            # remove the error handling here
        else:
            ref = self.make_ref(url)
            # i should make this more abstract, easier to think that way <---------------------------------------------------------------------------------

        # record:
        self._urls.append(url)
        self._refs.append(ref)
        i = len(self._refs) - 1
        
        refs = self._by_url.setdefault(url, [])
        if ref not in refs:
            refs.append(ref)

        locations = self._by_ref.setdefault(ref, [])
        locations.append(i)
        # now, _by_refs points to one or more locations; if repeat is on, each
        # ref can point to 1+ locations. otherwise, each ref will point to one
        # and only one location.

        # <----------------------------------------------------------------------------- I should consider simplifying this logic and enforcing repetition.

    def check_url(self, url):
        result = False
        if url in self._by_url:
            result = True
        return result
    
        # hypothetically, I should not need a list of the urls itself
        # i should be able to construct that on the fly from the refs
        # so to the extent i do use that, i should be mindful that that's just
        # cache. i should also weigh whether the refs or the links should be the
        # SSOT; the answer is the links

    def refresh_refs(self):
        """
        -> list

        returns list of refs
        """
        refs = list()
        for url in self._urls:
            ref = self.get_first_ref(url)
            refs.append(ref)
            # if uniqueness is enforced, i have to pop the value from the refs
            # so i need a deep copy or something

        # can also make this a batch process

        return refs
            
    
    def get_first_ref(self, url):
        result = self._by_url.get(url, None)
        if result:
            result = result[0]
        return result

    def get_refs(self, copy=True):
        result = self._refs
        if copy:
            result = result.copy()
        return result       
        
    def check_reuse(self):
        result = self._reuse_references
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

        return url

    def generate_index(self, urls, uniques=False, starting=1):
        # rename
        result = list()
        if uniques:
            result, lookup = self.get_uniques(urls, starting)
        else:
            result, lookup = self.get_repeats(urls, starting)
            
        return result, lookup
        

    def get_uniques(self, urls, starting=1):
        
        result = list()
        lookup = dict()
        
        for i, url in enumerate(urls):
            j = i + starting
            result.append(j)
            lookup[j] = url

        return result, lookup

    def get_repeats(self, urls, starting=1):
        result = list()
        i_to_url = dict()
        url_to_i = dict()
        # index to url
        
        i = starting

        for url in urls:
            if url not in url_to_i:
                url_to_i[url] = i
                j = i
                i += 1
            else:
                j = url_to_i[url]
                
            result.append(j)
            i_to_url[j] = url

        return result, i_to_url

    def encode_index_as_alpha(self, index):
        """

        return a list of strings. 
        """
        result = list()
        for i in index:
            caps = list_writer.turn_int_into_column(i)
            ref = caps.lower()
            result.append(ref)
            
        return result
        
    # Non-public
    def _append_ref(self, ref):
        result = len(self._refs)
        self._refs.append(ref)
        return result

# invert -> take a dictionary of indexes to urls and change that to urls to is   


yahoo = "www.yahoo.com"
bing = "www.bing.com"
link3 = yahoo
link4 = "www.chase.com"
links = [yahoo, bing, link3, link4]

def _run_test1():
    lm = LinkManager()
    return lm

def _run_test2(lm, links):
    uniques, lookup1 = lm.get_uniques(links)
    print("Uniques: \n%s\n" % uniques)
    print("Lookup:  \n%s\n" % lookup1)

    repeats, lookup2 = lm.get_repeats(links)
    print("Repeats: \n%s\n" % repeats)
    print("Lookup:  \n%s\n" % lookup2)
    
    print("Build passed Test 2.")

    result = [(uniques, lookup1), (repeats, lookup2)]
    return result

def _run_test3(lm, *indeces):
    result = list()
    for index in indeces:
        
        print("Index:   \n%s\n" % index)
        
        encoded = lm.encode_index_as_alpha(index)
        print("Encoded: \n%s\n" % encoded)
        
        result.append(encoded)
        
    print("Build passed Test 3.")
    return result

def _run_test4(lm, links):
    print("Running Test 4, links with offsets.")
    repeats, lookup = lm.generate_index(links, starting=36)
    print("Repeats: \n%s\n" % repeats)
    print("Lookup:  \n%s\n" % lookup)

    encoding = lm.encode_index_as_alpha(repeats)
    print("Encoding:  \n%s\n" % encoding)

    print("Build passed Test 4.")
    return encoding

# what am I thinking after this runs:
#  remove stuff i dont use
#  make the encode routine return a lookup
#  add the invert function
#  add the routine to go from refs to links?

def run_test():
    lm = _run_test1()
    stuff = _run_test2(lm, links)
    indeces = [stuff[0][0], stuff[1][0]]
    print("Indeces: \n%s\n" % indeces)

    encodings = _run_test3(lm, *indeces)

    shifted = _run_test4(lm, links)
    
    
if __name__ == "__main__":
    run_test()

