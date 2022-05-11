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
#    N/a

# 3) Constants
#    N/a

# 4) Functions
def get_request(container):
    pass

    # get_params()
    # get_headers()
    # encode()
    # add_security()

    # req = urllib.request.Request(url=url, headers=headers, params=params)
    # return req

def get_params(container):
    pass

    base = container.params.get()

    for attr in container.__dict__:
        if attr.startswith("_"):
            continue
        else:
            # if not function, attach
            # or define:
            # for container.defined_params:
            #   get param
            #   enrich base
            pass

    return base
    # for attr in attrs:
    # if not startswith _, attr get
    # get name
    # encode?

def get_headers(container):
    pass
    # result = container.headers.get()
    # add security?

def get_url(container):
    pass

    # result = container.endpoint.get()

# could also make this a handler
# class Handler or something.



    
