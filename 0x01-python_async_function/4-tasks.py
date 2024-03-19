#!/usr/bin/env python3
""" this module imports task_wait_n from 3-tasks and runs it """

import asyncio
from typing import List
twr = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ this method returns a list of delays """
    delays: List[float] = await asyncio.gather(
            *(twr(max_delay) for _ in range(n)))

    return sorted(delays)
