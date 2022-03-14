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

Module provides functions for loading a watchlist from file. 

------------------  ------------------------------------------------------------
Attribute           Description
------------------  ------------------------------------------------------------

DATA:

FUNCTIONS:

CLASSES:
Event               Object organizes information about a moment in time.
------------------  ------------------------------------------------------------
"""


# Imports
# 1) Built-ins
import csv
import os

# 2) Port.
import exceptions

# 3) Constants
BRAND = "Brand"
GROUP = "Group"

NORMALIZED_COLUMNS = [BRAND, GROUP]

# 4) Functions
def get_header(rows):
    """

    get_header() -> list

    Function returns a list of names for columns in a CSV file. You should
    supply a list of rows.
    """
    header = rows[0]
    return header

def normalize_header(header, columns=NORMALIZED_COLUMNS):
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

def guess_order(file, ratio=4):
    """

    guess_order() -> list

    Function returns a list of strings that can serve as a header.
    """
    result = list()
    fallback = [BRAND, GROUP]

    SAMPLE_LENGTH = 40
    sample = get_sample(file, length=SAMPLE_LENGTH)
    columns = make_columns(sample)

    scores = list()
##    min_score = 0
##    min_index = 0
##    
##    max_score = 0
##    max_index = 0
#     # placeholder for more complex comparisons

    column_count = len(columns)
    for i in range(column_count):
        
        column = columns[i]        
        uniques = set(column)
        number_of_uniques = len(uniques)
        score = round(number_of_uniques/SAMPLE_LENGTH * 100)
        scores.append(score)

##        if score <= min_score:
##            min_score = score
##            min_index = i
##    
##        if score >= max_score:
##            max_score = score
##            max_index = i
##
##        # placeholder logic, if i wanted to compare all the columns

    # the concept here is to take the column with the most unique strings, and
    # say that's the brands; the one with less is the groups
    score_a = scores[0]
    score_b = scores[1]        
    
    observed_ratio = max(score_a, score_b) / min(score_a, score_b)

    if observed_ratio < min_ratio:
        c = "can't guess, too close"
        raise exceptions.OperatorError
    else:
        if score_a > score_b:
            result = [BRAND, GROUP]
        else:
            result = [GROUP, BRAND]

    return result

    # the least unique is likely to be notes, because it has so many blanks
    # but that's also like an ungrouped watchlist, where the group is None

    # guess_col_with_brands(): max uniqueness score, returns i
    # guess_col_with_groups(): returns i, uniqueness less than brands,
    
def make_columns():
    pass

def get_sample(file, length=20):
    """

    get_sample() -> list

    Function returns a list of lines. You should pass in an open file.
    """
    lines = list()
    i = 0
    for line in file:
        # I am using the built-in iterator here to avoid loading the file into
        # memory. 
        lines.append(line)
        if i >= length:
            break
        i += 1
        
    return lines

def read_path(path, policy=None):
    """

    read_path() -> list

    Function reads the file at path and returns a list of rows from the file.
    You should specify a path to a CSV file that you generate in Excel.
    """    
    if not os.path.exists(path):
        raise exceptions.OperationError

    file = open(path, "r")
    iterator = csv.reader(file)
    rows = list(iterator)
    print(rows[:5])
    # policy?
    file.close()
    
    header = get_header(rows)
    print(header)
    # should i check for headers? may be

    no_header = rows[1:]
    # assumes there is a header
    entries = read_rows_as_pattern(no_header, header)
    # list of dictionaries
        
    return entries    

def read_rows_as_pattern(rows, header):
    """

    read_rows_as_pattern() -> list

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

def simplify():
    pass
    # takes a watchlist with notes and turns it into just a set of words.

def enrich():
    pass
    # inverse of simplify, adds metadata to each brand. 
    
def turn_entries_into_dict(entries, keep_data=True):
    """

    turn_entries_into_dict() -> dict()

    Function takes a list of rows that include brand and group name and
    organizes them into a dictionary keyed by group name. 
    """
    result = dict()
    for entry in entries:
        group_name = entry[GROUP]
        brand_name = entry[BRAND]
        group = result.setdefault(group_name, set())
        group.add(brand_name)
        # meta data? each brand should be a dictionary here? or an obj?
        
    return result

def turn_list_into_watchlist():
    pass
    # take a list and build the watchlist out of it
    # returns object

location = r"C:\Users\Ilya\Dropbox\Club\Product\Watchlist CSV.csv"

def run_test1(path):
    entries = read_path(path)
    sample = entries[:20]
    for entry in enumerate(sample):
        print(entry)

    return entries

def run_test2(entries):
    result = turn_entries_into_dict(entries)
    return result

def run_test3():
    pass
    # make the watchlist object

def run_test4():
    pass
    # export the watchlist into a file.
    
def run_test(path):
    entries = run_test1(path)
    result = run_test2(entries)
    print(result.keys())

    return result

if __name__ == "__main__":
    run_test(location)

# add guess on the order (brand, group)
# add metahandling
# add docstrings
# add export.
    #  what to do with None? with blanks? 
# -> by row
# handle "None" for group

