from django.shortcuts import render, redirect
from courses.models import Course
from .models import Lesson
from user.models import CustomUser
from lessons.lessonForm import LessonForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from exercises.models import Exercise_options, Exercise_passed, ExerciseMultipleOption
from user.repoisitoriesUser.user_repository import UserRepository
# Create your views here.
@login_required(login_url='/login/')
def lesson(request, id):
    user = request.user
    print("pasa por aquí")
    exercises = ExerciseMultipleOption.getExercisesFromLesson(id)
    lesson = Lesson.getLesson(id)
    if user.role == "Student":
        student = UserRepository.getUser(user.email, user.role)
        exercises_passed = Exercise_passed.get_exercises_completed_by_CustomUser(student.ci)
    else:
        exercises_passed = []
    return render(request, 'lesson_exercises.html', {'exercises':exercises,'exercises_passed':exercises_passed, 'lesson':lesson, 'user':user.role})

@login_required(login_url='/login/')
def createLesson(request, name_course):
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save(name_course)
            return redirect("myCourses")
    else:
        form = LessonForm()
    return render(request, 'create_lesson.html', {"form":form})

@login_required(login_url='/login/')
def edit_lesson(request, id):
    lesson = Lesson.objects.get(id = id)
    if request.method == "POST":
        form = LessonForm(request.POST, instance = lesson)
        if form.is_valid():
            form.save()
            return redirect("myCourses")
        else: print(form.errors)
    else:
        form = LessonForm(instance = lesson)
    return render(request, 'lesson_edit.html', {"form":form})



def delete_lesson(request, id_lesson):
    Lesson.objects.get(id = id_lesson).delete()
    return redirect("myCourses")