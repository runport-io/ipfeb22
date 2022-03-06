# datetime supplements

import time

def convert_to_tuple(string):
    """

    -> time tuple
    """
    tokens = string.split()
    print(tokens)
    day = tokens[0]
    day = day.strip(",")
    print("Day: ", day)
    date = tokens[1]
    month = tokens[2]
    year = tokens[3]
    hhmmss = tokens[4]
    # skips the time zone for now
    
    alt_tokens = [day, month, date, hhmmss, year]
    print("Alt tokens: \n", alt_tokens)
    
    alt_string = " ".join(alt_tokens)
    print("Alt string: \n", alt_string)

    result = time.strptime(alt_string)
    return result


    
    
