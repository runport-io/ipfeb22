# handles templates, requests, responses, and forms
class Cycle:
    def __init__(self):
        self.request = None
        self.response = None
        self.template = None
        self.form = None
        # blank by default
        # self.interval = None

    def make_form(self):
        form = Form()
        interval = self.template.interval.copy()
        form.set_interval(interval)
        return form

    def complete(self):
        # gets the response, fills out form
        pass
        # get_request()
        # get_response()
        # make_form()
        # fill_form()
        # no ops for each if already did

    # def copy()
    def get_request(self, template=None):
        data = template.get_data()
        interval = self.interval.get_tuple()
        # probably not?
        data.update(interval)
        req = template.get_request(data)
        return req

    def get_response(self, request=None):
        if request is None:
            request = self.get_request()

        response = handler.get_response(request)
        # delegate to the routine I wrote before
        return response

  
# Testing:
# 1) Get a request, make sure it looks right (includes dates in the right
#    format)

# 2) Get the response, make sure that works
# 3) Unpack the response [reqiures a build of Form]
# 4) Copy the Cycle

    
