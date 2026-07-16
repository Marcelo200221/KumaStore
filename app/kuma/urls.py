from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargarInicio),
    path('inicio', views.cargarInicio),
    path('login', views.cargarSesion),
    path('perfil', views.cargarPerfil, name="ver-perfil"),
    path('productos/', views.cargarProductos, name="cargar_productos"),
    path('bandana', views.cargarBandana),
    path('correa', views.cargarCorreas),
    path('colgante', views.cargarColgantes),
    path('juguete', views.cargarJuguetes),
    path('agregarProducto', views.cargarAgregarProducto),
    path('agregarProductoForm', views.agregarProducto),
    path('editarProducto/<sku>', views.cargarEditarProductos),
    path('editarProductoForm', views.editarProductoForm),
    path('eliminarProducto/<sku>', views.eliminarProducto),
    path('registrar', views.agregarUsuario, name='registrar'),
    path('editar', views.editarUsuario, name="editar-usuario"),
    path('comida', views.cargarComida),
    path('actualizar_stock/', views.actualizar_stock, name='actualizar_stock')
]