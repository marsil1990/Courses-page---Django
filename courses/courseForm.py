from django import forms
from .models import Course
from register.models import TeacherCourse, RegisterCourse
from lessons.models import Lesson

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["name", "subject", "difficulty", "description", "img"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Course Name"}),
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "Subject"}),
            "difficulty": forms.Select(attrs={"class": "form-select"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3, "placeholder": "Description"}),
            "img": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:  # Si estamos editando un curso existente, self.instance.pk verifica si el objeto tiene una clave primaria, es decir, si el curso ya existe en la base de datos.
            self.old_name = self.instance.name  # Guardar el nombre original

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Si el nombre fue cambiado, actualizamos manualmente
        """
        hasattr(self, 'old_name') → Verifica que old_name fue definido en __init__.
        self.old_name != instance.name → Compara el nombre original con el nuevo."""
        if hasattr(self, 'old_name') and self.old_name != instance.name:
            
            TeacherCourse.objects.filter(course__name=self.old_name).update(course=instance)
            RegisterCourse.objects.filter(course__name=self.old_name).update(course=instance)
            Lesson.objects.filter(course__name = self.old_name).update(course= instance)
            Course.objects.filter(name=self.old_name).update(
                name=instance.name,
                subject=instance.subject,
                difficulty=instance.difficulty,
                description=instance.description,
                img=instance.img
            )
            return Course.objects.get(name=instance.name)

        if commit:
            instance.save()
        return instance