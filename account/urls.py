from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
]
