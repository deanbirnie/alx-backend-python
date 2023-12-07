#!/usr/bin/env python3
"""
This module contains a function that verifies the input before returning an
element from the list.
"""
from typing import List, TypeVar, Optional


GenType = TypeVar('GenType')


def safe_first_element(lst: List[GenType]) -> Optional[GenType]:
    """
    This function verifies the input before returning the first item
    in the list.
    """
    if lst:
        return lst[0]
    else:
        return None
