from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/' , authapp.login, name= 'login'),
    path('logout/' , authapp.logout, name= 'logout'),
    path('edit/' , authapp.logout, name= 'edit'),
    path('register/' , authapp.logout, name= 'register'),
]
