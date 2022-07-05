from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppBazar.models import Bazar
from AppBazar.forms import BazarFormulario
# Create your views here.

#---------------------------------------------------------------------------------------------------

def bazar(self):
    
    bazar =  Bazar(nombre="Mate", precio="1500") 
    bazar.save()
    documento = f"-----> Blanqueria: {bazar.nombre}, Precio: {bazar.precio}"
    return HttpResponse(documento)


#---------------------------------------------------------------------------------------------------

def inicio(request):
      CopitoDeNieve = Bazar.objects.all()
      contexto = {'bazar':CopitoDeNieve}
      return render(request, "AppBazar/inicio.html", contexto)

#---------------------------------------------------------------------------------------------------


def bazar(request):
      CopitoDeNieve = Bazar.objects.all()
      contexto = {'bazar':CopitoDeNieve}
      return render(request, "AppBazar/bazar.html", contexto) 

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
            miFormulario = bazarAgregar()
      
      return render(request, "AppBazar/formulario.html",{"miFormulario":miFormulario})


#---------------------------------------------------------------------------------------------------




#---------------------------------------------------------------------------------------------------


def buscarBazar(request):
      
      return render(request, 'AppBazar/buscarBazar.html')

#---------------------------------------------------------------------------------------------------



def buscar(request):
      if request.GET['nombre']:
            nombre = request.GET['nombre']
            bazar = Bazar.objects.filter(nombre__icontains=nombre)
            
            return render(request, "AppBazar/resultadosBusqueda.html", {"bazar": Bazar, "nombre":nombre} )
      
      else:
            output = "No ingresaste ningun dato"
      
      return HttpResponse(output)

#---------------------------------------------------------------------------------------------------



            
                  
            

