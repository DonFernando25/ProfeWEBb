from django.urls import path
from . import views  
from views import inicio_view,generar_qr


urlpatterns = [
    path('', views.home, name='home'), 
    path('inicio/', inicio_view, name='inicio'),
     path('generar-qr/', generar_qr, name='generar_qr'),
    
    ]