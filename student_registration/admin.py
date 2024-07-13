from django.contrib import admin

# Register your models here.
from .models import Student, Register


@admin.register(Student)
class StudentdAdmin(admin.ModelAdmin):
    list_display= ('ci','email', 'first_name', 'last_name')
    list_filter = ('ci','email')
    search_fields = ('email',)

@admin.register(Register)
class RegisterdAdmin(admin.ModelAdmin):
    list_display= ('student','course', 'registration_date', 'aprove')
    list_filter = ('student','course')
    search_fields = ('course',)

     