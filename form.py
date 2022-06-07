# standardized container for data
# supports some rate ops

class Form:
    def __init__(self):
        self._template = None
        # consider wheter I need this
        self._count = None
        self.interval = Interval()
        self._articles = list()

    def get_count(self):
        return self._count

    def set_count(self, count):
        self._count = count

    def set_interval(self, interval):
        self.interval = interval

    def get_articles(self):
        return self._articles

    def set_articles(self, articles):
        self._articles = articles
    
    def get_rate(self, n=24):
        """
        -> float

        Returns number of events in specified period. n controls the # of hours.
        """
        count = self.get_count()
        hours = self.interval.get_hours()
        rate = count / hours * n
        return rate

    def fill(self, data):
        pass
    
