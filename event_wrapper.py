# Wrapper

class EventWrapper:
    def __init__(self, event):
        self.camera = Camera()
        self.event = event
        self.work = None
        # placeholder for tracking time, attention, etc.
        self.tags = None
        # placeholder for commentary, etc

    def unwrap(self):
        """

        returns a tuple of event, data, where data is what you would transmit
        to preserve the work done to date on the event. 
        """
        pass
        # take the work
        # take the tags
        # take the notes

    def tag(self, tag):
        pass
        # if tag in event.body:
        #   register it as a brand
        # else:
        #   record it as a tag.  

# then:
#  can have a wrap and unwrap event methods
#  wrap constructs one with the wrapper
#  unwrap just returns the event?
#   or the event with ._meta on it
#  wrap() builds up the wrapper
#  can also have an id on the wrapper too.


