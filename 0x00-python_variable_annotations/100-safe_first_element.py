#!/usr/bin/env python3
"""
This module contains a function that verifies the input before returning an
element from the list.
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    This function verifies the input before returning the first item
    in the list.
    """
    if lst:
        return lst[0]
    else:
        return None
