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
import urllib.parse

# 2) Port.
from . import parameter

# 3) Constants
#    N/a

# 4) Functions
class Domains:
    """
    This is a class for managing the excluded and included domains in NewsAPI
    Everything requests. This class only supports the delivery of a dictionary
    because it handles two parameters. 
    """

    NAME_EXCLUDED = "excludeDomains"
    NAME_INCLUDED = "domains"

    SEP = ","

    def __init__(self):
        self._included = set()
        self._excluded = set()
        self.p = parameter.Parameter("placeholder")

    def exclude(self, domain, avoid_conflicts=True):
        """

        exclude() -> None

        Method adds domain to the set excluded from the request. If
        "avoid_conflicts" is True and you have the domain in "included", method
        will remove it.
        """
        self._excluded.add(domain)
        if avoid_conflicts:
            if domain in self._included:
                self._included.remove(domain)
                
    def get_dict(self, tuples=[], encode=True, include_blanks=False):
        """

        get_dict() -> dict

        Method returns a dictionary that contains the values for the included
        and excluded parameters if they are defined, or an empty dictionary
        otherwise. If you disable encoding, you get the raw string.

        Method delegates to _get_list_of_tuples for the construction of the data
        and to self.p.get_dict() to process that data into a dictionary. 
        """
        if not tuples:
            tuples = self._get_list_of_tuples(encode=encode)
        result = self.p.get_dict(tuples, include_blanks=include_blanks)
        return result

    def get_excluded(self):
        """

        get_excluded() -> self

        Method returns the domains that the instance lists as excluded.
        """
        return self._excluded

    def get_included(self):
        """

        get_included() -> self

        Method returns the domains that the instance lists as excluded.
        """
        return self._included

    def include(self, domain, avoid_conflicts=True):
        """

        include() -> None

        Method records domain as one that the response should include. If
        "avoid_conflicts" is True and you have the domain in "excluded", method
        will remove it.
        """
        self._included.add(domain)
        if avoid_conflicts:
            if domain in self._excluded:
                self._excluded.remove(domain)

    # Non-Public

    def _get_list_of_tuples(self, encode=True):
        """

        get_tuples() -> list

        Method returns a list of 2 tuples, one for the included domains and one
        for the excluded ones. 
        """
        included = self.SEP.join(sorted(self._included))
        excluded = self.SEP.join(sorted(self._excluded))
        if encode:
            included = urllib.parse.urlencode(included, safe=self.SEP)
            excluded = urllib.parse.urlencode(excluded, safe=self.SEP)

        result = [(self.NAME_INCLUDED, included),
                  (self.NAME_EXCLUDED, excluded)]
        
        return result
