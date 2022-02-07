# Mini gui
# (c) Port. Prerogative Club 2022

import copy
import math

SCREEN_WIDTH = 80
COLUMNS = 4

column_width = SCREEN_WIDTH / COLUMNS
print ("Column width: ", column_width)

PADDING = 2
PADDING_CHAR = " "
BORDER_CHAR = "*"

HEADLINE = "headline"
BRAND = "brand"

event_width = column_width - (2 * PADDING)
print("Event width: ", event_width)
content_width = event_width - 2 * (len(BORDER_CHAR) + 1)
# + to account for the space, multiplied on each side 
content_width = int(content_width)

def make_border():
    string = BORDER_CHAR * int(event_width)
    return string

def clean(string):
    result = string.strip()
    chars = "\n"
    result = result.replace(chars, "")
    return result

def render_event(event):
    """

    render_event(event) -> list 

    Returns list of strings that formats event as a box.     
    """
    headline = clean(event[HEADLINE])
    brand = clean(event[BRAND])

    strings = list()
    first_row = make_border()
    strings.append(first_row)
    
    max_length = event_width - 4
    max_length = int(max_length)
    # on each side: one char of border, one char of padding

    
    headline_1 = headline[: max_length]
    headline_2 = headline[max_length : (max_length * 2)]

    left_pad = BORDER_CHAR + " "
    right_pad = " " + BORDER_CHAR
    
    second_row = left_pad + headline_1 + right_pad
    # can refactor into method make_row(content) -> string
    strings.append(second_row)

    third_row = left_pad + headline_2 + right_pad
    strings.append(third_row)

    fourth_row = left_pad + (" " * content_width) + right_pad
    # blank row
    strings.append(fourth_row)

    # Fifth row

    start = left_pad + brand[:max_length]
    rem = event_width - len(start) - len(right_pad)
    rem = int(rem)
    start = start + rem * " "
    start = start + right_pad
    fifth_row = start
    strings.append(fifth_row)

    sixth_row = copy.copy(fourth_row)
    strings.append(fourth_row)

    seventh_row = make_border()
    strings.append(seventh_row)

    return strings
    
def position_in_row(event_strings):
    """
    position_in_row(event_strings) -> string

    returns one string with new lines and padding
    
    """
    pass
    # result = ""
    # for string in event_strings:
    #   updated = padding + string + padding + new_line
    #   result = result + updated
    # return result

def align_in_column(event):
    """

    align_in_column(event) -> list

    Returns list of strings that represent an event, aligned for one column.
    """
    strings = render_event(event)
    result = []
    for string in strings:
        aligned = align_center(string)
        result.append(string)
    return result

def align_center(string, length = column_width):
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

def make_row(*events):
    """
    --> string
    makes one [or more rows?]
    """
    row = events[:COLUMNS]
    result = ""
    component_strings = []
    for event in row:
        event_string = render(event)
        component_strings.append(event_string)

    line_1 = ""
    line_2 = ""
    line_3 = ""
    
    for event in event_strings:
        line_1 = line_1 + PADDING + PADDING + event[0]
        # add events in a row
    # logic different for last event, first event, middle
    # need to have a list with all the strings for each event
    # build from start to accomodate blank events

def make_row2(events):
    # first column = generate a set of strings, 1+; left padded
    # last column = generate a set of strings, 1+, right padded
    # I know that rows are max height of certain number (8?)
    # middle rows = generate strings, padded on both sides

    # assemble the strings
    # for each line in the row: take the first, the middle, and the last
    # return row

    row = events[:COLUMNS]
    first_event = row.pop(0)
    first_column = make_first(first_event)
    # need to define make_first()
    last_event = row.pop()
    last_column = make_last(last_event)
    # need to make function
    
    strings_by_column = [first_column]
       
    for event in row:
        column = make_middle(event)
        strings_by_column.append(column)

    strings_by_column.append(last_column)
    # list now contains formatted strings

    concat = []
    while i < ROW_HEIGHT:
        # row height
        combined_line = line
        for column in strings_by_column:
            combined_line += column[i]
        concat.append(combined_line)
        i = i + 1

    if len(contact) != ROW_HEIGHT:
        raise Exception("problem")
    
    return concat

def make_first(event):
    """
    -> list()
    
    Returns list of strings was if the event appeared in the left-most column
    """
    event_strings = render_event(event)
    result = []
    pad = PADDING * PADDING_CHAR
    for string in event_strings:
        with_padding = pad + string + pad
        result.attach(with_padding)
    return result


def render_screen():
    # make rows
    # result = [] 
    # for each row:
    #   result.append(render_row(row))
    # for each row in result:
    #   print(row)
    pass
    
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

for line in align_in_column(event1):
    print(line)

for line in align_in_column(event2):
    print(line)

    
    
    
