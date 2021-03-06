"""proyecto_bd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appgestion import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar_todo/',views.listar_todo),
    path('listar_todo_persona/',views.listar_todo_persona),
    path('ingresar_persona/', views.ingresar_persona),
    path('ingreso_persona/',views.ingreso_persona),
    
    path('busqueda_persona/',views.busqueda_persona),
    path('buscar/',views.buscar),
    path('eliminar_persona/',views.eliminar_persona),
    path('eliminacion_persona/',views.eliminacion_persona),    
    path('',views.index),
    path('index/',views.index),
]

