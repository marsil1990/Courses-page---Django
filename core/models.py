from django.db import models

# Create your models here.

class Course(models.Model):
    difficulty_options ={
        "Easy":"Easy", 
        "Medium":"Medium",
        "Difficult":"Difficult",
    }
    name = models.CharField(max_length = 50, primary_key = True)
    img = models.ImageField(null = True)
    subject = models.CharField(max_length = 50)
    difficulty = models.CharField(max_length=10, choices=difficulty_options, default="Easy")
    descrption = models.TextField(max_length = 500)
    creation_date = models.DateTimeField(auto_now_add = True)
    
    @staticmethod
    def getAllcourse():
        return Course.objects.all()
    

   
    def course_exercises(self):
        from exercises.models import Exercise
        query = """SELECT * 
                FROM exercises_exercise e
                INNER JOIN lessons_lesson l ON e.lessons_id =l.id
                WHERE  l.course_id =%s"""
        exercises = Exercise.objects.raw(query, [self.name])
        return exercises
    
    
    def number_exercises_course(self):
        from lessons.models import Lesson
        query = """SELECT l.id, sum(l.numberOfEcercises) as total_exercises
                FROM lessons_lesson  l
                WHERE  l.course_id =%s"""
        result = Lesson.objects.raw(query, [self.name])
        total_exercises = result[0].total_exercises if result else 0
        return total_exercises
    
    @staticmethod
    def courses_progress(student):
        from student_registration.models import Register
        from exercises.models import Exercise_passed
        student_courses = Register.objects.filter(student=student)
        courses_percentage = dict()
        for c in student_courses:
            number_exercises = c.course.number_exercises_course()
            if number_exercises == None:
                number_exercises = 0
            number_exercies_passed = Exercise_passed.exercises_completed_by_student(student_email=student.ci, nameCurso=c.course.name)
            if number_exercises!=0:
                courses_percentage[c.course.name]=(number_exercies_passed/number_exercises)*100
            else:
                courses_percentage[c.course.name]=0
        return courses_percentage


        
        