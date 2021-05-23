from django import forms

class ProfileForm(forms.Form):   
    first_name = forms.CharField(max_length=100, required=True, label="Primer nombre")
    last_name = forms.CharField(max_length=100, required=True, label="Segundo nombre")
    bibliography = forms.CharField(max_length=500, required=True, label="bibliografia")
    birthdate = forms.DateField(required=False, label="Fecha de nacimiento")
    picture = forms.ImageField(required=False, label="Image de perfil")
