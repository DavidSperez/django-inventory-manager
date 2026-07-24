from django.http import JsonResponse
from .models import Movimiento

def listar_movimiento(request):
    movimientos = Movimiento.objects.all()

    datos = [{"id":m.id, "tipo":m.tipo, "fecha":m.fecha, "producto_id":m.producto_id} for m in movimientos]
    return JsonResponse(datos, safe=False)
