#!/usr/bin/env python3
"""this script demos taking a variable of two possible types"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """this takes a string and a float or int and returns a tuple"""
    return (k, float(v * v))
