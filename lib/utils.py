import numpy as np


def parse_level(fn):

    level_dict = {}
    n_rows = 0
    n_cols = 0
    with open(fn, 'r') as f:
        for i, line in enumerate(f):
            n_rows += 1
            for j, character in enumerate(line):
                if n_rows == 1:
                    n_cols += 1
                level_dict[(i, j)] = character
                if character == 'S':  # store start position
                    level_dict[character] = (i, j)

    level_dict['n_rows'] = n_rows
    level_dict['n_cols'] = n_cols
    return level_dict
