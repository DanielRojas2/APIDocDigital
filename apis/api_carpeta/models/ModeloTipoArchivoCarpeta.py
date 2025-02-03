from django.db import models
from django.utils.html import escape
from django.utils.timezone import now

from .ModeloCarpeta import ModeloCarpeta
from ...api_datoscarpeta.models.ModeloTipoArchivo import ModeloTipoArchivo

class ModeloTipoArchivoCarpeta(models.Model):
    carpeta = models.ForeignKey(
        ModeloCarpeta, on_delete=models.CASCADE, related_name='tipoarchivo_carpeta_set'
    )
    tipo_archivo = models.ManyToManyField(ModeloTipoArchivo)
    
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Asignacion Archivo Carpeta'
        verbose_name_plural = 'Asignacion Archivos Carpetas'
        ordering = ['creado']
        indexes = [
            models.Index(fields=['creado'])
        ]
    
    def __str__(self):
        return ', '.join(str(tipo) for tipo in self.tipo_archivo.all())
