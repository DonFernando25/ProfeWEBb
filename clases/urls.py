from django.urls import path
from . import views  

urlpatterns = [
    path('', views.index, name='index'),  
    path('generar_qr/<int:clase_id>/', views.generar_qr, name='generar_qr'),
    ]