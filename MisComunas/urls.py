from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_comunas, name='listado_comunas'),
    path('nueva/', views.nueva_comuna, name='nueva_comuna'),
    path('editar/<int:pk>/', views.editar_comuna, name='editar_comuna'),
    path('eliminar/<int:pk>/', views.eliminar_comuna, name='eliminar_comuna'),
]
