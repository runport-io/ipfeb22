# Copyright Port. Prerogative Club ("the Club")
#
# 
# This file is part of Port. 2.0. ("Port.")
#
# Port. is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Port. is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Port. If not, see <https://www.gnu.org/licenses/>.
#
# Questions? Contact hi@runport.io.


# can have DEV_PLAN and BIZ_PLAN policies. DEV_PLAN = {limit: x, window:y}, then
# apply_policy(DEV_PLAN). 

# Imports
# 1) Built-ins
import datetime

class Bundler2:
    """
    The real bundler.
    """

    # Dev plan
    MAX_DAILY = 100
    MAX_WINDOW = 30
    
    def __init__(self):
        self._for_top = 10
        # int
        # this is like a reserve
        # I should have reserved for top, and reserved for just in case. So two
        # reserves, not one.
        self.welder = Welder()
        # makes articles into events
        self.bundles = list()
        # should go something like top, then rest (substantive)
        self.last_bundle = 0
        
    def get_available(self):
        result = self.MAX_DAILY - self._for_top
        return result

    def get_top(self, start, end):
        bundle = Bundle()
        req = TopHeadlines()
        req.set_start(start)
        req.set_end(end)
        pair = Pair()
        pair.set_req(req)
        bundle.set_pairs([pair])
        return bundle

        # does not support to and from
        # <--------------------------- check what happens if you put those in

    def get_everything(self, chunk, start, end):
        bundle = Bundle()
        req = Everything()
        req.set_start()
        req.set_end()
        #< ------ move these to bundle
        # will also help walk backwards in time
        req.set_
        pair = Pair()
        pair.set_req(req)
        bundle.set_first(pair)

        # default window: 30 days from today, to today.

    def get_start(self, end=None, window=self.MAX_DAYS):
        """

        -> date

        Method returns a date that is window days' earlier than the end. If you
        don't specify the end, method will call self.get_end().
        """
        if end is None:
            end = self.get_end()
        end_ordinal = end.toordinal()
        start_ordinal = end_ordinal - window
        result = datetime.date.fromordinal(start_ordinal)
        return result

    def get_end(self, margin=1):
        """

        -> date

        Returns today's date plus margin in days.
        """
        today = datetime.date.today().toordinal()
        tomorrow = today + margin
        result = datetime.date.fromordinal(tomorrow)
        return result

    def get_chunks(self):
        pass

    # ops:
    # 1) split watchlist
    # 2) make the bundles
    # 3) make the first req, or get the first response
    # 4) compute budget [?] <----
    # 4.5) make events
    # 5) keep going until call budget exhausted
    
    def make_top_headline_bundles(self):
        pass
        # ideally this would since the last top_headlines() call
        # so time delimited

        # i want to start with one of these
        # i want to then do the first call for the other bundles
        # then either do another top if a lot of time has passed
        # or keep going

        # so need a method to advance the date somehow, though that's arguably
        # the case for all requests, since we agree that the window should
        # always be delimited by time.        

    def make_top_headline_pair(self, start_date=None, end_date=None):
        """

        -> Pair 
        """
        pair = Pair()
        top = request_for_top_headlines()
        if start_date is None:
            start_date = None #<--- what dtae?
        if end_date is None:
            end_date = None #<---- today?
        top.start.set_value(start_date)
        top.end.set_value(end_date)
        pair.set_request(top)

        return pair

        
    
    # i can make a big tape of pairs and keep going through them until there is
    # stop or i run out of calls.

    # get_tape() -> list of pairs of length n, where n is at most the number of
    # calls you have, or the max size per day.
    
    # go through pairs, fill them out, etc.
    # how does this jive with first_reqs: I presumably should take those out of
    # the equation.

    # so get_tape():
    #   get_top(start, end)
    #
    #   get_first(start, end)
    #       for each bundle, get_first_pair()
    #
    #   # now i have enough information to compute the reqs for each bundle
    #   # the issue is, either the pair is separate from the bundle, or not
    #   # on the flip side, the bundles are empty at first, so i can really
    #   # just start with pairs, and then get a certain number of pairs from
    #   # each bundle.
    #
    #  make_bundles()
    #  get_remaining_calls()
    #  compute_reqs(avail_calls)
    #    for each bundle, do this
    #  get_more_reqs()
    #     # now back to the issue of matching
    #     # i could keep this index on the pair or on the bundle
    #     # I coudl also add a is_mine() routine that returns a bool
    #     # or I could just go in loops through the active bundles, and fill them
    #     # one at a time <-- no tape, but preserves containers and stuff.
    #  # why do i need this?
    #     # to know what i sampled. and what i am missing.
    #     # and to know what brands the event relates to, to simplify how i tag it.
    #     # i could potentially not worry so much, and just hope for the best.
    #    
    
    def set_calls_per_day(self, calls):
        self._budget_for_daily_calls = calls

    def make_bundles(self, watchlist):
        chunks = self.split(watchlist)
        for c in chunks:
            # c is a set of brands
            bundle = Bundle(c)
            bundle.set_budget(budget)
            budnle.make_first_request(c) # same as above?
            self.bundles.append(bundle)

        # delegate to the old logic
    
    
    def get_first_responses(self):
        for bundle in self._bundles:
            bundle.get_first_response()

    def get_rest_of_responses(self):
        for bundle in self._bundles:
            bundle.get_rest()

    def compute_reqs(self):
        pass
        # sum required calls for each bundle
        # add together
        # subtract budget
        # should really be, get_calls_needed(), then divide that by days
        # and get something on a per day basis
        # then shrink the window.
        # 

    def compute_shortfall(self):
        pass
        # reqs less budget
        # to bundle

    def 

    
        
            
            

    

    
