# Alternator

import controller

class Alternator:
    # connects to controller.
    
    def __init__(self):
        pass

    def burn(self):
        pass
        # delete the events that I didn't save
        # almost want to do something like keep the event id and the date.

    def pull(self, count):
        """
        -> list

        pull events from controller.
        """
        events = controller.update(count)
        return events

    def save(self):
        pass
        # tell controller to save certain events
        # the save operation consists of a couple concepts:
        #   # 1) save even if not tagged
        #   # take certain events I want to remember and make sure they stay in
        #   # cold storage, as in, they do not get purged even if my cache runs
        #   # out of space
        #   #
        #   # so here, i don't modify the event, i just instruct controller to
        #   # store it
        #   # 
        #   # 2) tag the event and save the event metadata
        #   # save event.brands
        #   # save event.tags? or something else?
        #   #   lets say i measure reading time for the event. that should go in
        #   #   event.attention or something
        #   #   the question is what is part of what, right now i have event and
        #   #   then compositions around it.

    def get_event(self):
        pass
        # can request to retrieve events by id for example





    

    

    
        
