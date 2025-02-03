import os
import shutil
import tempfile
import zipfile
from django.http import FileResponse
from django.conf import settings
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..models.ModeloCarpeta import ModeloCarpeta
from ..serializers.CarpetaSerializer import (
    CarpetaSerializer, ReporteCarpetaSerializer, CarpetaDetalleSerializer
)
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

class CarpetaView(viewsets.ModelViewSet):
    queryset = ModeloCarpeta.objects.all()
    serializer_class = CarpetaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class ReporteCarpetaView(viewsets.ReadOnlyModelViewSet):
    queryset = ModeloCarpeta.objects.all()
    serializer_class = ReporteCarpetaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class DetalleCarpetaView(viewsets.ReadOnlyModelViewSet):
    queryset = ModeloCarpeta.objects.prefetch_related(
        'tipoarchivo_carpeta_set__tipo_archivo',
        'tipoarchivo_carpeta_set__documento_soporte'
    )
    serializer_class = CarpetaDetalleSerializer
    #authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'], url_path='descargar-zip')
    def descargar_zip(self, request, pk=None):
        carpeta = self.get_object()
        codigo_interno = carpeta.codigo_interno
        nro_dim = carpeta.nro_dim
        temp_dir = tempfile.mkdtemp()
        carpeta_archivos_path = os.path.join(temp_dir, codigo_interno)
        os.makedirs(carpeta_archivos_path, exist_ok=True)
        archivos = carpeta.tipoarchivo_carpeta_set.all()
        archivos_encontrados = False

        for archivo in archivos:
            if archivo.documento_soporte and archivo.documento_soporte.respaldo:
                respaldo_path = archivo.documento_soporte.respaldo.path
                if os.path.exists(respaldo_path):
                    archivos_encontrados = True
                    shutil.copy(
                        respaldo_path,
                        os.path.join(
                            carpeta_archivos_path,
                            os.path.basename(respaldo_path)
                        )
                    )

        if not archivos_encontrados:
            shutil.rmtree(temp_dir)
            return Response(
                {'detail': 'No hay archivos disponibles para descargar.'},
                status=status.HTTP_404_NOT_FOUND
            )

        detalles_pdf_path = os.path.join(
            temp_dir,
            f"Detalles {codigo_interno}.pdf"
        )
        self._generar_pdf_detalle(
            detalles_pdf_path,
            codigo_interno,
            nro_dim, archivos
        )

        zip_path = os.path.join(tempfile.gettempdir(), f"{codigo_interno}.zip")
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, temp_dir)
                    zipf.write(file_path, arcname)

        shutil.rmtree(temp_dir)

        response = FileResponse(
            open(zip_path, 'rb'),
            as_attachment=True,
            filename=f"{codigo_interno}.zip"
        )
        return response

    def _generar_pdf_detalle(self, pdf_path, codigo_interno, nro_dim, archivos):
        """Generar PDF con los detalles de la carpeta."""
        doc = SimpleDocTemplate(pdf_path, pagesize=landscape(letter))
        elements = []
        styles = getSampleStyleSheet()

        elements.append(Paragraph("<b>Detalle de Carpeta</b>", styles["Title"]))
        elements.append(Spacer(1, 12))

        general_data = [
            [Paragraph(f"<b>Código Interno:</b> {codigo_interno}", styles["Normal"]),
            Paragraph(f"<b>Nro DIM:</b> {nro_dim}", styles["Normal"])]
        ]
        general_table = Table(general_data, colWidths=[4.5 * inch, 4.5 * inch])
        general_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8)
        ]))
        elements.append(general_table)
        elements.append(Spacer(1, 12))

        def truncar_texto(texto, max_len=40):
            return texto if len(texto) <= max_len else texto[:max_len] + '...'

        data = [
            [
                "Archivo",
                "Código Referencia",
                "Estado Archivo",
                "Estado Respaldo"
            ]
        ]

        for archivo in archivos:
            if archivo.documento_soporte:
                nombre_archivo = truncar_texto(archivo.__str__(), 40)
                data.append([
                    nombre_archivo,
                    archivo.documento_soporte.codigo_referencia,
                    archivo.documento_soporte.estado_archivo,
                    archivo.documento_soporte.estado_respaldo
                ])

        table = Table(data, colWidths=[3.5 * inch, 2.5 * inch, 1.5 * inch, 1.5 * inch])
        table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 5),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))

        elements.append(table)

        doc.build(elements)
