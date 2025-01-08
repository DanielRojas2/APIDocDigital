from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError

class ModeloAduanaDespacho(models.Model):
    aduana_despacho = models.CharField(
        max_length=25, blank=False, null=False, unique=True,
    )
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Aduana Despacho'
        verbose_name_plural = 'Aduana Despacho'
        ordering = ['-creado']
        indexes = [
            models.Index(fields=['-creado'])
        ]

    def clean(self):
        if ModeloAduanaDespacho.objects.filter(
            aduana_despacho__iexact=self.aduana_despacho
        ).exists():
            raise ValidationError(
                {'aduana_despacho': 'Este recinto ya existe.'}
            )
    
    def __str__(self):
        return f"{self.aduana_despacho}"
