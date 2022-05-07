class TopHeadlines:
    def __init__(self):
        self.q = Query()
        self.pages = Pages()
        # this one would include page_size and the page, as well as page up and
        # page down
        self.countries = CachedParam()
        self.sources = CahedParam()

    def get_params(self):
        pass

    def get_headers(self):
        pass

    def get_request(self):
        pass

# Or make a module that does all this stuff, so that's reusable
# or just handle the construction in the top-level thingamajig

# get_request():
#   gets the endpoint, gets params, encodes,
#   


