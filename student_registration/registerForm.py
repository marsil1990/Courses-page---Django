from django import forms

class registerForm(forms.Form):
    register_course = forms.CharField(widget=forms.HiddenInput())