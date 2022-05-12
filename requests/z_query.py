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
#    N/a

# 2) Port.
from . import choice

# 3) Constants
#    N/a

# 4) Functions
class Query(choice.Choice):

    SEP = " OR "

    """

    Class provides a container for a list of brands that forms the basis of a
    query. For now, this is just a list with a defined separator, but in the
    future, I can add more methodology for handlings ands ors, etc. 
    """
    
    def __init__(self, name):

        choice.Choice.__init__(self, name)
        self.set_sep(self.SEP)
