from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.authtoken.views import obtain_auth_token

# Простое представление для корневого маршрута
def home(request):
    return HttpResponse("Welcome to the Todo API!")

urlpatterns = [
    path('', home, name='home'),  # Добавьте этот маршрут
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),
    path('api-token-auth/', obtain_auth_token),  # Для получения токена
]