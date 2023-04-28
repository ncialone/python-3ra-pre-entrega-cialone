from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):   #Nuestra primera vista :) 
	return HttpResponse("HOLA NAHUEL, PROBANDO DJANGO!")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :) ")