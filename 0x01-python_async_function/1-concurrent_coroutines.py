#!/usr/bin/env python3
"""
this module imports another async method and creates a sorted list of delays
"""

import asyncio
from typing import List
wr = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ this method returns a list of delays """
    delays: List[float] = await asyncio.gather(
            *(wr(max_delay) for _ in range(n)))

    return sorted(delays)
