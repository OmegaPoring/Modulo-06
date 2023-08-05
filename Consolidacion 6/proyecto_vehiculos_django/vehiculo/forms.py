from django import forms
from django.forms import ModelForm
from .models import Vehiculo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VehiculoForm(ModelForm):
    class Meta:
        model=Vehiculo
        fields=["marca", "modelo", "serial_carroceria", "serial_motor", "categoria", "precio"]

class InputForm(forms.Form):
    nombre=forms.CharField(max_length=200)
    apellido=forms.CharField(max_length=200)
    prioridad=forms.IntegerField(min_value=1, max_value=3)
    contrasenna=forms.CharField(widget=forms.PasswordInput())

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")