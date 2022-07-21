from django.db import models

# Create your models here.   

#---------------------------------------------------------------------------------------------------

class Bazar(models.Model):
    nombre= models.CharField(max_length=30)
    foto= models.CharField(max_length=255)
    precio = models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre}  - Precio ${self.precio}- "

class Contacto(models.Model):
    whatsapp= models.CharField(max_length=30)
    direccion= models.CharField(max_length=255)
    mail=models.CharField(max_length=30) 
    
class Encargue(models.Model):
    producto= models.CharField(max_length=30)
    comentario= models.CharField(max_length=255)
    cantidad=models.IntegerField()
    foto= models.CharField(max_length=255) 
    mail=models.CharField(max_length=30)

    def __str__(self):
        return f"Producto: {self.producto}  - Cantidad {self.cantidad}- Email {self.mail} " 
    
class Busqueda(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=255)
    comentario= models.CharField(max_length=255)
    mail=models.CharField(max_length=30) 






  
