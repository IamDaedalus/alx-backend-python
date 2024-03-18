#!/usr/bin/env python3
"""
this module imports another async method and creates a sorted list of delays
"""

import asyncio
wr = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """ this method returns a list of delays """
    delays = [wr(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
