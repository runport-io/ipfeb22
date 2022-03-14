# reader

# Imports
# 1) Built-ins
import csv
import os

# 2) Port.
import exceptions

# 3) Constants
BRAND = "Brand"
GROUP = "Group"

# 4) Functions
def sample_file(file, length=20):
    lines = list()
    i = 0
    while i < 20:
        line = file.readline()
        lines.append(line)
        i += 1
    return lines    

def read_path(path, policy=None):
    # check that file exists
    # open file
    # feed into csv
    # check for headers
    # parse each row
    # return results (as a list to start)
    
    if not os.path.exists(path):
        raise exceptions.OperationError

    file = open(path, "r")
    iterator = csv.reader(file)
    rows = list(iterator)
    print(rows[:5])
    # policy?
    file.close()
    
    header = read_header(rows)
    print(header)
    # should i check for headers? may be

    no_header = rows[1:]
    # assumes there is a header
    entries = read_rows_as_pattern(no_header, header)
    # list of dictionaries
        
    return entries    

def read_header(rows):
    header = rows[0]
    return header

def read_rows_as_pattern(rows, header):
    # returns list, expects pattern to be a list
    entries = list()
    for row in rows:
        labelled = zip(header, row)
        entry = dict(labelled)
        entries.append(entry)

    return entries
    
def turn_entries_into_dict(entries, keep_data=True):
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

def run_test(path):
    entries = run_test1(path)
    result = run_test2(entries)
    print(result.keys())

    return result

if __name__ == "__main__":
    run_test(location)

# add flex on the naming
# add guess on the order (brand, group)
# add metahandling
# add docstrings
        
