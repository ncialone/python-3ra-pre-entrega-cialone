from django.contrib import admin
from django.urls import path

#PARA ACCEDER A LAS VISTAS HAY QUE IMPORTAR EL MODULO Y EL METODO
from entrega_3.views import probandoTemplate
from App1.views import curso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('template/',probandoTemplate),
    path('curso/',curso),
]