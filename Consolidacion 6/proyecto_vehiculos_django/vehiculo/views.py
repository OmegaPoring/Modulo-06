from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
import datetime
from .forms import VehiculoForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Vehiculo
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def index_view(request):
    return render(request, "vehiculo/index.html")

@login_required(login_url="/login/")
def list_vehiculo(request):
    datos_vehiculo=Vehiculo.objects.all()
    context={"datos_vehiculo":datos_vehiculo}
    return render(request, "vehiculo/list_vehiculo.html", context)

@login_required(login_url="/login/")
@permission_required(perm="vehiculo.add_vehiculo", raise_exception=True)
def create_vehiculo(request):
    if request.method=="POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El vehiculo ha sido registrado exitosamente!")
            return HttpResponseRedirect("/vehiculo/add/")
        else:
            messages.error(request ,"Ha ocurrido un error al ingresar los datos, por favor verifique que los datos ingresados sean correctos.")
    else:
        form = VehiculoForm()
        context={"form":form}
        return render(request, "vehiculo/add_vehiculo.html", context)
    
def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            content_type=ContentType.objects.get_for_model(Vehiculo)
            visualizar_catalogo=Permission.objects.get(
                codename="visualizar_catalogo",
                content_type=content_type
            )
            user = form.save()

            user.user_permissions.add(visualizar_catalogo)

            login(request, user)
            messages.success(request, "Registrado Satisfactoriamente")
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos")
            return HttpResponseRedirect('/register/')
    
    form = UserRegisterForm()
    context = {"register_form":form}
    return render(request, 'vehiculo/register.html', context)

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
                return HttpResponseRedirect("/")
            else:
                messages.error(request, "Username o Password incorrectos")
                return HttpResponseRedirect("/login/")
        else:
            messages.error(request, "Username o Password incorrectos")
            return HttpResponseRedirect("/login/")
        
    form = AuthenticationForm()
    context = {"login_form":form}
    return render(request, "vehiculo/login.html", context)

def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado sesion satisfactoriamente")
    return HttpResponseRedirect("/login/")
