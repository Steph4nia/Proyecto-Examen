from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
#usuario = models.foreskay(user, on_delete.odels.CASCADE)

class Categoria(models.Model):
      nombreC = models.CharField(max_length=50)
      
      
      def __str__(self):
           return self.nombreC
      
    
      

class Obra(models.Model):
    nombreArt = models.CharField(max_length=50)
    tipO = models.CharField(max_length=50)
    nombreO = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    valorO = models.IntegerField()
    fechaO = models.DateField()
    correo = models.CharField(max_length=100)
    celular = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    foto = models.ImageField(upload_to="obra", null=True)

    def __str__(self):
           return self.nombreArt
             

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellidop = models.CharField(max_length=50)
    apellidom = models.CharField(max_length=50)
    nombreU = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    tipo_comuna= models.CharField(max_length=50)
    telefono = models.IntegerField()
   
   

    def __str__(self):
           return self.nombre #+ ""+self.telefono
    
class ContactoTrabajo(models.Model):
    nombre = models.CharField(max_length=50)
    apellidoPaterno = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    correo = models.CharField(max_length=100)
    celular = models.IntegerField()
    descripcionPersonal = models.CharField(max_length=200)
    experienciaLaboral = models.CharField(max_length=200)
    idiomas = models.CharField(max_length=200)
    foto = models.ImageField(upload_to="contactotrabajo", null=True)
    CV = models.ImageField(upload_to="contactotrabajo", null=True)

    def __str__(self):
           return self.nombre    




