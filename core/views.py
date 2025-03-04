from django.shortcuts import render
from courses.models import Course
from user.models import CustomUser
from register.models import RegisterCourse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from courses.repositories.course_repository import CourseRepository

# Create your views here.


# Create your views here.
def home(request):
   courses = CourseRepository.getAllcourse()
   try: 
      user = request.user.role
      return render(request, './home/home.html', {"courses":courses, "user":user})
   except: 
      print("Without Role")
      print(request.user)
      return render(request, './home/home.html',{"courses":courses, "user":request.user})
   




 
