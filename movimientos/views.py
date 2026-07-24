from django.http import JsonResponse
from django.db.models import Count
from .models import Movimiento

def listar_movimiento(request):
    movimientos = Movimiento.objects.all()

    datos = [{"id":m.id, "tipo":m.tipo, "fecha":m.fecha, "producto_id":m.producto_id} for m in movimientos]
    return JsonResponse(datos, safe=False)


def movimientos_por_producto(request):
    if request.method == "GET":
        resumen = Movimiento.objects.values("producto_id").annotate(total=Count("id"))
        return JsonResponse(list(resumen), safe=False)
    return JsonResponse({"error": "Método no permitido"}, status=405)


def movimientos_por_tipo(request):
    if request.method == "GET":
        resumen = Movimiento.objects.values("tipo").annotate(total=Count("id"))
        return JsonResponse(list(resumen), safe=False)
    return JsonResponse({"error": "Método no permitido"}, status=405)