from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError

class ModeloTipoArchivo(models.Model):
    tipo_archivo = models.CharField(
        max_length=55, blank=False, null=False, unique=True
    )
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tipo Archivo"
        verbose_name_plural = "Tipo Archivos"
        ordering = ['creado']
        indexes = [
            models.Index(fields=['creado'])
        ]
    
    def clean(self):
        if ModeloTipoArchivo.objects.filter(
            tipo_archivo__iexact=self.tipo_archivo
        ).exists():
            raise ValidationError(
                {'tipo_archivo':'Ya existe este tipo de archivo.'}
            )
    
    def __str__(self):
        return f"{self.tipo_archivo}"
