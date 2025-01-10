from django.urls import path
from rest_framework.routers import DefaultRouter
from .views.CarpetaView import (
    CarpetaView, ReporteCarpetaView, DetalleCarpetaView
)
from .views.DocumentoSoporteView import DocumentoSoporteView
from .views.PersonalCarpetaView import PersonalCarpetaView
from .views.TipoArchivoCarpetaView import TipoArchivoCarpetaView

router = DefaultRouter()

router.register(r'carpeta', CarpetaView, basename='carpeta')
router.register(r'reporte-carpetas', ReporteCarpetaView, basename='reporte-carpetas')
router.register(r'detalle-carpeta', DetalleCarpetaView, basename='detalle-carpeta')
router.register(
    r'documento-soporte', DocumentoSoporteView, basename='documento-soporte'
)
router.register(
    r'asignar-personal', PersonalCarpetaView, basename='asignar-personal'
)
router.register(
    r'asignar-tipoarchivo', TipoArchivoCarpetaView,
    basename='asignar-tipoarchivo'
)

urlpatterns = router.urls
