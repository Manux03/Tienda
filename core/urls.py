from django.urls import path
from .views import home, ProductoView

urlpatterns = [
    path('home/', home, name='home'),
    path('Producto/', ProductoView.as_view(), name='lista_de_usuarios'),
    path('Producto/<int:id>',ProductoView.as_view(), name='proceso_de_usuarios')
]
   