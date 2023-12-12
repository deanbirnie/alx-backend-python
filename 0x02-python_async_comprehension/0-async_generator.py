#!/usr/bin/env python3
"""
This module contains an asynchronous function that awaits a sleep cycle.
"""
from random import uniform
from asyncio import sleep
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    This function simply awaits a sleep cycle before returning a random
    floating number between 0 and 10 using uniform from random.
    """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
