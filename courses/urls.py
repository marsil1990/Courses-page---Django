from django.urls import path
from . import views

urlpatterns = [
    path('create_course/', views.create_course, name='create_course'),
    path('course/<str:name>/', views.course, name='course' ),
    path('editCourse/<str:name>/', views.editCourse, name='editCourse'),
]

