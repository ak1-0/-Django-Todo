import pytest
import requests
from django.contrib.auth.models import User

BASE_URL = "http://127.0.0.1:8000/api"

@pytest.fixture
def create_user(db):
    user = User.objects.create_user(username='testuser', password='testpass123')
    return user

@pytest.fixture
def get_token(create_user):
    response = requests.post(f'{BASE_URL}/api-token-auth/', data={
        'username': 'testuser',
        'password': 'testpass123'
    })
    return response.json()['token']

@pytest.fixture
def create_task(get_token):
    headers = {'Authorization': f'Token {get_token}'}
    data = {
        'title': 'Initial Task',
        'description': 'Initial Description',
        'completed': False
    }
    response = requests.post(f'{BASE_URL}/tasks/', json=data, headers=headers)
    return response.json()  # Возвращает созданную задачу

def test_create_task(get_token):
    headers = {'Authorization': f'Token {get_token}'}
    data = {
        'title': 'Test Task',
        'description': 'Test Description',
        'completed': False
    }
    response = requests.post(f'{BASE_URL}/tasks/', json=data, headers=headers)
    assert response.status_code == 201

def test_get_tasks(get_token, create_task):
    headers = {'Authorization': f'Token {get_token}'}
    response = requests.get(f'{BASE_URL}/tasks/', headers=headers)
    assert response.status_code == 200

def test_update_task(get_token, create_task):
    task_id = create_task['id']  # Получите ID созданной задачи
    headers = {'Authorization': f'Token {get_token}'}
    data = {'completed': True}
    response = requests.put(f'{BASE_URL}/tasks/{task_id}/', json=data, headers=headers)
    assert response.status_code == 200

def test_delete_task(get_token, create_task):
    task_id = create_task['id']  # Получите ID созданной задачи
    headers = {'Authorization': f'Token {get_token}'}
    response = requests.delete(f'{BASE_URL}/tasks/{task_id}/', headers=headers)
    assert response.status_code == 204