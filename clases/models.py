from django.db import models


    


class Asistencia(models.Model):
    alumno = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)
    codigo_qr = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.alumno} - {self.fecha}"