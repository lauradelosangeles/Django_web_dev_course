# Casos de Prueba — Formulario de Contacto

> Una **prueba funcional** verifica que el sistema hace exactamente lo que el usuario
> espera, sin importar cómo está programado por dentro.
> Esta tabla documenta los casos mínimos para el formulario en `/contacto/`.

---

## Tabla de Casos de Prueba

| # | Caso | Entrada | Resultado esperado | ¿Pasa? |
|---|------|---------|-------------------|--------|
| 1 | Formulario vacío | El usuario hace clic en "Enviar" sin llenar ningún campo | El formulario se muestra de nuevo con mensajes de error en los tres campos; no se guarda ningún `Mensaje` en la BD | ☐ |
| 2 | Correo inválido | `nombre="Ana"`, `correo="no-es-un-correo"`, `mensaje="Hola"` | El formulario muestra error en el campo correo: "Introduzca una dirección de correo electrónico válida"; no se guarda el mensaje | ☐ |
| 3 | Datos válidos | `nombre="Luis Pérez"`, `correo="luis@ejemplo.com"`, `mensaje="¿Hay tutoría esta semana?"` | Se guarda un nuevo `Mensaje` en la BD; la página muestra el mensaje de éxito "¡Mensaje recibido!"; el formulario queda vacío (patrón POST-Redirect-GET) | ☐ |
| 4 | _(Agrega tu caso)_ | _(Describe la entrada)_ | _(Describe el resultado esperado)_ | ☐ |
| 5 | _(Agrega tu caso)_ | _(Describe la entrada)_ | _(Describe el resultado esperado)_ | ☐ |

**Instrucción:** Ejecuta cada caso manualmente con el servidor corriendo
(`python manage.py runserver`) y marca ☑ si pasa o anota el error observado.

---

## Cómo ejecutar los casos manualmente

1. Abre `http://127.0.0.1:8000/contacto/` en el navegador.
2. Para cada caso, ingresa exactamente los datos de la columna "Entrada".
3. Haz clic en "Enviar mensaje".
4. Compara lo que ves en pantalla con la columna "Resultado esperado".
5. Para verificar que el caso 3 guardó el mensaje, entra a
   `http://127.0.0.1:8000/admin/hub/mensaje/` y confirma que aparece el registro.

---

## Prueba de carga — ¿Qué es y cómo simularla?

Una **prueba de carga** verifica que el sistema se comporta correctamente cuando
muchos usuarios lo usan al mismo tiempo o envían muchos formularios seguidos.

### ¿Qué buscamos detectar?
- Que el servidor no "se caiga" con muchos envíos simultáneos.
- Que cada mensaje se guarda sin duplicados ni pérdidas.
- Que el tiempo de respuesta no aumenta de forma desproporcionada.

### Simulación sencilla (sin herramientas externas)

Puedes simular envíos repetidos con un bucle en Python desde la terminal:

```python
# Ejecuta esto en una terminal separada mientras el servidor corre
import urllib.request, urllib.parse

datos = urllib.parse.urlencode({
    'nombre': 'Prueba Carga',
    'correo': 'carga@ejemplo.com',
    'mensaje': 'Mensaje de prueba automatizado',
    'csrfmiddlewaretoken': 'REEMPLAZA_CON_TOKEN_REAL',
}).encode()

for i in range(10):
    req = urllib.request.Request(
        'http://127.0.0.1:8000/contacto/',
        data=datos,
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
    )
    try:
        resp = urllib.request.urlopen(req)
        print(f"Envío {i+1}: {resp.status}")
    except Exception as e:
        print(f"Envío {i+1}: Error — {e}")
```

> **Nota sobre CSRF:** Django protege el formulario con un token único por sesión.
> Para pruebas de carga reales se usa una herramienta como **Locust** o **k6** que
> gestiona cookies y tokens automáticamente.

### Herramientas gratuitas para pruebas de carga más completas

| Herramienta | Instalación | Documentación |
|-------------|-------------|---------------|
| Locust | `pip install locust` | https://locust.io |
| k6 | Descarga binario | https://k6.io |

Estas herramientas se introducen en cursos avanzados; para este curso basta con
las pruebas funcionales manuales de la tabla anterior.
