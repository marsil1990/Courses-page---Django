from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('myCourse/', views.myCourses, name='myCourses'),
    path('deleteCourse/<str:name>', views.delete_course, name= 'delete_course'),
    path('editProfile/', views.edit_profile, name='editProfile')
]



