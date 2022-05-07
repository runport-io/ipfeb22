# sister level obj to Query
# this module should be stand alone





class NewsAPIRequest:

    MAX_PAGE_SIZE = 100
    
    def __init__(self):

        self.base = BaseRequest()
        
        self._page = 1
        self._pageSize = 100

        self._sources = list()
        # supplement base with things I know I added        

    def get_endpoint(self):
        """

        get_endpoint() -> string

        Method returns the endpoint for the instance.
        """
        result = self._endpoint
        return result
        # can refactor to have a better url obj

    def set_endpoint(self, endpoint):
        """

        set_endpoint() -> None

        Method sets the instance endpoint to the argument. 
        """
        self._endpoint = endpoint


    def get_headers(self):
        pass

    def get_params(self, encode=True):
        pass

    def get_page(self):
        pass

    def set_page(self, number):
        pass

    def get_page_size(self):
        """

        get_page_size() -> int

        Method returns the maximum number of results per page.
        """
        result = self._page_size
        return result

    def set_page_size(self, number, force=False):
        within_limits = False
        if number <= self.MAX_PAGE_SIZE:
            within_limits = True

        if force or within_limits:
            self._page_size = number
        else:
            raise exceptions.OperatorError

# so really, I do delegation one level down, then enrich. that's my pattern. 

def EverythingRequest:

    SORT_BY = [RELEVANCY, POPULARITY, PUBLISHED_AT]    
    
    def __init__(self):
        self.news_api_request = NewsAPIRequest()
        self._endpoint = "https://newsapi.org/v2/everything"
        # this should be rich
        
        self._search_in = None
        self._domains = None
        self._exludeDomains = None
        self._from = None
        self._to = None
        self._language = None
        # filter out ru
        self._sort_by = None

def TopHeadlinesRequest(NewsAPIRequest):
    def __init__(self):
        self._endpoint = "https://newsapi.org/v2/top-headlines"
        self._category = None
        self._country = None

    def set_country(self, code, force=False):
        pass
        # cannot do both this and sources. so need to do self.sources = None
        # then if the code is in codes, permit.
        
        # test whether this works for 2+ countries. unclear from docs.

    def set_category(self, category):
        pass
        # pick from a list of categories
        # does not mix with source, so have to reset. 
