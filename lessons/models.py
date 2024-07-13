from django.db import models
from core.models import Course
# Create your models here.
class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.IntegerField()
    numberOfEcercises = models.IntegerField(verbose_name = 'Number of Exercises')
    gol = models.TextField()
    topic = models.TextField()
    url_video = models.URLField()
    course = models.ForeignKey(Course, on_delete = models.CASCADE)

    @staticmethod
    def getCourse(name):
        course = Course.objects.get(name = name)
        return course