from django import forms
from django.contrib.auth.models import User
from manager_messages.models import Profile

class SignupForm(forms.Form):
    first_name = forms.CharField(min_length=2, max_length=50, required=True)
    last_name = forms.CharField(min_length=2, max_length=50, required=True)
    username = forms.CharField(min_length=4, max_length=50, required=True)
    password = forms.CharField(min_length=4, max_length=70, required=True, widget=forms.PasswordInput())
    password_confirmation =forms.CharField(min_length=4, max_length=70, required=True, widget=forms.PasswordInput())
    email = forms.CharField(min_length=6, max_length=70, required=True, widget=forms.EmailInput())

    def clean_username(self):
        username = self.cleaned_data['username']
        exist_username = User.objects.filter(username=username).exists()
        if exist_username:
            raise forms.ValidationError("Usuario ya existe")
        return username

    def clean_password_confirmation(self):
        password = None
        if (len(self.data["password"]) > 0):
            password = self.data["password"]

        password_confirmation = self.cleaned_data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no son iguales')
        
        return password_confirmation

    def save(self):
        data = self.cleaned_data
        data.pop("password_confirmation")
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.first_name = user.first_name
        profile.last_name = user.last_name
        profile.role_id = 4
        profile.save()