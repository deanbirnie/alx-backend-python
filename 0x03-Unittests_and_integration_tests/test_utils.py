#!/usr/bin/env python3
"""
Testing implementations for utils.py.
"""
from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Testing for the AccessNestedMap method in utils.py
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Method to test that the method returns what it is supposed to.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)
