from django.db import models
from lessons.models import Lesson


class ExerciseMultipleOption(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    url_video = models.URLField(blank=True, null=False)
    lessons = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    phrase_multiple_option = models.TextField(blank=True, null=False)
    answer_correct_multiOption = models.CharField(max_length=50, blank=True, null=False)

    @staticmethod
    def answers(self):
       answers = Exercise_options.objects.filter(exerciseMultipleOption=self)
       return answers
    
    @staticmethod
    def getExercisesFromLesson(lesson):
        exercises = ExerciseMultipleOption.objects.filter(lessons=lesson)
        return exercises


class Exercise_options(models.Model):
    exerciseMultipleOption = models.ForeignKey(ExerciseMultipleOption, on_delete=models.CASCADE, related_name='options')
    answer_option = models.CharField(max_length=100)
    class Meta:
        unique_together = (('exerciseMultipleOption', 'answer_option'),)
    
    
    
    
    
    

from user.models import CustomUser
class Exercise_passed(models.Model):
    key = models.AutoField(primary_key=True)
    exercise = models.ForeignKey(ExerciseMultipleOption, on_delete = models.CASCADE, default=None)
    CustomUser = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    class Meta:
        unique_together = ('CustomUser', 'exercise')

    @staticmethod
    def exercises_completed_by_CustomUser(user, curso):
        query ="""SELECT ep.key, COUNT(ep.key) as total_exercise
                FROM exercises_exercise_passed ep
                INNER JOIN exercises_exercisemultipleoption ej ON ep.exercise_id = ej.id
                INNER JOIN lessons_lesson l ON l.id = ej.lessons_id
                WHERE l.course_id = %s and ep.CustomUser_id = %s"""
        result = Exercise_passed.objects.raw(query, [curso.id, user.ci])
        total = result[0].total_exercise 
        if result:
           pass
        else:
          total = 0
        return total
    
    @staticmethod
    def get_exercises_completed_by_CustomUser(CustomUser_ci):
        query ="""SELECT ep.key
                FROM exercises_exercise_passed ep
                WHERE ep.CustomUser_id = %s"""
        result = Exercise_passed.objects.raw(query, [CustomUser_ci])
        exerciseMultioptionsPassed = []
        for e in result:
            exerciseMultioptionsPassed.append(e.exercise)
       # print(exerciseMultioptionsPassed)
        return exerciseMultioptionsPassed


    

    

