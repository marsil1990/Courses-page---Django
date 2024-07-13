from django import forms



class Do_exercise_to_complete_Form(forms.Form):
    enter_answer = forms.CharField()

class Do_exercise_to_MultipleOption_Form(forms.Form):
    enter_the_correct_option = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese la letra de l opción'}))

  