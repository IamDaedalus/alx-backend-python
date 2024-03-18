#!/usr/bin/env python3
""" this module imports task_wait_n from 3-tasks and runs it """

import asyncio
twr = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """ this method returns a list of delays using task_wait_random """
    delays = [twr(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
