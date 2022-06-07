# Ping / Touch / Clip / Meeting
# Container / Organizer [is the thing that holds the response data]
# what about linkages between them? form, molding, 
#
# contains request, template, response, data

class Transaction:
    def __init__(self):
        self._template = None
        self._request = None
        self._response = None
        self._data = None


    def get_template(self):
        return self._template
    
    def get_request(self, template=None):
        if template is None:
            template = self.get_template()
        request = template.get_request()
        return request

    def get_response(self, request=None):
        if request is None:
            request = self.get_request()
        response = urllib.request.open(request) #<--------------- bad command
        return response

    def get_data(self, response=None):
        if response is None:
            response = self.get_response()
        data = blah.get_data(response)
        return data

    # seems like this is the point of separation. above is the holder object. below
    # is logic for newsapi specifically.

    # release a NewsAPIResponse object; or make one
    # aka Organizer

class SomethingElse:

    def __init__(self):
        pass

    def make_from_data(self, data):
        pass
        # fill, update() etc.
    
    def get_count(self):
        pass

    def get_events(self, data=None):
        if data is None:
            data = self.get_data()
        # articles = get_articles(data)
        events = list()
        for article in articles:
            processor.make_event(article)
            events.append(article)

        return events
    
    
# add the logic for setting the data too? 
# need to handle security somewhere here

            
