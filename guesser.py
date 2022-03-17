# guesser
def make_columns(rows, pad=True):
    """

    make_columns() -> list

    Function creates a list of lists where the list in position 0 has items
    from each row[0], and so on. 
    """
    columns = list()

    lengths = [len(row) for row in rows]
    max_length = max(lengths)

    for i in range(max_length):
        column = list()
        for row in rows:
            item = None
            try:
                item = row[i]
            except IndexError:
                pass
            column.append(item)
        columns.append(column)

    return columns

def compute_uniqueness(container, ceiling=1):
    """

    score_container() -> float

    Function computes the ratio of unique values in the container to the length
    of the container. If you specify the "ceiling", the score will not exceed
    that number.
    """
    uniques = set(container)
    score = len(uniques) / len(container)
    if score > ceiling:
        score = ceiling

    return score
    
def compute_repetition(container):
    """

    compute_repetition() -> float

    Function counts the number of repetitions in the container and returns
    a score that divides that number by the length of the container. 
    """
    uniques = set(container)
    number_of_uniques = len(uniques)
    number_of_items = len(container)
    repetitions = number_of_items - number_of_uniques
    score = repetitions / number_of_items

def guess_alt(data):
    result = list()
    columns = make_columns(data)
    sample = columns[:2]

    scores = list()
    for column in sample:
        score = compute_repetitions(column)
        scores.append(score)

    max_score = max(scores)
    min_score = min(scores)
    
    if scores[0] == max_score:
        layout = [GROUPS, BRANDS]
        # groups should have more reptitions
    else:
        layout = [BRANDS, GROUPS]

    # probably need to pad, but the padding should be the column numbering. 
    # add logic to use a sample
    
    return result

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

# how this should work:
# if i say load(guess=True), I should
#  a) guess the header
#  b) print the header
#  c) accept the header?
#  d) modify the header?
#  then parse on the basis of the header
