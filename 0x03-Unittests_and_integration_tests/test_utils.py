#!/usr/bin/env python3
"""
Testing implementations for utils.py.
"""
from utils import access_nested_map, get_json
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock


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


    @parameterized.expand([
        ({}, ("a",), "KeyError('a')"),
        ({"a": 1}, ("a", "b"), "KeyError('b')"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception_message):
        """
        Raising exception while testing Access Nested Map
        """
        with self.assertRaises(KeyError) as context_manager:
            value = nested_map
            for key in path:
                value = value[key]
        self.assertEqual(str(context_manager.exception), expected_exception_message)


class TestGetJson(unittest.TestCase):
    """
    Testing get_json
    """
    @patch('your_module.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Mock HTTP calls for testing get_json
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        requests_get_mock = Mock(return_value=mock_response)

        with patch('your_module.requests.get', requests_get_mock):
            result = utils.get_json(test_url)
            requests_get_mock.assert_called_once_with(test_url)

            self.assertEqual(result, test_payload)
