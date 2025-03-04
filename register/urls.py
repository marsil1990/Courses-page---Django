from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register' ),
    path('register_course/<str:nameCourse>/', views.register_course, name='register_course'),
  
]
