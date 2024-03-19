#!/usr/bin/env python3
"""
this module imports async_generator and uses it to collect
10 random numbers into a list
"""

from typing import List
ag = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    this method collects 10 random values from the async generator
    function and returns them as a List
    """
    return [i async for i in ag()]
