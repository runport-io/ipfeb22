# Link Manager 2
# always unique

# Imports
# 1) Built-ins
# N/a

# 2) Port.
import list_writer

class UrlManager:
    def __init__(self):
        self.by_ref = dict()
        self.by_url = dict()
        self.refs = list()
        self.encode = list_writer.turn_int_into_column

    def get_ref(self, url):
        result = self.by_url.get(url, None)
        
        if not result:
            result = self.make_ref()
            self.record_url(url, result)

        return result
                
    def make_ref(self):
        """

        -> string
        """
        i = len(self.refs)
        j = i + 1
        ref = self.encode(j)
        self.refs.append(ref)

        return ref

    # consider adding get_ref()

    def record_url(self, url, ref):
        self.by_ref[ref] = url
        self.by_url[url] = ref
        

    

    
    

                
                
        
        

    
