from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from courses.models import Course

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Guarda la contraseña de manera segura
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    STUDENT = 'Student'
    TEACHER = 'Teacher'

    ROLE_CHOICES = {
        STUDENT: 'Student',
        TEACHER: 'Teacher',
    }

    ci = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    description = models.TextField(blank=True)
    country = models.CharField(max_length=50, blank=True)
    img = models.ImageField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=STUDENT)  # Define el rol

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['ci']
    
    def email_and_role(self):
       return f"{self.email} - {self.role}"

    def __str__(self):
        return f"{self.email} - {self.role}"
    
    def get_is_active(self):
        return self.is_active

 


    
    
class UserSocialNetworks (models.Model):
    user =  models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    network_name=  models.CharField(max_length=100)
    network_url = models.URLField(blank=True, null=True)
    
    class Meta:
        unique_together = ("user", "network_name")