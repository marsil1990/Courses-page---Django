from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from .courseForm import CourseForm
from user.repoisitoriesUser.user_repository import UserRepository
from register.models import TeacherCourse
from django.contrib import messages
from courses.repositories.course_repository import CourseRepository
from lessons.models import Lesson

# Create your views here.
@login_required(login_url='/login/')
def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save()
            user =  UserRepository.getUser(request.user.email, request.user.role)
            teacher_course = TeacherCourse(course=course, teacher = user)
            teacher_course.save()
            return redirect("myCourses")
    else:
        form = CourseForm()

    return render(request, "create_course.html", {"form": form})



@login_required(login_url='/login/')
def course(request, name):
    user = request.user
    try:  
       course = CourseRepository.get_course(name)
    except: print(f"No existe curso de nombre {name}")
    try:
        lessons = Lesson.getLessons(name)
    except:
        lessons = []
    return render(request, "course.html", {'course':course, 'lessons': lessons, 'user':user.role})
    
@login_required(login_url='/login/')
def editCourse(request, name):
    course = CourseRepository.get_course(name)
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect("myCourses")
    else:
        form = CourseForm(instance=course)

    return render(request, "edit_course.html", {"form": form, "course": course})
    
    

