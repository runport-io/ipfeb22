class Distributor:
    # organizes flow of information across several channels
    # alternator?

    def __init__(self):
        self.pattern = Pattern()

    def make_series(self, watchlist):
        pass
        # -> series

    # split the WL into chunks
    # make a series for each one
    # arrange them into an orchestra, or something like that
    # hit each one in order
    # each series can have a

    def make_series2(self, wl):
        result = list()
        
        chunks = self.chunk(wl)
        for chunk in chunks:
            series = Series()
            template = EverythingTemplate()
            template.set_query(chunk)
            
            series.set_template(template)

            #set budget
            
            result.append(series)
            
            
        return result

    def get_data():
        try:
            while True:
                serieses = self.get_series()
                for series in serieses:     
                    cycle = series.get_next()
                    cycle.complete()

        except OutOfBudgetException:
            pass

        # should really be on a discrete basis

    def add_general(self):
        # adds a TopHL series at the beginning and end?
        pass

        # or checks the clock and runs it if it is time to do so

        
    
