from django.urls import path
from .views import adm
from .views import TablaProducto,TablaProductoFamilia,TablaSubFamilia,TablaRegion,TablaProvincia,TablaComuna,TablaSucursal,TablaTipoPago,TablaEstado, TablaCompraEstado,TablaCompraDetalle,TablaCompra, TablaEstrategia,TablaEstrategiaDetalle 
from .views import AgregarProducto, AgregarFamilia, AgregarSubFamilia, AgregarRegion, AgregarProvincia, AgregarComuna, AgregarSucursal, AgregarTipoPago, AgregarEstado, AgregarCompraEstado, AgregarCompraDetalle, AgregarCompra, AgregarEstrategia, AgregarEstrategiaDetalle
from .views import EliminarProducto, EliminarFamilia, EliminarRegion,EliminarProvincia, EliminarComuna, EliminarSucursal, EliminarTipopago, EliminarEstado, EliminarCompra,  EliminarEstrategia
from .views import  ModificaProducto, ModificaFamilia, ModificaSubFamilia, ModificaRegion, ModificaProvincia,ModificaComuna, ModificaSucursal, ModificaTipoPago, ModificaEstado, ModificaCompraEstado, ModificaCompraDetalle, ModificaCompra, ModificaEstrategia, ModificaEstrategiaDetalle    

urlpatterns = [
    
    path('', adm, name='adm'),
    #listar
    path('tablas/Producto', TablaProducto, name='TablaProducto'), # FUNCIONA
    path('tablas/Familia', TablaProductoFamilia, name='TablaProductoFamilia'), # FUNCIONA
    path('tablas/SubFamilia', TablaSubFamilia, name='TablaSubFamilia'), # FUNCIONA
    path('tablas/Region', TablaRegion, name='TablaRegion'), # FUNCIONA
    path('tablas/Provincia', TablaProvincia, name='TablaProvincia'), # FUNCIONA
    path('tablas/Comuna', TablaComuna, name='TablaComuna'), # FUNCIONA
    path('tablas/Sucursal', TablaSucursal, name='TablaSucursal'), # FUNCIONA
    path('tablas/TipoPago', TablaTipoPago, name='TablaTipoPago'), # FUNCIONA
    path('tablas/Estado', TablaEstado, name='TablaEstado'),  # FUNCIONA
    path('tablas/Compra_Estado', TablaCompraEstado, name='TablaCompraEstado'),  # FUNCIONA
    path('tablas/CompraDetalle', TablaCompraDetalle, name='TablaCompraDetalle'), # FUNCIONA
    path('tablas/Compra', TablaCompra, name='TablaCompra'), # FUNCIONA
    path('tablas/Estrategia', TablaEstrategia, name='TablaEstrategia'), # FUNCIONA
    path('tablas/Estrategia_Detalle', TablaEstrategiaDetalle, name='TablaEstrategiaDetalle'),

    #agregar
    path('añadir/Producto', AgregarProducto, name='AgregarProducto'), # FUNCIONA
    path('añadir/Familia', AgregarFamilia, name='AgregarFamilia'), # FUNCIONA
    path('añadir/SubFamilia', AgregarSubFamilia, name='AgregarSubFamilia'), # FUNCIONA
    path('añadir/Region', AgregarRegion, name='AgregarRegion'), # FUNCIONA
    path('añadir/Provincia', AgregarProvincia, name='AgregarProvincia'), # FUNCIONA
    path('añadir/Comuna', AgregarComuna, name='AgregarComuna'), # FUNCIONA
    path('añadir/Sucursal', AgregarSucursal, name='AgregarSucursal'), # FUNCIONA
    path('añadir/TipoPago', AgregarTipoPago, name='AgregarTipoPago'), # FUNCIONA
    path('añadir/Estado', AgregarEstado, name='AgregarEstado'), # FUNCIONA
    path('añadir/Compra_Estado', AgregarCompraEstado, name='AgregarCompraEstado'),  # FUNCIONA
    path('añadir/CompraDetalle', AgregarCompraDetalle, name='AgregarCompraDetalle'), # FUNCIONA
    path('añadir/Compra', AgregarCompra, name='AgregarCompra'),  # FUNCIONA
    path('añadir/Estrategia', AgregarEstrategia, name='AgregarEstrategia'), # FUNCIONA
    path('añadir/Estrategia_Detalle', AgregarEstrategiaDetalle, name='AgregarEstrategiaDetalle'),
    
    #eliminar
    path('eliminar/Producto/<int:id>/', EliminarProducto,name='EliminarProducto'), # FUNCIONA
    path('eliminar/Familia/<int:id>/', EliminarFamilia,name='EliminarFamilia'), # FUNCIONA
    path('eliminar/Region/<int:id>/', EliminarRegion,name='EliminarRegion'), # FUNCIONA
    path('eliminar/Provincia/<int:id>/', EliminarProvincia,name='EliminarProvincia'), # FUNCIONA
    path('eliminar/Comuna/<int:id>/', EliminarComuna,name='EliminarComuna'), # FUNCIONA
    path('eliminar/Sucursal/<int:id>/', EliminarSucursal,name='EliminarSucursal'), # FUNCIONA
    path('eliminar/TipoPago/<int:id>/', EliminarTipopago,name='EliminarTipoPago'), # FUNCIONA
    path('eliminar/Estado/<int:id>/', EliminarEstado,name='EliminarEstado'), # FUNCIONA
    path('eliminar/Compra/<int:id>/', EliminarCompra,name='EliminarCompra'), # FUNCIONA
    path('eliminar/Estrategia/<int:id>/', EliminarEstrategia,name='EliminarEstrategia'), # FUNCIONA
    
    #update
    path('modificar/Producto/<int:id>/', ModificaProducto,name='ModificaProducto'), # FUNCIONA
    path('modificar/Familia/<int:id>/', ModificaFamilia,name='ModificarFamilia'), # FUNCIONA
    path('modificar/SubFamiliaFamilia/<int:id>/', ModificaSubFamilia,name='ModificaSubFamilia'), # FUNCIONA
    path('modificar/Region/<int:id>/', ModificaRegion,name='ModificaRegion'), # FUNCIONA
    path('modificar/Provincia/<int:id>/', ModificaProvincia,name='ModificaProvincia'), # FUNCIONA
    path('modificar/Comuna/<int:id>/', ModificaComuna,name='ModificaComuna'), # FUNCIONA
    path('modificar/Sucursal/<int:id>/', ModificaSucursal,name='ModificaSucursal'), # FUNCIONA
    path('modificar/TipoPago/<int:id>/', ModificaTipoPago,name='ModificaTipoPago'), # FUNCIONA
    path('modificar/Estado/<int:id>/', ModificaEstado,name='ModificaEstado'), # FUNCIONA
    path('modificar/Compra_Estado/<int:id>/', ModificaCompraEstado,name='ModificaCompraEstado'),  # FUNCIONA
    path('modificar/CompraDetalle/<int:id>/', ModificaCompraDetalle,name='ModificaCompraDetalle'), # FUNCIONA
    path('modificar/Compra/<int:id>/', ModificaCompra,name='ModificaCompra'), # FUNCIONA
    path('modificar/Estrategia/<int:id>/', ModificaEstrategia,name='ModificaEstrategia'), # FUNCIONA
    path('modificar/Estrategia_Detalle/<int:id>/', ModificaEstrategiaDetalle,name='ModificaEstrategiaDetalle'),

]