

class Req:
    def __init__(self):
        self._endpoint = None
        self._query = Query(name="q")
        self.headers = dict()
        
    def get_endpoint(self):
        return self._endpoint

    def set_endpoint(self, value):
        self._endpoint = value

    def get_params(self):
        result = dict()
        k = self._query.get_name()
        v = self._query.get_query()
        result[k] = v
        
        return result

    def get_headers(self):
        return self._headers

class NewsAPIReq(Req):
    def __init__(self):
        Req.__init__(self)
        self.page = Num(name="page")
        # 
        self.page_size = Num(name="page_size")
        # here I am still doing mostly composition

        def get_params(self):
            result = Req.get_params(self)
            for attr in [self.page, self.page_size]:
                # still need to figure out what to get
                
                data = attr.get_dict()
                result.update(data)

            return result

class EverythingReq(NewsApiReq):

    ATTR_NAMES = ["_from_date", "_to_date", "_sort_by"] 
    def __init__(self):
        NewsAPIReq.__init__(self)
        self._from_date = Date("from")
        self._to_date = Date("to")
        self._sort_by = Choice("sortBy")

    def get_params(self):
        result = NewsAPIReq.get_params(self)
        for attr in [self._from_date, self._to_date, self._sort_by]:
            # this thing is what I should be updating, then method can be
            # constant. Or could just do for attr in self.__dict__, try x, if
            # attribute error then pass. #<------------------------------------------- no need to declare then. 
            
            data = attr.get_dict()
            result.update(data)

        return result

class TopHeadlines(NewsApiReq):
    def __init__(self):
        NewsApiReq.__init__(self)
        self.category = Choice("category")

class Bundler:
    # makes bundles of requests
    def make_first(self, batch):
        pass
        # makes a EverythingRequest(batch).
        # req = EverythingRequest()
        # req.q.set_query(batch)
        # real_req = req.get_req()
        # return real_req

    def get_first_response(self, req):
        response = self.get_response(req)
        # return response

    def make_next_requests(self, batch):
        result = list()
        limit = min(batch, self.budget_per_batch)
        for i in range(1, limit):
            # don't include 1
            req = EverythingReq()
            req.page.set_value(i)
            
        return result

    def get_all(self, batch):
        first_req = self.make_first(batch)
        first_resp = self.get_first_response(first_req)
        remaining_reqs = self.make_next_requests(batch, first_resp)
        # should figure out the size from the resp
        # consider the signature one more time
        responses = [first_resp]
        for req in remaining_reqs:
            response = self.get_response(req)
            responses.append(response)

    def get_articles(self, responses):
        pass
        # go through and get all the articles

    # other:
    #   def get_relevancy_and_pop(req):
    #       flips it by type
    #       max value without pagination
    #       # always 3 requests
    #
    #   def measure_overlap(batches of articles):
    #       pass
    #       returns a series of integers or something

    #   def define_window(batch, start, end):
    #       adds a start and end date to the batch
    #       # narrower request, better for repetition, makes pagination less likely

    #   def compute_budget(watchlist):
    #       # generates a budget per batch
    #       # leaves room for h topheadlines

    #   def get_number_of_requests(self):
    #       returns number of reqs used today

    #   toggle_status(self):
    #       something about developer vs business settings
    #       max requests per day
    #       if switch to paid, then you have more requests, etc.
    #       leave room for other
    #       begs for storage
    #
    #   monitoring:
    #       objective: detect brands that appear in the news more than others
    #       so that a) I can manage those pages differently than low frequency
    #       events
    #       if a batch has a lot more events, split it in half
    #       if a batch has a lot more events, repeat until you get to a single
    #       brand.

    # storage:
    #       i want to make this reusable
    #       so this is a mini version of what runs through controller
    #       how?
    #       one topic per brand
    #       includes headlines, id, date, source.
    #       events stored elsewhere, keyed by id.
    #       group-level topics generated as you go
    #       call the objects a log.
    #
    # if i can reliably compare events, I can:
    #       filter out duplicates quickly, but capture their sources. the
    #       procedure should
    #       
    #       

    
            
        
        
