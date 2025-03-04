from django.urls import path
from . import views


urlpatterns = [
    path('lesson_exercises/<int:id>/', views.lesson, name='lesson_exercises'),
    path('createLesson/<str:name_course>/', views.createLesson, name='createLesson'),
    path('editLesson/<int:id>/', views.edit_lesson, name='editLesson'),
    path('deleteLesson/<int:id_lesson>', views.delete_lesson, name='delete_lesson')
]