"""Entrega1_OliveraRojasGonzalezServin URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from AppMercado.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", inicio),
    path("inicio/", inicio, name="inicio"),
    path("electrodomesticos/", electrodomesticos, name="electrodomesticos"),
    path("muebles/", muebles, name="muebles"),
    path("vehiculos/", vehiculos, name="vehiculos"),
    path(
        "electrodomesticosFormulario/",
        electrodomesticosFormulario,
        name="electrodomesticosFormulario",
    ),
    path("mueblesFormulario/", mueblesFormulario, name="mueblesFormulario"),
    path("vehiculosFormulario/", vehiculosFormulario, name="vehiculosFormulario"),
    path("publicacionExitosa/", publicacionExitosa, name="publicacionExitosa"),
    path(
        "busquedaElectrodomesticos/",
        busquedaElectrodomesticos,
        name="busquedaElectrodomesticos",
    ),
    path("busquedaMuebles/", busquedaMuebles, name="busquedaMuebles"),
    path("busquedaVehiculos/", busquedaVehiculos, name="busquedaVehiculos"),
    path(
        "buscarElectrodomesticos/",
        buscarElectrodomesticos,
        name="buscarElectrodomesticos",
    ),
    path("buscarMuebles/", buscarMuebles, name="buscarMuebles"),
    path("buscarVehiculos/", buscarVehiculos, name="buscarVehiculos"),
    path("blog/", include("blog.urls"))
    # path("resultadosBusqueda/", name="resultadosBusqueda"),
]
