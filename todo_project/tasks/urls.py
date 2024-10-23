from django.urls import path
from .views import (
    todo_list_html,     # Для отображения HTML-страницы со списком задач
    todo_create_html,   # Для создания задач (HTML-форма)
    todo_edit_html,     # Для редактирования задач (HTML-форма)
    TodoListView,       # Для API получения списка задач
    TodoDetailView,     # Для API работы с задачей по ID
    todo_delete,
)

urlpatterns = [
    # HTML-маршруты
    path('', todo_list_html, name='todo_list'),           # Главная страница с задачами
    path('create/', todo_create_html, name='todo_create'), # Страница создания новой задачи
    path('edit/<int:pk>/', todo_edit_html, name='todo_edit'), # Страница редактирования задачи
    path('<int:pk>/delete/', todo_delete, name='todo_delete'),  # Удаление задачи через HTML

    # API-маршруты
    path('api/tasks/', TodoListView.as_view(), name='todo_list_api'),         # API для получения списка задач
    path('api/tasks/<int:pk>/', TodoDetailView.as_view(), name='todo_detail_api'),  # API для работы с задачей по ID
]