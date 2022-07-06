from django.urls import path
from AppBazar import views

#---------------------------------------------------------------------------------------------------

urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('bazar/',views.bazar, name="bazar"),
    path('formulario', views.bazarAgregar, name="formulario"),
    path('buscarBazar', views.buscarBazar, name="buscarBazar"),
    path('buscar/',views.buscar)
    
]

#---------------------------------------------------------------------------------------------------