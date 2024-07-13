from django.shortcuts import render, redirect
from lessons.models import Lesson
from .models import ExerciseMultipleOption,Exercise_passed
from student_registration.models import Student, Register
from django.contrib.auth.decorators import login_required
from .form_do_exercise import Do_exercise_to_complete_Form, Do_exercise_to_MultipleOption_Form
from django.http import HttpResponseForbidden
# Create your views here.
@login_required(login_url='/login/')
def lesson_exercises(request, id):
    lesson = Lesson.objects.get(id = id)
    exercises = None
    exercises = []
    try: 
        get_exercises = ExerciseMultipleOption.objects.filter(lessons = id)
        exercises_passed = Exercise_passed.get_exercises_completed_by_student(student_ci=request.user.ci)
        for e in get_exercises:
            if e in exercises_passed:
                exercises.append({'exercise':e,'approved':True})
            else: exercises.append({'exercise':e,'approved':False})
    except:
        print("The table does not exist")
       

    return render(request, 'lesson_exercises.html', {'lesson':lesson, 'exercises': exercises})


@login_required(login_url='/login/')
def start_exercise(request, id):
    answers =[]
    reply = "Try until you find the correct answer"
    exercise = ExerciseMultipleOption.objects.get(id = id)
    answers = exercise.answers()
    if request.method == 'POST':
        do_an_exercise = Do_exercise_to_MultipleOption_Form(request.POST)
        if do_an_exercise.is_valid():
            answer = do_an_exercise.cleaned_data['enter_the_correct_option']
            if exercise.answer_correct_multiOption.lower() == answer[0].lower() :
                reply = "You were correct, congratulation!"
                student = Student.objects.get(email = request.user)
                if not Exercise_passed.objects.filter(exercise=exercise, student=student):
                    exercise_passed = Exercise_passed(exercise = exercise, student = student)
                    exercise_passed.save() 
                    course = exercise.lessons.course
                    numberOfexercise = course.number_exercises_course()
                    numberOfexercisePassed = Exercise_passed.exercises_completed_by_student(student_email=student.ci, nameCurso=course.name)
                    print(numberOfexercise,"yyy", numberOfexercisePassed)
                    if numberOfexercise == numberOfexercisePassed:
                        register_student_course = Register.objects.get(student=student, course=course)
                        register_student_course.aprove = True
                        register_student_course.save()
                    else:
                        register_student_course = Register.objects.get(student=student, course=course)
                        register_student_course.aprove = False
                        register_student_course.save()
    else: 
        do_an_exercise = Do_exercise_to_MultipleOption_Form()
                        
    return render(request, 'exercise.html',{'exercise':exercise, 'do_an_exercise':do_an_exercise, 'answers':answers,'reply':reply})

        
