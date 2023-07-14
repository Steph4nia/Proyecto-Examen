from django.contrib import admin
from .models import *

# Register your models here.

class ObraAdmin(admin.ModelAdmin):
    list_display= ['nombreArt', 'nombreO', 'descripcion', 'valorO', 'fechaO', 'correo', 'celular' ]
    list_editable= ['nombreO']
    search_fields= ['nombreArt']
    list_filter= ['correo']

class ContactoAdmin(admin.ModelAdmin):
    list_display= [ 'nombre', 'apellidop', 'apellidom', 'nombreU', 'ciudad', 'tipo_comuna', 'telefono' ]
    list_editable= ['apellidop']
    search_fields= ['nombre']
    list_filter= ['tipo_comuna']    

class ContactoTrabajoAdmin(admin.ModelAdmin):
    list_display= [ 'nombre', 'apellidoPaterno', 'fechaNacimiento', 'correo', 'celular', 'descripcionPersonal', 'experienciaLaboral', 'idiomas', 'foro', 'CV' ]
    list_editable= ['apellidoPaterno']
    search_fields= ['nombre']
    list_filter= ['correo']   


admin.site.register(Categoria)
admin.site.register(Obra, ObraAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(ContactoTrabajo)


