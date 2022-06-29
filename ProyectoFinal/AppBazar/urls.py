from django.urls import path
from AppBazar import views

#---------------------------------------------------------------------------------------------------

urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('bazar/',views.bazar, name="Bazar"),
    path('formulario', views.bazarAgregar, name="Formulario"),
    path('buscarBazar', views.buscarBazar, name="BuscarBazar"),
    path('buscar/',views.buscar)
    
]

#---------------------------------------------------------------------------------------------------