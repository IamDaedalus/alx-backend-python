#!/usr/bin/env python3
""" this module demonstrates async generators """

from asyncio import sleep
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """ this function yields a random number between 0 and 10 """
    for _ in range(10):
        await sleep(1)
        yield random.uniform(0, 10)
