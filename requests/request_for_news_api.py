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
from . import request_maker
from . import number

# 3) Constants
#    N/a

# 4) Functions
class RequestForNewsAPI(request_maker.RequestMaker):
    NAME_PAGE = "page"
    NAME_PAGE_SIZE = "pageSize"
    NAME_SOURCES = "sources"
    
    MAX_PAGE_SIZE = 100
    # Per NewsAPI docs
    
    MAX_SOURCES = 20
    # Per NewsAPI docs
    
    def __init__(self):
        request_maker.RequestMaker.__init__(self)

        self.page = Number(name=NAME_PAGE, value=1)
        self.page.set_floor(1)
        
        self.page_size = Number(name=NAME_PAGE_SIZE, value=MAX_PAGE_SIZE)
        self.page_size.set_ceiling(MAX_PAGE_SIZE)

        self.sources = Choice(name=NAME_SOURCES)
        self.sources.set_limit(MAX_SOURCES)
    
