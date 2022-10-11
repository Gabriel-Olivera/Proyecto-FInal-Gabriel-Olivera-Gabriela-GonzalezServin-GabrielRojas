from django.contrib import admin
from .models import *
from blog.models import *

# Register your models here.

admin.site.register(Electrodomesticos)
admin.site.register(Muebles)
admin.site.register(Vehiculos)
admin.site.register(Avatar)
admin.site.register(Blog)
