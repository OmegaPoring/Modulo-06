from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
import datetime
from random import randint
from .forms import NameForm, AuthorForm, InputForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Boards
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Create your views here.

def index_view(request):
    return HttpResponse("Hola Mundo")

class IndexView(TemplateView):
    template_name="boards/index.html"

def get_date_view(request, name):
    fecha_actual=datetime.datetime.now()
    context = {"fecha": fecha_actual, "nombre": name, "frutas": ["Platano", "Durazno", "Manzana", "Naranja"], "aleatorio": randint(0,9)}

    return render(request, "boards/fecha.html", context)

def name_view(request):
    if request.method=='POST':
        print(request.POST)
    return render(request, "boards/nombre.html")

def formulario_nombre(request):
    return render(request, "boards/formulario1.html")

def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
    else:
        form = NameForm()
        context={"form":form}
        return render(request, "boards/name.html",context)
    
def thanks(request):
    return render(request, "boards/gracias.html")

def create_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thanks/")
    else:
        form = AuthorForm()
        context={"form":form}
        return render(request, "boards/author.html",context)
    
def datosform(request):
    form=InputForm()
    contexto={"form":form}
    return render(request, "boards/datosform.html", contexto)

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            content_type=ContentType.objects.get_for_model(Boards)
            es_miembro_1=Permission.objects.get(
                codename="es_miembro_1",
                content_type=content_type
            )
            user = form.save()

            user.user_permissions.add(es_miembro_1)

            login(request, user)
            messages.success(request, "Registrado Satisfactoriamente")
            return HttpResponseRedirect('/thanks/')
        else:
            messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos")
            return HttpResponseRedirect('/register/')
    
    form = UserRegisterForm()
    context = {"register_form":form}
    return render(request, 'boards/register.html', context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user != None:
                login(request, user)
                messages.info(request, f"iniciaste sesion como {username}.")
                return HttpResponseRedirect("/thanks/")
            else:
                messages.error(request, "Username o Password incorrectos")
                return HttpResponseRedirect("/login/")
        else:
            messages.error(request, "Username o Password incorrectos")
            return HttpResponseRedirect("/login/")
        
    form = AuthenticationForm()
    context = {"login_form":form}
    return render(request, "boards/login.html", context)

def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado sesion satisfactoriamente")
    return HttpResponseRedirect("/login/")
