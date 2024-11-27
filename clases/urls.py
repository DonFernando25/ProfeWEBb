from django.urls import path
from . import views  
from .views import inicio, generar_qr



urlpatterns = [
    path('', views.home, name='home'), 
    path('inicio/', inicio, name='inicio'),
     path('generar-qr/', generar_qr, name='generar_qr'),
    
    ]