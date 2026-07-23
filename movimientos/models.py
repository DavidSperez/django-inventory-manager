from django.db import models
from productos.models import Producto

TIPOS = [
    ("entrada","entrada"),
    ("salida","salida"),
]

class Movimiento(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPOS)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

