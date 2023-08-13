from rest_framework import status
import pytest
import json

endpoint = '/ou/keys/'
pytestmark = pytest.mark.django_db

class TestAPIKeys:
    """Test case for the API Keys endpoint.

    During set up of the test case the framework logs in with
    user admin.

    This test case has three stages:
    * test_api_reachable - Tests if API endpoint is reachable
    * test_api_returns_data - Tests if API endpoint returns sane data
    * test_api_add_key - Tests if adding of a key works and is returned in following request

    Test case succeeds if 3/3 tests are OK.
    """
 

    def test_api_reachable(db, client):
        """
        Test if API endpoint is reachable, test if HTTP-status is code 200
        """
        client.login(username='admin', password='admin')
        response = client.get(endpoint)
        assert response.status_code == status.HTTP_200_OK


    def test_api_returns_data(db, client):
        """
        Test is returned data is sane.
        """
        client.login(username='admin', password='admin')
        response = client.get(endpoint)
        
        assert response.status_code == status.HTTP_200_OK

        assert response.json()['count'] == 2
        assert response.json()['results'][0]['role'] == 'private'
        assert response.json()['results'][1]['role'] == 'public'

    def test_api_add_key(db, client):
        """
        Test POST of new key (adding key).
        """
        client.login(username='admin', password='admin')
        test_data = {"key": "test", "role": "public", "platform_used": 1, "owner": 1}
        response = client.post(endpoint, 
            json.dumps(test_data),
            content_type="application/json")
        assert response.json()['key']  == 'test'    # Test response key
        assert response.json()['role'] == 'public'  # Test response role

        # Now test if we retreive the new key
        response = client.get('/ou/keys/')
        assert response.json()['count'] == 3                      # Now we have 3 keys in test data
        assert response.json()['results'][2]['key']  == 'test'    # Test response key
        assert response.json()['results'][2]['role'] == 'public'  # Test response role