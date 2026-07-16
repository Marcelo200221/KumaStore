from django import forms
from.models import Categoria, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    pass

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']