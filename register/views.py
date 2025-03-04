from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from register.formRegistration import RegistrationForm
from .models import CustomUser
from register.models import RegisterCourse
from courses.models import Course
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.urls import reverse
import uuid
from courses.repositories.course_repository import CourseRepository
from user.factory_user import UserFactory 
from user.repoisitoriesUser.user_repository import UserRepository
# Create your views here.


def register(request):
    user_active= False
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            ci = form.cleaned_data['ci']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            description = form.cleaned_data['description']
            role = form.cleaned_data['choose']
            UserFactory.create_user(ci=ci, password=password, first_name=first_name,last_name=last_name, email=email, description=description, role=role)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form, "user_active":user_active})



@login_required(login_url='/login/')
def register_course(request, nameCourse):
    student = UserRepository.getUser(request.user.email, request.user.role)
    course = CourseRepository.get_course(nameCourse)
    course_register  = RegisterCourse.objects.filter(student = student , course =CourseRepository.get_course(nameCourse))
    if course_register:
        return HttpResponse("Already registered for this course.")
    else: 
        RegisterCourse.objects.create(student= student, course = course)
        return render(request, 'register_course.html', {'course':nameCourse, "user":request.user.role})




