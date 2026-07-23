# Django Inventory Manager

API REST para la gestión de inventario y control de stock. 
Proyecto desarrollado desde cero para dominar el ORM 
de Django y el manejo de peticiones HTTP

---

## 📌 ¿Qué hace la aplicación?

Maneja el flujo completo de un inventario dividido 
en 3 módulos independientes por dominio:

* **Categorías:** Clasificación base del catálogo
* **Productos:** CRUD completo, precios y stock actual
* **Movimientos:** Historial de entradas y salidas de stock 
  usando opciones fijas (`choices`)

---

## 🛠️ Puntos clave del desarrollo

* **Arquitectura por apps:** Módulos separados (`categorias`, 
  `productos`, `movimientos`) con sus propias rutas delegadas 
  mediante `include()`

* **Base de datos y ORM:** Modelado con `ForeignKey`, 
  `DecimalField` para dinero y migraciones estructuradas

* **Control HTTP explícito:** Lectura directa del body JSON, 
  validaciones previas y respuestas con códigos de estado 
  correctos (`201`, `204`, `400`, `404`)

* **Consultas optimizadas:**
  * `select_related` para traer datos relacionados en un solo 
    JOIN sin sobrecargar la base de datos.
  * `values` + `annotate` para agrupar y contar registros 
    (equivalente a `GROUP BY` y `COUNT` en SQL)