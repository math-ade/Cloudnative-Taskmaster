import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert data['service'] == 'taskmaster-api'

def test_get_tasks_empty(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    data = response.get_json()
    assert 'tasks' in data
    assert 'count' in data

def test_create_task(client):
    response = client.post('/tasks',
        json={'title': 'Test task'},
        content_type='application/json'
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Test task'
    assert data['status'] == 'pending'
