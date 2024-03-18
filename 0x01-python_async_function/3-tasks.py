#!/usr/bin/env python3


import asyncio
wr = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ this method returns a Task """
    task = asyncio.create_task(wr(max_delay))
    return task
