from django.db import models

# Create your models here.   

#---------------------------------------------------------------------------------------------------

class Bazar(models.Model):
    nombre= models.CharField(max_length=30)
    foto= models.CharField(max_length=999999999)
    precio = models.IntegerField() 


