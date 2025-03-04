from django.contrib import admin
from register.models import TeacherCourse
from register.models import RegisterCourse


# Register your models here.
@admin.register(TeacherCourse)
class TeacherCourseAdmin(admin.ModelAdmin):
    list_display= ('get_course_name','teacher',)
    list_filter = ('course','teacher',)
    search_fields = ('course','teacher',)
    def get_course_name(self, obj):
        return obj.course.name  # 2️⃣ Devuelve el nombre del curso

@admin.register(RegisterCourse)
class RegisterdAdmin(admin.ModelAdmin):
    list_display= ('student','course', 'registration_date', 'aprove')
    list_filter = ('student','course')
    search_fields = ('course',)
    

