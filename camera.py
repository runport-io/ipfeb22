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

Module defines the Camera class, an object that takes pictures of Events.

------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:

FUNCTIONS:

CLASSES:
Camera              Renders Events as a set of strings.
------------------  ------------------------------------------------------------
"""

# Imports
# 1) Built-ins
# N/A
# 2) Port.
import gui

class Camera:
    # takes pictures of events
    def __init__(self, event=None):
        self.event = event
    
    def get_dot_for_top(self, event):
        """

        get_dot() -> str

        Method returns a string of length 1 that represents the event based on
        the brand that occurs most frequently in the event. If the event does
        not list any brands, returns the first charcter of the headline.
        """       
        char = event.get_word()[0]
        return char
        
    def get_block(self, event):
        """

        get_block() -> list

        Method returns a list of two strings for the event. If you print the
        strings, you get a block with two characters and a smiley that describe
        the string.
        """
        result = list()
        word = event.get_word()
        line1 = word[:2]
        result.append(line1)

        # score = event.scores.get_score(word)
        # # placeholder for sentiment, scores come in 1, 0, -1. can match them
        # to smileys here.

        smiley = ":|"
        result.append(smiley)

        return result      

    def get_tile(self, event):
        """

        get_tile() -> list()

        Returns a view of the event that draws the box. 
        """
        flat = dict()
        flat[gui.HEADLINE] = event.get_headline()
        flat[gui.BRAND] = event.get_word()
        lines = gui.render_event(flat)
        return lines

    def get_full(self, event, include_headline=True, width=None):
        """

        -> list()

        Returns a list of strings for the headline and body. Each line will be
        at most the width you specify. 
        """
        pass
    
