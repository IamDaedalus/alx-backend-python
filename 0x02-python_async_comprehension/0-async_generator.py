#!/usr/bin/env python3
""" this module demonstrates async generators """

import asyncio
from collections.abc import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """ this function yields a random number between 0 and 10 """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
