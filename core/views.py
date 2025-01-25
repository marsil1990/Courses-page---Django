from django.shortcuts import render
from .models import Course
from student_registration.models import Register
from student_registration.models import Student
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .repositories.course_repository import CourseRepository
# Create your views here.


# Create your views here.
def home(request):
   courses = CourseRepository.getAllcourse()
   user_id = request.session.get('user_id', None)
   if user_id == None:
      request.session['user_id'] = user_id
      user_active = False
   else:
      ci = request.session['user_id']
      user_active = Student.get_is_active(ci)
   
   return render(request, './home/home.html', {"courses":courses, "user_active":user_active})



@login_required(login_url='/login/')
def profile(request):
   user_email  =  str(request.user)
   courses_db = Register.objects.all()
   courses = []
   for c in courses_db:
      if c.student.email == user_email:
         courses.append(c.course)
   ci = request.session['user_id']
   user_active = Student.get_is_active(ci)
   return render(request, './home/myCourses.html', {"courses":courses, "user_active":user_active})
   
 
