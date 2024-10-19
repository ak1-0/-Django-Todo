# Django Todo REST API с автоматическим тестированием
[![Pytest](https://img.shields.io/badge/Tested%20with-Pytest-blue.svg)](https://docs.pytest.org/)
[![Django REST Framework](https://img.shields.io/badge/Django-REST%20Framework-green.svg)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue.svg)](https://www.postgresql.org/)

Этот проект представляет собой простое **Django Todo приложение**, которое предлагает полнофункциональный REST API для управления задачами. Приложение защищено с помощью **Token Authentication**, и поддерживает все основные операции CRUD (Create, Read, Update, Delete). Кроме того, проект включает **автоматическое тестирование** API с использованием библиотек **Pytest** и **Requests**, что обеспечивает стабильность и надежность.

## Возможности
- **Управление задачами**: Создание, обновление, удаление и просмотр задач.
- **Аутентификация на основе токенов**: Пользователи должны пройти аутентификацию с помощью токена для управления задачами.
- **PostgreSQL**: Реляционная база данных для масштабируемого и надежного хранения данных.
- **Автоматическое тестирование API**: Включает тесты на основе Pytest для всех ключевых операций API.
- **Безопасность**: Тесты для аутентификации и базовая защита от SQL инъекций.

## Технологический стек
- **Backend**: Django 4.x, Django REST Framework
- **База данных**: PostgreSQL
- **Тестирование**: Pytest, Requests
- **Аутентификация**: Token-based Authentication
- **DevOps**: Готово для использования с Docker
- **CI/CD**: Готово для интеграции с CI инструментами, такими как GitHub Actions

## Быстрый старт

### Необходимое ПО
- Python 3.8+
- PostgreSQL
- Pipenv или virtualenv для управления зависимостями

### Установка

1. **Клонируйте репозиторий**:
    ```bash
    git clone https://github.com/yourusername/django-todo-autotest.git
    cd django-todo-autotest
    ```

2. **Создайте и активируйте виртуальное окружение**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```

3. **Установите зависимости**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Настройте базу данных PostgreSQL**:
    Обновите раздел `DATABASES` в `settings.py`, чтобы он указывал на ваш экземпляр PostgreSQL:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'todo_db',
            'USER': 'your_postgres_user',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. **Запустите миграции**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Создайте суперпользователя**:
    ```bash
    python manage.py createsuperuser
    ```

7. **Запустите сервер разработки**:
    ```bash
    python manage.py runserver
    ```

### API Endpoints

Доступные API endpoints:
- **GET** `/api/tasks/` — Список всех задач.
- **POST** `/api/tasks/` — Создать новую задачу.
- **GET** `/api/tasks/<id>/` — Получить задачу по ID.
- **PUT** `/api/tasks/<id>/` — Обновить задачу.
- **DELETE** `/api/tasks/<id>/` — Удалить задачу.

### Аутентификация на основе токенов

Чтобы аутентифицироваться, сначала получите токен аутентификации, отправив POST запрос на `/api-token-auth/` с вашим именем пользователя и паролем:
```bash
POST /api-token-auth/
{
    "username": "yourusername",
    "password": "yourpassword"
}
```

Используйте полученный токен в заголовке Authorization для последующих запросов:
```bash
Authorization: Token <your_token>
```

###  Запуск тестов
Чтобы запустить тесты и убедиться в правильной работе API:
```bash
pytest
```

## Внимание

⚠️ **Проект находится в стадии разработки.** ⚠️
