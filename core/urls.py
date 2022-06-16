from django.urls import path
from .views import AgregarComuna, AgregarTipoPago, EliminarComuna, EliminarTipopago, ModificaComuna, TablaTipoPago, home, adm, homex, tables,eliminars,Tabla_Region,TablaComuna,TablaProvincia,AgregarRegion,ModificaRegion,EliminarRegion,ModificaProducto,AgregarProducto,AgregarFamilia,AgregarProvincia,AgregarSubFamilia,ModificaSubFamilia,Tabla_Producto_Familia,EliminarFamilia,ModificaFamilia,Tabla_Sub_Familia,TablaSucursal,AgregarSucursal, ModificaSucursal, AgregarTipoPago, EliminarSucursal, EliminarProvincia ,ModificaTipoPago, EliminarSucursal, ModificaProvincia, TablaEstado, AgregarEstado, EliminarEstado, ModificaEstado
urlpatterns = [
    path('home/', home, name='home'),
    path('adm/', adm, name='adm'),
    path('homex/', homex, name='homex'),
    #listar
    path('adm/tablas/Familia', Tabla_Producto_Familia, name='tablafamilia'),
    path('adm/tablas/SubFamilia', Tabla_Sub_Familia, name='tablasubfamilia'),
    path('adm/tablas/Region', Tabla_Region, name='TablaRegion'),
    path('adm/tablas/Comuna', TablaComuna, name='TablaComuna'),
    path('adm/tablas/Sucursal', TablaSucursal, name='TablaSucursal'),
    path('adm/tablas/Producto', tables, name='tables'),
    path('adm/tablas/Provincia', TablaProvincia, name='TablaProvincia'),
    path('adm/tablas/TipoPago', TablaTipoPago, name='TablaTipoPago'),
    path('adm/tablas/Estado', TablaEstado, name='TablaEstado'),
    #agregar
    path('adm/añadir/Producto', AgregarProducto, name='AgregarProducto'),
    path('adm/añadir/SubFamilia', AgregarSubFamilia, name='AgregarSubFamilia'),
    path('adm/añadir/Familia', AgregarFamilia, name='AgregarFamilia'),
    path('adm/añadir/Provincia', AgregarProvincia, name='AgregarProvincia'),
    path('adm/añadir/Region', AgregarRegion, name='AgregarRegion'),
    path('adm/añadir/Comuna', AgregarComuna, name='AgregarComuna'),
    path('adm/añadir/Sucursal', AgregarSucursal, name='AgregarSucursal'),
    path('adm/añadir/TipoPago', AgregarTipoPago, name='AgregarTipoPago'), 
    path('adm/añadir/Estado', AgregarEstado, name='AgregarEstado'), 
    path('delete/<int:id>/', eliminars,name='employee_delete'),
    #eliminar
    path('adm/eliminar/Familia/<int:id>/', EliminarFamilia,name='EliminarFamilia'),
    path('adm/eliminar/Provincia/<int:id>/', EliminarProvincia,name='EliminarProvincia'),
    path('adm/eliminar/Region/<int:id>/', EliminarRegion,name='EliminarRegion'),
    path('adm/eliminar/Comuna/<int:id>/', EliminarComuna,name='EliminarComuna'),
    path('adm/eliminar/Sucursal/<int:id>/', EliminarSucursal,name='EliminarSucursal'),
    path('adm/eliminar/Estado/<int:id>/', EliminarEstado,name='EliminarEstado'),
    path('adm/eliminar/TipoPago/<int:id>/', EliminarTipopago,name='EliminarTipoPago'),
    #update
    path('adm/modificar/Producto/<int:id>/', ModificaProducto,name='editar_imagen'),
    path('adm/modificar/Familia/<int:id>/', ModificaFamilia,name='ModificarFamilia'),
    path('adm/modificar/SubFamiliaFamilia/<int:id>/', ModificaSubFamilia,name='ModificaSubFamilia'),
    path('adm/modificar/Provincia/<int:id>/', ModificaProvincia,name='ModificaProvincia'),
    path('adm/modificar/Region/<int:id>/', ModificaRegion,name='ModificaRegion'),
    path('adm/modificar/Comuna/<int:id>/', ModificaComuna,name='ModificaComuna'),
    path('adm/modificar/Sucursal/<int:id>/', ModificaSucursal,name='ModificaSucursal'),
    path('adm/modificar/Estado/<int:id>/', ModificaEstado,name='ModificaEstado'),
    path('adm/modificar/TipoPago/<int:id>/', ModificaTipoPago,name='ModificaTipoPago')
]