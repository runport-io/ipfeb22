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
# N/a

# 2) Port.
import controller

# 3) Constants

# 4) Functions
class Alternator:
    # connects to controller.
    
    def __init__(self):
        pass

    def burn(self):
        pass
        # delete the events that I didn't save
        # almost want to do something like keep the event id and the date.

    def pull(self, count, offset):
        """
        -> list

        pull events from controller.
        """
        offset, events = controller.update(count=count, offset=offset)
        return events

    def save(self):
        pass
        # tell controller to save certain events
        # the save operation consists of a couple concepts:
        #   # 1) save even if not tagged
        #   # take certain events I want to remember and make sure they stay in
        #   # cold storage, as in, they do not get purged even if my cache runs
        #   # out of space
        #   #
        #   # so here, i don't modify the event, i just instruct controller to
        #   # store it
        #   # 
        #   # 2) tag the event and save the event metadata
        #   # save event.brands
        #   # save event.tags? or something else?
        #   #   lets say i measure reading time for the event. that should go in
        #   #   event.attention or something
        #   #   the question is what is part of what, right now i have event and
        #   #   then compositions around it.

    def get_event(self):
        pass
        # can request to retrieve events by id for example





    

    

    
        
