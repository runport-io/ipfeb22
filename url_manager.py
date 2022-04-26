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
        

    

    
    

                
                
        
        

    
