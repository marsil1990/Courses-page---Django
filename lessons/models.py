from django.db import models
from courses.models import Course
from courses.repositories.course_repository import CourseRepository
# Create your models here.

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.IntegerField()
    numberOfExercises = models.IntegerField(verbose_name = 'Number of Exercises', null=True)
    goal = models.TextField()
    topic = models.TextField()
    url_video = models.URLField()
    course = models.ForeignKey(Course, on_delete = models.CASCADE)

   
        