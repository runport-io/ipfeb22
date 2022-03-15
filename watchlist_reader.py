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

Module provides functions for opening CSV files and reading their contents as
a Watchlist.

------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:
BRAND               key for brand
GROUP               key for group #<------------------------------------------- pull from csv_saver
STANDARD_COLUMNS    columns that we want to have standard spelling

FUNCTIONS:
clean_data          replace empty string with None in keys
enrich              make each group in list a dictionary of brand name to data
enrich_group        make a dictionary of names to data for each brand in group

get_header          gets the first row of the file
group               takes a list of entries and keyes them by group
label               turns a row into a dictionary with fields defined by header
make_watchlist      creates an object on the basis of data
normalize_header    adjusts fields in header to standard spelling
read_rows           extracts data from file in the form of rows of objects
simplify            makes a dictionary of sets of brand names
simplify_group      returns a set of strings on the basis of keys

CLASSES:
N/a
------------------  ------------------------------------------------------------
"""


# Imports
# 1) Built-ins
/import copy
import csv
import os

# 2) Port.
import exceptions
import watchlist

# 3) Constants
BRAND = "Brand"
GROUP = "Group"

STANDARD_COLUMNS = [BRAND, GROUP]

# 4) Functions
def clean_data(data):
    """

    clean_data() -> dict

    Function replaces a blank string in the keys of the input with a None. You
    get a new dictionary back. 
    """
    result = dict()
    result.update(data)
    
    blank = ""
    if blank in result.keys():
        unlabelled = result.pop(blank)
        result[None] = unlabelled

    return result

def enrich(watchlist):
    """

    enrich() -> dict

    Function adds a dictionary of data to each brand in the watchlist. You can
    run this to construct an inverse of simplify.
    """
    result = dict()
    for group_name, group in watchlist.items():
        result[group_name] = enrich_group(group)
    return result

def enrich_group(group, default=None):
    """

    enrich_group() -> dict

    Function takes a set and returns a dictionary based on the set. If you don't
    specify a default, you get an empty dictionary for each brand; otherwise,
    the value for each brand will be a deepcopy of the default. 
    """
    result = dict()

    if default is None:
        default = dict()
            
    for brand in group:
        value = copy.deepcopy(default)
        result[brand] = value
        
    return result

def get_header(rows):
    """

    get_header() -> list

    Function returns a list of names for columns in a CSV file. You should
    supply a list of rows.
    """
    header = rows[0]
    return header

def group(entries, keep_data=False):
    """

    group() -> dict()

    Function takes a list of rows that include brand and group name and
    organizes them into a dictionary keyed by group name. 
    """
    result = dict()
    for entry in entries:
        group_name = entry.pop(GROUP)
        brand_name = entry.pop(BRAND)

        default_container = dict()
        group = result.setdefault(group_name, default_container)
        
        data = dict()
        if keep_data:
            data = entry
        
        group[brand_name] = data
        
    return result

def label(rows, header):
    """

    label() -> list

    Function takes each row and turns it into a dictionary keyed by the header
    of the column. You should include a list of names as the header.
    """
    # returns list, expects pattern to be a list
    entries = list()
    for row in rows:
        labelled = zip(header, row)
        entry = dict(labelled)
        entries.append(entry)

    return entries

def load(path):
    """

    load() -> dict

    Function loads data from the path.
    """
    result = dict()
    rows = read_rows(path)
    result = group(rows)
    return result

def make_watchlist(data, keep_data=False):
    """

    make_watchlist() -> obj

    Function constructs a Watchlist from the data. 
    """
    data = clean_data(data)
    if not keep_data:
        data = simplify(data)
    result = watchlist.Watchlist.from_flat(data, keep_data=False)
    return result
    # should be on the Watchlist? should I stop with cleaning the data? <-----------------------------------------------------

def normalize_header(header, columns=STANDARD_COLUMNS):
    """

    normalize_header() -> list

    Function returns a list of strings that replaces some values in header with
    a version that includes capitals. You can specify the replacement values
    in columns. 
    """
    result = list()
    standards = {c.casefold():c for c in columns}
    i = 0
    length = len(header)
    while i < length:
        column = header[i]
        caseless = column.casefold()
        if caseless in standards.keys():
            standard = standards[caseless]
            result.append(standard)
            # replace the header field with the cased version
        else:
            result.append(column)

        i += 1

def read_rows(path, trace=False):
    """

    read_rows() -> list

    Function reads the file at path and returns a list of rows from the file.
    You should specify a path to a CSV file that you generate in Excel.
    """    
    if not os.path.exists(path):
        c = "File not found."
        raise exceptions.OperationError(c)

    file = open(path, "r")
    iterator = csv.reader(file)
    rows = list(iterator)

    if trace:
        print(rows[:5])
        
    file.close()
    
    header = get_header(rows)
    if trace:
        print(header)
    # should i check for headers? may be

    remaining_rows = rows[1:]
    # assumes there is a header
    entries = label(remaining_rows, header)
            
    return entries

def simplify(watchlist):
    """

    simplify() -> dict

    Function strips out any data from each brand and returns a dictionary of
    groups of strings.
    """
    result = dict()
    for group_name, group in watchlist.items():
        result[group_name] = simplify_group(group)
    return result

def simplify_group(group):
    """

    simplify_group() -> set

    Function takes a group and returns a set of all the keys.
    """
    result = set(group.keys())
    return result
    
# Testing    
location = r"C:\Users\Ilya\Dropbox\Club\Product\Watchlist CSV.csv"

def run_test1(path):
    rows = read_rows(path)
    sample = rows[:20]
    for row in enumerate(sample):
        print(entry)

    return rows

def run_test2(entries):
    result = group(entries)
    return result

def run_test3(watchlist):
    result = clean_data(watchlist)
    return result

def run_test4(path):
    result = load(path)
    return result
    
def run_test(path):
    entries = run_test1(path)
    data = run_test2(entries)
    print(data.keys())
    
    cleaned = run_test3(data)
    print(cleaned.keys())
    
    full = run_test4(path)
    return full

if __name__ == "__main__":
    run_test(location)

# add metahandling

# add export.
    #  what to do with None? with blanks? 
# -> by row

## 3 modules:
# export
# import
# guess



