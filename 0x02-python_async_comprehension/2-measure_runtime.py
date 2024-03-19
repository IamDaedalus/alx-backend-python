#!/usr/bin/env python3
"""
this module imports and uses asynchronously runs an async definition at
once with all completing in abou 10s
"""

import time
import asyncio
ac = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ this function measures the runtime of the async functions """
    start = time.time()
    await asyncio.gather(ac(), ac(), ac(), ac())
    end = time.time()
    return end - start
