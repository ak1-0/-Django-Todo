from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),  # Подключаем все маршруты из tasks.urls
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Страница входа
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Страница выхода
    path('', RedirectView.as_view(url='tasks/')),  # Перенаправляем на список задач
]