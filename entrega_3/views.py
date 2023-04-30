from django.http import HttpResponse
import datetime
from django.template import Template, Context

def probandoTemplate(self):
    miHtml = open("C:/Users/Nahuel Cialone/OneDrive/DEVELOP/PYTHON/CODERHOUSE/ENTREGAS/entrega_3/entrega_3/templates/template1.html")
    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context
    miHtml.close() #Cerramos el archivo
    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo
    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento
    return HttpResponse(documento)