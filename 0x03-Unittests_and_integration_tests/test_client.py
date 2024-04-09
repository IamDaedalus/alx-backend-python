#!/usr/bin/env python3
""" tests for client """

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """This class contains tests for the GithubOrgClient class """
    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json")
    def test_org(self, test_org_name, get_json_mock):
        """Test GithubOrgClient returns the correct value """
        get_json_mock.return_value = {"test_key": test_org_name}
        client = GithubOrgClient(test_org_name)
        self.assertEqual(client.org, {"test_key": test_org_name})

    def test_public_repos_url(self):
        """ test resulf of _public_repos_url """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as org_mock:
            org_name = "google"
            url = "https://www.{}.com".format(org_name)
            org_mock.return_value = {"repos_url": url}
            client = GithubOrgClient(org_name)
            self.assertEqual(client._public_repos_url, url)

    @patch("client.get_json")
    def test_public_repos(self, get_json_mock):
        """ test the public repo method """
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as repo_url_mock:
            get_json_mock.return_value = [{"name": "name1"}, {"name": "name2"}]
            repo_url_mock.return_value = "https://www.google.com"
            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(), ["name1", "name2"])
            repo_url_mock.assert_called_once()
            get_json_mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, test_map, test_license, expected_output):
        """ test the has_licensce method """
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(
            test_map, test_license), expected_output)
