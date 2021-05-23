from django import forms

class ProfileForm(forms.Form):
    #Usand el parametro label puede cambiar el nombre a otro idioma manualmente
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    bibliography = forms.CharField(max_length=500, required=True)
    birthdate = forms.DateField(required=False)
    picture = forms.ImageField(required=False)
