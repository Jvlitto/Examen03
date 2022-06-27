from django.shortcuts import render
from appgestion.models import Persona
from django.http import HttpResponse

def ingresar_persona(request):
    return render(request,"ingresar_persona.html")

def index(request):
    return render(request,"index.html")

def busqueda_persona(request):
    return render(request,"busqueda_persona.html") 

def listar_todo(request):
    return render(request,"listar_todo.html")

def eliminar_persona(request):
    return render(request,"eliminar_persona.html")

# Create your views here.

def listar_todo_persona(request):
    datos = Persona.objects.all()  
    return render(request,"listar_todo.html",{'personas':datos})
    
def ingreso_persona(request):
    rut=request.GET["txt_rut"]
    nombre=request.GET["txt_nombre"]
    apellido_paterno=request.GET["txt_appaterno"]
    apellido_materno=request.GET["txt_apmaterno"]
    edad=request.GET["txt_edad"]
    vacuna=request.GET["txt_vacuna"]
    fecha=request.GET["txt_fecha"]
    if len(rut)>0 and len(nombre)>0 and len(apellido_paterno)>0 and len(apellido_materno)>0 and len(edad)>0 and len(vacuna)>0 and len(fecha)>0:
        per=Persona(rut=rut,nombre=nombre,apellido_paterno=apellido_paterno,apellido_materno=apellido_materno,edad=edad,vacuna=vacuna,fecha=fecha)  
        per.save()
        mensaje="<h1>Persona ingresada...</h1> <br> <a href='/index/'>Volver al Inicio</a>"
    else:
        mensaje="<h1>Persona no ingresada o datos faltantes...</h1> <br> <a href='/ingresar_persona/'>Volver a Ingresar</a><br> <a href='/index/'>Volver al inicio</a>"
    return HttpResponse(mensaje)

def buscar(request):
    if request.GET["txt_rut"]:
        rut = request.GET["txt_rut"]
        personas = Persona.objects.filter(rut__icontains=rut)
        return render(request,"listar.html",{"personas":personas,"query":rut})
    else:
        mensaje = "Debe ingresar el RUT de la persona a buscar <br> <a href='/busqueda_persona/'>Volver a Buscar</a>"
        return HttpResponse(mensaje)


def eliminacion_persona(request):
    if request.GET["txt_rut"]:
        rut_recibido = request.GET["txt_rut"]
        persona = Persona.objects.filter(rut=rut_recibido)
        if persona:
            per=Persona.objects.get(rut=rut_recibido)
            per.delete()
            mensaje = "Persona Eliminada... <br> <a href='/index/'>Volver al Inicio</a>"
        else:
            mensaje = "<h1>Persona NO eliminada...</h1><h2>RUT no existente</h2><a href='/eliminar_persona/'>Volver a Eliminar </a><br><br> <a href='/index/'>Volver al inicio</a>"
    else:
        mensaje = "<h1>Debe ingresar un RUT para eliminar...</h1><a href='/eliminar_persona/'>Volver a Eliminar </a><br><br> <a href='/index/'>Volver al inicio</a>"
    return HttpResponse(mensaje)


