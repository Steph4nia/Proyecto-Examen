from django import forms
from .models import Contacto, Obra, ContactoTrabajo, Categoria

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto


        #fields = [" nombre", "apellidop", "apellidom", "nombreU", "ciudad", "tipo_comuna", "telefono"]

        fields = "__all__"

class ObraForm(forms.ModelForm):
    class Meta:       
        model = Obra 
        fields = "__all__"

        widgets = {
            "fechaO": forms.SelectDateWidget()
        }

class TrabajaconForm(forms.ModelForm):

    class Meta:
        model = ContactoTrabajo


        #fields = [" nombre", "apellidop", "apellidom", "nombreU", "ciudad", "tipo_comuna", "telefono"]

        fields = "__all__"    