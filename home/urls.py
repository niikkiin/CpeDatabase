from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.DashBoardView.as_view(), name='home'),
    path('sections/', views.SectionsListView.as_view(), name='sections'),
    path('sections/create/', views.SectionCreateView.as_view(), name='create-section'),

    path('student/', views.StudentsListView.as_view(), name='student-list-view'),
    path('student/create/', views.StudentCreateView.as_view(), name='create-student'),

    # NOTE temp
    path('student/view/', views.StudentIndividualView.as_view(), name='view-student'),
]
