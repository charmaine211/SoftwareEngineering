"""
Test module from Django Framework.

Holds all test cases for this application.
Run tests with ``python manage.py test``.

Be aware: throughout this project we rather use PyTest. The tests defined here
are not complete, they're just implemented to complete the functionality of the
Djano Framework.
PyTest is also used for the Continuous Integration implementation.
"""

from django.test import TestCase
from rest_framework import status
import json

class APIKeysTestCase(TestCase):
    """Test case for the API Keys endpoint.

    During set up of the test case the framework logs in with
    user admin.

    This test case has two stages:
    * test_api_reachable - Tests if API endpoint is reachable
    * test_api_returns_data - Tests if API endpoint returns sane data

    Test case succeeds if 2/2 tests are OK.
    """
    fixtures = ['ou/tests.json']

    def setUp(self):
        self.client.login(username='admin', password='admin')

    def test_api_reachable(self):
        """
        Test if API endpoint is reachable, test if HTTP-status is code 200
        """
        response = self.client.get('/ou/keys/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_returns_data(self):
        """
        Test is returned data is sane.
        """
        response = self.client.get('/ou/keys/')
        self.assertEqual(response.json()['count'], 2)                      # Two keys are provided in test data
        self.assertEqual(response.json()['results'][0]['role'], 'private') # First key in test data is private
        self.assertEqual(response.json()['results'][1]['role'], 'public')  # Second key in test data is public

    def test_api_add_key(self):
        """
        Test POST of new key (adding key).
        """
        test_data = {"key": "test", "role": "public"}
        response = self.client.post('/ou/keys/', 
            json.dumps(test_data),
            content_type="application/json")
        self.assertEqual(response.json()['key'], 'test')     # Test response key
        self.assertEqual(response.json()['role'], 'public')  # Test response role

        # Now test if we retreive the new key
        response = self.client.get('/ou/keys/')
        self.assertEqual(response.json()['count'], 3)                      # Now we have 3 keys in test data
        self.assertEqual(response.json()['results'][2]['key'], 'test')     # Test response key
        self.assertEqual(response.json()['results'][2]['role'], 'public')  # Test response role