from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from AppBazar.models import Avatar, Encargue

#---------------------------------------------------------------------------------------------------
class formularioPedidoMayor(forms.ModelForm): 
     class Meta: 
        model = Encargue 
        fields = ['producto','comentario','foto','cantidad', 'mail'] 

class BazarFormulario(forms.Form):
    nombre= forms.CharField(max_length=50)
    foto= forms.ImageField()
    precio= forms.IntegerField()
   
    
class Postulacion(forms.Form):
    nombre=forms.CharField(max_length=50)
    profesion=forms.CharField(max_length=50)
    comentario=forms.CharField(max_length=255)
    mail=forms.CharField(max_length=50)

class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'repite la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        print(model)
        fields = ['username', 'password1', 'password2']
        help_texts= {k:"" for k in fields}


class UserEditForm(UserCreationForm): 
    #definimos lo básico para modificar del usuario
    username = forms.CharField()
    email = forms.EmailField(label='modificar email')
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'repita contraseña', widget=forms.PasswordInput)
    
    last_name = forms.CharField()
    first_name= forms.CharField()

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2','last_name','first_name']
        help_texts= {k:"" for k in fields}      

class AvatarFormulario(forms.Form):
    
    imagen = forms.ImageField(required=True)

class avatareditform(forms.Form):
      class Meta:
        model = Avatar
        fields = ['imagen',]
        help_texts= {k:"" for k in fields}
      def __init__(self, *args, **kwargs):
        super(avatareditform, self).__init__(*args, **kwargs)
        self.fields['imagen'].required = False  

    
