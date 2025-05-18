from django.db import models


class Secuencia(models.Model):
    TIPOS = [
        ("ADN", "ADN"),
        ("ARN", "ARN"),
        ("Proteina", "Proteína"),
    ]
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPOS)
    secuencia = models.TextField()
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"
