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
from django.contrib.auth.views import LogoutView
from AppMercado.views import *
from blog.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", inicio),
    path("inicio/", inicio, name="inicio"),
    path("quienessomos/", quienessomos, name="quienessomos"),
    path("electrodomesticos/", electrodomesticos, name="electrodomesticos"),
    path("muebles/", muebles, name="muebles"),
    path("vehiculos/", vehiculos, name="vehiculos"),
    path("electrodomesticosFormulario/", electrodomesticosFormulario, name="electrodomesticosFormulario"),
    path("mueblesFormulario/", mueblesFormulario, name="mueblesFormulario"),
    path("vehiculosFormulario/", vehiculosFormulario, name="vehiculosFormulario"),
    path("publicacionExitosa/", publicacionExitosa, name="publicacionExitosa"),
    path("busquedaElectrodomesticos/", busquedaElectrodomesticos, name="busquedaElectrodomesticos"),
    path("busquedaMuebles/", busquedaMuebles, name="busquedaMuebles"),
    path("busquedaVehiculos/", busquedaVehiculos, name="busquedaVehiculos"),
    path("buscarElectrodomesticos/", buscarElectrodomesticos, name="buscarElectrodomesticos"),
    path("buscarMuebles/", buscarMuebles, name="buscarMuebles"),
    path("buscarVehiculos/", buscarVehiculos, name="buscarVehiculos"),
    path("leerElectrodomesticos/", leerElectrodomesticos, name="leerElectrodomesticos"),
    path("leerMuebles/", leerMuebles, name="leerMuebles"),
    path("leerVehiculos/", leerVehiculos, name="leerVehiculos"),
    path("borrarElectrodomesticos/<id>", borrarElectrodomesticos, name="borrarElectrodomesticos"),
    path("borrarMuebles/<id>", borrarMuebles, name="borrarMuebles"),
    path("borrarVehiculos/<id>", borrarVehiculos, name="borrarVehiculos"),
    path("editarElectrodomesticos/<id>", editarElectrodomesticos, name="editarElectrodomesticos"),
    path("editarMuebles/<id>", editarMuebles, name="editarMuebles"),
    path("editarVehiculos/<id>", editarVehiculos, name="editarVehiculos"),
    path("login/", login_request, name="login"),
    path("register/", register, name="register"),
    path("logout/", LogoutView.as_view(template_name="AppMercado/logout.html"), name="logout"),
    path("editarPerfil/", editarPerfil, name="editarPerfil"),
    path("agregarAvatar/", agregarAvatar, name="agregarAvatar"),
    #path("blog/", blog, name="blog"),
    path("blog/", include("blog.urls")),
    path("chat/", include("chat.urls")),
    #path("resultadosBusqueda/", name="resultadosBusqueda"),
    
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

