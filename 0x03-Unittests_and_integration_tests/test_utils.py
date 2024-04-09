#!/usr/bin/env python3
""" various test cases and functions """

from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
import unittest
from unittest.mock import patch, MagicMock


class TestAccessNestedMap(unittest.TestCase):
    """ Test the utils and other modules with test cases """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected) -> None:
        """ test the access_nested_map function """
        self.assertEqual(access_nested_map(map, path), expected)

    @parameterized.expand([
        ({}, ("a",), {}),
        ({"a": 1}, ("a", "b"), {}),
    ])
    def test_access_nested_map_exception(self, map, path, expected) -> None:
        self.assertRaises(KeyError)


class TestGetJson(unittest.TestCase):
    """ class for testing get_json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, url, payload, mock_requests):
        """ test the get_json method """
        r = MagicMock()
        r.json.return_value = payload
        mock_requests.return_value = r
        self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """ class for testing memoize function """
    def test_memoize(self):
        """ test suite for memoize function """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        tc = TestClass()
        with patch.object(tc, "a_method") as a_method_mocked:
            a_method_mocked.return_value = 42

            test1 = tc.a_property
            test2 = tc.a_property

            a_method_mocked.assert_called_once()
            self.assertEqual(test1, 42)
            self.assertEqual(test2, 42)
