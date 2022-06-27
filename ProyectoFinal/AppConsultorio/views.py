from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import  Inicio, Pediatria, MedicoClinico, Cardiologia, Traumatologia, Ginecologia
# Create your views here.

def inicio(request):
      inicio= Inicio.objects.all()
      return render(request, "AppConsultorio/inicio.html",{"inicio":inicio})

def pediatria(request):
      pediatria= Pediatria.objects.all()
      return render(request, "AppConsultorio/pediatria.html",{"pediatria":pediatria}) 

def medicoclinico(request):
      medicoclinico= MedicoClinico.objects.all()
      return render(request, "AppConsultorio/medicoclinico.html",{"medicoclinico":medicoclinico})

def cardiologia(request):
      cardiologia= Cardiologia.objects.all()
      return render(request, "AppConsultorio/cardiologia.html",{"cardiologia":cardiologia})

def traumatologia(request):
      traumatologia= Traumatologia.objects.all()
      return render(request, "AppConsultorio/traumatologia.html",{"traumatologia":traumatologia})
  
def ginecologia(request):
      ginecologia= Ginecologia.objects.all()
      return render(request, "AppConsultorio/ginecologia.html", {"ginecologia":ginecologia})