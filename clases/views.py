from django.shortcuts import render
import qrcode
from io import BytesIO
from django.http import HttpResponse
from .models import Asistencia

def index(request):
    return render(request, 'index.html') 




def generar_qr(request, clase_id):
    asistencia = Asistencia.objects.get(id=clase_id)
    qr = qrcode.make(asistencia.clase + " " + str(asistencia.fecha))
    buffer = BytesIO()
    qr.save(buffer)
    buffer.seek(0)
    return HttpResponse(buffer, content_type="image/png")