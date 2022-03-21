# Copyright Port. Prerogative Club ("the Club")
#
# 
# This file is part of Port. 2 ("Port.")
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
import html.parser

# 2) Port.
# N/a

# 3) Constants
# N/A

# 4) Functions
class MiniParser(html.parser.HTMLParser):    
    def handle_comment(self, data):
        pass
    
    def handle_data(self, data, print_data=True):
        
        container = getattr(self, "container_for_text", None)
        if not container:
            self.container_for_text = ""
        if data:
            self.container_for_text += str(data)

        if print_data:
            print(data)        
        
        return data

    def handle_decl(self, decl):
        pass

    def handle_endtag(self, tag):
        pass

    def handle_starttag(self, tag, attrs):
        pass
    
    def handle_pi(self, data):
        pass

    def unknown_decl(self, data):
        pass
    
