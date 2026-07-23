from django.http import JsonResponse
from .models import Producto

def listar_productos(request):
    productos = Producto.objects.all()
    datos = [{"nombre":p.nombre,"precio":p.precio,"stock":p.stock} for p in productos]
    return JsonResponse(datos, safe=False)