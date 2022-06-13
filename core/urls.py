from django.urls import path
from .views import home, adm, tables,eliminars,ModificaProducto,AgregarProducto,AgregarFamilia,Tabla_Producto_Familia,EliminarFamilia,ModificaFamilia, ProductoView, FamiliaView, SubFamiliaView, RegionView, ProvinciaView, ComunaView ,Tipo_usuarioView, UsuarioView, SucursalView,EstrategiaView, Estrategia_DetalleView, TipopagoView, CompraView,EstadoView, Compra_DetalleView

urlpatterns = [
    path('home/', home, name='home'),
    path('adm/', adm, name='adm'),
    path('adm/tablas/Familia', Tabla_Producto_Familia, name='tablafamilia'),
    path('adm/tablas/Producto', tables, name='tables'),
    path('adm/añadir/Producto', AgregarProducto, name='AgregarProducto'),
    path('adm/añadir/Familia', AgregarFamilia, name='AgregarFamilia'),
    path('delete/<int:id>/', eliminars,name='employee_delete'),
    path('adm/eliminar/Familia/<int:id>/', EliminarFamilia,name='EliminarFamilia'),
    path('adm/modificar/Producto/<int:id>/', ModificaProducto,name='editar_imagen'),
    path('adm/modificar/Familia/<int:id>/', ModificaFamilia,name='ModificarFamilia'),
    path('Producto/', ProductoView.as_view(), name='lista_de_usuarios'),
    path('Producto/<int:id>',ProductoView.as_view(), name='proceso_de_usuarios'),
    path('Familia/', FamiliaView.as_view(), name='lista_de_familia'),
    path('Familia/<int:id>',FamiliaView.as_view(), name='proceso_de_familia'),
    path('SubFamilia/', SubFamiliaView.as_view(), name='lista_de_familia'),
    path('SubFamilia/<int:id>',SubFamiliaView.as_view(), name='proceso_de_subfamilia'),
    path('Region/', RegionView.as_view(), name='lista_de_region'),
    path('Region/<int:id>',RegionView.as_view(), name='proceso_de_region'),
    path('Provincia/', ProvinciaView.as_view(), name='lista_de_provincia'),
    path('Provincia/<int:id>',ProvinciaView.as_view(), name='proceso_de_provincia'),
    path('Comuna/', ComunaView.as_view(), name='lista_de_comuna'),
    path('Comuna/<int:id>',ComunaView.as_view(), name='proceso_de_comuna'),
    path('Tipo_usuario/', Tipo_usuarioView.as_view(), name='lista_tipo_usuario'),
    path('Tipo_usuario/<int:id>',Tipo_usuarioView.as_view(), name='proceso_tipo_usuario'),
    path('Usuario/', UsuarioView.as_view(), name='lista_de_usuario'),
    path('Usuario/<int:id>',UsuarioView.as_view(), name='proceso_de_usuario'),
    path('Sucursal/', SucursalView.as_view(), name='lista_de_sucursal'),
    path('Sucursal/<int:id>',SucursalView.as_view(), name='proceso_de_sucursal'),
    path('Estrategia/', EstrategiaView.as_view(), name='lista_de_estrategia'),
    path('Estrategia/<int:id>',EstrategiaView.as_view(), name='proceso_de_estrategia'),
    path('Estrategia_Detalle/', Estrategia_DetalleView.as_view(), name='lista_de_estrategia_detalle'),
    path('Estrategia_Detalle/<int:id>',Estrategia_DetalleView.as_view(), name='proceso_de_Estrategia_Detalle'),
    path('TipoPago/', TipopagoView.as_view(), name='lista_de_tipopago'),
    path('TipoPago/<int:id>',TipopagoView.as_view(), name='proceso_de_tipopago'),
    path('Compra/', CompraView.as_view(), name='lista_de_compra'),
    path('Compra/<int:id>',CompraView.as_view(), name='proceso_de_compra'),
    path('Estado/', EstadoView.as_view(), name='lista_de_estado'),
    path('Estado/<int:id>',EstadoView.as_view(), name='proceso_de_estado'),
    path('Compra_Detalle/', Compra_DetalleView.as_view(), name='lista_de_compra_detalle'),
    path('Compra_Detalle/<int:id>',Compra_DetalleView.as_view(), name='proceso_de_compra_detalle')
]