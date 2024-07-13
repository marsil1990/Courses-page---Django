from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Student(AbstractBaseUser, PermissionsMixin):
    ci = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=128)  # Field renamed to remove unsuitable characters.
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_staff

    @classmethod
    def get_by_ci_or_email(cls, ci_or_email):
        return cls.objects.filter(models.Q(ci=ci_or_email) | models.Q(email=ci_or_email)).first()


    def set_is_active(self, is_active):
        self.is_active = is_active
        self.save()

    @staticmethod
    def get_is_active(ci):
        student = Student.objects.filter(ci=ci).first()
        return student.is_active if student else False

    @staticmethod
    def getCI(email):
       student = Student.objects.filter(email=email).first()
       return student

    

from core.models import Course
class Register(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete =  models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    aprove = models.BooleanField(default = False)
    
    class Meta:
        unique_together = ('student', 'course')


    
    def courses_progress(self, nameCourse = None, student_email = None):
        pass
        
        


  