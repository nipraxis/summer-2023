""" Testing for anatomical notebook.
"""

import functools

import numpy as np

import nipraxis


n_slices = 32


@functools.lru_cache
def get_anatomical_lines():
    fname = nipraxis.fetch_file('anatomical.txt')
    with open(fname, 'rt') as fobj:
        return fobj.readlines()


def get_n_pixels():
    return len(get_anatomical_lines())


def get_n_pixels_slice():
    return get_n_pixels() / n_slices


def get_candidates():
    return [120, 130, 136, 156, 170, 195]


def get_pairs():
    return np.array(
        [[120, 221],
         [130, 204],
         [136, 195],
         [156, 170],
         [170, 156],
         [195, 136]])


def get_full_shape():
    return [170, 156, 32]
