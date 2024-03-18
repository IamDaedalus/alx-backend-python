#!/usr/bin/env python3
""" this module measures the runtime of the wait_n method """

import time
import asyncio
wn = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ this method returns the time it takes to execute the wait_n method """
    start = time.time()
    asyncio.run(wn(n, max_delay))
    end = time.time()
    return (end - start) / n
