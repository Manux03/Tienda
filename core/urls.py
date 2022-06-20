from django.urls import path
from .views import Tienda, home, adm, homex, ProductoDetalle
from .views import TablaProducto,TablaProductoFamilia,TablaSubFamilia,TablaRegion,TablaProvincia,TablaComuna,TablaSucursal,TablaTipoPago,TablaEstado, TablaCompraEstado,TablaCompraDetalle,TablaCompra, TablaEstrategia,TablaEstrategiaDetalle 
from .views import AgregarProducto, AgregarFamilia, AgregarSubFamilia, AgregarRegion, AgregarProvincia, AgregarComuna, AgregarSucursal, AgregarTipoPago, AgregarEstado, AgregarCompraEstado, AgregarCompraDetalle, AgregarCompra, AgregarEstrategia, AgregarEstrategiaDetalle
from .views import EliminarProducto, EliminarFamilia, EliminarRegion,EliminarProvincia, EliminarComuna, EliminarSucursal, EliminarTipopago, EliminarEstado, EliminarCompra,  EliminarEstrategia
from .views import  ModificaProducto, ModificaFamilia, ModificaSubFamilia, ModificaRegion, ModificaProvincia,ModificaComuna, ModificaSucursal, ModificaTipoPago, ModificaEstado, ModificaCompraEstado, ModificaCompraDetalle, ModificaCompra, ModificaEstrategia, ModificaEstrategiaDetalle    

