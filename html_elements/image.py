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
ALT_TEXT = "alt"
SOURCE = "src"

# 4) Functions
class Image:

    VIEW = "Image: {alt} {pointer}"
    LEFT = " |"
    RIGHT = "| "
    #< ----------------------------------------------------------------- consider moving these to element
    
    def __init__(self, data=None):
        self.element = element.Element()
        self.link = link.Link()
        
        self._alt = None
        self._source = None

        if data:
            self.update(data)
        
    def add_decoration(self, string):
        """

        -> string

        Method adds decoration to the string. 
        """
        result = self.LEFT + string + self.RIGHT
        return result
        
    def get_alt(self):
        result = self._alt
        return result

    def get_source(self):
        result = self.link.get_url()
        return result

    def get_url(self):
        """

        get_url() -> str

        Method returns the url from the instance's link.         
        """
        result = self.link.get_url()
        return result

    def set_alt(self, alt):
        self._alt = alt

    def set_source(self, source):
        self.link.set_url(source)
    
    def view(self, decorate=True):
        """

        view() -> string

        Method returns a string that represents the instance. You can turn off
        decoration if you want to include the result in some other object.
        """
        alt = self.get_alt()
        pointer = self.link.view_pointer()
        
        result = self.VIEW.format(alt=alt, pointer=pointer)
        if decorate:
            result = self.add_decoration(result)
        
        return result
        
    def update(self, data):
        """

        update() -> None

        Method updates the instance on the basis of the dictionary you supply. 
        """
        self.element.update(data)        

        attrs = self.element.get_attrs()
        alt = attrs.get(ALT_TEXT)
        self.set_alt(alt)

        src = attrs.get(SOURCE)
        self.set_source(src)


        

    
    
