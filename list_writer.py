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
Module defines functionality for saving lists to CSV.
"""

# Imports
# 1) Built-ins
import csv
import json
import os
import math

# 2) Port.
import exceptions
import list_reader

# 3) Constants
BLANK = "\n"
COPY_PREFIX = "z_"
COPY_SUFFIX = ""

BRAND = list_reader.BRAND
GROUP = list_reader.GROUP
DATA = "Data"
HEADER = [BRAND, GROUP, DATA]

CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWS = CAPS.lower()

# make the result readable in excel
def clean_lines(path, overwrite=False):
    """

    clean_lines() -> string

    Function removes blank lines from a file. If you turn off "overwrite", you
    get back a path to the old file.
    """
    # if not overwrite, saves a copy of the old file
    result = ""
    original = path
    cleaned = make_path_for_copy(path)

    remove_blanks_and_copy(original, cleaned)

    swap_names(original, cleaned)
    
    if overwrite:
        os.remove(cleaned)
    else:
        result = cleaned

    return result

def convert_to_column_index(number):
    """

    convert_to_column_index() -> str

    Function takes a number and returns a column name in Excel format. 
    """
    result = ""
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(caps)

    quotient = number // base
    if quotient:
        digits = str(quotient)
        for digit in digits:
            # digit is a string
            i = int(digit) - 1
            char = caps[i]
            result += char

    rem = number - quotient * base
    result += caps[rem]

    return result

def turn_column_into_int(string):
    """
    -> int

    assumes string is in "aaa" format. 
    """
    result = 0
    
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lows = caps.lower()
    #in "bac", the left-most position is in 26^2 units, the middle is in
    # 26^1 units, and the bottom is in 26^0 units.

    base = len(lows)
    highest_exp = len(string) - 1
    
    exp = highest_exp
    
    for char in string:
        # parses left to right
        multiplier = base**exp
        count = lows.find(char) + 1
        # probably should be gone
        value = count * multiplier
        
        result = result + value
        exp = exp - 1

    return result

def turn_int_into_column(number, trace=True):
    """
    -> string

    String comes back in "aaa" format.
    """
    result = ""
    
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lows = caps.lower()

    base = len(lows)

    # if number is lower than base ^ n + base ^ (n-1)
    # then you use n - 1 digits, else you use n digits
    # then you just go through units.

    # x = base ^ n + base ^ (n-1), solve for n <-- can make this prettier. 

    # so do it once for the difference. while n >= 0.
    # if rem, raise error.

    log = math.log(number, base)
    
    if trace:
        print("Crude raw: %s" % log)
        
    n = math.floor(log)
    # I assume I need the rounded-down number of symbols to represent the
    # number, unless I find out otherwise below
    
    if trace:
        print("Crude:     %s" % n)

    cutoff = compute_cutoff(log, base)
    # there is probably some equation I can solve to get this without a
    # function call
    
    if number > cutoff:
        n = n + 1
    # There is a chance I could get rid of this block.
    

    rem = number
    while n >= 0:
        
        if trace:
            print("Rem:    %s" % rem)
            print("n:      %s" % n)
            print("cut:    %s\n" % cutoff)
            
        if rem <= base:
            n = 0
        # defensive logic, I am trying to start counting in units of 26**0 for
        # 26, not 26**1
        
        unit = base**n
        count = rem // unit
        count = int(count)
        i = count - 1
        
        if trace:
            print("Unit:   %s" % unit)
            print("Count:  %s" % count)
            print("Type:   %s" % type(count))
            print("i:      %s\n" % i)    
        
        symbol = lows[i]
        result = result + symbol

        accounted = count * unit
        rem = rem - accounted            

        n = n - 1

        if trace:
            print("Symbol: %s" % symbol)
            print("Result: %s" % result)
            print("Acct'd: %s" % accounted)
            print("Rem:    %s" % rem)
            print("n:      %s\n\n" % n)
        
    else:
        if rem != 0:
            print(rem)
            raise exceptions.OperationError("should have 0 rem")   
    
    return result

def so_alt(num):
    pass
    # result = ""
    # exp = log(num, 26)

    # rem = num
    # for i in range(exp):
    #   # see how many you can account for in this unit
    #   # do a rem
    #   # can almost cycle up and cycle down
    #   # cycle up: max out, add a whatever

    # # number of singles (for btwn 27 and 52)
    # n - 26^0.
    # n - 26^0 + 26^1 -> if 0, then i get a
    
    # 26^0 = 1 # first number that's one symbol
    # 26^0 + 26^1 = 27 # first numnber thats two symboles
    # 26^0 + 26^1 + 26^2 = 703 # first number that's three symbols
    # 26^0 + 26^1 + 26^2 + 26^3 = x # first number that four symbols
    # distance from first number: n - that chunk
    # for twos:
    #   subtract 27
    #   if 0, you get a

    # so i take the log
    # i start going through it
    # i subtract 26 (26^1) to show it in a through z,
    # 26 are accounted for
    # then i divide the rest by 26    

def inefficient(num):
    pass
    # i take the number
    # i check if its < 26, if so i do one thing
    # I check if its < 702, i do another thing
    # I check if its < whatever, i do a third thing

    # I take the number, I check its log
    # I subtract the base ** floor(log)
    # I check the remainder vs the cutoff for log-1
    # if its less, i put the remainder through
    # if its more, i need one more char

    # or as i had it above
    #  get the log
    #  check if i am above or below the cutoff for that log
    #  if above, number of symbols is rounded up
    #  else, number of symbols is rounded down
    #  then start calculating
    # start with the number of symbols
    #  subtract the cutoff for that cutoff - 1
    #  divide the diff by the unit
    #  round up
    #  that's my index for the first char
    
    # repeat until done

    # may be i should make this recursive
    # may be it is easier to understand this way

def yo(number, symbols=LOWS):
    """

    -> string

    Return a string that translates a number into a string of symbols. 
    """
    result = ""
    number = int(number)
    # Will throw an exception if number is float. Floats don't work right now.
    
    base = len(symbols)
    log = math.log(number, base)

    # determine number of digits
    cutoff = compute_cutoff(log, base)
    if number < cutoff:
        n = math.floor(log)
    else:
        n = math.ceil(log)

    # get digits
    tail_length = max(n - 1, 0)
    
    max_tail = compute_cutoff(tail_length) - 1
    diff = number - max_tail

    unit = base**n
    count = diff // unit
    # this this should be in [0,base] by virtue of starting from a log
    count = int(count)
    position = count - 1

    head = symbols[position]
    result += head

    rem = number - count * unit
    # with <=26, rem should be 0 because units are 1
    if rem: 
        tail = yo(rem)
        result += tail

    return result

# if number < len(symbols), get the i
# else, go through the power stuff
# can be refactored as, generate a tuple of digits
# map tuple to symbols

def again(number, base=26):
    """

    -> list

    Function returns a list of integers. If youuse each integer as the index
    of a string that contains the symbols you use to express the base, you will
    get a string that represents the number.
    """
    result = list()
    
    log = math.log(number, base)
    exp = math.floor(log)

    rem = number
    for i in range(exp, -1, -1):
        # list(range(1,-1,-1)) generates [1, 0]
        unit = base**i
        
        tail = measure_tail(i, base)
        # tail is the max value that can be expressed by fewer than i chars
        
        amount = rem - tail        
        count = amount // unit
        
        if count:
##            result.insert(1, count)
            result.append(count)

        rem = rem - count * unit

    return result

def map_to_symbols(positions, symbols=LOWS):
    """

    -> string

    Function returns a string that maps the positions to the symbols. 
    """
    result = ""
    
    for i in positions:
        symbol = symbols[(i - 1)]
        result = result + symbol
        
    return result

def to_col(number, symbols=LOWS):
    """

    -> string

    Returns a string that represents the number in the symbols provided.
    """
    base = len(symbols)
    positions = again(number, base)
    result = map_to_symbols(positions, symbols)
    return result

def measure_tail(exp, base=26):
    """

    -> int

    Returns the max number that can be expressed in 1 fewer than the exponent.    
    """
    result = 0
    for i in range(exp):
        increment = base ** i
        result = result + increment

    return result

def compute_cutoff(log, base=26):
    """

    -> int

    Returns a base-10 integer that represents the first number that requires
    floor(log) + 1 symbols in the base. For example, if log is 1.25 and the base
    is 26, the function will return 703, the first number that requires 3
    symbols.
    """
    result = 0
    exp = math.ceil(log)
    # round down to the nearest integer.
    for i in range(exp):
        increment = base ** i
        result += increment

    result += base ** exp
    # range(2) is [0, 1], so i need to pick up the 2 itself.

    return result
    
def make_header(*fields):
    """

    make_header() -> list()

    Function returns a list of the arguments. 
    """
    result = list(fields)
    return result        
    
def make_path_for_copy(path, filename=None, prefix=COPY_PREFIX,
                       suffix=COPY_SUFFIX):
    """

    make_path_for_copy() -> string

    Function generates a path for copying a file on the basis of the input. If
    you leave the parameters as is, you will get something like
    dir\\filename_copy.ext.
    """
    result = ""
    # let's say path is "c:\\fruit\\bananas\\yellow.py"
    head, tail = os.path.split(path)
    # head is "c:\\fruit\\bananas\\", tail is "yellow.py"
    result += head

    t_name, ext = os.path.splitext(tail)
    # "name" is "yellow", ext is ".py"
    if not filename:
        filename = t_name

    file = prefix + filename + suffix + ext
    result = os.path.join(result, file)
    if os.path.exists(result):
        c = "A file exists at the path you built."
        raise exceptions.OperationError(c)
    
    return result

def make_row_per_layout(data, layout, flatten=True, field_for_remainder=DATA):
    """

    make_row_per_layout() -> list

    Function returns a list of entries that correspond to the order in layout.
    If you don't include a field in data, you get None; the remainder goes in the
    field_for_remainder, or at the end. 
    """
    row = list()
    wip = data.copy()

    field_count = len(layout)
    remainder_position = None
    
    for i in range(field_count):
        field = layout[i]
        if field == field_for_remainder:
            remainder_position = i
            row.append(None)
            # placeholder value
            continue
        else:
            value = wip.pop(field, None)
            row.append(value)

    rem = wip
    if flatten:
        rem = json.dumps(rem)

    if remainder_position is not None:
        row[remainder_position] = rem
    else:
        row.append(rem)

    return row
    # <----------------------------------------------- or just automatically
    # flatten and don't discard if the rem_field is not in the layout?
    
    
    # what do i want? i want:
    # a) make a 3 column thing, wehre it goes brand, group, data, and data picks
    # up anything that's not in brand or group
    #  - layout = ["Brand", "Group", "Data"]
    #  - entry = ["Piccolina", "Consumer", "{...}"]
    
    # b) make a 4 column thing, where it goes brand, group, data, on, and data
    # picks up everything that's left over
    #  - layout = ["Brand", "Group", "Data", "On"]
    #  - entry = ["Piccolina", "Consumer", "{...}", "True"]
    
def make_rows(watchlist, sort=False):
    """

    make_rows() -> list

    Function returns a list of rows for each brand in the watchlist. 
    """
    result = list()
    header = make_header(*HEADER)
    result.append(header)

    group_names = watchlist.keys()
    if sort:
        group_names = sorted(group_names)

    for group_name in group_names:
        group = watchlist[group_name]
        rows_for_group = make_rows_for_group(group_name, group, sort=sort,
                                             header=header)
        result.extend(rows_for_group)

    return result

def make_rows_for_group(group_name, group, sort=False, header=HEADER):
    """

    make_rows() -> list

    Function returns a list of rows, where each row represents the brand in the
    group. 
    """
    rows = list()
    wip = group.copy()
    
    brand_names = wip.keys()
    if sort:
        brand_names = sorted(brand_names)

    for brand_name in brand_names:
        data = dict()
        known = wip[brand_name]
        data.update(known)
        # need to avoid modifications of input. 
        
        data[BRAND] = brand_name
        data[GROUP] = group_name
        # enrich data here
        
        row = make_row_per_layout(data, header)
        rows.append(row)

    return rows

def remove_blanks_and_copy(src, dst, blank=BLANK):
    """

    remove_blanks_and_copy() -> int

    Function copies lines that do not match blank from src to dst. You get the
    number of lines removed back.
    """
    src_file = open(src, "r")
    dst_file = open(dst, "w")

    counter = 0
    for line in src_file:
        if line == blank:
            counter += 1
            continue
        else:
            dst_file.write(line)

    src_file.close()
    dst_file.close()

    return counter

def save(path, watchlist, clean=True, overwrite=False):
    """

    save() -> None

    Function saves the watchlist to a file as CSV.
    """
    
    file = open(path, "w")
    # add some safety to avoid overwrites?   
    writer = csv.writer(file)

    rows = make_rows(watchlist)
    writer.writerows(rows)
    file.close()

    if clean:
        clean_lines(path, overwrite=overwrite)

def swap_names(original, replica):
    """

    swap_names() -> None

    Function renames the original path as the replica and vice versa.
    """
    placeholder = make_path_for_copy(original, suffix=" temp")
    os.rename(original, placeholder)

    os.rename(replica, original)
    os.rename(placeholder, replica)    

# Testing
_LOCATION_1 = r"C:\Users\Ilya\Dropbox\Club\Product\Watchlist CSV2.csv"
_LOCATION_2 = r"C:\Users\Ilya\Dropbox\Club\Product\Watchlist CSV3.csv"

def _run_test1(path, trace=False):
    data = list_reader.load(list_reader._LOCATION)
    
    if trace:
        print(data)
        
    save(path, data, clean=False)

    return data

def _run_test2(path):
    backup = clean_lines(path, overwrite=False)
    return backup

def _run_test3(path, data):
    save(path, data, clean=True, overwrite=True)

def _clean_results(*paths):
    for p in paths:
        os.remove(p)

def _run_test4(path, data):
    recorded = list_reader.load(path)
    if recorded == data:
        _clean_results(path)
    else:
        c = "Recorded does not match data"
        raise exceptions.OperationError(c)
        # should define an equivalence error and return it with the args

    return recorded

def _run_test(clean=True, trace=True):
    data = _run_test1(_LOCATION_1)

    if trace:
        print("Test 1: passed.")
    
    backup = _run_test2(_LOCATION_1)
    if trace:
        print("Test 2: passed.")
        
    if clean:
        _clean_results(_LOCATION_1, backup)
    
    _run_test3(_LOCATION_2, data)
    if trace:
        print("Test 3: passed.")
        
    recorded = _run_test4(_LOCATION_2, data)
    if trace:
        print("Test 4: passed.")
        print("Tests completed.")
        print("Data recorded: ")
        print(recorded)

    return recorded

if __name__ == "__main__":
    _run_test()
