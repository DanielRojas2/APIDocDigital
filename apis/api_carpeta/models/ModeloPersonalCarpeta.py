from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.html import escape
from django.utils.timezone import now

from ...api_datoscarpeta.models.ModeloPersonalAgencia import ModeloPersonalAgencia
from .ModeloCarpeta import ModeloCarpeta

class ModeloPersonalCarpeta(models.Model):

    ROL_CHOICES = (
        ('tramitador', 'tramitador'),
        ('liquidador', 'liquidador'),
    )

    personal_asignado = models.ForeignKey(
        ModeloPersonalAgencia, on_delete=models.CASCADE
    )
    carpeta_asignada = models.ForeignKey(
        ModeloCarpeta, on_delete=models.CASCADE
    )
    rol_asignado = models.CharField(
        max_length=10, blank=False, null=False,
        choices=ROL_CHOICES,
        validators=[
            RegexValidator(
                regex='^(tramitador|liquidador)$',
                message='rol no permitido'
            )
        ]
    )

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Asignado a Carpeta'
        verbose_name_plural = 'Personal Carpeta'
        ordering = ['creado']
        indexes = [
            models.Index(fields=['creado'])
        ]

        constraints = [
            models.UniqueConstraint(
                fields=['personal_asignado', 'carpeta_asignada', 'rol_asignado'],
                name='unique_personal_carpeta_rol_asignado'
            )
        ]
    
    def clean(self):
        self.rol_asignado = escape(self.rol_asignado)

        if self.rol_asignado not in dict(self.ROL_CHOICES).keys():
            raise ValidationError(
                f"{self.rol_asignado} no es un rol válido"
            )

    def __str__(self):
        return f"{self.personal_asignado} - {self.carpeta_asignada} - {self.rol_asignado}"
