from django.urls import path
from . import views
from .views import (
    todo_list_html,     # Для отображения HTML-страницы со списком задач
    todo_create_html,   # Для создания задач (HTML-форма)
    todo_edit_html,     # Для редактирования задач (HTML-форма)
    todo_list,          # Для API получения списка задач
    todo_create,        # Для API создания задач
    todo_edit,          # Для API редактирования задач
    todo_delete,        # Для API удаления задач
)

urlpatterns = [
    # HTML-маршруты
    path('', todo_list_html, name='todo_list'),           # Главная страница с задачами
    path('create/', todo_create_html, name='todo_create'), # Страница создания новой задачи
    path('edit/<int:pk>/', todo_edit_html, name='todo_edit'), # Страница редактирования задачи
    path('<int:pk>/delete/', views.todo_delete, name='todo_delete'),

    # API-маршруты
    path('api/', todo_list, name='todo_list_api'),         # API для получения списка задач
    path('api/create/', todo_create, name='todo_create_api'), # API для создания новой задачи
    path('api/edit/<int:pk>/', todo_edit, name='todo_edit_api'), # API для редактирования задачи
    path('api/delete/<int:pk>/', todo_delete, name='todo_delete_api'), # API для удаления задачи
]