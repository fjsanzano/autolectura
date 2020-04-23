from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required = True, help_text = 'Campo requerido y 254 caracteres como maximo.')
    fullname = forms.CharField(label="Full name")

    class Meta:
        model = User
        fields = ['fullname', 'username', 'email', 'password1', 'password2']