#!/usr/bin/env python3
"""
This module contains a function that safely returns a value from a dictionary
"""
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    This function safely returns values from a dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
