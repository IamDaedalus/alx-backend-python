#!/usr/bin/env python3
"""this script is a mixed bag of types summed"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ sums a mixed list of floats and ints"""
    return sum(mxd_list)
