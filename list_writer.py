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
            i = int(digit)
            char = caps[i]
            result += char

    rem = number - quotient * base
    result += caps[rem]

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
