from django.urls import path
from AppBazar import views

#---------------------------------------------------------------------------------------------------

urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('bazar/',views.bazar, name="bazar"),
    path('contacto/',views.contacto, name="contacto"),
    #path('formulario/', views.bazarAgregar, name="formulario"),
    path('buscarBazar/', views.buscarBazar, name="buscarBazar"),
    path('buscar/',views.buscar),
    path('Pedidos/', views.Pedidos, name="Pedidos"),
    path('BusquedaLaboral/', views.BusquedaLaboral, name="BusquedaLaboral"),
    #path('eliminarBazar/<bazar_nombre>/', views.eliminarBazar, name="EliminarBazar"),
    #path('editarBazar/<bazar_nombre>/', views.editarBazar, name="EditarBazar"),
    path(r'^nuevo$', views.BazarCreacion.as_view(), name='formulario'),
    path(r'^editar/(?P<pk>\d+)$', views.BazarEditar.as_view(), name='EditarBazar'),
    path(r'^borrar/(?P<pk>\d+)$', views.BazarEliminar.as_view(), name='EliminarBazar'),
]

#---------------------------------------------------------------------------------------------------