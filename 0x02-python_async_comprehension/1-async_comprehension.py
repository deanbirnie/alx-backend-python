#!/usr/bin/env python3
"""
This module contains a function that collects random numbers from an async
generator and returns them.
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This function is a coroutine that collects 10 random numbers using async
    comprehension over async_generator and returns the numbers.
    """
    result = [i async for i in async_generator()]

    return result
