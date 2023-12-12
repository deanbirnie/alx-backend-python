#!/usr/bin/env python3
"""
This module contains a function that measures the time of an asynchronous
function.
"""
import time
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This function measures the runtime of an asynchronous function.
    """
    s = time.perf_counter()
    run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s

    return elapsed / n
