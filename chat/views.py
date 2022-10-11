from telnetlib import LOGOUT
from turtle import end_fill
from django.shortcuts import render
from .models import Chat
from AppMercado.forms import *
from chat.forms import ChatForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def chat(request):
    return render(request, "chat.html")
        # formulario=ChatForm(instance=usuario)



@login_required
def enviarmensaje(request):
    # usuario=request.user
    if request.method== "POST":
        formulario=ChatForm(request.POST)
        if formulario.is_valid():
            form=formulario.cleaned_data
            mensaje=Chat(user=request.user, content=form["content"], destinatario=form["destinatario"])
            mensaje.save()
            return render(request, "chat.html", {"mensaje":"Mensaje creado!"})
        else:
            return render(request, "enviarmensaje.html", {"formulario":formulario, "mensaje":"Mensaje no fue enviado"})
    else:
        formulario=ChatForm()
        return render(request, "enviarmensaje.html", {"formulario":formulario, "mensaje":"Creando mensaje"})
        # formulario=ChatForm(instance=usuario)


@login_required
def leermensajes(request):
    mensajes=Chat.objects.filter(destinatario=request.user)
    lista=[]
    for mensaje in mensajes:
        user_id=mensaje.user_id
        username=User.objects.get(id=user_id)
        lista.append(username)
    else:
        pass
    
    #     for men in mensajes:

    # enviado=Chat.objects.all()
    # users=User.objects.get(id=enviado.user_id)

    # users=User.objects.all()
    # usuarios=users.get("admin")
    # {"usuarios":usuarios}
    return render(request, "leermensajes.html", {"lista":lista, "mensajes":mensajes} )


    
# @login_required
# def editarPerfil(request):
#     usuario=request.user
#     if request.method == "POST":
#         form=UserEditForm(request.POST)
#         if form.is_valid():
#             info=form.cleaned_data
#             usuario.email=info["email"]
#             usuario.password1=info["password1"]
#             usuario.password2=info["password2"]
#             usuario.first_name=info["first_name"]
#             usuario.last_name=info["last_name"]
#             usuario.save()
#             return render(request, "AppMercado/inicio.html", {"mensaje":"Perfil actualizado!", "avatar":obtenerAvatar(request)})
#         else:
#             return render(request, "AppMercado/editarPerfil.html", {"formulario":form, "usuario":usuario, "mensaje":"Formulario inválido"})
#     else:
#         form=UserEditForm(instance=usuario)
#         return render(request, "AppMercado/editarPerfil.html", {"formulario":form, "usuario":usuario, "avatar":obtenerAvatar(request)})