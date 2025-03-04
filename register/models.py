from django.db import models
from courses.models import Course
from user.models import CustomUser
# Create your models here.


class RegisterCourse(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': CustomUser.STUDENT}, null=True)
    course = models.ForeignKey(Course, on_delete =  models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    aprove = models.BooleanField(default = False)
    
    class Meta:
        unique_together = ('student', 'course')

    def courses_progress(self, nameCourse = None, CustomUser_email = None):
        pass     
       
    @staticmethod
    def getCourses(student_email):
        student = CustomUser.objects.get(email = student_email)
        courses = RegisterCourse.objects.filter(student = student)
        return courses
        

class TeacherCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, unique=True)
    teacher = models.ForeignKey(CustomUser, on_delete=models.PROTECT, limit_choices_to={'role': CustomUser.TEACHER}) 
    
    
    
    @staticmethod
    def getCourses(teacher_email):
        return  TeacherCourse.objects.filter(teacher__email=teacher_email)
    #values_list('course', flat=True) devuelve solo los valores del campo course, sin necesidad de traer toda la instancia del modelo TeacherCourse.
        