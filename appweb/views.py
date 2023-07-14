from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Obra, ContactoTrabajo, Contacto
from .forms import ContactoForm, ObraForm, TrabajaconForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def home(request):
    messages.success(request, "Comienza a navegar")
    request.session["mensaje"] = "Holaaaa"
    return render(request, "home.html")

@login_required(login_url='/accounts/login')
@permission_required(['appweb.add_contacto'], login_url='/accounts/login')

def obra(request):
  
  obra= Obra.objects.all()

  if request.method == "POST":
      valor_buscado = request.POST.get("valor_buscado")
      
      obra = Obra.objects.filter(nombreO = valor_buscado)

  data={
      'obra': obra
  }

  return render(request, "obra.html", data)

def categoria(request):

    categoria = Categoria.objects.all()

    messages.success(request, request.session["mensaje"])

    Categoria = Categoria.objects.raw("select * from appweb_categoria where tipoO = true")


    data = {
        'categoria': Categoria
    }
    return render(request, 'categoria.html', data)

def contacto(request):

    data = {
        'form': ContactoForm,
        'mensaje':""
    }
    if request.method == "POST":
        formulario = ContactoForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Contacto guardado"
        else:
            data['form'] = formulario
            data['mensaje'] = "ocurrio un error"

    return render(request, 'contacto.html', data)

def agregar_obra(request):
    data = {
        "form": ObraForm
    }
    if request.method == "POST":
        formulario = ObraForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Obra guardada"
        else:
            data["mensaje"] = "hubo un error!!!"
            data["form"] = formulario

    return render(request, "mantenedor/obra/agregar.html", data)

def listar_obra(request):
    obras = Obra.objects.all()

    data= {
        'obras': obras
    }

    return render(request, "mantenedor/obra/listar.html", data)

def modificar_obra(request, nombreO ):

    obra = get_object_or_404(Obra, nombreO=nombreO )

    data = {
        "form": ObraForm(instance=obra)
    }

    if request.method == "POST":
        formulario = ObraForm(data=request.POST, instance=obra, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_obra")
        else:
            data['form'] = formulario
            data['mensaje'] = "Ocurrio un error"

    return render(request, "mantenedor/obra/modificar.html", data)

def eliminar_obra(request, nombreO ):
    obra = get_object_or_404(Obra, nombreO=nombreO )

    obra.delete()

    return redirect(to=listar_obra)

def login_usuario(request):

    print("Bienvenido: "+ request.user.username)
    print("este es el login")

    print('Grupos:', request.user.groups.all())
    
    

    return redirect(to='principaladmin')

@login_required(login_url="/accounts/login")
def registro_artista(request):

    data ={
        "mensaje" : ""

    }

    if request.POST:
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("correo")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        if password1 != password2:
            data["mensaje"] = "Las contraseñas deben ser identicas"

        else:
            usu = User()
            usu.set_password(password1)
            usu.email = correo
            usu.username = nombre
            usu.first_name = nombre
            usu.last_name = apellido
            grupo = Group.objects.get(name='artista')

            try:
                usu.save()
                usu.groups.add(grupo)
                data["mensaje"] = "Usuario creado"

                user = authenticate(username=usu.username, password=password1)
                login(request, user)
                return redirect(to= 'principaladmin')
                
            except:
                data["mensaje"] = "Hubo un error"

    return render(request, "registration/registro.html", data)
   

def nosotros(request):
    return render(request, 'nosotros.html')
def principaladmin(request):
    return render(request, 'principaladmin.html')
@login_required(login_url="/accounts/login")
def registro(request):

    return render(request, 'registro.html')
def solicitudes(request):
    obras = Obra.objects.all()

    data= {
        'obras': obras
    }
    return render(request, 'solicitudes.html', data)
def principalart(request):
    return render(request, 'principalart.html')


def subirpublicacion(request):

    

    return render(request, "subirpublicacion.html")

def trabajacon(request):
    data = {
        'form': TrabajaconForm
    }
    if request.method == "POST":
        formulario = TrabajaconForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Postulante guardado"

        else:
            data["mensaje"] = "hubo un error"
            data["form"] = formulario
    

    return render(request, "trabajacon.html", data)

def formulario(request):

    messages.success(request, "ok")
    request.session["mensaje"] = "Holaaaa"
    return render(request, 'formulario.html')
def ventas(request):
    return render(request, 'ventas.html')
def seguimientopubli(request):
    
    
    
    return render(request, 'seguimientopubli.html')

def imagen1(request):

    

    return render(request, "imagen1.html")

def imagen2(request):

    

    return render(request, "imagen2.html")

def imagen3(request):

    

    return render(request, "imagen3.html")

def imagen4(request):


    return render(request, "imagen4.html")

def eliminar_postulacion(request, nombre ):
    obra = get_object_or_404(ContactoTrabajo, nombre=nombre )

    obra.delete()

    return redirect(to=listar_postulacion)

def listar_postulacion(request):
    postulante = ContactoTrabajo.objects.all()

    data= {
        'postulante': postulante
    }

    return render(request, "listar_postulacion.html", data)


#def buscador(request):
    #artista = Obra.objects.all()

    #artista = Obra.objects.raw("select * from appweb_artista where aceptado = true")

    #data = {
       # 'artista': artista
    #}

    #if request.method == "POST":
    #    valor_buscado = request.POST.get("valor_buscado")
     #   if valor_buscado != "":
      #      artista = Obra.objects.filter(categoria = valor_buscado)
       #     data["artista"] = artista
        #else:
         #   data["artista"] = Obra.objects.raw("select * from appweb_artista where aceptado = true")

    #return render(request, 'obra.html', data)