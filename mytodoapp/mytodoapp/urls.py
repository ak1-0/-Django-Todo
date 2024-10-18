from django.contrib import admin
from django.urls import path, include  # Импортируйте include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),  # Подключите маршруты вашего приложения
]
