from django.urls import path
from .views import index_view, IndexView, get_date_view, name_view, formulario_nombre, get_name, thanks, create_author, datosform, register_view, login_view, logout_view

urlpatterns = [
    path('', index_view, name="index"),
    path("template/", IndexView.as_view(), name="Index_class"),
    path("date/<str:name>/", get_date_view, name="get_date"),
    path("name/", name_view, name="name"),
    path("formulario/", formulario_nombre, name="formulario1"),
    path("getname/", get_name, name="get_name"),
    path("thanks/", thanks, name="gracias"),
    path("createauthor/", create_author, name="create_autor"),
    path("datosform/", datosform, name="datosform"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
]
