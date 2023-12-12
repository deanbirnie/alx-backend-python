#!/usr/bin/env python3
"""
This module contains a function that returns multiple concurrent Task objects
"""
import asyncio
from asyncio import Task, create_task
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function runs multiple concurrent task objects
    """
    tasks = [
        task_wait_random(max_delay) for _ in range(n)
    ]

    return [await task for task in asyncio.as_completed(tasks)]
