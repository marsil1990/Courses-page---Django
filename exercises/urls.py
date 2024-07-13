from django.urls import path
from . import views

urlpatterns = [
    path('lesson_exercises/<int:id>', views.lesson_exercises, name='lesson_exercises'),
    path('exercise/<int:id>', views.start_exercise, name='exercise')
]