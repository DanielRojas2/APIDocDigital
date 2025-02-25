from django.contrib import admin

from .models.ModeloAduanaDespacho import ModeloAduanaDespacho
from .models.ModeloCanalApertura import ModeloCanalApertura
from .models.ModeloClasificacionCarpeta import ModeloClasificacionCarpeta
from .models.ModeloImportador import ModeloImportador
from .models.ModeloMercaderia import ModeloMercaderia
from .models.ModeloModalidadDespacho import ModeloModalidadDespacho
from .models.ModeloPersonalAgencia import ModeloPersonalAgencia
from .models.ModeloTipoArchivo import ModeloTipoArchivo

@admin.register(ModeloAduanaDespacho)
class AduanaDespachoAdmin(admin.ModelAdmin):
    list_display = ['aduana_despacho', 'creado']
    search_fields = ['aduana_despacho']
    date_hierarchy = 'creado'

@admin.register(ModeloCanalApertura)
class CanalAperturaAdmin(admin.ModelAdmin):
    list_display = ['tipo_canal', 'creado']
    search_fields = ['tipo_canal']
    date_hierarchy = 'creado'

@admin.register(ModeloClasificacionCarpeta)
class ClasificacionCarpetaAdmin(admin.ModelAdmin):
    list_display = ['clasificacion_carpeta']
    search_fields = ['clasificacion_carpeta']
    date_hierarchy = 'creado'

@admin.register(ModeloImportador)
class ImportadorAdmin(admin.ModelAdmin):
    list_display = [
        'nombre_importador', 'nit_importador', 'tipo_importador', 'creado'
    ]
    list_filter = ['tipo_importador']
    search_fields = ['nombre_importador', 'nit_importador']

@admin.register(ModeloMercaderia)
class MercaderiaAdmin(admin.ModelAdmin):
    list_display = ['nombre_mercaderia', 'creado']
    search_fields = ['nombre_mercaderia']

@admin.register(ModeloModalidadDespacho)
class ModalidadDespachoAdmin(admin.ModelAdmin):
    list_display = ['tipo_despacho', 'creado']
    search_fields = ['tipo_despacho']

@admin.register(ModeloPersonalAgencia)
class ModeloPersonalAgenciaAdmin(admin.ModelAdmin):
    list_display = ['nombre_personal', 'apellido_personal', 'telefono_personal']
    search_fields = ['nombre_personal', 'apellido_personal']

@admin.register(ModeloTipoArchivo)
class TipoArchivoAdmin(admin.ModelAdmin):
    list_display = ['tipo_archivo']
    date_hierarchy = 'creado'
