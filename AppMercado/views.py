from django.shortcuts import render
from .models import Electrodomesticos, Muebles, Vehiculos
from django.http import HttpResponse
from AppMercado.forms import ElectroForm, MueblesForm, VehiculosForm

# Create your views here.

def inicio(request):
    return render(request, "AppMercado/inicio.html")



def electrodomesticos(request):

    #return HttpResponse(texto)
    return render(request, "AppMercado/electrodomesticos.html")


def electrodomesticosFormulario(request):
    if request.method=="POST":
        form=ElectroForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            marca=informacion["marca"]
            precio=informacion["precio"]
            email_contacto=informacion["email_contacto"]
            fecha_publicacion=informacion["fecha_publicacion"]
            electrodomestico=Electrodomesticos(nombre=nombre, marca=marca, precio=precio, email_contacto=email_contacto, fecha_publicacion=fecha_publicacion)
            electrodomestico.save()
            return render(request, "AppMercado/publicacionExitosa.html")


    else:
        formulario=ElectroForm()
        return render(request, "AppMercado/electrodomesticosFormulario.html", {"formulario":formulario})



def muebles(request):

    return render(request, "AppMercado/muebles.html")
    # return render(request, "electromesticos.html")

def mueblesFormulario(request):
    if request.method=="POST":
        form=MueblesForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            material=informacion["material"]
            precio=informacion["precio"]
            email_contacto=informacion["email_contacto"]
            fecha_publicacion=informacion["fecha_publicacion"]
            muebles=Muebles(nombre=nombre, material=material, precio=precio, email_contacto=email_contacto, fecha_publicacion=fecha_publicacion)
            muebles.save()
            return render(request, "AppMercado/publicacionExitosa.html")

    else:
        formulario=MueblesForm()
        return render(request, "AppMercado/mueblesFormulario.html", {"formulario":formulario})



def vehiculos(request):

    return render(request, "AppMercado/vehiculos.html")
    # return render(request, "electromesticos.html")

def vehiculosFormulario(request):
    if request.method=="POST":
        form=VehiculosForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            marca=informacion["marca"]
            precio=informacion["precio"]
            email_contacto=informacion["email_contacto"]
            fecha_publicacion=informacion["fecha_publicacion"]
            vehiculo=Vehiculos(nombre=nombre, marca=marca, precio=precio, email_contacto=email_contacto, fecha_publicacion=fecha_publicacion)
            vehiculo.save()
            return render(request, "AppMercado/publicacionExitosa.html")
    
    else:
        formulario=VehiculosForm()
        return render(request, "AppMercado/vehiculosFormulario.html", {"formulario":formulario})

def publicacionExitosa(request):

    return render(request, "AppMercado/publicacionExitosa.html")


def busquedaElectrodomesticos(request):
    return render(request, "AppMercado/busquedaElectrodomesticos.html")

def buscarElectrodomesticos(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        electrodomesticos=Electrodomesticos.objects.filter(nombre=nombre)
        #respuesta=f"Estoy publicando el mueble"
        return render(request, "AppMercado/buscarElectrodomesticos.html", {"electrodomesticos":electrodomesticos})
    else:
        return render(request, "AppMercado/busquedaElectrodomesticos.html", {"mensaje":"Ingrese datos para realizar busqueda"})

def busquedaMuebles(request):
    return render(request, "AppMercado/busquedaMuebles.html")

def buscarMuebles(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        muebles=Muebles.objects.filter(nombre=nombre)
        #respuesta=f"Estoy publicando el mueble"
        return render(request, "AppMercado/buscarMuebles.html", {"muebles":muebles})
    else:
        return render(request, "AppMercado/busquedaMuebles.html", {"mensaje":"Ingrese datos para realizar busqueda"})


def busquedaVehiculos(request):
    return render(request, "AppMercado/busquedaVehiculos.html")

def buscarVehiculos(request):
    if request.GET["nombre"]:
        nombre=request.GET["nombre"]
        vehiculos=Vehiculos.objects.filter(nombre=nombre)

        #print(vehiculos)
        #respuesta=f"Estoy publicando el nombre {nombre}"
        #print(respuesta)
        #return HttpResponse(respuesta)
        return render(request, "AppMercado/buscarVehiculos.html", {"vehiculos":vehiculos})
    else:
        return render(request, "AppMercado/busquedaVehiculos.html", {"mensaje":"Ingrese datos para realizar busqueda"})

