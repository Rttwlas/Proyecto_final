from django import forms

#---------------------------------------------------------------------------------------------------

class BazarFormulario(forms.Form):
    nombre= forms.CharField(max_length=50)
    foto= forms.CharField(max_length=255)
    precio= forms.IntegerField()
   
class formularioPedidoMayor(forms.Form):
    producto=forms.CharField(max_length=50)
    comentario=forms.CharField(max_length=255)
    foto= forms.CharField(max_length=255)
    cantidad=forms.IntegerField()
    mail=forms.CharField(max_length=50)
    
class Postulacion(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    comentario=forms.CharField(max_length=255)
    mail=forms.CharField(max_length=50)

    
