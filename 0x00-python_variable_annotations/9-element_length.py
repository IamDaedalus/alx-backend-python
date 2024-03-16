#!/usr/bin/env python3
"""duck typing demo script"""

from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples containing a sequence and an int"""
    return [(i, len(i)) for i in lst]
