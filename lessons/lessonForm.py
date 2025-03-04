from django import forms
from .models import Course
from lessons.models import Lesson
from exercises.models import ExerciseMultipleOption
from courses.repositories.course_repository import CourseRepository


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ["id","order", "goal", "topic", "url_video"]
        widgets = {
            "order": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Lesson number"}),
            "goal": forms.TextInput(attrs={"class": "form-control", "placeholder": "Goal"}),
            "topic":forms.TextInput(attrs={"class": "form-control", "placeholder": "Topic"}),
            "url_video": forms.URLInput(attrs={"class": "form-control", "rows": 3, "placeholder": "Vide"}),
        }
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:  # Si estamos editando una lección existente, self.instance.pk verifica si el objeto tiene una clave primaria, es decir, si la lección ya existe en la base de datos.
            self.old_id = self.instance.id # Guardar el nombre original
        

    def save(self,name_course=None, commit=True):
        instance = super().save(commit=False)
        
        # Si el nombre fue cambiado, actualizamos manualmente
        """
        hasattr(self, 'old_id') → Verifica que old_id fue definido en __init__.
        self.old_id != instance.id → Compara el nombre original con el nuevo."""
        number_of_exercises = 0
        if hasattr(self, 'old_id'):
            number_of_exercises = ExerciseMultipleOption.objects.filter(lessons = instance).count()
            Lesson.objects.filter(id=self.old_id).update(
                id = instance.id,
                order=instance.order,
                numberOfExercises=number_of_exercises,
                goal = instance.goal,
                topic=instance.topic,
                url_video=instance.url_video,
                course = instance.course
            )
            
           
            return Lesson.objects.get(id = instance.id)

        if commit:
            instance.numberOfexercises = number_of_exercises
            instance.course = CourseRepository.get_course(name=name_course)
            instance.save()
        return instance