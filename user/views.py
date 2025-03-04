from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from register.formRegistration import RegistrationForm
from .models import CustomUser,  UserSocialNetworks
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
from register.models import TeacherCourse
from .repoisitoriesUser.user_repository import UserRepository
from .imgForm import ImgForm
from django.http import JsonResponse
import json


@login_required(login_url='/login/')
def profile(request):
    user_or_teacher = CustomUser.objects.get(email = request.user.email)
    user_or_teacher_ci = user_or_teacher.ci
    user_or_teacher_first_name = user_or_teacher.first_name
    user_or_teacher_last_name = user_or_teacher.last_name
    user_or_teacher_email = user_or_teacher.email
    user_or_teacher_phone = user_or_teacher.phone
    if user_or_teacher.img != None:
        user_or_teacher_img  = user_or_teacher.img
    if request.user.role == "Student":
        courses = CourseRepository.courses_progress(user_or_teacher)
    elif request.user.role == "Teacher":
        courses = CourseRepository.getAllcourse()
   
    user_social_networks = UserSocialNetworks.objects.filter(user = user_or_teacher)
    networks = []
    for n in user_social_networks:
        networks.append((n.network_name,n.network_url))
    print(user_or_teacher.img)
    
    return render(request, 'profile.html', {
        "ci":user_or_teacher_ci,
        "first_name":user_or_teacher_first_name,
        "last_name":user_or_teacher_last_name,
        "email":user_or_teacher_email,
        "courses_progress":courses,
        "user_img":user_or_teacher_img,
        "user":request.user.role,
        "networks":networks,
        "phone": user_or_teacher_phone
    }
)

@login_required(login_url='/login/')
def myCourses(request):
   role = request.user.role
   user_email  =  request.user.email
   if role == "Teacher":
       courses_db = TeacherCourse.getCourses(user_email)
   elif role == "Student":
       courses_db = RegisterCourse.getCourses(user_email)
   courses = []
   for c in courses_db:
       courses.append(c.course)
 
   return render(request, './myCourses.html', {"courses":courses,  'user':role})
   
 
    

@login_required(login_url='/login/')
def delete_course(request, name):
    CourseRepository.get_course(name=name).delete()
    return redirect('myCourses')
 
def edit_profile(request):
    user_or_teacher = CustomUser.objects.get(email = request.user.email)
    
    courses_progress = CourseRepository.courses_progress(user_or_teacher)
    user_social_networks = UserSocialNetworks.objects.filter(user = user_or_teacher)
    networks = []
    for n in user_social_networks:
        networks.append((n.network_name, n.network_url))
    if request.method == "POST":
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            try: 
                img = request.FILES["img_user"]
                user_or_teacher.img = img
            except: print("No se agrega una imagen")
            try :
                fullName = request.POST["option-fullName"].split(" ")
                name = fullName[0]
                if name:
                   user_or_teacher.first_name = name
                try: 
                    lastname = fullName[1]
                    if lastname:
                       user_or_teacher.last_name = lastname
                except: print("Out range")
            except:  print("Out range")
            try: 
                country = request.POST["option-country"]
                if country!="":
                   user_or_teacher.country = country
            except:
                print("No se agrega country")
            try: 
               socila_network_name = request.POST.getlist("option-social-name[]")
               socila_network_url = request.POST.getlist("option-social-url[]")
               UserSocialNetworks.objects.filter(user = user_or_teacher).delete()
               for i in range(len(socila_network_name)):
                   if socila_network_name[i] and socila_network_url[i]:
                        UserSocialNetworks.objects.create(user = user_or_teacher, network_name =socila_network_name[i], network_url=socila_network_url[i])
            except: print("Error")
            try:
                if  request.POST["option-email"]:
                    email = request.POST["option-email"]
                    user_or_teacher.email = email
            except:
                print("Error email")
            try: 
                if  request.POST["option-phone"]:
                   phone = request.POST["option-phone"]
                   user_or_teacher.phone = phone
            except:
                print("Error phone")
              
            try:
               if request.user.role == "Student":
                  deleted_courses = request.POST.get("deleted_courses")
                  if deleted_courses:
                       courses_name= json.loads(deleted_courses)
                       for names in courses_name:
                           RegisterCourse.objects.filter(course=CourseRepository.get_course(names)).delete()
            except:
                print("No se eliminaron los registros a los cursos")
            user_or_teacher.save()
            return redirect('profile')
 
    else:
        form = ImgForm()
    return render(request, 'profile_edit.html', {"form":form, "user":request.user.role, "courses":courses_progress, "networks":networks, "user_img":user_or_teacher})

