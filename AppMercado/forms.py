from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ElectroForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=50,)
    precio = forms.IntegerField()
    email_contacto = forms.EmailField()
    #fecha_publicacion = forms.DateField()


class MueblesForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    material = forms.CharField(max_length=50,)
    precio = forms.IntegerField()
    email_contacto = forms.EmailField()
    #fecha_publicacion = forms.DateField()


class VehiculosForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=50,)
    precio = forms.IntegerField()
    email_contacto = forms.EmailField()
    #fecha_publicacion = forms.DateField()

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    # password1=forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    # password2=forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    # first_name=forms.CharField(label="Ingrese nombre")
    # last_name=forms.CharField(label="Ingrese apellido")

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts={k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Ingrese nuevo email")
    password1=forms.CharField(label="Ingrese nueva Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repita nueva Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label="Ingrese nuevo nombre")
    last_name=forms.CharField(label="Ingrese nuevo apellido")

    class Meta:
        model=User
        fields=["email", "password1", "password2"]
        help_texts={k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")