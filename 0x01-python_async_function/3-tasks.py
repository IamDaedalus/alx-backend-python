#!/usr/bin/env python3
"""this module imports task_wait_random runs it and returns an asyncio.Task"""

import asyncio
from asyncio import Task
wr = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ this method returns a Task """
    task: Task = asyncio.create_task(wr(max_delay))
    return task
