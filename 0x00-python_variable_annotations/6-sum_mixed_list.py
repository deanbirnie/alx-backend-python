#!/usr/bin/env python3
"""
This module contains a function that takes a list of mixed values
and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function takes a list of mixed values (integers or floats) and
    returns their sum as a float.
    """
    sum_total: float = 0.0
    for value in mxd_lst:
        sum_total += float(value)

    return sum_total
