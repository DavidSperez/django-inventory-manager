from django.urls import path
from . import views

urlpatterns = [
    # 1. Ruta específica
    path("", views.listar_movimiento),

    # 2. Rutas dinámicas con ID
    path("por-producto/", views.movimientos_por_producto),
    path("por-tipo/", views.movimientos_por_tipo),

    ]