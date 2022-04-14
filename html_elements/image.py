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

# Imports
# 1) Built-ins
# n/a
# 2) Port.
from . import element
from . import link

# 3) Constants
#Image
ALT = "alt"

# 4) Functions
class Image:

    CAPTION = "| Image: {alt} |"
    
    def __init__(self, match=None):
        self.element = element.Element()
        self.link = link.Link()
        
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


        

    
    
