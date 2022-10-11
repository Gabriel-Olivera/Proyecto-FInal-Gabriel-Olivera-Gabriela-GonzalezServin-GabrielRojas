from telnetlib import LOGOUT
from django.shortcuts import render
from .models import Electrodomesticos, Muebles, Vehiculos, Avatar
from AppMercado.forms import ElectroForm, MueblesForm, VehiculosForm, UserRegisterForm, UserEditForm, AvatarForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

def inicio(request):
    return render(request, "AppMercado/inicio.html")

def quienessomos(request):
    return render(request, "AppMercado/quienessomos.html")

def electrodomesticos(request):

    #return HttpResponse(texto)
    return render(request, "AppMercado/electrodomesticos.html")

@login_required
def electrodomesticosFormulario(request):
    if request.method=="POST":
        form=ElectroForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            marca=informacion["marca"]
            precio=informacion["precio"]
            email_contacto=informacion["email_contacto"]
            #fecha_publicacion=informacion["fecha_publicacion"]
            electrodomestico=Electrodomesticos(nombre=nombre, marca=marca, precio=precio, email_contacto=email_contacto)
            electrodomestico.save()
            return render(request, "AppMercado/publicacionExitosa.html")
    else:
        formulario=ElectroForm()
        return render(request, "AppMercado/electrodomesticosFormulario.html", {"formulario":formulario})


def muebles(request):

    return render(request, "AppMercado/muebles.html")
    # return render(request, "electromesticos.html")

@login_required
def mueblesFormulario(request):
    if request.method=="POST":
        form=MueblesForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            material=informacion["material"]
            precio=informacion["precio"]
            email_contacto=informacion["email_contacto"]
            #fecha_publicacion=informacion["fecha_publicacion"]
            muebles=Muebles(nombre=nombre, material=material, precio=precio, email_contacto=email_contacto)
            muebles.save()
            return render(request, "AppMercado/publicacionExitosa.html")
    else:
        formulario=MueblesForm()
        return render(request, "AppMercado/mueblesFormulario.html", {"formulario":formulario})



def vehiculos(request):

    return render(request, "AppMercado/vehiculos.html")
    # return render(request, "electromesticos.html")

@login_required
def vehiculosFormulario(request):
    if request.method=="POST":
        form=VehiculosForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            marca=informacion["marca"]
            precio=informacion["precio"]
            email_contacto=informacion["email_contacto"]
            #fecha_publicacion=informacion["fecha_publicacion"]
            vehiculo=Vehiculos(nombre=nombre, marca=marca, precio=precio, email_contacto=email_contacto)
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
        return render(request, "AppMercado/buscarVehiculos.html", {"vehiculos":vehiculos})
    else:
        return render(request, "AppMercado/busquedaVehiculos.html", {"mensaje":"Ingrese datos para realizar busqueda"})

def leerElectrodomesticos(request):
        electrodomesticos=Electrodomesticos.objects.all()
        
        return render(request, "AppMercado/leerElectrodomesticos.html", {"electrodomesticos":electrodomesticos})

def leerMuebles(request):
        muebles=Muebles.objects.all()
        
        return render(request, "AppMercado/leerMuebles.html", {"muebles":muebles})

def leerVehiculos(request):
        vehiculos=Vehiculos.objects.all()
        
        return render(request, "AppMercado/leerVehiculos.html", {"vehiculos":vehiculos})

@staff_member_required
def borrarElectrodomesticos(request, id):
        electrodomesticos=Electrodomesticos.objects.get(id=id)
        electrodomesticos.delete()
        electrodomesticos=Electrodomesticos.objects.all()
        return render(request, "AppMercado/leerElectrodomesticos.html", {"electrodomesticos":electrodomesticos})

@staff_member_required
def borrarMuebles(request, id):
        muebles=Muebles.objects.get(id=id)
        muebles.delete()
        muebles=Muebles.objects.all()
        return render(request, "AppMercado/leerMuebles.html", {"muebles":muebles})

@staff_member_required
def borrarVehiculos(request, id):
        vehiculos=Vehiculos.objects.get(id=id)
        vehiculos.delete()
        vehiculos=Vehiculos.objects.all()
        return render(request, "AppMercado/leerVehiculos.html", {"vehiculos":vehiculos})

