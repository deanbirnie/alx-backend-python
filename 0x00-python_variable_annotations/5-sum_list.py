#!/usr/bin/ennv python3
"""
This module contains a funtion which takes a list input of
floats and returns their sum as a flot.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function takes a list of floats and returns a
    float value for the sum of all the entries in the list.
    """
    sum_total: float = 0
    for value in input_list:
        sum_total += value

    return sum_total
