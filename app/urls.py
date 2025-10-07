from django.urls import path
from . import views

urlpatterns = [
    path('hola_mundo/' , views.hola_mundo),
    path('' , views.estado_de_entrega),
    path('entregas_terminadas/', views.entregas_terminadas),
    path('rutas_por_hacer/', views.rutas_por_hacer),
    path('eliminar_entrega/<int:id_entrega>', views.eliminar_entrega),
    path('editar_entrega/<int:id>/', views.editar_entrega),
]