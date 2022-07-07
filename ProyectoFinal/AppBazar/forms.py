from django import forms

#---------------------------------------------------------------------------------------------------

class BazarFormulario(forms.Form):
    nombre= forms.CharField(max_length=50)
    foto= forms.CharField(max_length=9999999)
    precio= forms.IntegerField()
   
class formularioPedidoMayor(forms.Form):
    producto=forms.CharField(max_length=50)
    foto= forms.CharField(max_length=9999999)
    cantidad=forms.IntegerField()
    mail=forms.CharField(max_length=50)

    
