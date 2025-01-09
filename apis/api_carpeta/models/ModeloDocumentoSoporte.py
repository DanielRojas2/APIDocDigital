import os

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.html import escape
from django.utils.timezone import now

from .ModeloTipoArchivoCarpeta import ModeloTipoArchivoCarpeta
from ..funciones_custom.guardar_carpeta import get_upload_to
from ..funciones_custom.validar_pdf import validate_pdf

class ModeloDocumentoSoporte(models.Model):
    ESTADOARCHIVO_CHOICES = (
        ('original', 'original'),
        ('copia', 'copia'),
        ('fotocopia', 'fotocopia'),
        ('fax', 'fax'),
    )
    ESTADORESPALDO_CHOICES = (
        ('adjunto', 'adjunto'),
        ('no adjunto', 'no adjunto')
    )

    carpeta_tipoarchivo = models.OneToOneField(
        ModeloTipoArchivoCarpeta, on_delete=models.CASCADE, blank=False, null=False
    )
    codigo_referencia = models.CharField(
        max_length=75, blank=False, null=False
    )
    respaldo = models.FileField(
        blank=True, null=False,
        upload_to=get_upload_to,
        validators = [validate_pdf]
    )
    estado_archivo = models.CharField(
        max_length=10, blank=False, null=False,
        choices=ESTADOARCHIVO_CHOICES,
        validators=[
            RegexValidator(
                regex='^(original|copia|fotocopia)$',
                message='Estado del archivo inválido'
            )
        ]
    )
    estado_respaldo = models.CharField(
        max_length=10, blank=False, null=False, default='no adjunto',
        choices=ESTADORESPALDO_CHOICES,
        validators=[
            RegexValidator(
                regex='^(adjunto|no adjunto)$',
                message='Estado del respaldo inválido'
            )
        ]
    )
    
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.respaldo:
            self.estado_respaldo = 'adjunto'
        else:
            self.estado_respaldo = 'no adjunto'

        super(ModeloDocumentoSoporte, self).save(*args, **kwargs)

    def clean(self):
        self.estado_archivo = escape(self.estado_archivo)
        self.estado_respaldo = escape(self.estado_respaldo)

        if self.estado_archivo not in dict(self.ESTADOARCHIVO_CHOICES).keys():
            raise ValidationError(
                f"{self.estado_archivo} no es un estado válido"
            )
        if self.estado_respaldo not in dict(self.ESTADORESPALDO_CHOICES).keys():
            raise ValidationError(
                f"{self.estado_respaldo} no es un estado válido"
            )        

    class Meta:
        verbose_name = 'Documento Respaldo'
        verbose_name_plural = 'Documentos Respaldo'
        ordering = ['creado']
        indexes = [
            models.Index(fields=['creado'])
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['codigo_referencia', 'carpeta_tipoarchivo'],
                name='unique_codigo_referencia_carpeta_tipoarchivo'
            )
        ]
    
    def __str__(self):
        return f"{self.carpeta_tipoarchivo} | {self.creado}"
