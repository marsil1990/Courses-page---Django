from django.shortcuts import render, redirect
from .models import ExerciseMultipleOption, Exercise_options, Exercise_passed
from courses.repositories.course_repository import CourseRepository
from user.repoisitoriesUser.user_repository import UserRepository
from courses.models import Course
from user.models import CustomUser
from register.models import RegisterCourse
from django.contrib.auth.decorators import login_required
from .form_do_exercise import Do_exercise_to_MultipleOption_Form
from exercises.exerciseForm import ExerciseForm
from django.http import HttpResponseForbidden
# Create your views here.


@login_required(login_url='/login/')
def exercise(request, id):
    exercise = ExerciseMultipleOption.objects.get(id=id)
    if request.user.role == "Teacher":
        if request.method == 'POST':
            option = request.POST.get('selected_option')
            option = option.split("-")[0]
            if option == exercise.answer_correct_multiOption:
                message = "✅ Correct answer!"
            else:
                message = "❌ Incorrect answer. Try again!"
            return render(request, "exercise.html", {"exercise": exercise, "message": message, 'user':request.user.role})
    elif request.user.role == "Student":
        if request.method == 'POST':
            option = request.POST.get('selected_option')
            option = option.split("-")[0]
            if option == exercise.answer_correct_multiOption:
                message = "✅ Correct answer!"
                student = UserRepository.getUser(request.user.email, request.user.role)
                Exercise_passed.objects.create(exercise = exercise, CustomUser = student)
                course = exercise.lessons.course
                total_exercises = CourseRepository.number_exercises_course(course)
                if total_exercises == Exercise_passed.exercises_completed_by_CustomUser(student, course):
                    r = RegisterCourse.objects.get(course=course, student = student)
                    r.aprove = True
                    r.save()
            else:
                message = "❌ Incorrect answer. Try again!"
            return render(request, "exercise.html", {"exercise": exercise, "message": message, 'user':request.user.role})
        
        
    return render(request, 'exercise.html', {'exercise':exercise, 'user':request.user.role})


@login_required(login_url='/login/')
def create_exercise(request, id_lesson):
    user = request.user.role
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(id_lesson)
            options = request.POST.getlist("options[]")  # Obtiene todas las opciones ingresadas
            for option_text in options:
                if option_text.strip():  # Evita opciones vacías
                    print(option_text)
                    Exercise_options.objects.create(exerciseMultipleOption=exercise, answer_option=option_text)

            return redirect("myCourses")
    else:
        form = ExerciseForm()
    
    return render(request, 'create_exercise.html', {"form":form, "user":user})

def exercise_edit(request, id_exercise):
    exercise =  ExerciseMultipleOption.objects.get(id=id_exercise)
    lesson = exercise.lessons
    option_exercise = Exercise_options.objects.filter( exerciseMultipleOption=exercise)
    if request.method == "POST":
        form = ExerciseForm(request.POST, instance = exercise)
        if form.is_valid():
            Exercise_options.objects.filter( exerciseMultipleOption = exercise).delete()
            options = request.POST.getlist("options[]")  # Obtiene todas las opciones ingresadas
            for option_text in options:
                if option_text.strip():  # Evita opciones vacías
                    print(option_text)
                    Exercise_options.objects.create(exerciseMultipleOption=exercise, answer_option=option_text)
            form.save(lesson)
            return redirect('exercise', id_exercise)
    else:
        form = ExerciseForm(instance=exercise)

    return render(request, "exercise_edit.html", {"form": form, "options":option_exercise})

def delete_exercise(reuqest, id_exercise):
    exercise = ExerciseMultipleOption.objects.get(id =id_exercise)
    lesson = exercise.lessons
    lesson.numberOfExercises = lesson.numberOfExercises - 1
    lesson.save()
    exercise.delete()
    return redirect("myCourses")