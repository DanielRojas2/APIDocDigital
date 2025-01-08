from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError

class ModeloMercaderia(models.Model):

    nombre_mercaderia = models.CharField(
        max_length=75, blank=False, null=False, unique=True
    )

    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Mercadería'
        verbose_name_plural = 'Mercadería'
        ordering = ['creado']
        indexes = [
            models.Index(fields=['creado'])
        ]
    
    def clean(self):
        if ModeloMercaderia.objects.filter(
            nombre_mercaderia__iexact=self.nombre_mercaderia
        ).exists():
            raise ValidationError(
                {'nombre_mercaderia':'Ya existe mercaderia con este nombre.'}
            )

    def __str__(self):
        return f"{self.nombre_mercaderia}"
    