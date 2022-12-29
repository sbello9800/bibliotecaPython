from unicodedata import name
from django.urls import path
from djappsebm import views
from djappsebm.views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.inicio_sebm, name='inicio_sebm'),
    path('inicio2/', views.inicio_sebm2, name='inicio_sebm2'),
    path('error/', views.error, name='error'),
    path('inicio_sesion_sebm/', views.inicio_sesion_sebm, name='inicio_sesion_sebm'),
    path('cerrarSesion/', views.cerrar_sesion_sebm, name='cerrar_sesion_sebm'),

    #clientes
    path('clientes/addCliente/', Cliente_Create_sebm.as_view(), name='addCliente_sbm'),
    path('eliminarClient/<int:id_cli>/', Eliminar_cliente_sebm.as_view(), name='eliminar_cliente_sebm'),
    path('listClient/', Cliente_list_sebm.as_view(), name='listar_clientes_sebm'),
    path('editClient/<pk>/', Cliente_update_sebm.as_view(), name='editClient_sebm'),
    
    #usuarios
    path('usuarios/addUsuario/', Usuario_Create_sebm.as_view(), name='addUsuario_sbm'),
    path('eliminarUsuario/<int:id_u>/', Usuario_delete_sebm.as_view(), name='Usuario_delete_sebm'),
    path('listUsuarios/', Listar_usuario_sebm.as_view(), name='listar_usuarios_sebm'),
    path('editUsuario/<pk>/', Usuario_update_sebm.as_view(), name='editUsuario_sebm'),

    #categorias
    path('categorias/addCategoria/', Categoria_Create_sebm.as_view(), name='addCategoria_sbm'),
    path('eliminarCategoria/<int:id_cat>/', Categoria_eliminar_sebm.as_view(), name='Categoria_eliminar_sebm'),
    path('listCategoria/', Listar_categoria_sebm.as_view(), name='listar_categoria_sebm'),
    path('editCategoria/<pk>/', Categoria_update_sebm.as_view(), name='categorias_editar'),
    
    #libros
    path('libros/addLibro/', Libro_Create_sebm.as_view(), name='addLibro_sbm'),
    path('eliminarLibro/<int:id_lib>/', Eliminar_libro_sebm.as_view(), name='Eliminar_libro_sebm'),
    path('listLibro/', Listar_libro_sebm.as_view(), name='listar_libros_sebm'),
    path('editLibro/<pk>/', Libro_update_sebm.as_view(), name='Libro_update_sebm'),

    #autor
    path('autor/addAutor/', Insertar_autor_sebm.as_view(), name='Insertar_autor_sebm'),
    path('eliminarAutor/<int:id_aut>/', Eliminar_autor_sebm.as_view(), name='Eliminar_autor_sebm'),
    path('listAutor/', Listar_autor_sebm.as_view(), name='Listar_autor_sebm'),
    path('editAutor/<pk>/', Editar_autor_sebm.as_view(), name='Editar_autor_sebm'),
    path('reporte_autor', Reporte_autor_sebm.as_view(), name='Reporte_autor_sebm'),

    # Pedido cliente

    path('pedidoCliente', insertar_Pedido_cliente_sebm.as_view(), name='pedidoCliente'),
    path('listar_PedidoCliente', listar_Pedido_cliente_sebm.as_view(), name='listar_PedidoCliente'),
    path('editar_pedido_clientes/<pk>/', editar_Pedido_cliente_sebm.as_view(), name='editar_pedido_clientes'),
    path('eliminar_PedidoCliente/<int:id_ped_sebm>/', eliminar_Pedido_cliente_sebm.as_view(), name='eliminar_PedidoCliente'),
    path('reporte_pedidoCliente', reporte_pedido_cliente_sebm.as_view(), name='reporte_pedidoCliente'),

#LibroPorAutor
    path('insertar_libro_por_autor', Libros_Autor_Create_sebm.as_view(), name='insertar_libro_por_autor'),
    path('listar_libro_por_autor',Libros_Autor_list_sebm.as_view(), name='listar_libro_por_autor'),
    path('editar_libro_por_autor/<pk>/', Libros_Autor_update_sebm.as_view(), name='editar_libro_por_autor'),
    path('eliminar_libro_por_autor/<int:id_lib_aut_sebm>/', Libros_Autor_delate_sebm.as_view(), name='eliminar_libro_por_autor'),
    
]
