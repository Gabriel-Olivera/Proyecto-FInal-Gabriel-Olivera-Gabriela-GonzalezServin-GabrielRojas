from django import forms


class ElectroForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=50,)
    precio = forms.IntegerField()
    email_contacto = forms.EmailField()
    fecha_publicacion = forms.DateField()


class MueblesForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    material = forms.CharField(max_length=50,)
    precio = forms.IntegerField()
    email_contacto = forms.EmailField()
    fecha_publicacion = forms.DateField()


class VehiculosForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    marca = forms.CharField(max_length=50,)
    precio = forms.IntegerField()
    email_contacto = forms.EmailField()
    fecha_publicacion = forms.DateField()
