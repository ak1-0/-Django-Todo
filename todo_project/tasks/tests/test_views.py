import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from tasks.models import Todo

User = get_user_model()

@pytest.fixture
def test_user(db):
    user = User.objects.create_user(username='testuser', password='password')
    return user

@pytest.fixture
def client_logged_in(client, test_user):
    client.login(username='testuser', password='password')
    return client

@pytest.mark.django_db
def test_todo_list_view(client_logged_in):
    response = client_logged_in.get(reverse('todo_list'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_todo_create_view(client_logged_in):
    response = client_logged_in.post(reverse('todo_create'), {'title': 'Test Todo', 'description': 'Test Description'})
    assert response.status_code == 302
    assert Todo.objects.filter(title='Test Todo').exists()

@pytest.mark.django_db
def test_todo_edit_view(client_logged_in, test_user):
    todo = Todo.objects.create(title='Test Todo', description='Test Description', user=test_user)
    response = client_logged_in.post(reverse('todo_edit', args=[todo.id]), {'title': 'Updated Todo', 'description': 'Updated Description'})
    assert response.status_code == 302
    todo.refresh_from_db()
    assert todo.title == 'Updated Todo'
    assert todo.description == 'Updated Description'

@pytest.mark.django_db
def test_todo_delete_view(client_logged_in, test_user):
    todo = Todo.objects.create(title='Test Todo', description='Test Description', user=test_user)
    response = client_logged_in.post(reverse('todo_delete', args=[todo.id]))
    assert response.status_code == 302
    assert not Todo.objects.filter(id=todo.id).exists()

@pytest.mark.django_db
def test_todo_list_api(client_logged_in):
    response = client_logged_in.get(reverse('todo_list_api'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_todo_create_api(client_logged_in):
    response = client_logged_in.post(reverse('todo_list_api'), {'title': 'Test Todo API', 'description': 'Test Description API'})
    assert response.status_code == 201
    assert Todo.objects.filter(title='Test Todo API').exists()

@pytest.mark.django_db
def test_todo_detail_api(client_logged_in, test_user):
    todo = Todo.objects.create(title='Test Todo', description='Test Description', user=test_user)
    response = client_logged_in.get(reverse('todo_detail_api', args=[todo.id]))
    assert response.status_code == 200

@pytest.mark.django_db
def test_todo_update_api(client_logged_in, test_user):
    todo = Todo.objects.create(title='Test Todo', description='Test Description', user=test_user)
    response = client_logged_in.put(reverse('todo_detail_api', args=[todo.id]), {'title': 'Updated Todo API', 'description': 'Updated Description API'}, content_type='application/json')
    assert response.status_code == 200
    todo.refresh_from_db()
    assert todo.title == 'Updated Todo API'
    assert todo.description == 'Updated Description API'

@pytest.mark.django_db
def test_todo_delete_api(client_logged_in, test_user):
    todo = Todo.objects.create(title='Test Todo', description='Test Description', user=test_user)
    response = client_logged_in.delete(reverse('todo_detail_api', args=[todo.id]))
    assert response.status_code == 204
    assert not Todo.objects.filter(id=todo.id).exists()