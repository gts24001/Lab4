# test-my-server.py
import pytest
from my_server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_root_route(client):
    """Test the root route returns 200 and correct content."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello" in response.data  

def test_hello_route(client):
    """Test /hello route with query parameter."""
    response = client.get('/hello?name=Phil')
    assert response.status_code == 200
    assert b"Hello, Phil!" in response.data

def test_not_found(client):
    """Test unknown route returns 404."""
    response = client.get('/nonexistent')
    assert response.status_code == 404
