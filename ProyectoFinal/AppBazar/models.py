from django.db import models
from django.contrib.auth.models import User

# Create your models here.   

#---------------------------------------------------------------------------------------------------

class Bazar(models.Model):
    nombre= models.CharField(max_length=30)
    foto= models.ImageField()
    precio = models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} --- Precio: ${self.precio}- "

class Contacto(models.Model):
    whatsapp= models.CharField(max_length=30)
    direccion= models.CharField(max_length=255)
    mail=models.CharField(max_length=30) 
    
class Encargue(models.Model):
    producto= models.CharField(max_length=30)
    comentario= models.CharField(max_length=255)
    cantidad=models.IntegerField()
    foto= models.ImageField(upload_to='encargueBazar', verbose_name='foto',null=True,blank=True) 
    mail=models.CharField(max_length=30)

    def __str__(self):
        return f"Producto: {self.producto} --- Cantidad: {self.cantidad} --- Email: {self.mail} " 
    
class Busqueda(models.Model):
    nombre= models.CharField(max_length=30)
    profesion= models.CharField(max_length=255)
    comentario= models.CharField(max_length=255)
    mail=models.CharField(max_length=30)

    def __str__(self):
        return f"Profesion: {self.profesion} --- Email: {self.mail} " 

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta avatares media
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True) 

    def __str__(self):
        return f"Usuario: {self.user} "


    
 






  
