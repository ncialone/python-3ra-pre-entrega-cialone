from django.contrib import admin
from django.urls import path
from entrega_3.views import saludo, segunda_vista, probandoTemplate  #Para acceder a la vista hay que importar el modulo y el método

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('segunda_vista/',segunda_vista),
    path('template/',probandoTemplate),
]