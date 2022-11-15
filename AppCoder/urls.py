"""ProyectoCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from .views import mostrar_curso, mostrar_index, mostrar_referencias, mostrar_repaso, crear_curso, crear_profesor, buscar_comision, buscar_profesor

urlpatterns = [
    path('mostrar_curso/', mostrar_curso, name='Mostrar'),
    path('', mostrar_index, name='Home'),
    path('mostrar_referencias/', mostrar_referencias, name='Referencias'),
    path('mostrar_repaso/', mostrar_repaso, name='Repaso'),
    path('crear_curso/', crear_curso, name='Crear Curso'),
    path('crear_profesor/', crear_profesor, name='Crear Profesor'),
    path('buscar_comision/', buscar_comision, name='Buscar Comision'),
    path('buscar_profesor/', buscar_profesor, name='Buscar Profesor'),
]
