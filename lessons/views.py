from django.shortcuts import render
from core.models import Course
from .models import Lesson
from student_registration.models import Register, Student

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
# Create your views here.
@login_required(login_url='/login/')
def course_lessons(request, name):
    print(request.user.is_authenticated)
    if not Student.get_is_active(request.session['user_id']):
        return HttpResponseForbidden("Solo los estudiantes tienen acceso a esta zona.")
    student  = request.session['user_id']
    if not Student.objects.filter(ci=student).exists():
        return HttpResponseForbidden("Debes estar registrado en este curso para acceder a esta zona.")
    course = Lesson.getCourse(name=name)
    lessons = Lesson.objects.filter(course = course.name)
    return render(request, 'course_lessons.html',{'course':course, 'lesson':lessons})


