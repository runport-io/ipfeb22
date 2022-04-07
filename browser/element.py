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

Module defines a class for storing a segment of HTML.

"""

class Element:
    def __init__(self):
        
        self._attrs = dict()
        self._comments = None
        self._data = ""
        self._end = None
        self._start = None

    def get_attrs(self, copy=True):
        """

        get_attrs() -> dict

        Method returns a dictionary of the attributes for the element. To avoid
        in place changes, you get a copy back by default. 
        """
        result = self._attrs.copy()
        return result

    def get_comments(self):
        """

        get_attrs() -> dict

        Method returns the comments for the element.
        """
        result = self._comments
        return result

    def get_data(self):
        """

        get_data() -> str

        Method returns the data for the instance. The data is whatever appears
        between the start and end tags.
        """
        result = self._data
        return result

    def get_end(self):
        """

        get_end() -> str or None

        Method returns the end tag for the instance, if defeind.
        """
        result = self._end
        return result

    def get_start(self):
        """

        get_end() -> str or None

        Method returns the start tag for the instance, if defeind.
        """
        result = self._start
        return result

    def set_attrs(self, attrs):
        """

        set_attrs() -> None

        Method stores the attributes for the element. Attributes are usually
        defined in the opening tag and include things like name and "href".
        """
        self._attrs = attrs
        # <----------------------------------------------------------------------- consider making tag name "_name"

    def set_comments(self):
        """

        ** NOT DEFINED **

        set_comments() -> None
        
        Method stores the comments for the element. 
        """
        raise exceptions.NotYetDefined
        # I need to consider appending comments in a list. 

    def set_data(self, data):
        """

        set_end() -> None

        Method stores the data for the element in the instance, such as "Search
        Engine" or a string representing an image element (data can include
        nesting). You can access the information through get_data(). 
        """
        self._data = data

    def set_end(self, end_tag):
        """

        set_end() -> None

        Method stores the end tag for the element on the instance, such as
        "</a>". You can retrieve the tag using get_end(). 
        """
        self._end = end_tag

    def set_start(self, start_tag):
        """

        set_start() -> None

        Method stores the starting tag for the element on the instance, such as
        '<a href="www.yahoo.com">'. You can retrieve the tag using get_start().
        """
        self._start = start_tag
