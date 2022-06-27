from django.urls import path
from AppConsultorio import views


urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('pediatria/', views.pediatria, name="pediatria"),
    path('medicoclinico/', views.medicoclinico, name="medicoclinico"),
    path('traumatologia/', views.traumatologia, name="traumatologia"),
    path('cardiologia/', views.cardiologia, name="cardiologia"),
    path('ginecologia/', views.ginecologia, name="ginecologia"),
]