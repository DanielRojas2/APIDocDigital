from django.urls import path
from rest_framework.routers import DefaultRouter
from .views.CarpetaView import CarpetaView, ReporteCarpetaView
from .views.DocumentoSoporteView import DocumentoSoporteView
from .views.PersonalCarpetaView import PersonalCarpetaView
from .views.TipoArchivoCarpetaView import TipoArchivoCarpetaView

router = DefaultRouter()

router.register(r'carpeta', CarpetaView, basename='carpeta')
router.register(r'reporte-carpetas', ReporteCarpetaView, basename='reporte-carpetas')
router.register(
    r'documento-soporte', DocumentoSoporteView, basename='documento_soporte'
)
router.register(
    r'asignar-personal', PersonalCarpetaView, basename='asignar_personal'
)
router.register(
    r'asignar-tipoarchivo', TipoArchivoCarpetaView,
    basename='asignar_tipoarchivo'
)

urlpatterns = router.urls
