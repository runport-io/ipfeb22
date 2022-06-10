DAY = 60*60*24
MAX_LENGTH = 30 * DAY

class Series:

    def __init__(self):
        self._template = Template()
        self._budget = None
        
        # each cycle should share a template?
    def get_budget(self):
        return self._budget()

    def set_budget(self, budget):
        self._budget = budget
    
    def get_next(self):
        """

        -> Cycle
        
        """
        # either make one or adjust
        # return
        if self._cycles:
            last = self._cycles[-1]
            new = last.copy()

            new.change_period()
            # original: start wide (0), figure out rate per day, set intervals to
            # one page's worth going forward, vary the starting point for next

            # alt: start with a one-day window, then adjust to smaller or larger
            # as necessary to maintain one page

            # I could potentially decompose a Cycle into a template and an
            # interval.
            # Perhaps rate should also go on there.

    def set_template(self, template):
        self._template = template

    def make_first(self):
        cycle = Cycle()
        template = self.get_template()
        # contains the brands
        
        cycle.set_template(template)
        
        self._cycles.append(cycle)
        # may be? 
        
        return cycle
        
        # get template
        # make first Cycle
        # complete the first Cycle
        # adjust the timeframe on the next cycle

    def make_first_30_day(self):
        cycle = Cycle()
        template = self.get_template()
        # does not come with an interval
        cycle.set_template(template)

        now = time.time()
        cycle.interval.set_end(now)
        cycle.interval.set_length(MAX_LENGTH)
        # should automatically change the interval starting point

        return cycle
        # default cycle length should be one day

    def make_cycle(self, end=None, length=DAY):
        # by default, should make end today and length
        template = self.get_template()
        cycle = Cycle(template)

        cycle.interval.set_length(length)
        if end is not None:
            cycle.interval.set_end(end)

        return cycle

    # how do I walk it back? i can do: new = old - day
    # problems with testing: by default, the cycle should start and end when?

    def calibrate(self):
        first = self.cycles[0]
        # consider making the first here
        first.complete()
        # gets the response, fills out the form
        rate = first.form.get_rate()
        # per day
        days = 100 / rate
        default_length = days * DAY
        self.set_default_length(default_length)
        # now subsequent cycles should have the legnth of default length

    def make_next(self):
        budget = self.get_budget()
        if budget is not None:
            count = len(self.cycles)
            if count == budget:
                raise Exception("out of budget")
        
        last = self.cycles[-1]
        pozavchera = last.copy()
        # or consider copying last
        start = last.interval.get_start()
        pozavchera.interval.set_end(start)
        length = self.get_default_length()
        pozavchera.interval.set_length(length)

        if append:
            self.cycles.append(pozavchera)
            
        return pozavchera

    def start(self):
        first = self.make_first_30_day()
        self.cycles.append(first)

        # consider moving the first.complete() here
        default_length = self.calibrate()
        self.set_length(default_length)

    # can now make a budget for each series
    # 
        
        

    
    
