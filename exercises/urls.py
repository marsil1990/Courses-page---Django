from django.urls import path
from . import views

urlpatterns = [
    path('exercise/<int:id>/', views.exercise, name='exercise'),
    path('exercise_edit/<int:id_exercise>/', views.exercise_edit, name='exercise_edit'),
    path('create_exercise/<int:id_lesson>/', views.create_exercise, name='createExercise'),
    path('deleteExercise/<int:id_exercise>/', views.delete_exercise, name='delete_exercise')
    
]