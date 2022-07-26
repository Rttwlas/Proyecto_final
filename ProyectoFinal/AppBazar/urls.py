from django.urls import path
from AppBazar import views
from django.contrib.auth.views import LogoutView


#---------------------------------------------------------------------------------------------------

urlpatterns = [
    path('', views.inicio, name="inicio"),
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
    path('login',views.login_request, name= 'Login'),
    path('register',views.register, name= 'Register'),
    path('logout', LogoutView.as_view(template_name= 'AppBazar/logout.html') ,name= 'Logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
    path(r'^new$', views.ProductosCreacion.as_view(), name='New'),
]

#---------------------------------------------------------------------------------------------------