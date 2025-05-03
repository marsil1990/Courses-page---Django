from lessons.models import Lesson
from courses.repositories.course_repository import CourseRepository

class LessonRepository():
    @staticmethod
    def getCourse(name):
        course = CourseRepository.get_course(name = name)
        return course
    
    @staticmethod
    def getLessons(course_name):
        lessons = Lesson.objects.filter(course__name = course_name)
        return lessons
    
    @staticmethod
    def getLesson(lesson):
        lesson = Lesson.objects.filter(id = lesson).first()
        return lesson