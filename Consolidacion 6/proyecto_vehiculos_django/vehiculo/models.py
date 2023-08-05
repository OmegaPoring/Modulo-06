from django.db import models

# Create your models here.

MARCA_CHOICES=[
    ("FIAT","Fiat"),
    ("CHEVROLET","Chevrolet"),
    ("FORD","Ford"),
    ("TOYOTA","Toyota"),
]

CATEGORIA_CHOICES=[
    ("PARTICULAR","Particular"),
    ("TRANSPORTE","Transporte"),
    ("CARGA","Carga"),
]
class Vehiculo(models.Model):
    id=models.AutoField(primary_key=True)
    marca=models.CharField(max_length=20, choices=MARCA_CHOICES, default=MARCA_CHOICES[2])
    modelo=models.CharField(max_length=100)
    serial_carroceria=models.CharField(max_length=50)
    serial_motor=models.CharField(max_length=50)
    categoria=models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default=MARCA_CHOICES[0])
    precio=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (("visualizar_catalogo","Visualizar Catalogo"),)