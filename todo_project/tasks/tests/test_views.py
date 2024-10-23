import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def test_user(db):
    user = User.objects.create_user(username='testuser', password='password')
    return user

@pytest.mark.django_db
def test_todo_list_view(client, test_user):
    client.login(username='testuser', password='password')
    response = client.get(reverse('todo_list'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_todo_create_view(client, test_user):
    client.login(username='testuser', password='password')
    response = client.post(reverse('todo_create'), {'title': 'Test Todo', 'description': 'Test Description'})
    assert response.status_code == 302