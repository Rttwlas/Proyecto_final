from pyexpat.errors import messages
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse

#From para importar modelos y formularios
from AppBazar.models import Bazar, Busqueda, Encargue
from AppBazar.forms import *


# From para los CRUD - Crear, editar y eliminar.
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

#From para registrarse, logear y deslogearse de la web.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



 



#---------------------------------------------------------------------------------------------------
#@login_required
def inicio(request):
      CopitoDeNieve = Bazar.objects.all()
      
      return render(request, "AppBazar/inicio.html", {'contexto':CopitoDeNieve, 'url': buscar_url_avatar(request.user.id)})
      
#---------------------------------------------------------------------------------------------------


def bazar(request):
      bazar = Bazar.objects.all()
      return render(request, "AppBazar/bazar.html", {'bazar':bazar, 'url': buscar_url_avatar(request.user.id)})
      
#---------------------------------------------------------------------------------------------------

def eliminarBazar(request, bazar_nombre):

      bazar = Bazar.objects.get(nombre=bazar_nombre)
      bazar.delete()
      
      #vuelvo al menú
      bazar1 = Bazar.objects.all() #trae todos los bazar

      contexto= {"bazar1":bazar1} 

      return render(request, "AppBazar/bazar.html",contexto)

#---------------------------------------------------------------------------------------------------

def editarBazar(request, bazar_nombre):

      #Recibe el nombre del bazar que vamos a modificar
      bazar = Bazar.objects.get(nombre=bazar_nombre)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = BazarFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  bazar.nombre = informacion['nombre']
                  bazar.precio = informacion['precio']
                  bazar.foto = informacion['foto']

                  bazar.save()

                  return render(request, "AppBazar/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= BazarFormulario(initial={'nombre': bazar.nombre, 
            'precio':bazar.precio, 'foto':bazar.foto}) 

      #Voy al html que me permite editar
      return render(request, "AppBazar/editarBazar.html", {"miFormulario":miFormulario, "bazar_nombre":bazar_nombre, 'url': buscar_url_avatar(request.user.id)})

#---------------------------------------------------------------------------------------------------

def bazarAgregar(request):
      if request.method == 'POST':
            
            miFormulario = BazarFormulario(request.POST)
            
            print(miFormulario)
            
            if BazarFormulario.is_valid:
                  
                  informacion = miFormulario.cleaned_data
                  
                  bazar1 = Bazar(nombre=informacion['nombre'],foto=informacion['foto'], precio=informacion['precio'])                  
                  bazar1.save()
                  
                  return render(request, 'AppBazar/inicio.html')
      
      else:
            miFormulario = BazarFormulario()
      
      return render(request, "AppBazar/formulario.html",{"miFormulario":miFormulario,'url': buscar_url_avatar(request.user.id)})


#---------------------------------------------------------------------------------------------------

def Pedidos(request):
      if request.method == 'POST':
            
            miFormulario = formularioPedidoMayor(request.POST)
            
            print(miFormulario)
            
            if miFormulario.is_valid:
                  
                  informacion = miFormulario.cleaned_data
                  
                  Pedido = Encargue(producto=informacion['producto'],comentario=informacion['comentario'], foto=informacion['foto'], cantidad=informacion['cantidad'] , mail=informacion['mail'])              
                  Pedido.save()
                  
                  return render(request, 'AppBazar/inicio.html')
      
      else: 
            miFormulario = formularioPedidoMayor()
      
      return render(request, "AppBazar/bazarPedido.html",{"miFormulario":miFormulario,'url': buscar_url_avatar(request.user.id)})
    
    



#---------------------------------------------------------------------------------------------------
def BusquedaLaboral(request):
      if request.method == 'POST':
            
            miFormulario = Postulacion(request.POST)
            
            print(miFormulario)
            
            if miFormulario.is_valid:
                  
                  informacion = miFormulario.cleaned_data
                  
                  busqueda = Busqueda(nombre=informacion['nombre'], profesion=informacion['profesion'] , comentario=informacion['comentario'] , mail=informacion['mail'])              
                  busqueda.save()
                  
                  return render(request, 'AppBazar/inicio.html')
      
      else: 
            miFormulario = Postulacion()
      
      return render(request, "AppBazar/contacto.html",{"miFormulario":miFormulario,'url': buscar_url_avatar(request.user.id)})


#---------------------------------------------------------------------------------------------------

def buscarBazar(request):
      
      return render(request, 'AppBazar/buscarBazar.html',{'url': buscar_url_avatar(request.user.id)})

#---------------------------------------------------------------------------------------------------

#Funcion para buscar ,lo que ya habia agragado en la base de datos, en este caso bazares