@staff_member_required
def editarElectrodomesticos(request, id):
        electrodomesticos=Electrodomesticos.objects.get(id=id)
        if request.method == "POST":
            form=ElectroForm(request.POST)
            if form.is_valid():
                informacion=form.cleaned_data
                electrodomesticos.nombre=informacion["nombre"]
                electrodomesticos.marca=informacion["marca"]
                electrodomesticos.precio=informacion["precio"]
                electrodomesticos.email_contacto=informacion["email_contacto"]
                electrodomesticos.save()
                electrodomesticos=Electrodomesticos.objects.all()
                return render(request, "AppMercado/leerElectrodomesticos.html", {"electrodomesticos":electrodomesticos})
        else:
            form=ElectroForm(initial={"nombre":electrodomesticos.nombre, "marca":electrodomesticos.marca, "precio":electrodomesticos.precio, "email_contacto":electrodomesticos.email_contacto})
            return render(request, "AppMercado/editarElectrodomesticos.html", {"formulario":form, "electrodomesticos":electrodomesticos})

@staff_member_required
def editarMuebles(request, id):
        muebles=Muebles.objects.get(id=id)
        if request.method=="POST":
            form=MueblesForm(request.POST)
            if form.is_valid():
                informacion=form.cleaned_data
                muebles.nombre=informacion["nombre"]
                muebles.material=informacion["material"]
                muebles.precio=informacion["precio"]
                muebles.email_contacto=informacion["email_contacto"]
                muebles.save()
                muebles=Muebles.objects.all()
                return render(request, "AppMercado/leerMuebles.html", {"muebles":muebles})
        else:
            form=MueblesForm(initial={"nombre":muebles.nombre, "material":muebles.material, "precio":muebles.precio, "email_contacto":muebles.email_contacto})
            return render(request, "AppMercado/editarMuebles.html", {"formulario":form, "muebles":muebles})

@staff_member_required
def editarVehiculos(request, id):
        vehiculos=Vehiculos.objects.get(id=id)
        if request.method == "POST":
            form=VehiculosForm(request.POST)
            if form.is_valid():
                informacion=form.cleaned_data
                vehiculos.nombre=informacion["nombre"]
                vehiculos.marca=informacion["marca"]
                vehiculos.precio=informacion["precio"]
                vehiculos.email_contacto=informacion["email_contacto"]
                vehiculos.save()
                vehiculos=Vehiculos.objects.all()
                return render(request, "AppMercado/leerVehiculos.html", {"vehiculos":vehiculos})
        else:
            form=VehiculosForm(initial={"nombre":vehiculos.nombre, "marca":vehiculos.marca, "precio":vehiculos.precio, "email_contacto":vehiculos.email_contacto})
            return render(request, "AppMercado/editarVehiculos.html", {"formulario":form, "vehiculos":vehiculos})


def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            passw=request.POST["password"]

            usuario=authenticate(username=usu, password=passw)
            if usuario is not None:
                login(request,usuario)
                return render(request, "AppMercado/inicio.html", {"mensaje":"Login exitoso! Bienvenido!"})
            else:
                return render(request, "AppMercado/login.html", {"formulario":form, "mensaje":"Usuario y/o contraseña incorrectos"})
        else:
            return render(request, "AppMercado/login.html", {"formulario":form, "mensaje":"Usuario y/o contraseña incorrectos"})
    else: 
        form=AuthenticationForm()
        return render(request, "AppMercado/login.html", {"formulario":form})

def register(request):
    if request.method == "POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "AppMercado/inicio.html", {"mensaje":"Registro de usuario exitoso!"})
        else:
            return render(request, "AppMercado/register.html", {"formulario":form, "mensaje":"Formulario inválido"})
    else:
        form=UserRegisterForm()
        return render(request, "AppMercado/register.html", {"formulario":form})

@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method == "POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "AppMercado/inicio.html", {"mensaje":"Perfil actualizado!", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "AppMercado/editarPerfil.html", {"formulario":form, "usuario":usuario, "mensaje":"Formulario inválido"})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "AppMercado/editarPerfil.html", {"formulario":form, "usuario":usuario, "avatar":obtenerAvatar(request)})

@login_required
def agregarAvatar(request):
    if request.method=="POST":
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if(len(avatarViejo)!=0):
                avatarViejo[0].delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, "AppMercado/inicio.html", {"mensaje":"Avatar actualizado!", "avatar": avatar.imagen.url})
        else:
            return render(request, "AppMercado/agregarAvatar.html", {"formulario":formulario, "mensaje":"No se pudo actualizar Avatar"})
    else:
        formulario=AvatarForm()
        return render(request, "AppMercado/agregarAvatar.html", {"formulario":formulario, "usuario":request.user, "avatar":obtenerAvatar(request)})

def obtenerAvatar(request):
    avatar=Avatar.objects.filter(user=request.user)
    if(len(avatar)!=0):
        imagen=avatar[0].imagen.url
    else:
        imagen="\media\avatares\default.png"
    return imagen


