from django.shortcuts import render
from django.http import HttpResponse
from django.forms.widgets import DateInput
from App1.models import Curso, Profesor, Estudiante, Entregable
from App1.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, EntregableFormulario

# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')
def cursos(request):
    return render(request,'App1/cursos.html')
def profesores(request):
    return render(request,'App1/profesores.html')
def estudiantes(request):
    return render(request,'App1/estudiantes.html')
def entregables(request):
    return render(request,'App1/entregables.html')

def cursos(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(str(informacion['nombre']), int(informacion['curso']))
            curso.save()
            return render(request, "App1/inicio.html")
    else:
        miFormulario = CursoFormulario
    return render(request, "App1/cursos.html", {"miFormulario": miFormulario})

def profesores(request):
    if request.method == "POST":
        miFormulario = ProfesorFormulario(request.POST) # Aqui me llega la informacion del html
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Profesor(str(informacion['nombre']),str(informacion['apellido']),
                            informacion['email'], informacion['profesion'])
            curso.save()
            return render(request, "App1/inicio.html")
    else:
        miFormulario = ProfesorFormulario()
    return render(request, "App1/profesores.html", {"miFormulario": miFormulario})

def estudiantes(request):
    if request.method == "POST":
        miFormulario = EstudianteFormulario(request.POST) # Aqui me llega la informacion del html
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Estudiante(str(informacion['nombre']),str(informacion['apellido']),
                                informacion['email'])
            curso.save()
            return render(request, "App1/inicio.html")
    else:
        miFormulario = EstudianteFormulario()       
    return render(request, "App1/estudiantes.html", {"miFormulario": miFormulario})

def entregables(request):
    if request.method =="POST":
        miFormulario = EntregableFormulario(request.POST) # Aqui me llega la informacion del html
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Entregable(str(informacion['nombre']),(informacion['fechaentrega']),bool(informacion['entregado'])) 
            curso.save()
            return render(request, "App1/inicio.html")
    else:
        miFormulario = EntregableFormulario()
        miFormulario.fields['fechaentrega'].widget = DateInput(attrs={'type': 'date'})       
    return render(request, "App1/entregables.html", {"miFormulario": miFormulario})

def busquedaCurso(request):
    return render(request,'App1/busquedaCurso.html')

def buscar(request):
    if request.method == 'POST':
        # Verifica si la clave 'curso' está presente en el diccionario POST
        if 'curso' in request.POST:
            # Si la clave está presente, obtiene su valor y realiza la búsqueda
            numero_curso = request.POST['curso']
            cursos = Curso.objects.filter(curso__icontains=numero_curso)
            return render(request, 'App1/resultadosBusqueda.html', {'cursos': cursos})
    return render(request, 'App1/.html')