from django import forms

class ImgForm(forms.Form):
   img_user = forms.FileField(
    label="Select an Image",
    widget=forms.ClearableFileInput(attrs={"class": "form-control"}),
    required=False  # Hace que la imagen no sea obligatoria
)
