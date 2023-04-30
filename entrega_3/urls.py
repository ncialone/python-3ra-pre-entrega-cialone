#PARA ACCEDER A LAS VISTAS HAY QUE IMPORTAR EL MODULO Y EL METODO
from django.contrib import admin
from django.urls import path,include #con INCLUDE traemos todas las URLs de la APP1

urlpatterns = [
    path("admin/", admin.site.urls),
    path('App1/',include('App1.urls'))
]