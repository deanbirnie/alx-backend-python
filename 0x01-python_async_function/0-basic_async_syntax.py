#!/usr/bin/env python3
"""
This module that waits a certain amount of time before returning
to test async functions.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    This function takes an integer value for the maximum amount of delay
    and waits for a random amount of time between zero and max delay
    (inclusive) after which the actual time the function waited for
    is returned.
    """
    wait_for = random.uniform(0, max_delay)
    await asyncio.sleep(wait_for)
    return wait_for
