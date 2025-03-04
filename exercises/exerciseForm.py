from django import forms
from .models import ExerciseMultipleOption, Exercise_options
from lessons.models import Lesson



class ExerciseForm(forms.ModelForm):
    class Meta:
        model = ExerciseMultipleOption
        fields = ["id","description", "url_video", "phrase_multiple_option", "answer_correct_multiOption"]
        """ widgets = {
            "description": forms.TextInput(attrs={"class": "form-control", "placeholder": "Description"}),
            "url_video": forms.URLInput(attrs={"class": "form-control", "placeholder": "Video"}),
            "phrase_multiple_option": forms.TextInput(attrs={"class": "form-control", "placeholder": "Write the Problem with the options", "rows": 4}),
            "answer_correct_multiOption":forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter de correct option"}),
        }
        """
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:  # Si estamos editando una lección existente, self.instance.pk verifica si el objeto tiene una clave primaria, es decir, si la lección ya existe en la base de datos.
            self.old_id = self.instance.id # Guardar el nombre original
        

    def save(self, lesson, commit=True):
        instance = super().save(commit=False)
        
        # Si el nombre fue cambiado, actualizamos manualmente
        """
        hasattr(self, 'old_name') → Verifica que old_id fue definido en __init__.
        self.old_id != instance.id → Compara el nombre original con el nuevo."""
    
        if hasattr(self, 'old_id'):
            ExerciseMultipleOption.objects.filter(id=self.old_id).update(
                id = instance.id,
                description=instance.description,
                url_video= instance.url_video,
                phrase_multiple_option = instance.phrase_multiple_option,
                answer_correct_multiOption=instance.answer_correct_multiOption,
            )
            return ExerciseMultipleOption.objects.get(id = instance.id)

        if commit:
            if Lesson.objects.get(id = lesson).numberOfExercises == None:
                Lesson.objects.filter(id = lesson).update(numberOfExercises =  1)
            else: 
                Lesson.objects.filter(id = lesson).update(numberOfExercises =  Lesson.objects.get(id = lesson).numberOfExercises + 1)
            instance.lessons = Lesson.objects.get(id = lesson)
            instance.save()
        return instance

"""class exerciseOptionsForm(forms.ModelForm):
    class Meta:
        model = Exercise_options
        fields = ["answer_option"]
"""