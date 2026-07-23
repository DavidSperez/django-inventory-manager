from django.http import JsonResponse
from .models import Categoria

def listar_categorias(request):
    categorias = Categoria.objects.all()

    datos = [{"id":c.id, "nombre":c.nombre} for c in categorias]
    return JsonResponse(datos, safe=False)
