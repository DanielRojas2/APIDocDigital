from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.html import escape
from django.utils.timezone import now

class ModeloClasificacionCarpeta(models.Model):
    CLASIFICACION_CHOICES = (
        ('importación', 'Importación'),
        ('adminisión temporal', 'Admisión Temporal'),
        ('exportación definitiva', 'Exportación Definitiva'),
        ('ritex', 'Ritex')
    )
    clasificacion_carpeta = models.CharField(
        max_length=22, blank=False, null=False, unique=True,
        choices=CLASIFICACION_CHOICES,
        validators=[
            RegexValidator(
                regex='^(importación|adminisión temporal|exportación definitiva|ritex)$',
                message='Clasificacion de carpeta inválida'
            )
        ]
    )
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Clasificacion Carpeta'
        verbose_name_plural = 'Clasificacion Carpetas'
        ordering = ['creado']
        indexes = [
            models.Index(fields=['creado'])
        ]

    def clean(self):
        self.clasificacion_carpeta = escape(self.clasificacion_carpeta)

        if self.clasificacion_carpeta not in dict(self.CLASIFICACION_CHOICES).keys():
            raise ValidationError(
                f"{self.clasificacion_carpeta} no es un canal válido"
            )
    
    def __str__(self):
        return f"{self.clasificacion_carpeta}"
