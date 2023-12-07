#!/usr/bin/env python3
"""
This module contains a function that takes a list argument and
tuple for each item in the list consisting of the item as the first
element and the items length as the second element.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes a list argument and
    tuple for each item in the list consisting of the item as the first
    element and the items length as the second element.
    """
    return [(i, len(i)) for i in lst]
