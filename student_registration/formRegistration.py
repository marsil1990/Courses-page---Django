from django import forms
from .models import Student
from django.contrib.auth.hashers import check_password

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['ci','password','first_name','last_name','email','description']
    
    


class CustomAuthenticationForm(forms.Form):
    ci_or_email = forms.CharField(label="Ci o Email")
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        ci_or_email = cleaned_data.get("ci_or_email")
        password = cleaned_data.get("password")
        student = None
        if ci_or_email:
            # Intentar buscar al usuario por ci de usuario
            student = Student.objects.filter(ci=ci_or_email).first()
            # Si no se encuentra por ci de usuario, intentar por correo electrónico
            if not student:
                student = Student.objects.filter(email=ci_or_email).first()
        if student and not student.check_password(password):
            self.add_error('password', 'Contraseña incorrecta.')
        elif not student:
            self.add_error('ci_or_email', 'Estudiante no encontrado.')
        else:
            self.user = student
        return cleaned_data