from django import forms
from user.models import CustomUser

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    choose = forms.ChoiceField(choices=[('Student', 'Student'), ('Teacher', 'Teacher')])

    class Meta:
        model = CustomUser
        fields = ['ci','password','first_name','last_name','email','description']
    
    


class CustomAuthenticationForm(forms.Form):
    ci_or_email = forms.CharField(label="Ci o Email")
    password = forms.CharField(widget=forms.PasswordInput)

