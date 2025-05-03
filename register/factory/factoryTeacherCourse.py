from register.models import TeacherCourse
class TeacherCourseFactory:
    @staticmethod
    def create_teacher_course(course, teacher):
        """
        Factory Method para crear instancias del modelo Course con reglas de negocio específicas.
        """
        try: 
            teacher_course = TeacherCourse(course=course, teacher = teacher)
            teacher_course.save()
            return teacher_course
        except:
            return "Error"
            
        