def buscar(request):
      if request.GET['nombre']:
            nombre = request.GET['nombre']
            bazar = Bazar.objects.filter(nombre__icontains=nombre)
            
            return render(request, "AppBazar/resultadosBusqueda.html", {"bazar": bazar, "nombre":nombre,'url': buscar_url_avatar(request.user.id)} )
      
      else:
            output = "No ingresaste ningun dato"
      
      return HttpResponse(output)

#---------------------------------------------------------------------------------------------------

def contacto(request):
      return render(request, 'AppBazar/contacto.html',{'url': buscar_url_avatar(request.user.id)})

            
#---------------------------------------------------------------------------------------------------             
#Classes para crear bazar , editar y elimnar           
@method_decorator(staff_member_required, name= 'dispatch')
class BazarCreacion(CreateView):
      model = Bazar
      template_name = "AppBazar/bazarAgregar.html"
      fields = ['nombre','foto','precio']
      success_url = reverse_lazy('formulario')

@method_decorator(staff_member_required, name= 'dispatch')
class BazarEditar(UpdateView):
      model = Bazar
      template_name = "AppBazar/editarBazar.html"
      fields = ['nombre','foto','precio']
      success_url = reverse_lazy('bazar')

@method_decorator(staff_member_required, name= 'dispatch')
class BazarEliminar(DeleteView):
      model = Bazar
      template_name = "AppBazar/eliminar_confirm.html"
      fields = ['nombre','foto','precio']
      success_url = reverse_lazy('formulario')

#---------------------------------------------------------------------------------------------------
# Login

def login_request(request):
      #capturamos el post
      if request.method == "POST":
            #inicio esl uso del formulario de autenticación que me da Django
            #me toma dos parámetros el request y los datos que toma del request
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
               
                  user = authenticate(username = usuario , password = contra)
                 
                  if user is not None:
                        login(request, user)

                        return render (request, "AppBazar/inicio.html", {"mensaje": f"Bienvenido/a {usuario}"})
                  else:
                       
                        return render (request, "AppBazar/inicio.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "AppBazar/inicio.html", {"mensaje":"Formulario erroneo"})
      
      #al final recuperamos el form
      form = AuthenticationForm()
    
      return render(request, "AppBazar/login.html", {'form': form})

#############################REGISTRO################################3

def register(request):
      
      if request.method == "POST":

            form = UserCreationForm(request.POST)
            
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()

                  return render(request, "AppBazar/inicio.html", {"mensaje": "usuario creado",'url': buscar_url_avatar(request.user.id)})

      else: 
            form = UserRegisterForm()

      return render(request, "AppBazar/registro.html", {"form": form})

####################### FUNCION DE LOGGEO ###################

def logout_request(request):
      logout(request)
      messages.info(request, "Saliste sin problemas")
      return redirect("inicio")

###################### FUNCION DE EDITAR PERFIL ##################################

@login_required
def editarPerfil(request):
      #se instancia el Login; 
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid(): #si pasa la validación Django
                  informacion = miFormulario.cleaned_data
                  
                  #datos que modificaríamos
                  usuario.username= informacion ['username']
                  usuario.email = informacion['email']#alg@algo.com
                  usuario.password1 = informacion['password1']#pass
                  usuario.password2 = informacion['password2']
                  usuario.lastname = informacion['lastname']
                  usuario.firstname= informacion['firstname']
                  usuario.save()
            
                  return render(request, "AppBazar/inicio.html") #vuelvo a inicio

      else:
            #creo el formulario con los datos que voy a modificar
            miFormulario = UserEditForm(initial={'email':usuario.email})
      
      #voy al HTML que me permite editar
      return render(request, "AppBazar/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

################FUNCION DE VALIDACION DE AVATAR ########################
def buscar_url_avatar(user):
    avatares = Avatar.objects.filter(user=user)
    if avatares.exists():
        
        return avatares.first().imagen.url

    
    return None

#----------------------------FUNCION DE AGREGAR AVATAR----------------------------------------------


def agregarAvatar(request):
      if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html

            if miFormulario.is_valid():   #Si pasó la validación de Django


                  u = User.objects.get(username=request.user)
                
                  avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                  avatar.save()

                  return redirect('editar') 

      else: 

            miFormulario= AvatarFormulario() #Formulario vacio para construir el html

      return render(request, "agregarAvatar.html", {"miFormulario":miFormulario, 'url': buscar_url_avatar(request.user.id)})


class ProductosCreacion(CreateView):
    model=Encargue
    template_name="AppBazar/bazarPedido.html"
    fields = ['producto','comentario','foto','cantidad', 'mail'] 
    success_url=reverse_lazy('inicio')