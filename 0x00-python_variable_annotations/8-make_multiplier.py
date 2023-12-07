#!/usr/bin/env python3
"""
This module contains a function that takes a float multiplier
and returns a function that multiplies a float by `multiplier`
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a multiplier (float) and returns a function that
    multiplies a float by `multiplier`
    """
    def multiplier_func(value: float) -> float:
        return value * multiplier
    return multiplier_func
