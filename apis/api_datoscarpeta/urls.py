from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.AduanaDespachoView import AduanaDespachoView
from .views.CanalAperturaView import CanalAperturaView
from .views.ClasficacionCarpetaView import ClasificacionCarpetaView
from .views.ImportadorView import ImportadorView
from .views.MercaderiaView import MercaderiaView
from .views.ModalidadDespachoView import ModalidadDespachoView
from .views.PersonalAgenciaView import PersonalAgenciaView
from .views.TipoArchivoView import TipoArchivoView

router = DefaultRouter()

router.register(
    r'recinto-aduanero', AduanaDespachoView, basename='recinto_aduanero'
)
router.register(
    r'canal-apertura', CanalAperturaView, basename='canal_apertura'
)
router.register(
    r'clasificacion-carpeta', ClasificacionCarpetaView,
    basename='clasificacion_carpeta'
)
router.register(
    r'importador', ImportadorView, basename='importador'
)
router.register(
    r'mercaderia', MercaderiaView, basename='mercaderia'
)
router.register(
    r'modalidad-despacho', ModalidadDespachoView,
    basename='modalidad_despacho'
)
router.register(
    r'personal-agencia', PersonalAgenciaView, basename='personal-agencia'
)
router.register(
    r'tipo-archivo', TipoArchivoView, basename='tipo-archivo'
)

urlpatterns = router.urls
