from django.urls import path
from . import views

urlpatterns = [
    path("", views.listar_productos),

    path("<int:id>/stock/", views.actualizar_stock_producto),

    path("<int:id>/eliminar/",views.eliminar_producto),

    path("<int:id>/", views.obtener_producto_id),

    ]