from django.test import Client
import pytest

pytestmark = pytest.mark.django_db

class TestViews:
    """Test case for the views.

    These tests ensure the expected views are defined correctly and available.
    """

    def test_index(client):
        client = Client()
        response = client.get('/')
        assert response.status_code == 200

    def test_login(client):
        client = Client()
        response = client.get('/users/login_user')
        assert response.status_code == 200

    def test_register(client):
        client = Client()
        response = client.get('/users/register_user')
        assert response.status_code == 200

    def test_sign(client):
        client = Client()
        response = client.get('/ou/sign/')
        assert response.status_code == 200

    def test_signature_list(client):
        client = Client()
        response = client.get('/ou/signature_list/')
        assert response.status_code == 200

    def test_verify(client):
        client = Client()
        response = client.get('/ou/verify/')
        assert response.status_code == 200

    def test_keys(client):
        client = Client()
        response = client.get('/ou/keys2/')
        assert response.status_code == 200

    def test_admin(client):
        client = Client()
        response = client.get('/admin')
        assert response.status_code == 301