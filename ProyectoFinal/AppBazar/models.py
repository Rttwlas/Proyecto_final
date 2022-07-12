from django.db import models

# Create your models here.   

#---------------------------------------------------------------------------------------------------

class Bazar(models.Model):
    nombre= models.CharField(max_length=30)
    foto= models.CharField(max_length=255)
    precio = models.IntegerField() 

class Contacto(models.Model):
    nombre= models.CharField(max_length=30)
    mail= models.CharField(max_length=255)
    precio = models.IntegerField() 
    
class PedidoPorEncargue(models.Model):
    producto= models.CharField(max_length=30)
    cantidad=models.IntegerField() 
    mail=models.CharField(max_length=30)


  
