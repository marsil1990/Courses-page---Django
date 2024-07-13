from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('myCourse/', views.profile, name='myCourses'),
]
