from django.db import models

# Create your models here.
class Course(models.Model):
    difficulty_options ={
        "Easy":"Easy", 
        "Medium":"Medium",
        "Difficult":"Difficult",
    }
    name = models.CharField(max_length = 50, unique = True)
    img = models.ImageField(null = True)
    subject = models.CharField(max_length = 50)
    difficulty = models.CharField(max_length=10, choices=difficulty_options, default="Easy")
    description = models.TextField(max_length = 500)
    creation_date = models.DateTimeField(auto_now_add = True)