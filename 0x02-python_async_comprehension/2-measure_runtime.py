#!/usr/bin/env python3
"""
This module contains a function that measures the runtime of asynchronous
generator comprehension tasks.
"""
import time
from asyncio import gather

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This function measures the runtime of asynchronous generator
    comprehension tasks and returns the time as a float value.
    """
    s = time.perf_counter()
    tasks = [async_comprehension() for i in range(4)]
    await gather(*tasks)
    elapsed = time.perf_counter() - s

    return elapsed
