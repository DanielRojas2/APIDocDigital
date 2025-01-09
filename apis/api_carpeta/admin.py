from django.contrib import admin
from .models.ModeloCarpeta import ModeloCarpeta
from .models.ModeloDocumentoSoporte import ModeloDocumentoSoporte
from .models.ModeloPersonalCarpeta import ModeloPersonalCarpeta
from .models.ModeloTipoArchivoCarpeta import ModeloTipoArchivoCarpeta

@admin.register(ModeloCarpeta)
class CarpetaAdmin(admin.ModelAdmin):
    list_display = [
        'codigo_interno',
        'nro_dim',
        'canal',
        'modalidad_despacho',
        'importador',
        'aduana_despacho',
        'clasificacion_carpeta',
        'fecha_apertura',
        'mercaderia'
    ]
    list_filter = ['canal', 'importador', 'clasificacion_carpeta']
    search_fields = ['codigo_interno', 'nro_dim']
    date_hierarchy = 'fecha_apertura'

@admin.register(ModeloDocumentoSoporte)
class DocumentoSoporte(admin.ModelAdmin):
    list_display = [
        'carpeta_tipoarchivo',
        'codigo_referencia',
        'respaldo',
        'estado_archivo',
        'estado_respaldo'
    ]
    list_filter = ['estado_archivo', 'estado_respaldo']

@admin.register(ModeloPersonalCarpeta)
class PersonalCarpeta(admin.ModelAdmin):
    list_display = [
        'personal_asignado',
        'carpeta_asignada',
        'rol_asignado'
    ]
    list_filter = ['rol_asignado']

@admin.register(ModeloTipoArchivoCarpeta)
class TipoArchivoCarpeta(admin.ModelAdmin):
    list_display = ['carpeta', 'tipo_archivo']
    list_filter = ['carpeta']
