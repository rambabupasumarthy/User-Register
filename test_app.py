import pytest
from event_app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test if the registration form loads successfully"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Event Registration" in response.data

def test_register(client):
    """Test form submission"""
    response = client.post('/register', data={
        'name': 'John Doe',
        'email': 'john@example.com',
        'phone': '1234567890',
        'event': 'workshop'
    })
    assert response.status_code == 200
    assert b"success" in response.data
