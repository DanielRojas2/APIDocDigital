import os

def get_upload_to(instance, filename):

    codigo_interno = instance.carpeta_tipoarchivo.carpeta.codigo_interno
    fecha_apertura = instance.carpeta_tipoarchivo.carpeta.fecha_apertura
    
    year = fecha_apertura.year
    month_name = fecha_apertura.strftime('%B')

    month_translation = {
        'January': 'enero',
        'February': 'febrero',
        'March': 'marzo',
        'April': 'abril',
        'May': 'mayo',
        'June': 'junio',
        'July': 'julio',
        'August': 'agosto',
        'September': 'septiembre',
        'October': 'octubre',
        'November': 'noviembre',
        'December': 'diciembre'
    }

    month_name_es = month_translation.get(month_name, month_name)

    return os.path.join('archivos', str(year), month_name_es, codigo_interno, filename)
