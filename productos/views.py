from django.http import JsonResponse, HttpResponse
from .models import Producto
import json

def listar_productos(request):
    productos = Producto.objects.all()
    datos = [{"nombre":p.nombre,"precio":p.precio,"stock":p.stock} for p in productos]
    return JsonResponse(datos, safe=False)

def obtener_producto_id(request, id):
    producto = Producto.objects.filter(id=id).first()
    
    if not producto:
       return JsonResponse({"error":"Producto no encontrado"}, status=404)

    datos= {
        "id":producto.id,
        "nombre": producto.nombre,
        "precio": float(producto.precio),
        "stock": producto.stock,
        "categoria_id": producto.categoria_id
        }
    return JsonResponse(datos, status=200)

def crear_producto(request):
    if request.method == "POST":
        datos = json.loads(request.body)
        nombre = datos.get("nombre")
        precio = datos.get("precio")
        stock = datos.get("stock", 0)
        categoria_id = datos.get("categoria_id")

        if not nombre or not precio or not categoria_id:
            return JsonResponse({"error":"datos faltantes"}, status=400)
        
        producto = Producto.objects.create(nombre=nombre,precio=precio,stock=stock, categoria_id=categoria_id)
        return JsonResponse({"id":producto.id}, status=201)
    return JsonResponse({"error":"Metodo no permitido"}, status=405)
    

def actualizar_stock_producto(request, id):
    if request.method == "PUT":
        datos = json.loads(request.body)
        stock_actual = datos.get("stock_actual")
        if stock_actual is None:
            return JsonResponse({"error":"Datos faltantes"}, status = 400)

        producto = Producto.objects.filter(id=id).first()
        if not producto:
            return JsonResponse ({"error":"producto no encontrado"}, status = 404)
        producto.stock = stock_actual
        producto.save()

        return JsonResponse ({"mensaje":"actualizado"}, status = 200)
    return JsonResponse({"error":"metodo no perminitdo"}, status = 405)

def eliminar_producto(request, id):
    if request.method == "DELETE":
        producto = Producto.objects.filter(id=id).first()

        if not producto:
            return JsonResponse({"error":"Producto no encontrado"}, status=404)
        producto.delete()
        return HttpResponse(status=204)
    return JsonResponse({"error":"Metodo no permitido"}, status=405)