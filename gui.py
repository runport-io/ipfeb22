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

import copy

SCREEN_WIDTH = int(80)
COLUMNS = int(4)

column_width = SCREEN_WIDTH / COLUMNS
print ("Column width: ", column_width)

PADDING = 2
PADDING_CHAR = " "
BORDER_CHAR = "*"

HEADLINE = "headline"
BRAND = "brand"

event_width = column_width - (2 * PADDING)
print("Event width: ", event_width)

def make_border(border_char=BORDER_CHAR):
    string = border_char * int(event_width)
    return string

def clean(string):
    result = string.strip()
    chars = "\n"
    result = result.replace(chars, "")
    return result

def render_event(event, border_char=BORDER_CHAR):
    """

    render_event(event) -> list 

    Returns list of strings that formats event as a box.     
    """
    strings = list()
    if event is None:
        for i in range(7):
            strings.append("/n")
    else:
        left_pad = border_char + " "
        right_pad = " " + border_char

        max_length = event_width - len(left_pad) - len(right_pad)
        max_length = int(max_length)

        try:
            stated_brand = event.get_word()
        except AttributeError:
            stated_brand = event[BRAND]

        try:
            stated_headline = event.get_headline()
        except AttributeError:
            stated_headline = event[HEADLINE]
            
        brand = clean(stated_brand)
        headline = clean(stated_headline)

        if not headline:
            headline = PADDING_CHAR * max_length

        headline_1 = headline[: max_length]
        headline_2 = headline[max_length : (max_length * 2)]

        first_row = make_border()
        strings.append(first_row)

        second_row = render_line(headline_1)
        strings.append(second_row)

        third_row = render_line(headline_2)
        strings.append(third_row)

        fourth_row = render_line("")
        # blank row
        strings.append(fourth_row)

        # Fifth row
        fifth_row = render_line(brand)
        strings.append(fifth_row)

        sixth_row = copy.copy(fourth_row)
        strings.append(fourth_row)

        seventh_row = make_border()
        strings.append(seventh_row)

    return strings

def render_line(content, length=event_width, border_char=BORDER_CHAR,
                padding_char=PADDING_CHAR):
    """
    """
    margin_left = border_char + padding_char
    margin_right = padding_char + border_char
    content_length = length - len(margin_left + margin_right)
    content_length = int(content_length)

    adj_content = content
    if len(adj_content) < content_length:
        filler_width = content_length - len(content)
        filler_width = int(filler_width)
        adj_content = content + filler_width * padding_char
    elif len(adj_content) >= content_length:
        adj_content = adj_content[:content_length]

    result = margin_left + adj_content + margin_right
    # can modify to return remainder of what's not shown
            
    return result    

def align_center(string, length=column_width):
    """

    align_center(string) --> string

    Returns string with specified length. If string is shorter than length,
    function pads string with padding characters; otherwise, function truncates
    string.
    """
    length = int(length)
    wip = string[:length]
    padding = length - len(wip)
    margin = round(padding/2)
    one_side = int(margin) * PADDING_CHAR
    result = one_side + wip + one_side
    overage = length - len(result)
    if overage:
        result = one_side + wip[:-overage] + one_side
    return result  

def align_in_column(event):
    """

    align_in_column(event) -> list

    Returns list of strings that represent an event, aligned for one column.
    """
    strings = render_event(event)
    result = []
    for string in strings:
        aligned = align_center(string)
        result.append(aligned)
    return result

def align_in_row(strings):
    """

    align_in_row(list_of_strings) -> list

    Adds line break before and after the strings.
    """
    line_break = "\n"
    result = strings.copy()
    result.insert(0, line_break)
    result.append(line_break)
    
    return result

def render_column(*events):
    """

    render_column(*events) -> list

    Returns list of strings that represents each event.
    """
    result = list()
    for event in events:
        prepped = align_in_column(event)
        prepped = align_in_row(prepped)
        result.append(prepped)

    return result
    
def render_row(*events):
    """

    render_row(*events) -> list

    Renders events, aligns in column, joins columns, returns list of strings.
    """
    aligned_events = list()
    for event in events[ :COLUMNS]:
        prepped = align_in_column(event)
        aligned_events.append(prepped)

    # join
    row_height = len(aligned_events[0])
    i = 0
    joined_columns = list()
    while i < row_height:
        line = ""
        for column in aligned_events:
            line = line + column[i]
        joined_columns.append(line)
        i = i + 1

    if len(joined_columns) != row_height:
        raise Exception("Problem detected.")

    # add top and bottom margins
    result = align_in_row(joined_columns)
    
    return result
    
event1 = {
    HEADLINE : """The volcano erupted in Tonga and people
    are not paying attention.""",
    BRAND : "Tonga"
    }

event2 = {
    HEADLINE : """
    Meanwhile, Zoom is melting, with its stock price down 80% YTD.
    """,
    BRAND : "Zoom"
    }

event3 = {
    HEADLINE : """
    Meet Rockets of Awesome Founder Rachel Blumenthal!
    """,
    BRAND : "Rockets of Awesome"
    }

event4 = {
    HEADLINE : """
    The trendy kids' brand Rockets of Awesome is the latest DTC to stumble.
    """,
    BRAND : "Rockets of Awesome"
    }

for line in align_in_column(event1):
    print(line)

for line in align_in_column(event2):
    print(line)

for line in render_row(event1, event2):
    print(line)
    
events = [event1, event2, event3, event4]

for line in render_row(*events):
    print(line)

blank1 = {
    HEADLINE : "",
    BRAND : "Rockets of Awesome"
    }

blank2 = {
    HEADLINE : "",
    BRAND : ""
    }

for line in align_in_column(blank1):
    print(line)

for line in align_in_column(blank2):
    print(line)

spacer = render_event(blank2, border_char=" ")

# TODO
# 1) unpack column
# 2) align signatures
# 3) consider making border an event attribute
# 4) add a mini:
# 5) add a zoom
# 6) add a refresh logic
# 7) add numbering of events
# 8) move to oop in CLI gui? take JSON event, turn them into objects, then make
#    it easier to do stuff like keep track of read or not, hide, save.
# 9) some kind of filter (by brand? bigger boxes?)
# 10) some kind of filter by channel


