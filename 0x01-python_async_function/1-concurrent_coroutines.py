#!/usr/bin/env python3
"""
This module contains a function that executes multiple coroutines at the same
time using asynchronous functions.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function executes multiple coroutines at the same time.
    """
    coroutines = [
        asyncio.create_task(wait_random(max_delay)) for _ in range(n)
    ]

    return [routine for routine in asyncio.as_completed(coroutines)]