urlpatterns = [
    path('home/', home, name='home'),
    path('adm/', adm, name='adm'),
    path('homex/', homex, name='homex'),
    path('Tienda/', Tienda, name='Tienda'),
    path('Tienda/Producto/<int:id>/', ProductoDetalle,name='ProductoDetalle'), 
    #listar
    path('adm/tablas/Producto', TablaProducto, name='TablaProducto'), # FUNCIONA
    path('adm/tablas/Familia', TablaProductoFamilia, name='TablaProductoFamilia'), # FUNCIONA
    path('adm/tablas/SubFamilia', TablaSubFamilia, name='TablaSubFamilia'), # FUNCIONA
    path('adm/tablas/Region', TablaRegion, name='TablaRegion'), # FUNCIONA
    path('adm/tablas/Provincia', TablaProvincia, name='TablaProvincia'), # FUNCIONA
    path('adm/tablas/Comuna', TablaComuna, name='TablaComuna'), # FUNCIONA
    path('adm/tablas/Sucursal', TablaSucursal, name='TablaSucursal'), # FUNCIONA
    path('adm/tablas/TipoPago', TablaTipoPago, name='TablaTipoPago'), # FUNCIONA
    path('adm/tablas/Estado', TablaEstado, name='TablaEstado'),  # FUNCIONA
    path('adm/tablas/Compra_Estado', TablaCompraEstado, name='TablaCompraEstado'),  # FUNCIONA
    path('adm/tablas/CompraDetalle', TablaCompraDetalle, name='TablaCompraDetalle'), # FUNCIONA
    path('adm/tablas/Compra', TablaCompra, name='TablaCompra'), # FUNCIONA
    path('adm/tablas/Estrategia', TablaEstrategia, name='TablaEstrategia'), # FUNCIONA
    path('adm/tablas/Estrategia_Detalle', TablaEstrategiaDetalle, name='TablaEstrategiaDetalle'),

    #agregar
    path('adm/añadir/Producto', AgregarProducto, name='AgregarProducto'), # FUNCIONA
    path('adm/añadir/Familia', AgregarFamilia, name='AgregarFamilia'), # FUNCIONA
    path('adm/añadir/SubFamilia', AgregarSubFamilia, name='AgregarSubFamilia'), # FUNCIONA
    path('adm/añadir/Region', AgregarRegion, name='AgregarRegion'), # FUNCIONA
    path('adm/añadir/Provincia', AgregarProvincia, name='AgregarProvincia'), # FUNCIONA
    path('adm/añadir/Comuna', AgregarComuna, name='AgregarComuna'), # FUNCIONA
    path('adm/añadir/Sucursal', AgregarSucursal, name='AgregarSucursal'), # FUNCIONA
    path('adm/añadir/TipoPago', AgregarTipoPago, name='AgregarTipoPago'), # FUNCIONA
    path('adm/añadir/Estado', AgregarEstado, name='AgregarEstado'), # FUNCIONA
    path('adm/añadir/Compra_Estado', AgregarCompraEstado, name='AgregarCompraEstado'),  # FUNCIONA
    path('adm/añadir/CompraDetalle', AgregarCompraDetalle, name='AgregarCompraDetalle'), # FUNCIONA
    path('adm/añadir/Compra', AgregarCompra, name='AgregarCompra'),  # FUNCIONA
    path('adm/añadir/Estrategia', AgregarEstrategia, name='AgregarEstrategia'), # FUNCIONA
    path('adm/añadir/Estrategia_Detalle', AgregarEstrategiaDetalle, name='AgregarEstrategiaDetalle'),
    
    #eliminar
    path('adm/eliminar/Producto/<int:id>/', EliminarProducto,name='EliminarProducto'), # FUNCIONA
    path('adm/eliminar/Familia/<int:id>/', EliminarFamilia,name='EliminarFamilia'), # FUNCIONA
    path('adm/eliminar/Region/<int:id>/', EliminarRegion,name='EliminarRegion'), # FUNCIONA
    path('adm/eliminar/Provincia/<int:id>/', EliminarProvincia,name='EliminarProvincia'), # FUNCIONA
    path('adm/eliminar/Comuna/<int:id>/', EliminarComuna,name='EliminarComuna'), # FUNCIONA
    path('adm/eliminar/Sucursal/<int:id>/', EliminarSucursal,name='EliminarSucursal'), # FUNCIONA
    path('adm/eliminar/TipoPago/<int:id>/', EliminarTipopago,name='EliminarTipoPago'), # FUNCIONA
    path('adm/eliminar/Estado/<int:id>/', EliminarEstado,name='EliminarEstado'), # FUNCIONA
    path('adm/eliminar/Compra/<int:id>/', EliminarCompra,name='EliminarCompra'), # FUNCIONA
    path('adm/eliminar/Estrategia/<int:id>/', EliminarEstrategia,name='EliminarEstrategia'), # FUNCIONA
    
    #update
    path('adm/modificar/Producto/<int:id>/', ModificaProducto,name='ModificaProducto'), # FUNCIONA
    path('adm/modificar/Familia/<int:id>/', ModificaFamilia,name='ModificarFamilia'), # FUNCIONA
    path('adm/modificar/SubFamiliaFamilia/<int:id>/', ModificaSubFamilia,name='ModificaSubFamilia'), # FUNCIONA
    path('adm/modificar/Region/<int:id>/', ModificaRegion,name='ModificaRegion'), # FUNCIONA
    path('adm/modificar/Provincia/<int:id>/', ModificaProvincia,name='ModificaProvincia'), # FUNCIONA
    path('adm/modificar/Comuna/<int:id>/', ModificaComuna,name='ModificaComuna'), # FUNCIONA
    path('adm/modificar/Sucursal/<int:id>/', ModificaSucursal,name='ModificaSucursal'), # FUNCIONA
    path('adm/modificar/TipoPago/<int:id>/', ModificaTipoPago,name='ModificaTipoPago'), # FUNCIONA
    path('adm/modificar/Estado/<int:id>/', ModificaEstado,name='ModificaEstado'), # FUNCIONA
    path('adm/modificar/Compra_Estado/<int:id>/', ModificaCompraEstado,name='ModificaCompraEstado'),  # FUNCIONA
    path('adm/modificar/CompraDetalle/<int:id>/', ModificaCompraDetalle,name='ModificaCompraDetalle'), # FUNCIONA
    path('adm/modificar/Compra/<int:id>/', ModificaCompra,name='ModificaCompra'), # FUNCIONA
    path('adm/modificar/Estrategia/<int:id>/', ModificaEstrategia,name='ModificaEstrategia'), # FUNCIONA
    path('adm/modificar/Estrategia_Detalle/<int:id>/', ModificaEstrategiaDetalle,name='ModificaEstrategiaDetalle'),
    
    
]