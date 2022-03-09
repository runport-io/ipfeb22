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
# N/a

# 2) Port.

class Storage:
    def __init__(self):
        pass

    def construct_path(self, event, check_conflicts=True, fix_conflicts=False):
        """

        construct_path() -> path

        Method returns a path object.         
        """
        path = self.make_filename(event)
        if check_conflicts:
            status = os.path.checkpath(path)
            if status:
                if not fix_conflicts:
                    raise OperatorError
                else:
                    path = self.fix_conflicts(path)
        # can check for conflicts here if I want, 

    def fix_conflicts(self, path):
        pass
        # checks the path
        # if there is an existing location, appends a 1
        # repeats until there is not an existing location or you run out of chars.

        
    def make_filename(self, event, max_length=40):
        """

        make_filename() -> str

        Returns a filename in the format "YYYY.MM.DD Source Headline.json"
        """
        pass
        
        
    def get_location(self, number):
        """

        get_location() -> path

        Returns a path from the index. 
        """
        path = self._index.get(number)
        return path
        
    def load_event(self, number):
        """

        load_event() -> event

        Method returns an event. 
        """
        location = self.get_location(number)
        flat = self.load_file(location)
        event = self.make_event_from_flat(flat)
        return event

    def load_file(self, location):
        """

        load_file() -> dict

        Method returns a JSON object.
        """
        contents = open(location, rb)
        flat = json.load(open)
        return flat

    def load_index(self, location):
        file = open(location, "rb")
        # I should abstract out this open routine
        index = json.load(file)
        self.set_index(index)
        return index
        # loads everything, no size limitations.
        
    def make_event_from_flat(self, flat):
        """

        make_event_from_flat() -> Event

        Method constructs an instance of Event from the data.
        """
        event = Event.from_flat(flat)
        return event

    def save_event(self, event):
        number = event.get_number()
        status = self.check_index(number)
        if not status:
            path = self.save_event_to_file(event)
            self.add_path_to_index(event, path)
        else:
            if alert_conflicts:
                raise OperationError

    def save_event_to_file(self, event):
        """

        save_event_to_file() -> path

        Method constructs a file name for the event, turns it into a path,
        opens a file at this path, and saves the flat version of the event to
        the file.
        """
        path = self.construct_path(event)
        file = open(path, "wb")
        flat = event.get_flat()
        json.dump(flat)
        file.close()

    def set_index(self, index):
        self._index = index

        
