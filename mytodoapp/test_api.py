import requests

BASE_URL = "http://127.0.0.1:8000"
proxies = {
    "http": None,
    "https": None,
}

def test_create_task():
    url = f"{BASE_URL}/create/"
    data = {
        "title": "Test Task",
        "description": "Test Description",
        "completed": False
    }
    response = requests.post(url, data=data, proxies=proxies)
    assert response.status_code == 302  # Изменено на 302
    # Вы можете сделать дополнительный запрос для проверки созданной задачи

def test_update_task():
    task_id = 1  # ID существующей задачи
    url = f"{BASE_URL}/update/{task_id}/"
    updated_data = {
        "title": "Updated Task",
        "description": "Updated Description",
        "completed": True
    }
    response = requests.post(url, data=updated_data, proxies=proxies)  # Изменено на POST
    assert response.status_code == 302  # Изменено на 302
    # Вы можете сделать дополнительный запрос для проверки обновленной задачи

def test_delete_task():
    task_id = 1  # ID существующей задачи
    url = f"{BASE_URL}/delete/{task_id}/"
    response = requests.post(url, proxies=proxies)  # Изменено на POST
    assert response.status_code == 204  # Оставлено без изменений