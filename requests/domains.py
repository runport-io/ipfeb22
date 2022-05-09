class Domains:
    # This is a class for managing the excluded and included domains in NewsAPI
    # Everything requests.

    EXCLUDED = "excludeDomains"
    INCLUDED = "domains"

    SEP = ","
    # consider moving this to the field

    def __init__(self):
        self._included = set()
        self._excluded = set()

    def include(self, domain):
        self._included.add(domain)
        if domain in self._excluded:
            self._excluded.remove(domain)

    def exclude(self, domain):
        self._excluded.add(domain)
        if domain in self._included:
            self._included.remove(domain)

    def get_params(self):
        e_domains = sorted(self._excluded)
        e_value = self.SEP.join(e_domains)

        i_domains = sorted(self._included)
        i_value = self.SEP.join(i_domains)

        result = {self.INCLUDED : i_value, self.EXCLUDED : e_value}
        return result

    

        

    
