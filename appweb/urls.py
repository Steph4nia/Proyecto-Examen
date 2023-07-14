from django.urls import path
from .views import  home, contacto, obra, categoria, nosotros, principaladmin, seguimientopubli,  registro, solicitudes, principalart, subirpublicacion, formulario, ventas, agregar_obra, listar_obra, modificar_obra, eliminar_obra, login_usuario, registro_artista, imagen1, imagen2, imagen3, imagen4, trabajacon, listar_postulacion, eliminar_postulacion

urlpatterns = [
    path('home/', home, name="home"),
    path('', home, name="home"),
    path('categoria/', categoria, name="categoria"),
    path('principaladmin/', principaladmin, name="principaladmin"),
    path('registro/', registro, name="registro"),
    path('solicitudes/', solicitudes, name="solicitudes"),
    path('principalart/', principalart, name="principalart"),
    #path('subirpublicacion/', subirpublicacion, name="subirpublicacion"),
    path('contacto/', contacto, name="contacto"),
    path('formulario/', formulario, name="formulario"),
    path('nosotros/', nosotros, name="nosotros"),
    path('seguimientopubli/', seguimientopubli, name="seguimientopubli"),
    path('ventas/', ventas, name="ventas"),
    path('obra/', obra, name="obra"),
    path('mantenedor/obra/agregar', agregar_obra, name="agregar_obra"),
    path('mantenedor/obra/listar', listar_obra, name="listar_obra"),
    path('mantenedor/obra/modificar/<nombreO>', modificar_obra, name="modificar_obra"),
    path('mantenedor/obra/eliminar/<nombreO>', eliminar_obra, name="eliminar_obra"),
    path('login_usuario/', login_usuario, name="login_usuario"),
    path('registro_artista/', registro_artista, name="registro_artista"),
    path('imagen1/', imagen1, name="imagen1"),
    path('imagen2/', imagen2, name="imagen2"),
    path('imagen3/', imagen3, name="imagen3"),
    path('imagen4/', imagen4, name="imagen4"),
    path('trabajacon/', trabajacon, name="trabajacon"),
    path('listar_postulacion/', listar_postulacion, name="listar_postulacion"),
    path('eliminar_postulacion/', eliminar_postulacion, name="eliminar_postulacion"),
  
  


]