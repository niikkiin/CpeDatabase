from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.DashBoardView.as_view(), name='home'),
    path('sections/', views.SectionsView.as_view(), name='sections'),
]
