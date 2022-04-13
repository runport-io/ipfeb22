#Image
ALT = "alt"

class Image:

    CAPTION = "| Image: {alt} |"
    
    def __init__(self, match=None):
        self.element = Element()
        self.link = Link()
        
        self._alt = None
        self._source = None

        if match:
            self.apply_match(match)
        
    def get_alt(self):
        result = self._alt
        return result

    def get_source(self):
        result = self.link.get_url()
        return result

    def set_alt(self, alt):
        self._alt = alt

    def set_source(self, source):
        self.link.set_url(source)

    def view(self):
        caption = self.get_alt()
        self.link.set_caption(caption)
        
        result = self.link.view()
        return result

    def apply_match(self, match):

        self.element.apply_match(match)        

        attrs = self.element.get_attrs()
        alt = attrs.get(ALT_TEXT)
        self.set_alt(alt)

        src = attrs.get(SOURCE)
        self.set_source(src)

# so now I need to keep track of the refs across the page
# page.um.


        

    
    
