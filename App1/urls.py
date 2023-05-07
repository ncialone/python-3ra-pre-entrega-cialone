from django.urls import path
from App1 import views

urlpatterns = [
    path('', views.inicio, name="Inicio"), #este era nuestro primer view
    path('buscar/',views.buscar, name='buscar'),
    path('cursos', views.cursos, name="Cursos"),
    path('cursos_list', views.cursos_list, name="cursos_list"),
    path('profesores', views.profesores, name="Profesores"),
    path('profesores_list', views.profesores_list, name="profesores_list"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('estudiantes_list', views.estudiantes_list, name="estudiantes_list"),
    path('entregables', views.entregables, name="Entregables"),
    path('entregables_list', views.entregables_list, name="entregables_list"),
]    
#path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
#path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
#path('estudianteFormulario', views.estudianteFormulario, name="EstudianteFormulario"),
#path('entregableFormulario', views.entregableFormulario, name="EntregableFormulario"),
#path('busquedaCurso',views.busquedaCurso,name="BusquedaCurso"),
