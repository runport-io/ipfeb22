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

    
