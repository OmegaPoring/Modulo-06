from django import forms
from .models import Author, Book
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NameForm(forms.Form):
    your_name = forms.CharField(label="Enter your name...", max_length=100)
    
class AuthorForm(ModelForm):
    class Meta:
        model=Author
        fields=["name", "title", "birth_date"]

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