# Tablero Kanban y Cierre del Curso

> Un **tablero Kanban** visualiza el flujo de trabajo: qué tareas están pendientes,
> cuáles están en progreso y cuáles están terminadas.
> Al final del curso, publicaremos el Hub como una release oficial en GitHub.

---

## 1. Crear el tablero en GitHub Projects

### Paso a paso

1. **Ve a tu repositorio** en GitHub.
2. Haz clic en la pestaña **Projects** → **New project**.
3. Selecciona la plantilla **Board** (tablero Kanban).
4. Nómbralo: `Hub Personal del Docente — 5 Semanas`.
5. El tablero crea automáticamente tres columnas:
   - **Todo** (Por hacer)
   - **In Progress** (En curso)
   - **Done** (Hecho)

### Personalizar columnas (opcional)

Puedes renombrar las columnas en español:
- **Por hacer** — tareas planificadas pero no iniciadas.
- **En curso** — tareas en las que estás trabajando ahora.
- **En revisión** — tareas terminadas que esperan revisión del docente.
- **Hecho** — tareas completadas y aceptadas.

---

## 2. Tareas del tablero — una por cada entregable

Crea una tarjeta (card) en la columna **Por hacer** para cada tarea.
Muévela a **En curso** cuando la empieces y a **Hecho** cuando la termines.

### Semana 1
- [ ] Configurar entorno virtual y Django
- [ ] Crear proyecto `hub_docente` y app `hub`
- [ ] Primera vista con `HttpResponse`

### Semana 2
- [ ] Conectar URLs y vistas
- [ ] Pasar datos con diccionario de contexto
- [ ] Probar rutas en el navegador

### Semana 3
- [ ] Crear `templates/base.html` con Bootstrap 5
- [ ] Convertir vistas a `render()` con herencia de plantillas
- [ ] Completar wireframe de `/recursos/` y checklist de accesibilidad

### Semana 4
- [ ] Definir modelos `Recurso` y `Mensaje` en `models.py`
- [ ] Ejecutar `makemigrations` y `migrate`
- [ ] Registrar modelos en `admin.py`
- [ ] Conectar `recursos_view()` al ORM
- [ ] Ejecutar las pruebas unitarias (`python manage.py test`)

### Semana 5
- [ ] Crear `ContactoForm` y vista `contacto()`
- [ ] Probar casos funcionales del formulario (casos_de_prueba.md)
- [ ] Configurar `.env` para producción
- [ ] Subir el Hub a PythonAnywhere
- [ ] Publicar release v1.0 en GitHub

---

## 3. Alternativa: Trello

Si prefieres Trello (sin necesidad de cuenta GitHub):

1. Ve a [trello.com](https://trello.com) y crea una cuenta gratuita.
2. Crea un tablero nuevo: **Hub Personal del Docente**.
3. Agrega tres listas: **Por hacer**, **En curso**, **Hecho**.
4. Crea una tarjeta por cada tarea de la lista anterior.
5. Arrastra las tarjetas entre columnas conforme avanzas.

**Ventaja de Trello sobre GitHub Projects:** más visual e intuitivo para principiantes.  
**Ventaja de GitHub Projects:** integrado con el repositorio; puedes vincular tarjetas
a commits e issues.

---

## 4. Cerrar el curso — Release v1.0 en GitHub

Una **release** es una versión estable y etiquetada del proyecto, como publicar
la "versión final" de un documento.

### Paso a paso para publicar la release

```bash
# 1. Asegúrate de que todo está en main y commiteado
git checkout main
git status

# 2. Crea la etiqueta de versión
git tag -a v1.0 -m "Hub Personal del Docente — versión final del curso"

# 3. Sube la etiqueta al repositorio remoto
git push origin v1.0
```

### En la interfaz de GitHub

1. Ve a tu repositorio → **Releases** → **Draft a new release**.
2. En **Tag version**, selecciona `v1.0`.
3. Título: `Hub Personal del Docente v1.0`
4. En la descripción, incluye:
   - URL del Hub publicado en PythonAnywhere.
   - Lista de funcionalidades completadas (inicio, acerca, recursos, contacto, admin).
   - Créditos (nombre del docente, institución, fecha).
5. Haz clic en **Publish release**.

### Comparte el resultado

Con la release publicada, puedes compartir:
- **URL del Hub:** `https://tuusuario.pythonanywhere.com`
- **URL de la release:** `https://github.com/tuusuario/tu-repo/releases/tag/v1.0`

¡Felicitaciones! Completaste el curso y tienes un Hub Personal del Docente
en producción, documentado y con control de versiones.
