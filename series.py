class Series:

    def __init__(self):
        self._template = template
        
        # each cycle should share a template?
        
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
        
        

    
    
