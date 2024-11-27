from django.shortcuts import render
import qrcode
from io import BytesIO
from .models import Asistencia
from .models import Usuario
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login



def home(request):
    if request.method == 'POST':
        nombre_usuario = request.POST['nombre_usuario']
        contrasena = request.POST['contrasena']

        
        usuario = authenticate(request, username=nombre_usuario, password=contrasena)

        if usuario:
            login(request, usuario)  
            return redirect('inicio')  
        else:
            return render(request, 'home.html', {'error': 'Credenciales incorrectas'})

    return render(request, 'home.html')


@login_required
def generar_qr(request):
    
    return HttpResponse("Generando QR para la clase...")