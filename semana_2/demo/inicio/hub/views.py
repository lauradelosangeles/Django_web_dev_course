from django.http import HttpResponse

# Datos del docente — personaliza estas variables
nombre_docente   = "Prof. González Silva"
materia          = "Matemáticas"
institucion      = "Colegio Dolores Sucre"
años_experiencia = "10"

# AQUÍ CONSTRUIMOS EN CLASE:
# El profesor escribe las funciones inicio() y acerca()
def inicio(request):
    return HttpResponse(f"""
    <!DOCTYPE html>
    <html>
    <head><title>{nombre_docente}</title></head>
    <body>
        <h1>Bienvenidos al hub de {nombre_docente}</h1>
        <p>Docente en {institucion} a sus servicios</p>
        <a href="/acerca/">Ver mi perfil</a>
    </body>
    </html>
    """)
def acerca(request):
    return HttpResponse(f"""
    <!DOCTYPE html>
    <html>
    <head><title>Acerca de {nombre_docente}</title></head>
    <body>
        <h1>Acerca de {nombre_docente}</h1>
        <p>Docente de {materia} en {institucion}</p>
        <p>Años de experiencia: {años_experiencia}</p>
    </body>
    </html>
    """)