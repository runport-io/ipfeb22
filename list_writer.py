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

# imports
# 1) Built-ins
import csv
import json
import os

# 2) Port.
import list_reader

# 3) Constants
BLANK = "\n"

def make_row(group_name, brand_name, data=None, flatten=True):
    """

    make_row() -> list()

    Function returns a list that represents a row associated with the inputs.
    """
    if flatten:
        data = json.dumps(data)
    row = [brand_name, group_name, data]
    # this should run on a layout object of some sort
    
    return row

def make_rows_for_group(group_name, group, sort=False):
    """

    make_rows() -> list

    Function returns a list of rows, where each row represents the brand in the
    group. 
    """
    rows = list()
    
    brand_names = group.keys()
    if sort:
        brand_names = sorted(brand_names)

    for brand_name in brand_names:
        data = group[brand_name]
        row = make_row(group_name, brand_name, data)
        rows.append(row)

    return rows

def make_rows(watchlist, sort=False):
    """

    make_rows() -> list

    Function returns a list of rows for each brand in the watchlist. 
    """
    result = list()

    group_names = watchlist.keys()
    if sort:
        group_names = sorted(group_names)

    for group_name in group_names:
        group = watchlist[group_name]
        rows_for_group = make_rows_for_group(group_name, group, sort=sort)
        result.extend(rows_for_group)

    return result

def remove_blanks(path, prefix="z_"):
    directory = os.path.dirname(path)
    base = os.path.basename(path)
    file_name, extension = os.path.splitext(base)
    new_name = prefix + file_name + extension
    new_path = os.path.join(base, new_name)   

    os.rename(path, new_path)

    file_start = open(new_path, "r")
    file_end = open(path, "w")

    for line in file_start:
        if line == "\n":
            continue
        else:
            file_end.writeline(line)

    # removes all blanks.

def get_non_blanks_alt(path, blank=BLANK):
    lines = list()
    f = open(path, "r")
    for line in f:
        if line == blank:
            continue
        else:
            lines.append(line)

    f.close()
    return lines

def remove_blanks_and_copy(src, dst, blank=BLANK):
    """

    -> int

    Function copies lines that do not match blank from src to dst. 
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

def save(path, watchlist):
    """

    save() -> list

    Function saves the watchlist to a file as CSV.
    """
    
    file = open(path, "w")
    # add some safety to avoid overwrites?   
    writer = csv.writer(file)

    rows = make_rows(watchlist)
    writer.writerows(rows)
    file.close()

    remove_blanks(path)

    return rows

# make the result readable in excel
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

# Testing
_LOCATION_2 = r"C:\Users\Ilya\Dropbox\Club\Product\Watchlist CSV2.csv"

def run_test1(path, trace=True):
    data = list_reader.run_test4(list_reader._LOCATION)
    
    if trace:
        print(data)
        
    save(path, data)

def run_test():
    run_test1(_LOCATION_2)

if __name__ == "__main__":
    run_test()
