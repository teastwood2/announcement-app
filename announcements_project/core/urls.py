from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, custom_login
urlpatterns = [path('register/', register, name = 'register'), #path('login/', auth_views.LoginView.as_view(template_name = 'core/login.html'), name = 'login'), 
               path('login/', custom_login, name = 'login'),
               path('logout/', auth_views.LogoutView.as_view(), name = 'logout')]
