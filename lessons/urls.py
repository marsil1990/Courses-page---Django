from django.urls import path
from . import views


urlpatterns = [
    path('course_lessons/<str:name>/', views.course_lessons, name='course_lessons'),
]