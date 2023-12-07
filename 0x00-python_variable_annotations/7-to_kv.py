#!/usr/bin/env python3
"""
This module contains a function that takes a string (k) and an int OR float
(v) and returns a tuple with the first element of the tuple being string k
and the second element being the square of the int or float v
annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function accepts a string (k) and an integer or a float (v)
    and returns a tuple with the first element of the tuple being string k
    and the second element being the square of the int or float v
    annotated as a float.
    """
    square: Union[int, float] = v ** 2

    return k, square
