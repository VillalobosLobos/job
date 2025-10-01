from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name='index'),
    path('terminadas/' , views.entregasTerminadas, name='terminadas'),
    path('rutas/' , views.rutasPorHacer , name='rutas')
]