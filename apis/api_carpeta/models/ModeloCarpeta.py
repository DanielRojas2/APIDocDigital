from django.db import models
from django.utils.timezone import now

from ...api_datoscarpeta.models.ModeloAduanaDespacho import ModeloAduanaDespacho
from ...api_datoscarpeta.models.ModeloCanalApertura import ModeloCanalApertura
from ...api_datoscarpeta.models.ModeloClasificacionCarpeta import (
    ModeloClasificacionCarpeta
)
from ...api_datoscarpeta.models.ModeloImportador import ModeloImportador
from ...api_datoscarpeta.models.ModeloMercaderia import ModeloMercaderia
from ...api_datoscarpeta.models.ModeloModalidadDespacho import ModeloModalidadDespacho

class ModeloCarpeta(models.Model):

    codigo_interno = models.CharField(
        max_length=6, primary_key=True, unique=True, blank=False, null=False
    )
    nro_dim = models.CharField(
        max_length=20, unique=True, blank=False, null=False
    )
    canal = models.ForeignKey(
        ModeloCanalApertura, on_delete=models.CASCADE
    )
    modalidad_despacho = models.ForeignKey(
        ModeloModalidadDespacho, on_delete=models.CASCADE
    )
    importador = models.ForeignKey(
        ModeloImportador, on_delete=models.CASCADE
    )
    aduana_despacho = models.ForeignKey(
        ModeloAduanaDespacho, on_delete=models.CASCADE
    )
    clasificacion_carpeta = models.ForeignKey(
        ModeloClasificacionCarpeta, on_delete=models.CASCADE
    )
    fecha_apertura = models.DateField()
    mercaderia = models.ForeignKey(
        ModeloMercaderia, on_delete=models.CASCADE
    )

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Carpeta'
        verbose_name_plural = 'Carpetas'
        ordering = ['creado']
        indexes = [
            models.Index(fields=['creado'])
        ]

    def __str__(self):
        return self.codigo_interno
