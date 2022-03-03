class Terminal:
    def __init__(self):
        self.watchlist = None
        self.events = None

    def brand_events(self):
        brands = self.watchlist.flatten()
        self.scanner.scan(events, brands)

    def refresh_brands(self):
        flat_watchlist = self.watchlist.flatten()
        events = self.get_events()
        for event in events:
            new = event.brands.get_new(flat_watchlist)
            # returns flat_watchlist - brands in index
            result = self.scanner.scan(event, new)
            # modifies event?
            # if not: event.brands.record_location(result)

    def load_events(self):
        pass
        # get events from controller
        # check_brands

    def view_all(self):
        # returns all events
        pass

    def filter_events(self, events, watchlist):
        # filters by watchlist
        pass


    
