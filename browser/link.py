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

"""

This module defines an object to store information about links.

"""

class Link:

    POINTER = "{Link: %s}"
    VIEW = "~{caption} {pointer}~"
       
    def __init__(self, url="", caption=""):
        self._attrs = None
        self._caption = caption
        self._data = None
        self._end = None
        self._ref = ""
        self._start = None
        
        self._url = url
        
        self._view = None

    def get_caption(self):
        """

        -> string

        Returns the caption for the instance.
        """    
        result = self._caption
        return result
    
    def get_raw(self):        
        result = self._start + self._data + self._end
        return result
        
    def get_ref(self):
        """

        -> string

        Returns the reference for the instance. The reference is usually a code,
        such as "aa", based on the URL. 
        """
        result = self._ref
        return result

    def get_url(self):
        """

        -> string

        Returns the url, if specified for the link.
        """
        result = self._url
        return result

    def set_caption(self, caption):
        """

        -> None

        Method sets the caption for the instance.
        """
        self._caption = caption

    def set_attrs(self, attrs):
        self._attrs = attrs

    def set_data(self, data):
        self._data = data

    def set_end(self, end):
        self._end = end

    def set_ref(self, ref):
        """

        -> None

        Method sets the ref for the instance. 
        """
        self._ref = ref

    def set_start(self, start):
        self._start = start

    def set_url(self, url):
        """

        -> None

        Method sets the url for the instance.
        """
        self._url = url      

    def view(self):
        """

        -> string

        Method returns a string that represents the link, including a reference
        to the URL. 
        """
        pointer = self.view_pointer()
        caption = self.get_caption()
        result = self.VIEW.format(caption=caption, pointer=pointer)
        return result

    def view_pointer(self):
        """

        -> string

        Method returns a string that includes the reference to the URL.
        """
        ref = self.get_ref()
        result = self.POINTER % ref
        return result
    
    # add hash? 
    #   add the id thingamajig 
    
