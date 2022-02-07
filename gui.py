# Mini gui
# (c) Port. Prerogative Club 2022

SCREEN_WIDTH = 80
COLUMNS = 4

column_width = SCREEN_WIDTH / COLUMNS
print ("Column width: ", column_width)

PADDING = 2
BORDER_CHAR = "*"

event_width = column_width - (2 * PADDING)
print("Border width: ", border_width)
content_width = event_width - 2 * (len(BORDER_CHAR) + 1)
# + to account for the space, multiplied on each side 

def make_boundary():
    string = BORDER_CHAR * event_width
    return string
    
def render(event):
    """
    render(event) -> string

    Does not include new line chars for now
    """
    strings = list()
    first_row = make_boundary()
    strings.append(first_row)
    
    max_length = event_width - 4
    # on each side: one char of border, one char of padding

    headline_1 = event.headline[: max_length]
    headline_2 = event.headline[max_length : (max_length * 2)]

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

    fifth_row = third_row.copy()
    strings.append(fifth_row)

    sixth_row = make_boundary()
    strings.append(sixth_row)

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

      
        

event1 = {
    "headline" : """
    The volcano erupted in Tonga and people are
    not paying attention.
    """,
    "brand" : "Tonga"
    }

event2 = "headline" : """
    Meanwhile, Zoom is melting, with its stock price down 80% YTD.
    """,
    "brand" : "Zoom"
    }


    
    
    
    
