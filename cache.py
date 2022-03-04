# cache 2

class Cache:
    """
    container for events. Provides storage at run time. Does not persist.
    """
    def __init__(self):
        self._events = set()

    def get_events(self):
        result = self._events.copy()
        return result

    def add_events(self, events):
        for event in events:
            self._events.add(event)

# improvements I can consider making:
# size management (by event)
# organization (by brand)
