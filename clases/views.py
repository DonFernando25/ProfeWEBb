from django.shortcuts import render
import qrcode
from io import BytesIO
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

def inicio(request):
    return render(request, 'inicio.html')


@login_required
def generar_qr(request):
    if request.method == 'POST':
        # Texto o información para el QR (puede venir de un formulario o ser fijo)
        texto_qr = request.POST.get('texto', 'Clase de prueba')

        # Generar el QR
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(texto_qr)
        qr.make(fit=True)

        # Crear la imagen del QR
        img = qr.make_image(fill_color="black", back_color="white")

        # Guardar la imagen en un buffer de memoria
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # Devolver la imagen como respuesta HTTP
        return HttpResponse(buffer, content_type="image/png")

    return render(request, 'generar_qr.html')