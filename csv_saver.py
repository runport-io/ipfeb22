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

def generate_rows(group, sort=False):
    """

    generate_rows() -> list

    Function generates a list of rows (lists) for each brand in the group. If
    you specify sort, the order of the rows is stable. 
    """
    result = list()
    
    brand_names = group.keys()
    if sort:
        brand_names = sorted(brand_names)

    for brand in brand_names:
        data = group[brand]
        flat = json.dumps(data)
        row = [brand, group, flat]
        result.append(row)

    return result

def export2(watchlist, path, sort=False):
    group_names = watchlist.keys()
    if sort:
        group_names = sorted(group_names)

    rows = list()
    for group_name in group_names:
        group = watchlist[group_name]
        rows_for_group = generate_rows(group, sort=sort)
        rows.extend(rows_for_group)

    file = open(path, "w")
    writer = csv.writer(file)
    writer.writerows(rows)
    file.close()

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
