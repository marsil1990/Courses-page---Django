"""
Repository Pattern:
Extrae la lógica de consultas SQL crudas (course_exercises, number_exercises_course, etc.) a un repositorio dedicado o servicio separado.
Esto ayudará a mantener el modelo más limpio y enfocado en representar datos.
Por qué usarlo:
Mejora la separación de responsabilidades.
"""
from courses.models import Course
from register.models import RegisterCourse

class CourseRepository():
    @staticmethod
    def getAllcourse():
        return Course.objects.all()
    
    @staticmethod
    def get_course(name):
        return Course.objects.get(name = name)
        
    

    @staticmethod
    def course_exercises(course_name):
        from exercises.models import ExerciseMultipleOption
        query = """SELECT * 
                FROM exercises_exercisemultipleoption e
                INNER JOIN lessons_lesson l ON e.lessons_id =l.id
                WHERE  l.course_id =%s"""
        exercises = ExerciseMultipleOption.objects.raw(query, [course_name])
        
        return exercises
    
    @staticmethod
    def number_exercises_course(course):
        from lessons.models import Lesson
       
        query = """SELECT l.id, SUM(l.numberOfExercises) AS total_exercises
                FROM lessons_lesson  l
                WHERE  l.course_id =%s"""
        result = Lesson.objects.raw(query, [course.id])
        total_exercises = result[0].total_exercises if result else 0
        return total_exercises

    
    @staticmethod
    def courses_progress(user):
        from exercises.models import Exercise_passed
        user_courses = RegisterCourse.objects.filter(student=user)
        courses_percentage = dict()
        for c in user_courses:
            number_exercises = CourseRepository.number_exercises_course(c.course)
            if number_exercises == None:
                number_exercises = 0
            number_exercies_passed = Exercise_passed.exercises_completed_by_CustomUser(user = user, curso =c.course)
        
            if number_exercises!=0:
                courses_percentage[c.course.name]=(number_exercies_passed/number_exercises)*100
            else:
                courses_percentage[c.course.name]=0
        
        return courses_percentage
